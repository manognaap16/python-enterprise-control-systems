import random
from state_machine.task import Task
from state_machine.states import TaskState


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def run(self):
        for task in self.tasks:
            if task.state == TaskState.PENDING or task.state == TaskState.RETRYING:
                self._execute_task(task)

    def _execute_task(self, task: Task):
        task.mark_running()

        # Simulate success or failure
        success = random.choice([True, False])

        if success:
            task.mark_completed()
            print(f"Task {task.task_id} completed successfully")
        else:
            task.mark_failed()
            print(
                f"Task {task.task_id} failed. "
                f"State: {task.state.value}, Retries: {task.retry_count}"
            )
