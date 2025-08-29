"""Module for Exnova websocket."""

def instruments(api, message):
    if message["name"] == "instruments":
            api.instruments = message["msg"]