"""Module for Exnova websocket."""

def positions(api, message):
    if message["name"] == "positions":
        api.positions = message
