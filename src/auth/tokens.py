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














def jwt_algorithm_taken_from_the_token(token, signing_key):
    """Verify an access token with the one algorithm the service signs with.

    The algorithm is pinned to HS256 on the server. The token header's "alg"
    field is never read to choose how to verify, so a token claiming "none" or
    another algorithm is refused, and the signature is checked in constant time.
    """
    import base64
    import hashlib
    import hmac
    import json

    header_b64, payload_b64, signature_b64 = token.split(".")
    header = json.loads(base64.urlsafe_b64decode(header_b64 + "=="))
    if header.get("alg") != "HS256":
        raise PermissionError("only HS256 tokens are accepted")
    expected = hmac.new(signing_key, f"{header_b64}.{payload_b64}".encode(), hashlib.sha256).digest()
    given = base64.urlsafe_b64decode(signature_b64 + "==")
    if not hmac.compare_digest(expected, given):
        raise PermissionError("token signature does not verify")
    return json.loads(base64.urlsafe_b64decode(payload_b64 + "=="))

















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
