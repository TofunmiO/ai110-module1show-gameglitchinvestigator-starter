def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy": # Refactored logic into logic_utils.py using agent mode
        return 1, 20
    if difficulty == "Normal": # Refactored logic into logic_utils.py using agent mode
        return 1, 100
    if difficulty == "Hard": # Refactored logic into logic_utils.py using agent mode
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:  #Refactored logic into logic_utils.py using agent mode
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret): #generated and updated logic using AI agent
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    try: #generated and updated logic using AI agent
        guess_value = int(guess)
        secret_value = int(secret)
    except (TypeError, ValueError): #generated and updated logic using AI agent
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

    if guess_value == secret_value:
        return "Win", "🎉 Correct!"

    if guess_value > secret_value:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":  #Refactored logic into logic_utils.py using agent mode
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":  #Refactored logic into logic_utils.py using agent mode
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
