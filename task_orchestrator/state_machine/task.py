from state_machine.states import TaskState


class Task:
    def __init__(self, task_id, max_retries=3):
        self.task_id = task_id
        self.state = TaskState.PENDING
        self.retry_count = 0
        self.max_retries = max_retries

    def mark_running(self):
        self.state = TaskState.RUNNING

    def mark_completed(self):
        self.state = TaskState.COMPLETED

    def mark_failed(self):
        if self.retry_count < self.max_retries:
            self.retry_count += 1
            self.state = TaskState.RETRYING
        else:
            self.state = TaskState.QUARANTINED
