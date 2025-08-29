"""Module for Exnova websocket."""

def balances(api, message):
    if message["name"] == "balances":
        api.balances_raw = message