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
    
    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        """        Find an event by its ID and return its details along with the count of attendees.

        Args:
            http_request (HttpRequest): The HTTP request object containing the event ID in the parameters.

        Returns:
            HttpResponse: The HTTP response object containing the event details and attendee count.

        Raises:
            Exception: If the event is not found.
        """

        event_id = http_request.param["event_id"]
        event = self.__events_repository.get_eventy_by_id(event_id)
        if not event: raise Exception("Evento nao encontrado")

        event_attendees_count = self.__events_repository.count_event_attendees(event_id)

        return HttpResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "detail": event.details,
                    "slug": event.slug,
                    "maximumAttendees": event.maximum_attendees,
                    "attendeesAmount": event_attendees_count["attendeesAmount"]
                }
            },
            status_code=200
        )