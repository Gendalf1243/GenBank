import re
import string


class Profile:
    def __init__(self, first_dictionary, second_dictionary):
        self.first_dictionary: dict = first_dictionary
        self.second_dictionary: dict = second_dictionary

    def func_1(self):
        open_dictionary = open('genbank.GENBANK')
        for i in range(27):
            value_string: str = open_dictionary.readline()
            if value_string[0] == ' ':
                continue
            else:
                pattern = re.compile(r'\w+')
                key = pattern.search(value_string).group()
                self.first_dictionary[key] = value_string
        return self.first_dictionary

    def func_2(self):
        open_dictionary_1 = open('genbank.GENBANK')
        alphabet = string.ascii_uppercase
        for i in range(27):
            value_string_1: str = open_dictionary_1.readline()
            if (value_string_1[2] in alphabet) and (value_string_1[0] == ' '):
                pattern = re.compile(r'\w+')
                key_1 = pattern.search(value_string_1).group()
                self.second_dictionary[key_1] = value_string_1
        return self.second_dictionary


profile = Profile({}, {})
print(profile.func_1())
print(profile.func_2())
