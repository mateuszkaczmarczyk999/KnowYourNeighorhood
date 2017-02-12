import os
from ui import *
from location import *

class Menu:

    @staticmethod
    def display_menu():

        while True:

            header = "What would you like to do:"

            options = ["List statistics",
                       "Display 3 cities with longest names",
                       "Display county's name with the largest number of communities",
                       "Display locations, that belong to more than one category",
                       "Advanced search",
                       "Exit program"]

            os.system("clear")
            Ui.print_menu(header, options)
            user_input = Ui.get_input("Option: ", True)

            if user_input == 1:
                title, data = Location.list_statistics()
                Ui.print_table(title, data)
                Ui.get_input("Press Enter to continue.")

            if user_input == 2:
                title, data = Community.communities_sorted_by_length()
                Ui.print_table(title, data)
                Ui.get_input("Press Enter to continue.")

            if user_input == 3:
                title, data = County.counties_by_communities()
                Ui.print_table(title, data)
                Ui.get_input("Press Enter to continue.")

            if user_input == 4:
                title, data = Community.communities_category_count()
                Ui.print_table(title, data)
                Ui.get_input("Press Enter to continue.")

            if user_input == 5:
                phrase = Ui.get_input("Searching for: ")
                title, data = Location.advance_search(phrase)
                Ui.print_result(["Found {} locations.\n".format(len(data))])
                Ui.print_table(title, data)
                Ui.get_input("Press Enter to continue.")

            if user_input == 6:
                return
