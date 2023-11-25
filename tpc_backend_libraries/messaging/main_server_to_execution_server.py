from pydantic import BaseModel
from enum import IntEnum


class ExecutionStatus(IntEnum):
    SUCCESS = 0
    FAILURE = 1


class RunPodRequest(BaseModel):
    repository_url: str
    repository_user: str
    repository_access_key: str
    image_name: str
    job_id: str
    s3_bucket: str
    s3_key: str
    s3_access_key: str
    s3_secret_key: str
    execution_server_ip: str
    execution_server_port: int


class ExecutionServerClientWSDetails(BaseModel):
    ip: str
    port: int

class ExecutionServerWSDetails(BaseModel):
    ip: str
    port: int

    client_details: ExecutionServerClientWSDetails


class ExecutionResponse(BaseModel):
    job_id: str
    status: ExecutionStatus
