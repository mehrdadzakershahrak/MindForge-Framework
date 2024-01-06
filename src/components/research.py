def research(user_query, lm_service, instructions, notes="", queries=""):
    prompt = "\n\n".join([f"{key} {value}" for key, value in instructions.items()])
    prompt += f"\n\nUser Query: {user_query}\nNotes: {notes}\nPrevious Queries: {queries}"
    response = lm_service.query_language_model(prompt)
    return response
