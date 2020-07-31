import praw
from imgurpython import ImgurClient

def imgur():
    client_id = "9c5e85230d3df52"
    client_secret = "3d722b8f08385aef8ebb92c284457325ecb15347"

    client = ImgurClient(client_id,client_secret)

    response = client.upload_from_path("pog.png")
    print(response["link"])
    return response["link"]

def reddit(link,caption):
    reddit = praw.Reddit(client_id="DHIiBuNzG_WkAQ",
                         client_secret="og2LS94QeZ45FBweeuE_RHVa1eg",
                         user_agent="For posting recorded videos of a chair falling apart to a custom subreddit.",
                         username="owiehack",
                         password="drewee602")

    subreddit = reddit.subreddit("owiehack")
    subreddit.submit(title=caption,url=link)
