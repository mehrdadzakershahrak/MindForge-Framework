from FrameworkCore import FrameworkCore
from TaskPipeline import TaskPipeline
from ResourceManager import ResourceManager
from LanguageModelService import LanguageModelService
from self_talk import self_talk, think_out_loud, create_task
from components import analysis, drafting, research

def read_instructions(file_path):
    instructions = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                key, value = line.split(None, 1)
                instructions[key] = value.strip()
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

    # Task execution and other logic...

if __name__ == "__main__":
    main()