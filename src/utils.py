from Task import Task
from sentence_transformers import SentenceTransformer, util

def self_talk(component1, component2, initial_input, lm_service, joint_response=True, threshold=0.5):
    response1 = component1(initial_input, lm_service)
    response2 = component2(initial_input, lm_service)

    # Ensure responses are strings
    response1_text = response1 if isinstance(response1, str) else str(response1)
    response2_text = response2 if isinstance(response2, str) else str(response2)
    
    if calculate_semantic_difference(response1_text, response2_text) > threshold:
        questions = [
            "Why did you do that?",
            "Why you didn't do what that have done?",
            "Why is what you propose to do is more efficient/safe/cheap than something that would have done?",
            "Why can't you do that?",
            "Why do I not need to do that at this point?"
        ]
        for question in questions:
            modified_question1 = question.replace("that", response2_text)
            modified_question2 = question.replace("that", response1_text)
            lm_service.query_language_model(modified_question1)
            lm_service.query_language_model(modified_question2)

    if joint_response:
        return f"{response1_text} | {response2_text}"
    else:
        return response1_text, response2_text

# Function to calculate cosine similarity
def cosine_similarity(embedding1, embedding2):
    return util.pytorch_cos_sim(embedding1, embedding2).item()

# Add more similarity functions as needed

def calculate_semantic_difference(response1, response2, similarity_func=cosine_similarity):
    model = SentenceTransformer('all-MiniLM-L12-v2')  # A pre-trained model

    # Convert responses to strings if they are not already
    response1 = str(response1) if not isinstance(response1, str) else response1
    response2 = str(response2) if not isinstance(response2, str) else response2

    # Encode the responses to get their embeddings
    embedding1 = model.encode(response1, convert_to_tensor=True)
    embedding2 = model.encode(response2, convert_to_tensor=True)

    # Calculate similarity based on the specified function
    similarity_score = similarity_func(embedding1, embedding2)

    # Return the difference (1 - similarity for 'difference')
    return 1 - similarity_score

def think_out_loud(initial_response, refinement_func, iterations, *args):
    refined_response = initial_response
    for _ in range(iterations):
        refined_response = refinement_func(refined_response, *args)
    return refined_response

# Dynamic task composition
def create_task(name, component_sequence, instructions, task_type='standard'):
    return Task(name, component_sequence, instructions, task_type)

def self_talk_with_feedback(component1, component2, initial_input, lm_service, feedback, memory_store):
    response1 = component1(initial_input, lm_service)
    response1_embedding = generate_embedding(response1)
    high_quality, noise = memory_store.process_feedback(response1, feedback)
    refined_embedding = memory_store.refine_embedding(response1_embedding, high_quality, noise)
    refined_response1 = memory_store.generate_response_from_embedding(refined_embedding)
    
    response2 = component1(initial_input, lm_service)
    response2_embedding = generate_embedding(response1)
    high_quality, noise = memory_store.process_feedback(response2, feedback)
    refined_embedding = memory_store.refine_embedding(response2_embedding, high_quality, noise)
    refined_response2 = memory_store.generate_response_from_embedding(refined_embedding)

    memory_store.add_interaction(initial_input, response1, feedback, similarity_between_feedback_and_response1)
    return refined_response1, refined_response2

def think_out_loud_with_feedback(initial_response, refinement_func, iterations, memory_store, *args):
    refined_response = initial_response
    for _ in range(iterations):
        refined_response = refinement_func(refined_response, *args)
        feedback = memory_store.capture_human_feedback(refined_response)
        high_quality, noise = memory_store.process_feedback(refined_response, feedback)
        refined_embedding = memory_store.refine_embedding(refined_response, high_quality, noise)
        refined_response = memory_store.generate_response_from_embedding(refined_embedding)
    return refined_response
