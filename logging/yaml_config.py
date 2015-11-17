import logging.config
import yaml


def yaml_config(log_file):
    with open(log_file) as yaml_file:
        dict_file = yaml.load(yaml_file)
    return logging.config.dictConfig(dict_file)
