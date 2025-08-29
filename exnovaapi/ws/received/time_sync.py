"""Module for Exnova websocket."""

def time_sync(api, message):
    if message["name"] == "timeSync":
        api.timesync.server_timestamp = message["msg"]