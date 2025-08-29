"""Module for Exnova http getprofile resource."""

from exnovaapi.http.resource import Resource


class Getprofile(Resource):
    """Class for Exnova getprofile resource."""
    # pylint: disable=too-few-public-methods

    url = "getprofile"

    def _get(self):
        """Send get request for Exnova API getprofile http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("GET")

    def __call__(self):
        """Method to get Exnova API getprofile http request.

        :returns: The instance of :class:`requests.Response`.
        """
        return self._get()
