
def main():
    names = ["Jimbo", "Bart", "Lisa", "Maggie", "Ralph", "Martin", "Dolph"]
    ages = [14, 10, 8, 1, 8, 10, 14]


def get_dictionary_1(list_1, list_2):
    """manually create dictionary from parallel lists"""
    new_dict = {}
    for i in range(len(list_1)):
        new_dict[list_1[i]] = list_2[i]
    return new_dict


def get_dictionary_2(list_1, list_2):
    """manually create dictionary from parallel lists using enumerate"""
    new_dict = {}
    for i, name in enumerate(list_1):
        new_dict[name] = list_2[i]
    return new_dict


def get_dictionary_3(list_1, list_2):
    """simply zip up parallel lists into a single dictionary"""
    new_dict = dict(zip(list_1, list_2))
    return new_dict


main()
