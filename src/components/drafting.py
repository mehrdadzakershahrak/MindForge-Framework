def drafting(user_query, lm_service, instructions, notes="", queries=""):
    # Constructing the prompt from the instructions
    prompt_parts = [f"{key} {value}" for key, value in instructions.items()]
    prompt_parts.append(f"User Needs: {user_query}")
    
    # Include 'Searched Notes' in the prompt only if 'notes' is not empty
    if notes.strip():  # Checks if 'notes' is not just empty or whitespace
        prompt_parts.append(f"Searched Notes: {notes}")

    # Combine all parts into the final prompt
    prompt = "\n\n".join(prompt_parts)

    # Querying the language model with the constructed prompt
    full_response = lm_service.query_language_model(prompt)
    return full_response
