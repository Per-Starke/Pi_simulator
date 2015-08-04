__author__ = 'Per'

class Number(object):

    def __init__(self, number_as_string):
        self.Number_as_string = number_as_string


    def numbers_in_list(self):
        list_with_numbers_as_string = []
        for character in self.Number_as_string:
            if self.character_is_number(character) == True:
                list_with_numbers_as_string.append(character)
        return list_with_numbers_as_string

    def character_is_number(self, character_to_verify):
        if character_to_verify in ["0","1","2","3","4","5","6","7","8","9"]:
            is_number = True
        else:
            is_number = False
        return is_number

pi = Number("3.141 59265 359")

list_of_pi_numbers = pi.numbers_in_list()
print(list_of_pi_numbers) 
