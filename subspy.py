import praw
import re
from collections import Counter

reddit = praw.Reddit(
    client_id="", #add your client id here
    client_secret="", #add your client secret here
    user_agent="subspyder by ", #add your reddit u/username after by
)

subreddit = reddit.subreddit('<subreddit you want to analyse>')

#this was the code i wrote in 30 min or so, the main idea is you can use re module to do any kind of text extraction.
# i in this script extracting the Mention of age and gender format used on all popular subreddits.
word_counter = Counter()
age_sex_counter = Counter()

for submission in subreddit.new(limit=20000):
    title = submission.title.lower()
    body = submission.selftext.lower()

    words = re.findall(r'\w+', title + ' ' + body)
    word_counter.update(words)

    age_sex_matches = re.findall(r'\b\d{1,2}[MFmf]\b', title + ' ' + body)
    age_sex_counter.update(age_sex_matches)

top_words = word_counter.most_common(2000)
top_age_sex = age_sex_counter.most_common(30)

# Define the file name
file_name = "reddit_analysis.txt"

# Open the file for writing
with open(file_name, "w") as file:
    file.write("Top Words:\n")
    for cnt, (word, count) in enumerate(top_words, start=1):
        file.write(f"{cnt}. {word}: {count}\n")
    
    file.write("\nTop Age/Sex Group:\n")
    for cnt, (age_sex, count) in enumerate(top_age_sex, start=1):
        file.write(f"{cnt}. {age_sex}: {count}\n")

print(f"Results have been written to {file_name}")
