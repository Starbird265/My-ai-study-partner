# pipeline/orchestrator.py

from .data_ingestion.crawler_wrapper import AICrawlerWrapper
from .question_answering.webglm_wrapper import WebGLMWrapper
from .certainty_assessment.entropix_wrapper import EntropixWrapper
from .model_routing.hybrid_llm_wrapper import HybridLLMWrapper
# Import common data models if they were defined, e.g.:
# from .common.data_models import Question, Answer, Context

class PipelineOrchestrator:
    def __init__(self, math_content_urls=None):
        print("Initializing Pipeline Orchestrator...")
        self.crawler = AICrawlerWrapper()
        self.webglm = WebGLMWrapper()
        self.entropix = EntropixWrapper()
        self.hybrid_llm = HybridLLMWrapper()
        self.math_content_urls = math_content_urls if math_content_urls else []
        # Ensure the vector_db directory exists for the dummy crawler
        self.vector_db_dir = "pipeline/data_ingestion/vector_db/"
        self.vector_db_path = self.vector_db_dir + "math_db.index"
        import os
        os.makedirs(self.vector_db_dir, exist_ok=True)


        if self.math_content_urls:
            self._ingest_initial_content()

    def _ingest_initial_content(self):
        print(f"Starting initial content ingestion for URLs: {self.math_content_urls}")
        crawl_job_id = self.crawler.start_crawl(self.math_content_urls, self.vector_db_path)
        if crawl_job_id:
            print(f"Crawling initiated with job ID: {crawl_job_id}. Vector DB will be at {self.vector_db_path}")
        else:
            print("Failed to initiate crawling.")

    def process_question(self, user_question: str):
        print(f"\nReceived question: '{user_question}'")

        print("\nStep 1: Generating initial answer with WebGLM...")
        initial_answer, retrieved_context = self.webglm.get_answer(user_question, self.vector_db_path)
        if not initial_answer:
            print("Failed to get an initial answer from WebGLM.")
            return "Sorry, I could not process your question at this time."
        print(f"Retrieved context: {retrieved_context}")
        print(f"Initial answer: {initial_answer}")

        print("\nStep 2: Evaluating answer certainty with Entropix...")
        entropy_score, certainty_level = self.entropix.evaluate_certainty(initial_answer)
        print(f"Entropy score: {entropy_score}, Certainty level: {certainty_level}")

        print("\nStep 3: Performing adaptive model routing with HybridLLM...")
        final_answer = self.hybrid_llm.route_and_generate(
            user_question,
            initial_answer,
            retrieved_context,
            certainty_level
        )
        if not final_answer:
            print("HybridLLM did not provide a final answer, using initial answer.")
            final_answer = initial_answer

        print(f"\nFinal answer after HybridLLM routing: {final_answer}")
        return final_answer

def main():
    print("--- Starting Math Study Pipeline Demo ---")

    sample_math_urls = [
        "https://en.wikipedia.org/wiki/Algebra",
        "https://en.wikipedia.org/wiki/Calculus"
    ]

    orchestrator = PipelineOrchestrator(math_content_urls=sample_math_urls)

    question1 = "What is algebra?"
    answer1 = orchestrator.process_question(question1)
    print(f"\nQ: {question1}\nA: {answer1}")

    question2 = "Can you explain the fundamental theorem of calculus?"
    answer2 = orchestrator.process_question(question2)
    print(f"\nQ: {question2}\nA: {answer2}")

    print("\n--- Math Study Pipeline Demo Finished ---")

if __name__ == "__main__":
    main()
