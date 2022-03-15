

class GenStrategy:
    """A class to store sequence"""

    MAGIC_NUMBER = 27
    """A number of tabs in str"""

    def __init__(self, space_bool, first_split_string_list, second_split_string_list, dictionary):
        self.space_bool: bool = space_bool
        """If first ten elements are empty - return True"""
        self.first_split_string_list: list = first_split_string_list
        """Constant, which include string"""
        self.second_split_string_list = second_split_string_list
        """Constant, which include second floor string"""
        self.dictionary: dict = dictionary
        """Dictionary which conclude first word like a key"""

    def space_determinant(self):
        """If tabs_counter = 10 - return True"""
        open_file = open('genbank.GENBANK')
        reader = open_file.readline()
        for i in reader:
            tabs = i
            if tabs[:10] == ' ':
                true_or_not = True
                self.space_bool = true_or_not
                return true_or_not

    def first_space_reader(self):
        """Returns split string"""
        open_file = open('genbank.GENBANK')
        # Conclude split string
        split_string_in_list: list = []
        for i in range(self.MAGIC_NUMBER):
            readline_string = open_file.readline()
            if self.space_bool:
                split_string_in_list.append(readline_string.split())
            if readline_string[0] == ' ':
                continue
            elif readline_string[0] != ' ':
                split_string_in_list.append(readline_string.split())
            elif readline_string[3] == ' ':
                split_string_in_list.append(readline_string.split())
        self.first_split_string_list = split_string_in_list
        return split_string_in_list

    def second_space_reader(self):
        """Returns split string with first tab"""
        open_file = open('genbank.GENBANK')
        unimportant_list: list = []
        for i in range(self.MAGIC_NUMBER):
            string_list = open_file.readline()
            if self.space_bool:
                unimportant_list.append(string_list.split())
            if string_list[0] == ' ':
                unimportant_list.append(string_list.split())
            else:
                continue
        self.second_split_string_list = unimportant_list
        return unimportant_list


gen = GenStrategy(False, [], [], {})
gen.first_space_reader()
gen.second_space_reader()
gen.space_determinant()
for line in gen.first_split_string_list:
    print(line)
print(' ')
for line in gen.second_split_string_list:
    print(line)

