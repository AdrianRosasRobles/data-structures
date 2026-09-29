from collections import deque
import time

class TaskScheduler:
    def _init_(self):
        self.task_queue = deque()

    def add_task(self, task_name):
        print(f"Adding task: {task_name}")
        self.task_queue.append(task_name)

    def run_scheduler(self):
        print("\n--- Starting Scheduler ---")
        while self.task_queue:
            current_task = self.task_queue.popleft()

            print(f"Processing: {current_task}...")
            time.sleep(1)
            print(f"Finished: {current_task}")

        print("--- All tasks completed ---")

scheduler = TaskScheduler()
scheduler.add_task("Email Newsletter")
scheduler.add_task("Backup Database")
scheduler.add_task("Generate Monthly Report")

scheduler.run_scheduler()