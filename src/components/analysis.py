def analysis(researched_questions, cached_data, lm_service, instructions):
    notes = ""
    for question in researched_questions:
        if question not in cached_data:
            prompt = "\n\n".join([f"{key} {value}" for key, value in instructions.items()])
            prompt += f"\n\nAnalyze Question: {question}"
            response, tokens = lm_service.query_language_model(prompt)
            cached_data[question] = response
            notes += f"Question: {question}\nAnswer: {response}\n\n"
    
    return notes, cached_data
