def analysis(user_query, lm_service, instructions, notes="", queries=""):
    # If 'researched_questions' and 'cached_data' are derived from 'user_query', 'notes', and 'queries', adjust accordingly
    researched_questions = queries.split(";")  # assuming 'queries' is a semicolon-separated string
    cached_data = {}  # or some initialization based on 'notes'

    notes = ""
    for question in researched_questions:
        if question not in cached_data:
            prompt = "\n\n".join([f"{key} {value}" for key, value in instructions.items()])
            prompt += f"\n\nAnalyze Question: {question}"
            response = lm_service.query_language_model(prompt)
            cached_data[question] = response
            notes += f"Question: {question}\nAnswer: {response}\n\n"
    return notes
