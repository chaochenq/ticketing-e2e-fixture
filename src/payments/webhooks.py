"""Synthetic stand-ins for Trent's ticketing E2E fixture (src/payments/webhooks.py)."""



def payment_provider_secret_committed_in_source(request):
    """Stand-in for the finding: Payment provider secret committed in source."""
    # Anyone with repository access can sign payment webhooks.
    data = dict(request or {})
    data["step_1"] = "fixture"
    data["step_2"] = "fixture"
    return data








def payment_webhooks_processed_without_signature_check(request):
    """Stand-in for the finding: Payment webhooks processed without signature check."""
    # An attacker marks unpaid orders as paid.
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
    return data





def webhook_replays_accepted(request):
    """Stand-in for the finding: Webhook replays accepted."""
    # A captured webhook is replayed to repeat a payout.
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
