import threading

class TaskPipeline:
    def __init__(self, tasks, resource_manager=None):
        self.tasks = tasks
        self.resource_manager = resource_manager

    def execute_sequentially(self, framework, initial_input):
        result = initial_input
        for task in self.tasks:
            result = task.execute(framework, result)
        return result

    def execute_in_parallel(self, framework, initial_inputs):
        results = [None] * len(self.tasks)
        threads = []

        def run_task(task_index, task, input_data):
            if self.resource_manager:
                self.resource_manager.acquire_resources()
            results[task_index] = task.execute(framework, input_data)
            if self.resource_manager:
                self.resource_manager.release_resources()

        for i, (task, input_data) in enumerate(zip(self.tasks, initial_inputs)):
            thread = threading.Thread(target=run_task, args=(i, task, input_data))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return results
    
    def execute_pipeline(self, initial_input):
        current_input = initial_input
        for task in self.tasks:
            current_input = task.execute(self, current_input)
        return current_input