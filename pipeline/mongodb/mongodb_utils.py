import pymongo
from pymongo import UpdateOne, DeleteOne, UpdateMany
from pymongo.errors import BulkWriteError, ConfigurationError, InvalidName, CollectionInvalid, ConnectionFailure, \
    InvalidOperation


def init_db(test_db=None):
    from common.config_db import config_db
    from common.config_db import collection_names
    try:
        client = pymongo.MongoClient(config_db.db_address)
        if test_db is not None:
            mydb = client[test_db]
        else:
            mydb = client[config_db.db_name]
        collection_dict = {
            collection_names.active: mydb[collection_names.active],
            collection_names.pending: mydb[collection_names.pending],
            collection_names.completed: mydb[collection_names.completed],
            collection_names.leads: mydb[collection_names.leads],
            collection_names.abandoned: mydb[collection_names.abandoned]
        }
        return collection_dict
    except ConfigurationError or InvalidName or CollectionInvalid or ConnectionFailure:
        raise ConfigurationError(f"{config_db.db_name} or {config_db.db_address} or a collection not found")


def get_db():
    from common.config_db import collection_names
    # Init DB and return all collections
    collections_dict = init_db()
    active_collection = collections_dict.get(collection_names.active)
    pending_collection = collections_dict.get(collection_names.pending)
    completed_collection = collections_dict.get(collection_names.completed)
    leads_collection = collections_dict.get(collection_names.leads)
    abandoned_collection = collections_dict.get(collection_names.abandoned)
    return collections_dict, active_collection, pending_collection, completed_collection, leads_collection, abandoned_collection


def find_in_mongodb(key, target_collection):
    if not key:
        return
    try:
        user_schema = target_collection.find(key)
        return user_schema
    except:
        return False


def dump_to_mongodb(entries, target_collection):
    """
    Dumps the entries to a given mongodb collection

    :param entries: collection of objects to dump
    :param target_collection: name of the collection where to save the entries
    """
    if not entries:
        return
    try:
        target_collection.insert_many(entries, False)
    except BulkWriteError as bwe:
        for err in bwe.details['writeErrors']:
            if int(err['code']) == 11000:
                # duplicate key, don't care
                pass
            else:
                print(err['errmsg'])


def push_updates_to_db_reply_chat_id_key(dicts_with_items_to_set, collection):
    # UpdateOne({'_id': 1}, {'$set': {'foo': 'bar'}})
    from common.config_db import schema_fields
    requests = []
    flag_perform_update = False
    for object_id, dict_to_update in dicts_with_items_to_set.items():
        if dict_to_update:
            flag_perform_update = True
            if schema_fields.chat in dict_to_update:
                chat = dict_to_update.pop(schema_fields.chat)
                requests.append(UpdateOne({schema_fields.reply_chat_id: object_id},
                                          {'$set': dict_to_update}))
                requests.append(UpdateOne({schema_fields.reply_chat_id: object_id},
                                          {'$push': {schema_fields.chat: chat}}))
            else:
                requests.append(UpdateOne({schema_fields.reply_chat_id: object_id}, {'$set': dict_to_update}))
    if flag_perform_update:
        try:
            collection.bulk_write(requests)
            return True
        except BulkWriteError or InvalidOperation as bwe:
            print(f"DB_ERROR: {bwe.details}")
            return False
    else:
        return False


def remove_from_collection_by_id(collection, ids_list):
    from common.config_db import schema_fields
    if not len(ids_list):
        return True

    requests = []
    for object_id in ids_list:
        requests.append(DeleteOne({schema_fields.id: object_id}))

    try:
        collection.bulk_write(requests)
        return True
    except BulkWriteError or InvalidOperation as bwe:
        print(f"DB_ERROR: {bwe.details}")
        return False


def remove_from_collection_by_reply_chat_id(reply_chat_id_list, collection):
    from common.config_db import schema_fields
    if not len(reply_chat_id_list):
        return True

    requests = []
    for object_id in reply_chat_id_list:
        requests.append(DeleteOne({schema_fields.reply_chat_id: object_id}))

    try:
        collection.bulk_write(requests)
        return True
    except BulkWriteError or InvalidOperation as bwe:
        print(f"DB_ERROR: {bwe.details}")
        return False


def check_and_move_documents():
    from common.config_db import schema_fields, active_collection, leads_collection
    try:
        requests_to_remove = []
        key = {schema_fields.user_registration_completed: True}
        user_schema = find_in_mongodb(key, active_collection)
        if user_schema.count():
            return True

        user_schema = find_in_mongodb(key, leads_collection)
        if user_schema.count():
            dump_to_mongodb(user_schema, active_collection)
            for user_details in user_schema:
                requests_to_remove.append(user_details[schema_fields.reply_chat_id])
            remove_from_collection_by_reply_chat_id(requests_to_remove, leads_collection)
            return True
        else:
            return False
    except BulkWriteError or InvalidOperation as bwe:
        print(f"DB_ERROR: {bwe.details}")
        return False
