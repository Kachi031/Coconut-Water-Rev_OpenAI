from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Args:
        There is a filepath to the json file that contains reviews
    Returns:
        We are returning a list of sentiments for each line of review
        
    """
    # open the json object
    with open(filepath, "r") as js:
        results = json.load(js)

    # extract the reviews from the json file
    Extract_rev = results["results"]

    # get a list of sentiments for each line using get_sentiment
    rev_list = get_sentiment(Extract_rev)

    # plot a visualization expressing sentiment ratio
    make_plot(rev_list)

    return rev_list


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
