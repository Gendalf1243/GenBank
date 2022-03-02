

class GEN:
    def __init__(self, string_list_1, string_reader_str):
        self.string_list_1: list = string_list_1
        self.string_reader_str: str = string_reader_str

    def func(self):
        open_dictionary = open('genbank.GENBANK')
        informal_list: list = []
        for i in range(27):
            string_reader_str = open_dictionary.readline()
            if string_reader_str[0] == ' ':
                continue
            else:
                string_list_1 = open_dictionary.readline().split()
                informal_list.append(string_list_1)
        self.string_list_1 = informal_list
        return informal_list


gen = GEN([], '')
gen.func()
print(gen.string_list_1)
