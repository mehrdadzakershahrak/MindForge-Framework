def research(user_query, notes, queries, mission, output_format, refine_queries, lm_service):
    prompt = f"# Mission\n{mission}\n\n# User Query\n{user_query}\n\n# Notes\n{notes}\n\n# Previous Queries\n{queries}"
    response, tokens = lm_service.query_language_model(prompt)
    return queries, notes + "\n" + response, tokens

# Similar modifications can be made to other components.
