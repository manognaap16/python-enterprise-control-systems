from scheduler.scheduler import TaskScheduler
from state_machine.task import Task


def main():
    scheduler = TaskScheduler()

    # Create sample tasks
    task1 = Task(task_id="TASK-001", max_retries=2)
    task2 = Task(task_id="TASK-002", max_retries=1)
    task3 = Task(task_id="TASK-003", max_retries=3)

    # Add tasks to scheduler
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)

    # Run scheduler multiple times to simulate retries
    for cycle in range(1, 6):
        print(f"\n--- Scheduler Cycle {cycle} ---")
        scheduler.run()


if __name__ == "__main__":
    main()
