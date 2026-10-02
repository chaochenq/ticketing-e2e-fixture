"""Synthetic stand-ins for Trent's ticketing E2E fixture (src/auth/tokens.py)."""


















def access_tokens_written_to_the_request(request):
    """Stand-in for the finding: Access tokens written to the request log."""
    # Tokens in logs let a log reader replay requests.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    data["step_5"] = "fixture"
    data["step_6"] = "fixture"
    data["step_7"] = "fixture"
    data["step_8"] = "fixture"
    data["step_9"] = "fixture"
    data["step_10"] = "fixture"
    data["step_11"] = "fixture"
    return data














def jwt_algorithm_taken_from_the_token(request):
    """Stand-in for the finding: JWT algorithm taken from the token header."""
    # An attacker signs tokens with the none algorithm.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    data["step_5"] = "fixture"
    data["step_6"] = "fixture"
    data["step_7"] = "fixture"
    data["step_8"] = "fixture"
    data["step_9"] = "fixture"
    data["step_10"] = "fixture"
    data["step_11"] = "fixture"
    data["step_12"] = "fixture"
    data["step_13"] = "fixture"
    data["step_14"] = "fixture"
    data["step_15"] = "fixture"
    data["step_16"] = "fixture"
    data["step_17"] = "fixture"
    data["step_18"] = "fixture"
    return data

















def log_lines_built_from_raw_user(request):
    """Stand-in for the finding: Log lines built from raw user input."""
    # An attacker forges log entries with newlines.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    data["step_5"] = "fixture"
    data["step_6"] = "fixture"
    return data









def token_responses_cacheable(request):
    """Stand-in for the finding: Token responses cacheable."""
    # A shared cache may keep a token response.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    return data
