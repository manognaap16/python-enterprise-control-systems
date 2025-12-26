from state_machine.states import TaskState


class FailureManager:
    def handle_failure(self, task):
        """
        Decide what to do when a task fails.
        """
        if task.retry_count < task.max_retries:
            task.retry_count += 1
            task.state = TaskState.RETRYING
            return "RETRY"
        else:
            task.state = TaskState.QUARANTINED
            return "QUARANTINE"
