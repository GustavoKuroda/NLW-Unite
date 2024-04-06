from typing import Dict

class HttpResponse:
    def __init__(self, body: Dict, status_code: int) -> None:
        """        Initialize the class instance with the provided body and status code.

        Args:
            body (Dict): A dictionary containing the response body.
            status_code (int): An integer representing the status code of the response.
        """

        self.body = body
        self.status_code = status_code