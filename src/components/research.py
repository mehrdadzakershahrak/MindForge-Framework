def research(user_query, notes, queries, lm_service, instructions):
    prompt = "\n\n".join([f"{key} {value}" for key, value in instructions.items()])
    prompt += f"\n\nUser Query: {user_query}\nNotes: {notes}\nPrevious Queries: {queries}"
    response, tokens = lm_service.query_language_model(prompt)
    return response, tokens
