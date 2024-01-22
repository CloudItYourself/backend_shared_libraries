from pydantic import BaseModel


class KubernetesAccessResponse(BaseModel):
    k8s_config_file: str
