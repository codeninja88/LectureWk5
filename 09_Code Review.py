"""
Bad Code example for refactoring in Lecture 5 Code Review Demo
"""

def main():
    """get and store names and breeds of dogs in dictionary"""
    totalDog = int(input("How many Dogs do you have?: "))
    dogDict = {}


    if totalDog > 0:
        for i in range(totalDog):
            name = input("Dog {}'s Name?: ".format(i))
            breed = input("{}'s breed?: ".format(name))
            dogDict[name] = breed
    print(dogDict)

    # TODO: fix naming
    # TODO: fix formatting
    # TODO: start counting dogs at 1, not 0
main()
