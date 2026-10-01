"""Synthetic stand-ins for Trent's ticketing E2E fixture (src/api/admin.py)."""






def admin_routes_skip_the_role_check(request):
    """Stand-in for the finding: Admin routes skip the role check."""
    # Any signed-in user reaches admin actions.
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
    return data















def admin_page_shows_the_build_version(request):
    """Stand-in for the finding: Admin page shows the build version."""
    # The version helps an attacker pick known exploits.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    return data
