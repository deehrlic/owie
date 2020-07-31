import praw

reddit = praw.Reddit(client_id="DHIiBuNzG_WkAQ",
                     client_secret="og2LS94QeZ45FBweeuE_RHVa1eg",
                     user_agent="For posting recorded videos of a chair falling apart to a custom subreddit.",
                     username="owiehack",
                     password="drewee602")

subreddit = reddit.subreddit("owiehack")
subreddit.submit(title="owiehack test",url="https://imgur.com/r/bonehurtingjuice/2prFix9")
