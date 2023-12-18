from FrameworkCore import FrameworkCore
from TaskPipeline import TaskPipeline
from ResourceManager import ResourceManager
from Task import create_task
from LanguageModelService import LanguageModelService
from self_talk import self_talk, think_out_loud
from components import analysis, drafting, research

def main():
    framework = FrameworkCore()
    lm_service = LanguageModelService(provider='openai')

    # Define and add functions to the framework
    framework.add_function('research', research)
    # Add other components as needed...
    framework.add_function('self_talk', self_talk)
    framework.add_function('think_out_loud', think_out_loud)
    
    # Define instructions for each component
    research_instructions = {
        'mission': "Generate search queries based on user input.",
        'output_format': "JSON",
        'refine_queries': "Refine and optimize queries."
    }
    # Define instructions for other components...

    # Create tasks with instructions
    research_task = create_task("Research Task", ['research'], {'research': research_instructions})
    # Create other tasks...

    # Create a pipeline of tasks
    resource_manager = ResourceManager(max_concurrent_tasks=3)
    pipeline = TaskPipeline([research_task], resource_manager)  # Add other tasks as needed

    # Execute tasks sequentially
    sequential_result = pipeline.execute_sequentially(framework, ('initial input', 'lm_service'))

    # Execute tasks in parallel with resource management
    parallel_results = pipeline.execute_in_parallel(framework, [('input1', 'lm_service'), ('input2', 'lm_service')])

    print(f"Sequential Execution Result: {sequential_result}")
    print(f"Parallel Execution Results with Resource Management: {parallel_results}")
    
    # Example usage of thinking out loud
    initial_response = "Initial prompt"
    refined_response = think_out_loud(initial_response, self_talk, 3, component1, component2, lm_service, True)

    print(f"Refined Response: {refined_response}")


if __name__ == "__main__":
    main()