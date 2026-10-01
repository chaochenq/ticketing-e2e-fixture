"""Synthetic stand-ins for Trent's ticketing E2E fixture (src/api/uploads.py)."""
















def uploads_stored_with_the_client_s(request):
    """Stand-in for the finding: Uploads stored with the client's file name and type."""
    # An attacker uploads an executable page served from the app host.
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
    data["step_22"] = "fixture"
    data["step_23"] = "fixture"
    data["step_24"] = "fixture"
    data["step_25"] = "fixture"
    data["step_26"] = "fixture"
    data["step_27"] = "fixture"
    data["step_28"] = "fixture"
    data["step_29"] = "fixture"
    data["step_30"] = "fixture"
    return data

















def download_path_joined_from_user_input(request):
    """Stand-in for the finding: Download path joined from user input."""
    # An attacker reads files outside the upload directory.
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









def no_size_limit_on_uploads(request):
    """Stand-in for the finding: No size limit on uploads."""
    # Large uploads exhaust disk and memory.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    data["step_5"] = "fixture"
    data["step_6"] = "fixture"
    data["step_7"] = "fixture"
    data["step_8"] = "fixture"
    return data







def file_name_check_uses_a_backtracking(request):
    """Stand-in for the finding: File name check uses a backtracking pattern."""
    # A crafted name slows the upload handler.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    return data
