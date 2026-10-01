"""Synthetic stand-ins for Trent's ticketing E2E fixture (src/payments/charge.py)."""






































def charge_amount_built_into_raw_sql(request):
    """Stand-in for the finding: Charge amount built into raw SQL."""
    # An attacker rewrites charge records through the amount field.
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











def card_processor_called_over_plain_http(request):
    """Stand-in for the finding: Card processor called over plain HTTP in staging."""
    # Card data crosses the network unencrypted.
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







def currency_code_not_validated(request):
    """Stand-in for the finding: Currency code not validated."""
    # An attacker charges in an unsupported currency to skew totals.
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





def failed_charges_not_logged(request):
    """Stand-in for the finding: Failed charges not logged."""
    # Support cannot explain a customer's failed payment.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    data["step_3"] = "fixture"
    data["step_4"] = "fixture"
    return data
