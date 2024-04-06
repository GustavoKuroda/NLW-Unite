# Operations with entities of Events

from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        """        Insert an event into the database.

        This function inserts an event into the database using the provided event information.

        Args:
            eventsInfo (Dict): A dictionary containing information about the event, including 'uuid', 'title', 'details', 'slug', and 'maximum_attendees'.

        Returns:
            Dict: The input eventsInfo dictionary.

        Raises:
            IntegrityError: If the event is already registered in the database.
            Exception: If any other exception occurs during the insertion process.
        """

        with db_connection_handler as database:
            try:
                event = Events(
                    id=eventsInfo.get("uuid"),
                    title=eventsInfo.get("title"),
                    details=eventsInfo.get("details"),
                    slug=eventsInfo.get("slug"),
                    maximum_attendees=eventsInfo.get("maximum_attendees"),
                )
                database.session.add(event)
                database.session.commit()

                return eventsInfo
            
            except IntegrityError:
                raise Exception('Evento ja cadastrado')
            
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_eventy_by_id(self, event_id: str) -> Events:
        """        Retrieve an event by its ID.

        This method retrieves an event from the database based on the provided event ID.

        Args:
            event_id (str): The unique identifier of the event.

        Returns:
            Events: The event object corresponding to the provided event ID.

        Raises:
            NoResultFound: If no event is found for the given event ID in the database.
        """

        with db_connection_handler as database:
            try:
                event = (
                    database.session
                    .query(Events)
                    .filter(Events.id == event_id)
                    .one()
                )
                return event
            
            except NoResultFound:
                return None