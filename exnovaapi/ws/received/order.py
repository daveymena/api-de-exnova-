"""Module for Exnova websocket."""

def order(api, message):
    if message["name"] == "order":
        api.order_data = message
