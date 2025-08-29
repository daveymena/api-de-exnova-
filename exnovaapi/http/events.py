"""Module for Exnova http login resource."""

from exnovaapi.http.resource import Resource


class Events(Resource):
    """Class for Exnova login resource."""
    # pylint: disable=too-few-public-methods

    url = ""

    def send_http(self,method, data=None, headers=None):
        """Send get request for Exnova API login http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_http_request_v2(method=method, url="https://event.trade.exnova.com/api/v1/events",data=data)

    def __call__(self,method,data,headers=None):
        """Method to get Exnova API login http request.

        :param str username: The username of a Exnova server.
        :param str password: The password of a Exnova server.

        :returns: The instance of :class:`requests.Response`.
        """
         
         
        return self.send_http(method=method,data=data,headers=headers)
