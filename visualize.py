import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Assigned each sentiment to a variable and then created a graph for each of those sentiments 
    
    """
    data=()
    a= sentiments.count ("positive")
    b= sentiments.count ("negative")
    c= sentiments.count ("neutral")
    d= sentiments.count ("irrelevant")
    
    print(b)
    
    
    
    fig, ax = plt.subplots()
    ax.bar(["positive", "negative", "neutral", "irrelevant"], [a,b,c,d])
    ax.set_title("Test Plot")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    fig.savefig("images/")