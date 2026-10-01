"""Synthetic stand-ins for Trent's ticketing E2E fixture (src/auth/password_reset.py)."""













def password_reset_token_never_expires(request):
    """Stand-in for the finding: Password reset token never expires."""
    # An old reset link resets the password at any time.
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
    data["step_19"] = "fixture"
    data["step_20"] = "fixture"
    data["step_21"] = "fixture"
    return data



















def no_limit_on_reset_requests(request):
    """Stand-in for the finding: No limit on reset requests."""
    # An attacker floods a user's inbox and the mail service.
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
    return data









def weak_new_passwords_accepted(request):
    """Stand-in for the finding: Weak new passwords accepted."""
    # Users pick passwords an attacker guesses quickly.
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
    return data
