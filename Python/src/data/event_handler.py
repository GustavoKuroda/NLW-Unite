import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventHandler:
    def __init__(self) -> None:
        """        Initializes the class instance with an EventsRepository object.
        """

        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        """        Register a new event and return the event ID.

        This method registers a new event by adding a UUID to the request body and then inserts the event into the events repository.

        Args:
            http_request (HttpRequest): The HTTP request object containing the event details.

        Returns:
            HttpResponse: An HTTP response object with the event ID in the body and a status code of 200.
        """

        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)

        return HttpResponse(
            body={ "eventId": body["uuid"] },
            status_code=200
        )