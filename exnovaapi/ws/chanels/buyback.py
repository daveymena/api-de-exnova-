"""Module for Exnova buyback websocket chanel."""

from exnovaapi.ws.chanels.base import Base


class Buyback(Base):
    """Class for Exnova subscribe to buyback websocket chanel."""
    # pylint: disable=too-few-public-methods

    name = "buyback"

    def __call__(self):
        """Method to send message to buyback websocket chanel."""
        pass
