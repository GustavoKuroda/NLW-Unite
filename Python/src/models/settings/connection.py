from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class __DBConnectionHandler:
    def __init__(self) -> None:
        """        Initialize the database connection.

        It initializes the database connection using the provided connection string and sets the session to None.

        Args:
            self: The object instance.
        """

        self.__connection_string = "{}:///{}".format(
            "sqlite",
            "storage.db"
        )
        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        """        Connect to the database using the provided connection string.

        This method establishes a connection to the database using the connection string provided during object initialization.
        """

        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        """        Returns the engine object associated with the current instance.

        Returns:
            object: The engine object associated with the current instance.
        """

        return self.__engine

    def __enter__(self):
        """        Context manager entry method for creating a session.

        This method is used as a context manager to create a session using the provided engine.

        Returns:
            Session: A session object for database interaction.
        """

        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """        Closes the session when exiting a context manager.

        This method is called when exiting a context manager and closes the session.

        Args:
            exc_type (type): The type of the exception raised, if any.
            exc_val (Exception): The exception raised, if any.
            exc_tb (traceback): The traceback object, if any.
        """

        self.session.close()

# Uses only one instance of a database connection
db_connection_handler = __DBConnectionHandler()