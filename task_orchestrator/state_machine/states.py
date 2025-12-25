from enum import Enum


class TaskState(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    RETRYING = "RETRYING"
    FAILED = "FAILED"
    QUARANTINED = "QUARANTINED"
    COMPLETED = "COMPLETED"
