class DistrictNotFoundException(Exception):
    """
    Exception to be raised if correct district is not provided by user
    """

    def __init__(self, message="District not found for following text provided check district spelling."):
        self.message = message
        super().__init__(self.message)


class DistrictNotProvidedException(Exception):
    """
    Exception to be raised if  district is not provided by user
    """

    def __init__(self, message="District not provided"):
        self.message = message
        super().__init__(self.message)
