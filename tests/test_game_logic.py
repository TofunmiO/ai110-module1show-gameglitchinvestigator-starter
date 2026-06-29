from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_get_range_for_difficulty_returns_expected_bounds():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_rejects_values_outside_the_selected_range():
    ok, value, error = parse_guess("0", 1, 20)
    assert ok is False
    assert value is None
    assert error == "Guess must be between 1 and 20."

    ok, value, error = parse_guess("1", 1, 20)
    assert ok is True
    assert value == 1
    assert error is None


def test_parse_guess_rejects_values_below_1_and_above_100(): #generated test using AI agent
    for raw_guess in ["0", "-5", "101", "150"]:
        ok, value, error = parse_guess(raw_guess, 1, 100)
        assert ok is False
        assert value is None
        assert error == "Guess must be between 1 and 100."


def test_guess_lower_than_secret_returns_go_higher_hint(): #generated test using AI agent
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_guess_higher_than_secret_returns_go_lower_hint(): #generated test using AI agent
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_higher_than_secret_with_string_secret_returns_go_lower_hint(): #generated test using AI agent
    outcome, message = check_guess(100, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_update_score_awards_points_for_a_win():
    assert update_score(0, "Win", 1) == 80
    assert update_score(0, "Win", 9) == 10
