"""Synthetic stand-ins for Trent's ticketing E2E fixture (src/payments/refunds.py)."""




















def refunds_leave_no_audit_record(request):
    """Stand-in for the finding: Refunds leave no audit record."""
    # A refund cannot be traced to the person who issued it.
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
    return data











def any_support_agent_can_refund_any(request):
    """Stand-in for the finding: Any support agent can refund any amount."""
    # A support account drains funds through refunds.
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











def refund_service_runs_with_the_database(request):
    """Stand-in for the finding: Refund service runs with the database owner role."""
    # A bug in refunds can alter any table.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    data["step_5"] = "fixture"
    data["step_6"] = "fixture"
    data["step_7"] = "fixture"
    return data








def refund_export_opens_formulas_in_spreadsheets(request):
    """Stand-in for the finding: Refund export opens formulas in spreadsheets."""
    # A crafted reason runs a formula in an analyst's sheet.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    data["step_5"] = "fixture"
    data["step_6"] = "fixture"
    return data
