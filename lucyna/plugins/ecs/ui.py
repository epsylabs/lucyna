from enum import Enum

from ...ui import StatusEnum


class TaskLifecycleStatusEnum(Enum):
    RUNNING = StatusEnum.ACTIVE.value
    ACTIVATING = StatusEnum.IN_PROGRESS.value
    DEACTIVATING = StatusEnum.IN_PROGRESS.value
    PENDING = StatusEnum.IN_PROGRESS.value
    STOPPING = StatusEnum.IN_PROGRESS.value
    PROVISIONING = StatusEnum.IN_PROGRESS.value
    DEPROVISIONING = StatusEnum.IN_PROGRESS.value
    STOPPED = StatusEnum.STOPPED.value
