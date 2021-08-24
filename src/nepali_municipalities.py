import json

from exceptions import DistrictNotFoundException, DistrictNotProvidedException


class NepalMunicipality:
    def __init__(self, district_name=None):
        self.district_name = district_name
        f = open('data.json', 'r')
        self.data = json.loads(f.read())
        self.district = []

    def all_districts(self):
        """
        Use this method to get a list of all districts of nepal
        """
        for items in self.data:
            for item in items.keys():
                self.district.append(item)
        return self.district

    def all_municipalities(self):
        """
        Use this to get list of all municipalities of specific district
        provided from class instance if district is none You will get None as return Value
        """
        if self.district_name is not None:
            for items in self.data:
                if self.district_name in self.all_districts():
                    if items.get(self.district_name) is not None:
                        return items.get(self.district_name)
                else:
                    raise DistrictNotFoundException
        raise DistrictNotProvidedException


print(NepalMunicipality('Kathmandu').all_municipalities())
