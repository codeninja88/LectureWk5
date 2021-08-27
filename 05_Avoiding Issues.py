sentence = "If i think like a programmer i will soon BECOME a programmer"


def main():
    pass


def get_counts_0(words):
    """Taking the risk..."""
    count_dict = {}
    for word in words:
        count_dict[word] += 1
    return count_dict


def get_counts_1(words):
    """Simple membership test"""
    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict


def get_counts_2(words):
    """Same thing but exception handling"""
    word_count = {}
    for word in words:
        try:
            word_count[word] += 1
        except KeyError:
            word_count[word] = 1
    return word_count


def get_counts_3(words):
    """Using the get method"""
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


main()
