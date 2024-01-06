def split(user_query, lm_service, instructions, notes="", queries=""):
    # Constructing the prompt from the instructions
    prompt_instructions = "\n".join([f"{key}: {value}" for key, value in instructions.items()])
    prompt = f"{prompt_instructions}\n\nUser Query: {user_query}\nNotes: {notes}\nPrevious Queries: {queries}"
    
    # Querying the language model with the constructed prompt
    response = lm_service.query_language_model(prompt)
    return response
