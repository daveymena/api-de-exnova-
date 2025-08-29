"""Module for Exnova http getregdata resource."""

from exnovaapi.http.resource import Resource
from exnovaapi.http.register import Register


class Getprofile(Resource):
    """Class for Exnova getregdata resource."""
    # pylint: disable=too-few-public-methods

    url = "/".join((Register.url, "getregdata"))

    def _get(self):
        """Send get request for Exnova API getregdata http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("GET")

    def __call__(self):
        """Method to get Exnova API getregdata http request.

        :returns: The instance of :class:`requests.Response`.
        """
        return self._get()
