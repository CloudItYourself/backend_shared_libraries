from pydantic import BaseModel
class ContainerMetrics(BaseModel):
    pod_name: str
    cpu_utilization: float
    memory_used: float


class WorkerMetrics(BaseModel):
    total_cpu_utilization: float
    total_memory_used: float
    total_memory_available: float

    vm_cpu_utilization: float
    vm_cpu_allocated: float
    vm_memory_used: float
    vm_memory_available: float
    container_metrics: List[ContainerMetrics]


class WorkerDiscoveryMessage(BaseModel):
    worker_id: str