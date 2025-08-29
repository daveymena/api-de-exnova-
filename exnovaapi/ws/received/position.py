"""Module for Exnova websocket."""

def position(api, message):
    if message["name"] == "position":
        api.position = message
