"""Synthetic stand-ins for Trent's ticketing E2E fixture (src/auth/session.py)."""










def session_cookie_accepted_without_signature_check(request):
    """Stand-in for the finding: Session cookie accepted without signature check."""
    # An attacker forges a session and acts as any user.
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
    return data













def session_id_kept_across_login(request):
    """Stand-in for the finding: Session id kept across login."""
    # A fixed session id lets an attacker ride a victim's login.
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
    return data








def session_cookie_sent_without_secure_flag(request):
    """Stand-in for the finding: Session cookie sent without Secure flag."""
    # The cookie travels over plain HTTP on a downgrade.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    return data






def sessions_survive_password_change(request):
    """Stand-in for the finding: Sessions survive password change."""
    # A stolen session stays valid after the user changes the password.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    data["step_5"] = "fixture"
    data["step_6"] = "fixture"
    data["step_7"] = "fixture"
    return data
