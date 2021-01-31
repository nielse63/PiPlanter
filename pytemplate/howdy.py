class Howdy:
    """
    The howdy module

    This is the extended description

    :param message: Message string
    :type message: str
    """

    def __init__(self, message: str):
        self.message: str = message

    def hello(self, str: str = "") -> str:
        """
        Print a fun message

        This is the extended description

        :param str: Message to print, defaults to ''
        :type str: str, optional
        :return: Output message
        :rtype: str
        """
        return f"Hi there {str}: {self.message}"
