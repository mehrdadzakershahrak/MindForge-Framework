import time

class ResourceManager:
    def __init__(self, max_concurrent_tasks=5):
        self.max_concurrent_tasks = max_concurrent_tasks
        self.current_tasks = 0

    def acquire_resources(self):
        while self.current_tasks >= self.max_concurrent_tasks:
            time.sleep(0.1)  # Wait before retrying
        self.current_tasks += 1

    def release_resources(self):
        self.current_tasks -= 1
