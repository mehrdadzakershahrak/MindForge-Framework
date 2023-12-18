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

    # Add functions to the framework
    framework.add_function('research', research)
    framework.add_function('analysis', analysis)
    framework.add_function('drafting', drafting),
    
    # Define instructions for each component
    research_instructions = {
        '# MISSION': "You are a search query generator. You will be given a specific query or problem by the USER and you are to generate a JSON list of at most 5 questions that will be used to search the internet. Make sure you generate comprehensive and counterfactual search queries. Employ everything you know about information foraging and information literacy to generate the best possible questions.",
        '# REFINE QUERIES:' : "You might be given a first-pass information need, in which case you will do the best you can to generate ``naive queries`` (uninformed search queries). However the USER might also give you previous search queries or other background information such as accumulated notes. If these materials are present, you are to generate ``informed queries`` - more specific search queries that aim to zero in on the correct information domain. Do not duplicate previously asked questions. Use the notes and other information presented to create targeted queries and/or to cast a wider net.",
        '# OUTPUT FORMAT:' : "In all cases, your output must be a simple JSON list of strings. "
    }
     
    
    # Create tasks with instructions
    research_task = create_task("Research Task", ['research'], {'research': research_instructions})
    analysis_task = create_task("Analysis Task", ['analysis'], {'analysis': analysis_instructions})
    drafting_task = create_task("Drafting Task", ['drafting'], {'drafting': drafting_instructions})
    # Create other tasks...

    # Example usage
    researched_questions = ['What is AI?', 'Latest AI technologies']
    cached_data = {}  # Initialize an empty cache

    # Perform analysis
    notes, new_cache = framework.run_function('analysis', researched_questions, cached_data, lm_service, analysis_instructions)

    # Drafting process
    user_needs = "Need an overview of AI technologies"
    draft, iteration = framework.run_function('drafting', notes, user_needs, lm_service, drafting_instructions)

    print(f"Draft (Iteration {iteration}): {draft}")

if __name__ == "__main__":
    main()