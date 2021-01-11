from common.config_db import active_collection, pending_collection, leads_collection, abandoned_collection
from common.config_db import schema_fields
from pymongo.errors import ConfigurationError, InvalidName, CollectionInvalid, ConnectionFailure
from common.config_db import config_db
from mongodb.mongodb_utils import dump_to_mongodb, find_in_mongodb, push_updates_to_db_reply_chat_id_key
from common.config_utils import get_timestamp
from telebot import types
from common.config import get_updates, welcome_buttons, first_time_user_registration_message, \
    first_time_user_registration_question, welcome_message, first_time_user_registration_completed_message, \
    welcome_message_after_user_registration, model_selected_FAQs, model_selected_QUICK_HEALTH_CHECK_message, \
    model_selected_QUICK_HEALTH_CHECK, message_after_module
from random import randint
from analytics.runner import QUICK_HEALTH_CHECK_analysis, main_analytics


def welcome_with_message(welcome_message):
    return welcome_message[randint(0, len(welcome_message) - 1)]


def welcome_with_keyboard(buttons_list):
    welcome_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for iobject in buttons_list:
        welcome_keyboard.add(types.KeyboardButton(text=iobject))
    return welcome_keyboard


def user_registration_if_in_leads(bot, message):
    try:
        key = {schema_fields.reply_chat_id: message.chat.id}
        user_schema = find_in_mongodb(key, active_collection)
        if user_schema.count():
            return True
        user_schema = find_in_mongodb(key, leads_collection)
        if user_schema.count():
            for user_details in user_schema:
                # first_name
                if message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.first_name in user_details and not bool(user_details[
                                                                                                               schema_fields.first_name]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.first_name: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    # last_name
                elif message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.last_name in user_details and not bool(user_details[
                                                                                                              schema_fields.last_name]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.last_name: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    # age
                elif message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.age in user_details and not bool(user_details[
                                                                                                        schema_fields.age]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.age: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    # phone
                elif message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.phone in user_details and not bool(user_details[
                                                                                                          schema_fields.phone]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.phone: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    # email
                elif message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.email in user_details and not bool(user_details[
                                                                                                          schema_fields.email]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.email: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    # address
                elif message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.address in user_details and not bool(user_details[
                                                                                                            schema_fields.address]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.address: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    # city
                elif message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.city in user_details and not bool(user_details[
                                                                                                         schema_fields.city]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.city: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    # state
                elif message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.state in user_details and not bool(user_details[
                                                                                                          schema_fields.state]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.state: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    # pincode
                elif message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.pincode in user_details and not bool(user_details[
                                                                                                            schema_fields.pincode]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.pincode: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    # country
                elif message.chat.id == user_details[
                    schema_fields.reply_chat_id] and schema_fields.country in user_details and not bool(user_details[
                                                                                                            schema_fields.country]):
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.country: message.text,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)

        user_schema = find_in_mongodb(key, leads_collection)
        if user_schema.count():
            for user_details in user_schema:
                if schema_fields.first_name not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[0],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.first_name: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    0], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                elif schema_fields.last_name not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[1],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.last_name: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    1], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                elif schema_fields.age not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[2],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.age: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    2], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                elif schema_fields.phone not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[3],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.phone: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    3], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                elif schema_fields.email not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[4],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.email: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    4], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                elif schema_fields.address not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[5],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.address: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    5], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                elif schema_fields.city not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[6],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.city: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    6], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                elif schema_fields.state not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[7],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.state: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    7], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                elif schema_fields.pincode not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[8],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.pincode: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    8], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                elif schema_fields.country not in user_details:
                    bot.send_message(chat_id=message.chat.id,
                                     text=first_time_user_registration_question[9],
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.country: False,
                                                                            schema_fields.chat: create_chat_entries(
                                                                                first_time_user_registration_question[
                                                                                    9], None),
                                                                            schema_fields.timestamp_last_touch: get_timestamp()}},
                                                         leads_collection)
                    return False
                else:
                    bot.send_message(chat_id=message.chat.id,
                                     text=welcome_with_message(first_time_user_registration_completed_message),
                                     parse_mode='HTML')
                    bot.send_message(chat_id=message.chat.id,
                                     text=welcome_with_message(welcome_message_after_user_registration),
                                     reply_markup=welcome_with_keyboard(welcome_buttons),
                                     parse_mode='HTML')
                    push_updates_to_db_reply_chat_id_key(
                        {message.chat.id: {schema_fields.user_registration_completed: True,
                                           schema_fields.timestamp_last_touch: get_timestamp()}},
                        leads_collection)
                    return True

        """bot.send_message(chat_id=message.chat.id,
                         text=welcome_with_message(first_time_user_registration_message),
                         parse_mode='HTML')
        for iobject in first_time_user_registration_question:
            bot.send_message(chat_id=message.chat.id,
                             text=iobject,
                             parse_mode='HTML')"""
        # push_updates_to_db_reply_chat_id_key({message.chat.id: {schema_fields.first_name: "Shiv"}}, leads_collection)
    except ConfigurationError or InvalidName or CollectionInvalid or ConnectionFailure:
        raise ConfigurationError("[ERROR] User registration issue")


def create_chat_entries(agent_message, user_message):
    return {"agent": agent_message, "reply": user_message, "timestamp": get_timestamp()}


def save_telegram_request_to_db(bot, message):
    try:
        key = {schema_fields.reply_chat_id: message.chat.id}
        user_schema = find_in_mongodb(key, leads_collection)
        if not user_schema.count():
            entries = [{schema_fields.reply_chat_id: message.chat.id, schema_fields.timestamp: get_timestamp(),
                        schema_fields.timestamp_last_touch: get_timestamp(),
                        schema_fields.chat: [create_chat_entries(None, message.text)],
                        schema_fields.user_registration_completed: False}]
            dump_to_mongodb(entries, leads_collection)
            bot.send_message(chat_id=message.chat.id,
                             text=welcome_with_message(welcome_message),
                             parse_mode='HTML')
            bot.send_message(chat_id=message.chat.id,
                             text=welcome_with_message(first_time_user_registration_message),
                             parse_mode='HTML')
            # TODO: New user registration
            return True
        else:
            pass
    except ConfigurationError or InvalidName or CollectionInvalid or ConnectionFailure:
        raise ConfigurationError(f"{config_db.db_name} or {config_db.db_address} or a collection not found")


def get_messages_and_forward_to_FAQ_pipeline(bot, message):
    if message.text.upper() == welcome_buttons[0].upper():
        try:
            key = {message.chat.id: {schema_fields.active_model: message.text.upper(),
                                     schema_fields.chat: [create_chat_entries(None, message.text.upper())],
                                     schema_fields.timestamp_last_touch: get_timestamp()}}
            push_updates_to_db_reply_chat_id_key(key, active_collection)
            bot.send_message(chat_id=message.chat.id,
                             text=welcome_with_message(model_selected_FAQs),
                             parse_mode='HTML')
        except:
            return False
    else:
        try:
            key = {schema_fields.reply_chat_id: message.chat.id}
            user_schema = find_in_mongodb(key, active_collection)
            for user_details in user_schema:
                if user_details[schema_fields.active_model] == welcome_buttons[0].upper():
                    bot.send_message(chat_id=message.chat.id,
                                     text=main_analytics([message.text]),
                                     parse_mode='HTML')
                    key = {message.chat.id: {schema_fields.active_model: False,
                                             schema_fields.chat: [create_chat_entries(None, message.text.upper())],
                                             schema_fields.timestamp_last_touch: get_timestamp()}}
                    push_updates_to_db_reply_chat_id_key(key, active_collection)
        except:
            return False


def get_messages_and_forward_to_QUICK_HEALTH_CHECK_pipeline(bot, message):
    if message.text.upper() == welcome_buttons[1].upper():
        key = {message.chat.id: {schema_fields.active_model: message.text.upper(),
                                 schema_fields.chat: [create_chat_entries(None, message.text)],
                                 schema_fields.timestamp_last_touch: get_timestamp(),
                                 schema_fields.active_model_chat: model_selected_QUICK_HEALTH_CHECK}}
        push_updates_to_db_reply_chat_id_key(key, active_collection)
        bot.send_message(chat_id=message.chat.id,
                         text=welcome_with_message(welcome_with_message(model_selected_QUICK_HEALTH_CHECK_message)),
                         parse_mode='HTML')
    try:
        key = {schema_fields.reply_chat_id: message.chat.id}
        user_schema = find_in_mongodb(key, active_collection)
        for user_details in user_schema:
            active_model = user_details.get(schema_fields.active_model, None)
            active_model_chat = user_details.get(schema_fields.active_model_chat, None)
            count = -1
            reply_for_symptom = 0
            for symptoms in active_model_chat:
                count = count + 1
                if symptoms['reply'] is None:
                    print(symptoms['symptom'])
                    active_model_chat[count]['reply'] = False
                    key = {message.chat.id: {schema_fields.active_model: welcome_buttons[1].upper(),
                                             schema_fields.active_model_chat: active_model_chat,
                                             schema_fields.chat: [create_chat_entries(None, welcome_buttons[1].upper())],
                                             schema_fields.timestamp_last_touch: get_timestamp()}}
                    push_updates_to_db_reply_chat_id_key(key, active_collection)
                    bot.send_message(chat_id=message.chat.id,
                                     text=symptoms['symptom'],
                                     reply_markup=welcome_with_keyboard(symptoms['button']),
                                     parse_mode='HTML')
                    return False
                elif not symptoms['reply']:
                    active_model_chat[count]['reply'] = message.text
                    key = {message.chat.id: {schema_fields.active_model: welcome_buttons[1].upper(),
                                             schema_fields.active_model_chat: active_model_chat,
                                             schema_fields.chat: [create_chat_entries(symptoms['reply'], None)],
                                             schema_fields.timestamp_last_touch: get_timestamp()}}
                    push_updates_to_db_reply_chat_id_key(key, active_collection)
                else:
                    reply_for_symptom = reply_for_symptom + 1

            if reply_for_symptom == len(active_model_chat) - 1:
                bot.send_message(chat_id=message.chat.id,
                                 text='Checking...',
                                 parse_mode='HTML')
                symptoms_matching, flag_symptoms_matching = QUICK_HEALTH_CHECK_analysis(bot, message,
                                                                                        active_model_chat)
                if flag_symptoms_matching:
                    str_symptoms_matching = ', '.join([str(values) for values in symptoms_matching])
                    bot.send_message(chat_id=message.chat.id,
                                     text=str_symptoms_matching,
                                     parse_mode='HTML')
                elif flag_symptoms_matching:
                    bot.send_message(chat_id=message.chat.id,
                                     text="According to WHO, the symptoms does not match enough. You are safe!",
                                     parse_mode='HTML')
                key = {message.chat.id: {schema_fields.active_model: None,
                                         schema_fields.active_model_chat: None,
                                         schema_fields.timestamp_last_touch: get_timestamp()}}
                push_updates_to_db_reply_chat_id_key(key, active_collection)

    except:
        return False


def get_messages_and_give_UPDATE(bot, message):
    bot.send_message(chat_id=message.chat.id,
                     text=get_updates,
                     parse_mode='HTML')


def get_messages_and_give_HOSPITALS(bot, message):
    import json
    hospitals_details = json.loads('configs/TEST/hospitals.json')
    temp = 0

    for i in range(0, 5):
        with open('configs/TEST/hospitals.json') as f:
            hospital = json.load(f)
        if temp < 5:
            text = hospital['placeUrl'] + "\n" + hospital['title'] +"\n"+ hospital['address']+"\n"+hospital['phoneNumber']
            bot.send_message(chat_id=message.chat.id,
                             text=text,
                             parse_mode='HTML')
        else:
            break
def check_the_session():
    key = {schema_fields.reply_chat_id}
    user_schema = find_in_mongodb(key, active_collection)
    for user_details in user_schema:
        now = get_timestamp()
        timestamp_last_touch = user_details[schema_fields.timestamp_last_touch]
        if now - timestamp_last_touch >= 5:
            key = {user_details[schema_fields.reply_chat_id]: {schema_fields.active_model: None,
                                                               schema_fields.active_model_chat: None,
                                                               schema_fields.timestamp_last_touch: get_timestamp()}}
            push_updates_to_db_reply_chat_id_key(key, active_collection)


def choose_a_model(bot, message):
    bot.send_message(chat_id=message.chat.id,
                     text=welcome_with_message(message_after_module),
                     reply_markup=welcome_with_keyboard(welcome_buttons),
                     parse_mode='HTML')


def end_session(bot, message):
    bot.send_message(chat_id=message.chat.id,
                     text="It was nice talking to you. See you soon!",
                     parse_mode='HTML')


def start_session(bot, message):
    bot.send_message(chat_id=message.chat.id,
                     text="Hello!",
                     parse_mode='HTML')