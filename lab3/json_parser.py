class JsonParser:
    """
     Class that represents json parser.
     It can serialize and deserialize objects.
     """

    @staticmethod
    def dumps(obj) -> str:
        """
        Serializes object to json string
        :param obj: object to serialization
        :return: string json representation of object
        """
        return ''

    @staticmethod
    def dump(obj, file):
        """
        Serializes object to json and writes it to file
        :param obj: object to serialization
        :param file: file to writing
        """

    @staticmethod
    def loads(obj: str):
        """
        Deserializes string to object
        :param obj: source string
        :return: deserialized object
        """
        return None

    @staticmethod
    def load(file):
        """
        Deserializes file content to object
        :param file: source file
        :return: deserialized object
        """
        return None
