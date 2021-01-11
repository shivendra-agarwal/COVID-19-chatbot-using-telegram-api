import os
import json
import collections
import datetime


def read_project_name(configs_folder):
    project_name_file = os.path.join(configs_folder, 'active_project.json')
    with open(project_name_file, 'r') as f:
        project_name = json.load(f)
    print(project_name)
    return project_name.get('project_name', 'TEST')


def read_telegram_config(configs_folder, PROJECT):
    services_path = os.path.join(configs_folder, PROJECT, 'telegram_config.json')
    with open(services_path, 'r') as f:
        config_telegram = json.load(f)
    print("Chat with: ", config_telegram.get('first_name', None))
    return config_telegram


def get_pipeline_config_local(configs_folder, PROJECT):
    pipeline_config_dict_system = json.load(open(os.path.join(configs_folder, PROJECT, 'project_config.json'), 'r'))

    config_db_properties = ['db_address', 'db_name']
    db_collections_tuple = collections.namedtuple('config_db', config_db_properties)
    config_db = db_collections_tuple(**dict([(x, pipeline_config_dict_system[x]) for x in config_db_properties]))

    return config_db


def get_timestamp(epoch=False):
    if epoch:
        timestamp = datetime.datetime(1970, 1, 1, 0, 0, 0)
    else:
        timestamp = datetime.datetime.utcnow()
    return timestamp


def read_project_config_credentials(configs_folder, PROJECT):
    services_path = os.path.join(configs_folder, PROJECT, 'project_config.json')
    with open(services_path, 'r') as f:
        project_config = json.load(f)
    return project_config
