class AlgumaCoisa:
    def __enter__(self):
        """        Context manager entry method.

        This method is called when entering a context managed block. It prints a message indicating that it is entering the block.
        """

        print('Estou entrando')

    def __exit__(self, exc_type, exc_val, exc_tb):
        """        Method to exit the context manager.

        This method is called when exiting the context manager. It can be used to perform any necessary cleanup operations.

        Args:
            exc_type (type): The type of the exception that occurred, if any.
            exc_val (Exception): The exception that occurred, if any.
            exc_tb (traceback): The traceback of the exception that occurred, if any.
        """

        print('Estou saindo')


with AlgumaCoisa() as ola:
    print('Estou no meio')