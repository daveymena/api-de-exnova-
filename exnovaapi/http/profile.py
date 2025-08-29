"""Module for Exnova profile resource."""

from exnovaapi.http.resource import Resource


class Profile(Resource):
    """Class for Exnova profile resource."""
    # pylint: disable=too-few-public-methods

    url = "profile"
