import json


class DistrictNotFoundException(Exception):
    """
    Exception to be raised if correct district is not provided by user
    """
    pass


class DistrictNotProvidedException(Exception):
    """
    Exception to be raised if  district is not provided by user
    """
    pass


class NepalMunicipality:
    def __init__(self, district_name=None):
        self._district_name = district_name
        f = open('data/data.json', 'r')
        self._data = json.loads(f.read())
        self._district = []

    def all_districts(self):
        """
        Use this method to get a list of all districts of nepal
        """
        for items in self._data:
            for item in items.keys():
                self._district.append(item)
        return self._district

    def all_municipalities(self):
        """
        Use this to get list of all municipalities of specific district
        provided from class instance if district is none You will get None as return Value
        """
        if self._district_name is not None:
            for items in self._data:
                if self._district_name in self.all_districts():
                    if items.get(self._district_name) is not None:
                        return items.get(self._district_name)
                else:
                    raise DistrictNotFoundException('District not found for following text provided check district '
                                                    'spelling.')
        raise DistrictNotProvidedException('District not provided please provided district.')


