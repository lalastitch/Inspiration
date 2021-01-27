import json
import random

class Quotes():

    # get a quote and returns a tuple of ("quote", "author")
    def get(self, id):

        # takes the json file and turns it into a list of dictionaries
        with open('quotes.json', 'r') as file:
            quoteDict = json.load(file)
        

        # takes a random quote from dictionary
        index = random.randint(0, len(quoteDict))
        chosenQuote = quoteDict[index]

        # turns the given quote dict into a tuple of ("quote", "author")
        tempList = [value for key, value in chosenQuote.items()]

        return tuple(tempList)

