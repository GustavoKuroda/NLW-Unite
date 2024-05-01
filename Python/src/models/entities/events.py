from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer


class Events(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)

    def __repr__(self):
        """        Return a string representation of the Events object.

        Returns:
            str: A string containing the title and maximum_attendees of the Events object.
        """

        return f"Events [title={self.title}, maximum_attendees={self.maximum_attendees}]"