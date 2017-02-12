class Location:

    list_of_locations = []

    def __init__(self, id_of_location, name, type_of_location):
        self.id_of_location = id_of_location
        self.name = name
        self.type_of_location = type_of_location
        Location.list_of_locations.append(self)

    def __str__(self):
        return "{} -- {} -- {}".format(self.id_of_location, self.name, self.type_of_location)

    @classmethod
    def location_from_csv(cls, csv_row):
        id_of_location, name, type_of_location = csv_row[:4], csv_row[4], csv_row[5]
        cls(id_of_location, name, type_of_location)

    @classmethod
    def list_statistics(cls):

        list_of_category = []
        header = [""]

        for location in cls.list_of_locations:
            list_of_category.append(location.type_of_location)

            if isinstance(location, Province):
                header.append(location.name)

        table = []

        for uniq_category in sorted(set(list_of_category), reverse=True):
            count_of_category = list_of_category.count(uniq_category)
            row = [count_of_category, uniq_category]
            table.append(row)

        return header, table

    @classmethod
    def advance_search(cls, phrase):

        phrase = phrase.lower()

        header = ["LOCATION", "TYPE"]
        table = []

        for location in cls.list_of_locations:
            name = location.name.lower()
            if name.find(phrase) != -1:
                row = [location.name, location.type_of_location]
                table.append(row)

        table = sorted(table, key = lambda element: element[0].lower(), reverse=False)

        return header, table


class Community(Location):

    list_of_communities = []

    def __init__(self, id_of_location, name, type_of_location):
        super().__init__(id_of_location, name, type_of_location)
        Community.list_of_communities.append(self)

    @classmethod
    def communities_sorted_by_length(cls, count=3, descending=True):

        name_length_func = lambda community: len(community.name)
        sorted_communities = sorted(cls.list_of_communities, key=name_length_func, reverse=descending)

        header = ["LOCATION", "TYPE"]
        table = []

        for location in sorted_communities[:count]:
            row = [location.name, location.type_of_location]
            table.append(row)

        return header, table

    @classmethod
    def communities_category_count(cls, min_value=2):

        name_list = []
        communities = cls.list_of_communities

        for community in communities:
            name_list.append(community.name)

        header = ["LOCATION", "TYPE"]
        table = []

        for community in communities:
            count = name_list.count(community.name)
            if count > min_value:
                row = [community.name, community.type_of_location]
                table.append(row)

        return header, table


class Province(Location):

    list_of_provincies = []

    def __init__(self, id_of_location, name, type_of_location):
        super().__init__(id_of_location, name, type_of_location)
        self.counties = []
        Province.list_of_provincies.append(self)


class County(Location):

    list_of_counties = []

    def __init__(self, id_of_location, name, type_of_location):
        super().__init__(id_of_location, name, type_of_location)
        self.communities = []
        County.list_of_counties.append(self)

    @classmethod
    def counties_by_communities(cls, count=1, descending=True):

        community_count_func = lambda county: len(county.communities)
        sorted_counties = sorted(cls.list_of_counties, key=community_count_func, reverse=descending)

        header = ["LOCATION", "TYPE", "NUMBER OF COMMUNITIES"]
        table = []

        for county in sorted_counties[:count]:
            row = [county.name, county.type_of_location, len(county.communities)]
            table.append(row)

        return header, table