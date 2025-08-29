"""Module for Exnova billing resource."""

from exnovaapi.http.resource import Resource


class Billing(Resource):
    """Class for Exnova billing resource."""
    # pylint: disable=too-few-public-methods

    url = "billing"
