# pipeline/model_routing/hybrid_llm_wrapper.py
from pipeline.common.ai_rotator import AIRotator # Adjusted import path

class HybridLLMWrapper:
    def __init__(self):
        print("[HybridLLMWrapper] Initializing with AIRotator.")
        self.ai_rotator = AIRotator()
        # Ensure the context directory exists for the rotator
        import os
        from config import CONTEXT_FILE # Import to get directory
        context_dir = os.path.dirname(CONTEXT_FILE)
        if not os.path.exists(context_dir):
            os.makedirs(context_dir, exist_ok=True)
            print(f"[HybridLLMWrapper] Created context directory: {context_dir}")


    def route_and_generate(self, question, initial_answer, context, certainty_level):
        print(f"[HybridLLMWrapper] SIMULATING routing for '{question}' with certainty '{certainty_level}'")

        if certainty_level == "HIGH_UNCERTAINTY" or certainty_level == "MEDIUM_UNCERTAINTY":
            selected_ai = self.ai_rotator.next_ai()
            if selected_ai:
                print(f"[HybridLLMWrapper] Routing to powerful model. Selected AI: {selected_ai} (from AIRotator)")
                # Simulate using the selected AI
                refined_answer = f"Simulated HybridLLM ({selected_ai}) refined answer for: {question}"
                self.ai_rotator.record_usage(selected_ai)
                return refined_answer
            else:
                print("[HybridLLMWrapper] Wanted to use powerful model, but no AI available via AIRotator. Falling back.")
                return initial_answer # Fallback to initial answer
        else: # LOW_UNCERTAINTY
            print("[HybridLLMWrapper] Using initial answer is sufficient.")
            return initial_answer
