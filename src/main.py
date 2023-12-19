from FrameworkCore import FrameworkCore
from TaskPipeline import TaskPipeline
from ResourceManager import ResourceManager
from LanguageModelService import LanguageModelService
from utils import self_talk, think_out_loud, create_task
from Task import Task
from components.research import research
from components.analysis import analysis
from components.drafting import drafting
from halo import Halo

def read_instructions(file_path):
    instructions = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                key, value = line.split(None, 1)
                formatted_key = key.strip('#').replace(' ', '').lower()
                if formatted_key:  # Ensure the key is not empty
                    instructions[formatted_key] = value.strip()
    return instructions


def main():
    framework = FrameworkCore()
    lm_service = LanguageModelService(provider='openai')

    # Add functions to the framework
    framework.add_component('research', research)
    framework.add_component('analysis', analysis)
    framework.add_component('drafting', drafting)
    # Add other components...

    # Read instructions for each component from files
    research_instructions = read_instructions('instructions/research.txt')
    analysis_instructions = read_instructions('instructions/analysis.txt')
    drafting_instructions = read_instructions('instructions/draft.txt')

    # Create tasks with instructions
    research_task = create_task("Research Task", ['research'], {'research': research_instructions})
    analysis_task = create_task("Analysis Task", ['analysis'], {'analysis': analysis_instructions})
    drafting_task = create_task("Drafting Task", ['drafting'], {'drafting': drafting_instructions})
    # Create other tasks...

    # Task execution and other logic
    
    # Define the number of iterations for research and analysis
    n_iterations = 3 # Example value
    user_input = input("Please enter the initial input: ")
    spinner = Halo(text='Thinking...', spinner='dots')
    spinner.start()
    
    # Sequential execution of tasks with iteration
    for _ in range(n_iterations):
        research_output = research_task.execute(framework, (user_input, '', '', lm_service))
        print(f"Research Task Output: {research_output}")

        analysis_output = analysis_task.execute(framework, (research_output, '', lm_service))
        print(f"Analysis Task Output: {analysis_output}")

    draft_output = drafting_task.execute(framework, (analysis_output, '', lm_service))
    print(f"Drafting Task Output: {draft_output}")
    
    spinner.stop()

if __name__ == "__main__":
    main()