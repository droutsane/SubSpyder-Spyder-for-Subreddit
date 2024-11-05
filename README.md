# Reddit Subreddit Analysis Tool

This project is a Python script designed to analyze posts within a specified Reddit subreddit. It collects data on frequently used words and common age/sex markers in the titles and body of posts, offering insight into popular terms and demographic trends. This tool is helpful for social research, content analysis, and understanding subreddit-specific language and topics.

## Features
- Fetches the latest posts from any specified subreddit
- Analyzes the word frequency within post titles and body text
- Identifies common age and sex markers (e.g., "20M," "25F") from post content
- Outputs results to a text file with a list of the top words and demographic markers

## Requirements
- [Python 3.6+](https://www.python.org/downloads/)
- [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/)

You can install PRAW via pip: pip install praw

Usage

Set Up the Reddit API Credentials: Obtain API credentials from Reddit's developer portal, then enter your client_id, client_secret, and user_agent in the script.
Run the Script: python your_script_name.py
    Execute the script in a Python environment.
    It will fetch data from the specified subreddit, analyze it, and write the results to reddit_analysis.txt.

Output

The script generates a file (reddit_analysis.txt) that contains:
A list of the top words, ranked by frequency.
A list of common age and sex groups in the posts.
