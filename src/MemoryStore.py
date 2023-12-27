from utils import self_talk_with_feedback, think_out_loud_with_feedback

class MemoryStore:
    def __init__(self):
        self.data = []

    def add_interaction(self, ai_response, human_feedback, similarity):
        self.data.append((ai_response, human_feedback, similarity))

    def apply_q_learning(self):
        # Implement your Q-learning logic here
        # Adjust AI behavior based on accumulated data
        pass

memory_store = MemoryStore()

# After each interaction
ai_response = "AI's response"
human_feedback = input("Your feedback: ")
similarity = compare_embeddings(ai_response, human_feedback)
memory_store.add_interaction(ai_response, human_feedback, similarity)

# Periodically or after certain conditions
memory_store.apply_q_learning()