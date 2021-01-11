from common.config_utils import get_pipeline_config_local, get_timestamp
from common.config import PROJECT, configs_folder
from mongodb.mongodb_utils import get_db
import collections


config_db = get_pipeline_config_local(configs_folder, PROJECT)

db_collection_names = [
    'active',
    "pending",
    "completed",
    'leads',
    'abandoned'
]

db_collections_tuple = collections.namedtuple('collections', db_collection_names)
collection_names = db_collections_tuple(**dict([(x, x) for x in db_collection_names]))

db_field_names = [
    "initiated_from",
    "initiated_id",

    "reply_chat_id",
    "reply_url",
    "reply_from_username",

    'first_name',
    'last_name',
    'age',
    'phone',
    'email',
    'address',
    'city',
    'state',
    'pincode',
    'country',

    'chat',

    'active_model',
    'active_model_chat',
    'active_model_bool',

    'timestamp',
    "timestamp_last_touch",
    "timestamp_last_messaged",
    "timestamp_next_touch",

    "user_registration_completed"
]
db_fields_tuple = collections.namedtuple('schema', db_field_names)
schema_fields = db_fields_tuple(**dict([(x, x) if x != 'id' else (x, f"_{x}") for x in db_field_names]))
# schema for db entry
schema = {
    schema_fields.initiated_from: "",
    schema_fields.initiated_id: "",
    schema_fields.reply_chat_id: "",
    schema_fields.reply_url: "",
    schema_fields.reply_from_username: "",

    schema_fields.first_name: "",
    schema_fields.last_name: "",
    schema_fields.age: "",
    schema_fields.phone: "",
    schema_fields.email: "",
    schema_fields.address: "",
    schema_fields.city: "",
    schema_fields.state: "",
    schema_fields.pincode: "",
    schema_fields.country: "",

    schema_fields.chat: [],

    schema_fields.active_model: "",
    schema_fields.active_model_bool: False,
    schema_fields.active_model_chat: [],

    schema_fields.timestamp: get_timestamp(epoch=True),                    # time
    schema_fields.timestamp_last_touch: get_timestamp(epoch=True),         # time, timestamp of our last action with the item
    schema_fields.timestamp_last_messaged: get_timestamp(epoch=True),      # time, timestamp of (follow up) message
    schema_fields.timestamp_next_touch: "",

    schema_fields.user_registration_completed: False  # default Bool: False

}

collections_dict, active_collection, pending_collection, completed_collection, leads_collection, abandoned_collection = get_db()