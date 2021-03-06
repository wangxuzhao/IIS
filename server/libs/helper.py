import configparser
import json

def check_exist():
    """检测所需文件是否存在"""
    if os.path.isfile('config.ini'):
        return True
    else:
        return False

def get_config():
    configInstance = configparser.ConfigParser()
    if not check_exist():
        print('run init first')
        return
    configInstance.read('config.ini')
    return configInstance
    pass

def get_config_json():

def init():
    configInstance = configparser.ConfigParser()
    configInstance["target"] = {}
    configInstance["target"]["platform"]  = 'raspi'
    with open('config.ini', 'w') as configfile:
        configInstance.write(configfile)
    print('done')
