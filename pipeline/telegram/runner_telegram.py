from common.config import telegram_api_key
from telegram.message_utils import get_messages_and_give_HOSPITALS, get_messages_and_give_UPDATE, welcome_buttons, save_telegram_request_to_db, user_registration_if_in_leads, \
    choose_a_model, start_session, end_session, get_messages_and_forward_to_FAQ_pipeline, get_messages_and_forward_to_QUICK_HEALTH_CHECK_pipeline, check_the_session, choose_a_model
import telebot
import time
from mongodb.mongodb_utils import check_and_move_documents


def get_messages():
    bot = telebot.TeleBot(telegram_api_key)

    @bot.message_handler(commands=['help'])
    def send_welcome1(message):
        choose_a_model(bot, message)

    @bot.message_handler(commands=['bye'])
    def send_welcome2(message):
        end_session(bot, message)

    @bot.message_handler(content_types=['text'])
    def handle_command_admin_window(message):
        save_telegram_request_to_db(bot, message)
        user_registration_if_in_leads(bot, message)

        check_and_move_documents()  # TODO: will go in other runner
        if message.text.upper() == welcome_buttons[0].upper():
            get_messages_and_forward_to_FAQ_pipeline(bot, message)
        elif message.text.upper() == welcome_buttons[1].upper():
            get_messages_and_forward_to_QUICK_HEALTH_CHECK_pipeline(bot, message)
        elif message.text.upper() == welcome_buttons[2].upper():
            get_messages_and_give_HOSPITALS(bot, message)
        elif message.text.upper() == welcome_buttons[3].upper():
            get_messages_and_give_UPDATE(bot, message)
        print(message.text)
        get_messages_and_forward_to_FAQ_pipeline(bot, message)
        get_messages_and_forward_to_QUICK_HEALTH_CHECK_pipeline(bot, message)

    while True:
        try:
            # bot waits for default time before terminating
            bot.polling(none_stop=True, interval=0, timeout=0)
        except:
            time.sleep(100)


if __name__ == "__main__":

    get_messages()