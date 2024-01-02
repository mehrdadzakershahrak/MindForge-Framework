def split(user_query, notes, queries, lm_service, instructions):
    # Constructing the prompt from the instructions
    prompt = "\n\n".join([f"{key} {value}" for key, value in instructions.items() if key.isupper()])
    prompt += f"\n\nUser Query: {user_query}\nNotes: {notes}\nPrevious Queries: {queries}"
    
    # Querying the language model with the constructed prompt
    response = lm_service.query_language_model(prompt)
    return response
