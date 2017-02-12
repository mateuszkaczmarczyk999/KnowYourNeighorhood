class Ui:


    @staticmethod
    def get_input(prompt, integer_input=False):
        """
        :param prompt: string
        :param integer_input: boolean
        :return: string or integer
        """

        while True:

            if not isinstance(prompt, str):
                raise TypeError("Prompt must be a string object")

            user_input = input(prompt)

            if integer_input:
                try:
                    return int(user_input)
                except:
                    continue
            else:
                return user_input


    @staticmethod
    def print_result(result):
        if not isinstance(result, list):
            raise TypeError("Result must be a list object")
        for val in result:
            print("----{}".format(val))


    @staticmethod
    def print_menu(header, options):
        """
        :param headers: string
        :param options: list of strings
        :return: None
        """

        print("{}\n".format(header))
        for idx, option in enumerate(options):
            print("({}) {}".format(idx+1, option))
        print("\n")

    @staticmethod
    def print_table(headers, table):
        """
        :param headers: list of strings
        :param table: list of lists
        :return: None
        """

        # initialize all the lists used in method
        retable = []
        width_list = []
        parsed_table = [headers] + table

        # calculate longest string in the content
        for i in range(len(parsed_table[0])):
            longest_string = 0
            for row in parsed_table:
                if len(str(row[i])) > longest_string:
                    longest_string = len(str(row[i]))
            width_list.append(longest_string)

        # print header
        retable.append("╔")
        for column in range(len(parsed_table[0])):
            retable.append("{0:═^{w}}".format("═", w=width_list[column] + 2))
            if column + 1 != len(parsed_table[0]):
                retable.append("╦")
        retable.append("╗\n")
        # print content
        for row_number, row in enumerate(parsed_table):
            for column, cell in enumerate(row):
                retable.append("║{0:^{w}}".format(str(cell), w=width_list[column] + 2))
            retable.append("║\n")
            if row_number + 1 != len(parsed_table):
                retable.append("╠")
                for column, cell in enumerate(row):
                    retable.append("{0:═^{w}}".format("═", w=width_list[column] + 2))
                    if column + 1 != len(parsed_table[0]):
                        retable.append("╬")
                retable.append("╣\n")
            # print footer
            if row_number + 1 == len(parsed_table):
                retable.append("╚")
                for column, cell in enumerate(row):
                    retable.append("{0:═^{w}}".format("═", w=width_list[column] + 2))
                    if column + 1 != len(parsed_table[0]):
                        retable.append("╩")
                retable.append("╝")

        print("".join(retable))