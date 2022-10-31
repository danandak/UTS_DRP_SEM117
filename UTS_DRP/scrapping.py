import snscrape.modules.twitter as sntwitter
import csv

with open("snscrape.csv", "w", encoding="utf-8", newline="") as f:
    header = ["No.","Tweets","Tendensi"]
    no_of_tweets = 1000
    writer = csv.writer(f)
    writer.writerow(header)

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper("krisis ekonomi 2023", "resesi").get_items()):
        if i >= no_of_tweets:   
            break
        content = [i+1, tweet.content, 0]
        writer.writerow(content)