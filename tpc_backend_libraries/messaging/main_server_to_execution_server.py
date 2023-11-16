from pydantic import BaseModel
from enum import IntEnum
class ExecutionStatus(IntEnum):
    SUCCESS = 0
    FAILURE = 1
class RunPodRequest(BaseModel):
    image_name: str
    image_version: str
    job_id: str
    s3_bucket: str
    s3_key: str
    s3_access_key: str
    s3_secret_key: str
    execution_server_ip: str
    execution_server_port: int


class ExecutionResponse(BaseModel):
    job_id: str
    status: ExecutionStatus