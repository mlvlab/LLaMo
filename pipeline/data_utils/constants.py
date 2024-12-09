# system messages
SYSTEM_BASE = "The following is a conversation between a curious human and AI assistant."
# SYSTEM_DETAIL = "The assistant gives helpful, detailed, and polite answers to the user's questions."
# SYSTEM_MESSAGE = SYSTEM_BASE + " " + SYSTEM_DETAIL
SYSTEM_MESSAGE = SYSTEM_BASE

# special media tokens
GRAPH = "<graph>"

# Role pattern tokens
HUMAN = "Human: "
AI = "AI: "

ROLE_PATTERNS = {
    "human": f"\n{HUMAN}",
    "user": f"\n{HUMAN}",
    "\n[|Human|] ": f"\n{HUMAN}",
    "gpt": f"\n{AI}",
    "\n[|AI|] ": f"\n{AI}",
}
MEDIA_TOKENS = {
    "graph": [GRAPH],
}

# constants
IGNORE_INDEX = -100  # default ignore index of CrossEntropyLoss

