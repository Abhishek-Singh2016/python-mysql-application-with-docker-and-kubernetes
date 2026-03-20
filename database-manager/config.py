from typedconfig import Config, key, section, group_key
from typedconfig.source import EnvironmentConfigSource, DictConfigSource # pipenv install typed-config
import os
import json
from dotenv import load_dotenv # pipenv install python-dotenv


def parse_string(string):
    parsed = json.loads(string)
    return parsed


@section('APP')
class APP(Config):
    LOGGING_CONFIG = key(cast=str, default="logging_production_k8s.config")
    SAVE_FOLDER = key(cast=str, default="/tmp/save")


@section('DB_MOVIE')
class DB_MOVIE(Config):
    HOST = key(cast=str)
    DATABASE = key(cast=str)
    USER = key(cast=str)
    PASSWORD = key(cast=str)
    PORT = key(cast=int)


class AppConfig(Config):
    APP = group_key(APP)
    DB_MOVIE = group_key(DB_MOVIE)


def read_configuration() -> AppConfig:
    
    # option for using env files in different folder vs the script:
    #load_dotenv(dotenv_path="C:\\configurations\\env-files\\movie_app_env_local_db.env")
    #load_dotenv(dotenv_path="/usr/app/src/movie_app_env_k8s.env")
    #load_dotenv(dotenv_path="/usr/app/src/movie_app_env_docker_compose.env")
    #load_dotenv(dotenv_path="/mnt/c/configurations/env-files/movie_app_env_ubuntu.env")


    # option for using env files in the same folder as the script:
    #env_file = "env_movie_app_k8s.env"
    #env_file = "env_movie_app_docker_compose.env"
    #env_file = "env_movie_app_local_db.env"
    #env_file = "env_movie_app_ubuntu.env"
    #env_path = os.getcwd() + "/" + env_file   # works only if you run the file from the file's own directory
    #print(env_path)  # /usr/app/src/env_docker_compose.env
    #load_dotenv(env_path)  # take environment variables from .env file
    manual_dict = {
        "APP": {
            "LOGGING_CONFIG": os.environ.get("APP_LOGGING_CONFIG", "logging_production_k8s.config"),
            "SAVE_FOLDER": os.environ.get("APP_SAVE_FOLDER", "/tmp/save")
        },
        "DB_MOVIE": {
            "HOST":     os.environ.get("DB_HOST", "mysql-service"),
            "DATABASE": os.environ.get("DB_NAME", "mov"),
            "USER":     os.environ.get("USER_NAME", ""),
            "PASSWORD": os.environ.get("USER_PWD", ""), # No default for passwords (safety)
            "PORT":     str(os.environ.get("DB_PORT", "3306")) # Cast to int manually
        }
    }
    #AppConfig
    config = AppConfig()
    config.add_source(EnvironmentConfigSource())
    config.add_source(DictConfigSource(manual_dict))
    config.read()
    return config

config = read_configuration()
print(config)
print(config.APP.LOGGING_CONFIG)
print(config.DB_MOVIE.PASSWORD)  