def drafting(searched_notes, user_needs, lm_service, instructions, iteration=1):
    prompt = "\n\n".join([f"{key} {value}" for key, value in instructions.items()])
    prompt += f"\n\nUser Needs: {user_needs}\nSearched Notes: {searched_notes}\nIteration: {iteration}"
    draft, tokens = lm_service.query_language_model(prompt)
    return draft, iteration + 1
