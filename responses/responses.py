from random import choice, randint

def get_responses(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == 'hi':
        return ':3'
    