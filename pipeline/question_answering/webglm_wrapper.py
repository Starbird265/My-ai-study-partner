# pipeline/question_answering/webglm_wrapper.py
class WebGLMWrapper:
    def get_answer(self, question, db_path):
        print(f"[WebGLMWrapper] SIMULATING getting answer for '{question}' using DB '{db_path}'")
        # In reality, this would call WebGLM
        retrieved_context = f"Simulated context for '{question}' from {db_path}"
        simulated_answer = f"Simulated WebGLM answer for: {question}"
        return simulated_answer, retrieved_context
