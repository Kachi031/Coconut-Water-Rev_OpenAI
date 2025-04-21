import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Args:
    Assigned each sentiment to a variable and then created a graph for each of those sentiments 
    Return:
    Graph populates from print through the sentiment assigning
    
    """
    a= sentiments.count ("positive")
    b= sentiments.count ("negative")
    c= sentiments.count ("neutral")
    d= sentiments.count ("irrelevant")
    
    print(b)
    
    
    
    fig, ax = plt.subplots()
    ax.bar(["positive", "negative", "neutral", "irrelevant"], [a,b,c,d])
    ax.set_title("Test Plot")
    ax.set_xlabel("Sentiments")
    ax.set_ylabel("Amount of Sentiments")
    fig.savefig("images/Visual_sentiment")