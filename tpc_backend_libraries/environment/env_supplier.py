import os
import certifi
from dataclasses import dataclass
from typing import Final

from pymongo import MongoClient

from tpc_backend_libraries.general.singleton import Singleton


@dataclass
class LoggerDetails:
    dataset: str
    api_token: str


@dataclass
class GitLabDetails:
    url: str
    token: str


@dataclass
class S3Details:
    user_name: str
    url: str
    bucket: str
    access_key: str
    secret_key: str


class EnvironmentSupplier(metaclass=Singleton):
    def __init__(self):
        self._mongo_uri = os.environ['MONGO_URI']
        self._mongo_client = MongoClient(self._mongo_uri, tlsCAFile=certifi.where())

    def get_axiom_logger_details(self) -> LoggerDetails:
        collection = self._mongo_client.Configurations.backend
        document = collection.find_one({'config_name': 'axiom_details'})
        return LoggerDetails(
            dataset=document['dataset'],
            api_token=document['api_token']
        )

    def get_gitlab_details(self) -> GitLabDetails:
        collection = self._mongo_client.Configurations.backend
        document = collection.find_one({'config_name': 'gitlab_details'})
        return GitLabDetails(
            url=document['repository_url'],
            token=document['access_key']
        )

    def get_user_code_s3_details(self) -> S3Details:
        collection = self._mongo_client.Configurations.backend
        document = collection.find_one({'config_name': 'user_s3'})
        return S3Details(
            url=document['s3_url'],
            bucket=document['s3_bucket'],
            access_key=document['s3_access_key'],
            secret_key=document['s3_secret_key'],
            user_name=document['s3_user']
        )

    def get_admin_s3_details(self) -> S3Details:
        collection = self._mongo_client.Configurations.backend
        document = collection.find_one({'config_name': 'admin_s3'})
        return S3Details(
            url=document['s3_url'],
            bucket=document['s3_bucket'],
            access_key=document['s3_access_key'],
            secret_key=document['s3_secret_key'],
            user_name=document['s3_user']
        )
