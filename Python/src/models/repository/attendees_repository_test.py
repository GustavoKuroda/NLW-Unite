# Integration tests for "attendees_repository.py"

import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo Registro no banco de dados")
def test_insert_attendee():
    """    Test the insertion of an attendee into the database.

    This function tests the insertion of an attendee into the database by creating a sample attendee information
    and then calling the insert_attendee method of the AttendeesRepository class to insert the attendee.

    Returns:
        str: The response from the insert_attendee method.
    """

    event_id = "meu-uuid-e-nois"
    attendees_info = {
        "uuid": "meu_uuid_ateendee",
        "name": "ateendee name",
        "email": "email@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="Nao precisa")
def test_get_attendee_badge_by_id():
    """    Test the retrieval of an attendee's badge by ID.

    This function tests the functionality of retrieving an attendee's badge by their unique ID from the attendees repository.

    Returns:
        str: The attendee's badge retrieved by ID.
    """

    attendee_id = "meu_uuid_ateendee"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)
    print(attendee)
    print(attendee.title)