def main():
    ages_dict = {"Bill": 17, "Jane": 34, "Jack": 56, "Sven": 13}
    new_ones = {name: age for name, age in ages_dict.items() if age < 18}
    print(new_ones)

    """
    Let's try it out
     - each of the ages need to be
        1) age by  1... they're getting older
        2) become decimal values
    """
    people = {"Jimbo": 14, "Bart": 10, "Lisa": 8, "Maggie": 1, "Ralph": 8, "Dolph": 14}


main()
