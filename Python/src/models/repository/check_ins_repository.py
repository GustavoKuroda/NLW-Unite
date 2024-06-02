from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError

class CheckInsRpository:
    def insert_check_in(self, attendee_id):
        """        Insert a check-in record for the given attendee ID.

        This function inserts a check-in record for the specified attendee ID into the database.
        If the check-in is already registered, it raises an IntegrityError.

        Args:
            attendee_id (int): The ID of the attendee for whom the check-in is being recorded.

        Returns:
            int: The ID of the attendee for whom the check-in was recorded.

        Raises:
            IntegrityError: If the check-in is already registered for the specified attendee ID.
            Exception: For any other unexpected errors during the check-in process.
        """

        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(attendeeId=attendee_id)
                )
                database.session.add(check_in)
                database.session.commit()
                return attendee_id
            
            except IntegrityError:
                raise Exception('Check In ja cadastrado')
            
            except Exception as exception:
                database.session.rollback()
                raise exception