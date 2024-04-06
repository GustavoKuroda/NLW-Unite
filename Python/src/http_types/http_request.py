from typing import Dict

class HttpRequest:
    def __init__(self, body: Dict = None, param: Dict = None) -> None:
        """        Initialize the class instance with body and param.

        Args:
            body (Dict?): A dictionary representing the body.
            param (Dict?): A dictionary representing the parameters.
        """

        self.body = body
        self.param = param