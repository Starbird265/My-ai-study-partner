AI_ROTATION_ORDER = ["openai", "claude", "kimi", "deepseek", "mistral"]

AI_LIMITS = {
    "openai": {"max_prompts": 10, "cooldown_mins": 180},
    "claude": {"max_prompts": 10, "cooldown_mins": 180},
    "kimi": {"max_prompts": 20, "cooldown_mins": 180},
    "deepseek": {"max_prompts": 30, "cooldown_mins": 90},
    "mistral": {"max_prompts": 9999, "cooldown_mins": 1},
}

CONTEXT_FILE = "context/context.json"