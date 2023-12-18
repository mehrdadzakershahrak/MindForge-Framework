class FrameworkCore:
    def __init__(self):
        self.functions = {}

    def add_function(self, function_name, function):
        self.functions[function_name] = function

    def run_function(self, function_name, *args, **kwargs):
        return self.functions[function_name](*args, **kwargs)

def main():
    framework = FrameworkCore()
    # Add functions to framework...

    # Create tasks...
    research_task = create_task("Research Task", ['research'], {'research': research_instructions})
    drafting_task = create_task("Drafting Task", ['drafting'], {'drafting': drafting_instructions})

    # Create a pipeline
    pipeline = TaskPipeline([research_task, drafting_task])

    # Execute tasks sequentially
    sequential_result = pipeline.execute_sequentially(framework, ('initial input',))

    # Execute tasks in parallel
    parallel_results = pipeline.execute_in_parallel(framework, [('input1',), ('input2',)])

    print(f"Sequential Execution Result: {sequential_result}")
    print(f"Parallel Execution Results: {parallel_results}")

if __name__ == "__main__":
    main()
