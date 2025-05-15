import json, time, os
from config import AI_ROTATION_ORDER, AI_LIMITS, CONTEXT_FILE

class AIRotator:
    def __init__(self):
            self.context = self.load_context()

                def load_context(self):
                        if os.path.exists(CONTEXT_FILE):
                                    with open(CONTEXT_FILE, "r") as f:
                                                    return json.load(f)
                                                            return {ai: {"used": 0, "last_used": 0} for ai in AI_ROTATION_ORDER}

                                                                def save_context(self):
                                                                        with open(CONTEXT_FILE, "w") as f:
                                                                                    json.dump(self.context, f, indent=2)

                                                                                        def is_ready(self, ai):
                                                                                                status = self.context.get(ai, {"used": 0, "last_used": 0})
                                                                                                        limit = AI_LIMITS[ai]
                                                                                                                since_last = time.time() - status["last_used"]
                                                                                                                        return status["used"] < limit["max_prompts"] or since_last > limit["cooldown_mins"] * 60

                                                                                                                            def next_ai(self):
                                                                                                                                    for ai in AI_ROTATION_ORDER:
                                                                                                                                                if self.is_ready(ai):
                                                                                                                                                                return ai
                                                                                                                                                                        return None

                                                                                                                                                                            def record_usage(self, ai):
                                                                                                                                                                                    now = time.time()
                                                                                                                                                                                            if time.time() - self.context[ai]["last_used"] > AI_LIMITS[ai]["cooldown_mins"] * 60:
                                                                                                                                                                                                        self.context[ai]["used"] = 0
                                                                                                                                                                                                                self.context[ai]["used"] += 1
                                                                                                                                                                                                                        self.context[ai]["last_used"] = now
                                                                                                                                                                                                                                self.save_context()
                                                                                                                                                                                                                                