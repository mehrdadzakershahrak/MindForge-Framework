from Task import Task
from sentence_transformers import SentenceTransformer, util

def self_talk(component1, component2, initial_input, lm_service, joint_response=True, threshold=0.5):
    response1 = component1(initial_input, lm_service)
    response2 = component2(initial_input, lm_service)
    
    if calculate_semantic_difference(response1, response2) > threshold:
        questions = [
            "Why did you do that?",
            "Why you didn't do what that have done?",
            "Why is what you propose to do is more efficient/safe/cheap than something that would have done?",
            "Why can't you do that?",
            "Why do I not need to do that at this point?"
        ]
        for question in questions:
            modified_question1 = question.replace("that", response2)
            modified_question2 = question.replace("that", response1)
            # Assuming lm_service can handle these questions
            lm_service.query_language_model(modified_question1)
            lm_service.query_language_model(modified_question2)

    if joint_response:
        return f"{response1} | {response2}"
    else:
        return (response1, response2)

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