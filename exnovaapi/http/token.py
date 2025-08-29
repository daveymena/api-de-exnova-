"""Module for Exnova http token resource."""

from exnovaapi.http.resource import Resource
from exnovaapi.http.auth import Auth


class Token(Resource):
    """Class for Exnova http token resource."""
    # pylint: disable=too-few-public-methods

    url = "/".join((Auth.url, "token"))

    def __init__(self, api):
        super(Token, self).__init__(api)

    def _get(self):
        """Send get request for Exnova API token http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("GET")

    def __call__(self):
        """Method to get Exnova API token http request.

        :returns: The instance of :class:`requests.Response`.
        """
        return self._get()
