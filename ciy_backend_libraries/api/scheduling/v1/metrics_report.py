import datetime

from pydantic import BaseModel


class WorkerMetrics(BaseModel):
    timestamp: datetime.datetime.timestamp
    total_cpu_utilization: float
    total_memory_used: float
    total_memory_available: float

    vm_cpu_utilization: float
    vm_cpu_allocated: float
    vm_memory_used: float
    vm_memory_available: float
