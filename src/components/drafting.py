def drafting(user_query, lm_service, instructions, notes="", queries=""):
    # If 'searched_notes' and 'user_needs' are derived from 'notes' and 'user_query', adjust accordingly
    searched_notes = notes  # or some processing based on 'notes'
    user_needs = user_query  # or some processing based on 'user_query'
    iteration = 1  # If iteration is needed, determine how to incorporate it

    prompt = "\n\n".join([f"{key} {value}" for key, value in instructions.items()])
    prompt += f"\n\nUser Needs: {user_query}\nSearched Notes: {notes}\nIteration: 1"  # Adjust as needed

    full_response = lm_service.query_language_model(prompt)
    return full_response
