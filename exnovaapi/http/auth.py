"""Module for Exnova http auth resource."""

from exnovaapi.http.resource import Resource


class Auth(Resource):
    """Class for Exnova http auth resource."""
    # pylint: disable=too-few-public-methods

    url = "auth"
