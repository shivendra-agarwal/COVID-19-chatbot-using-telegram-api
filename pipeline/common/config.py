from common.config_utils import read_telegram_config, read_project_name, read_project_config_credentials


configs_folder = 'configs'
header_accept = "application/json"

# Get project name
PROJECT = read_project_name(configs_folder)

# Get telegram details of active project
config_telegram = read_telegram_config(configs_folder, PROJECT)
telegram_api_key = config_telegram.get('api_key', None)

# Get project config of active project
project_config = read_project_config_credentials(configs_folder, PROJECT)

welcome_message = project_config.get('welcome_message', None)
welcome_buttons = project_config.get('welcome_buttons', None)
first_time_user_registration_message = project_config.get('first_time_user_registration_message', None)
first_time_user_registration_question = project_config.get('first_time_user_registration_question', None)
first_time_user_registration_completed_message = project_config.get('first_time_user_registration_completed_message', None)
welcome_message_after_user_registration = project_config.get('welcome_message_after_user_registration', None)
get_updates = project_config.get('get_updates', None)
message_after_module = project_config.get('message_after_module', None)

model_selected_FAQs = project_config.get('model_selected_FAQs', None)
model_selected_QUICK_HEALTH_CHECK = project_config.get('model_selected_QUICK_HEALTH_CHECK', None)
model_selected_QUICK_HEALTH_CHECK_message = project_config.get('model_selected_QUICK_HEALTH_CHECK_message', None)

thank_you_messages = project_config.get('thank_you_messages', None)
greeting_message = project_config.get('greeting_message', None)

