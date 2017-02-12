import csv
from location import *

class DataReader:

    @classmethod
    def object_from_csv(cls, path):
        rows = cls.import_file(path)

        for row in rows:

            if row[3] != "" and row[3].isnumeric():
                Community.location_from_csv(row)
            if row[1] != "" and row[2] == "":
                County.location_from_csv(row)
            if row[1] == "":
                Province.location_from_csv(row)

        for county in County.list_of_counties:
            for community in Community.list_of_communities:
                if county.id_of_location[1] == community.id_of_location[1]:
                    county.communities.append(community)

        for province in Province.list_of_provincies:
            for county in County.list_of_counties:
                if province.id_of_location[0] == county.id_of_location[0]:
                    province.counties.append(county)

    @staticmethod
    def import_file(path):
        rows = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                rows.append(row)
        return rows
