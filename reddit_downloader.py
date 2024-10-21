import praw
import requests
import os
import time

# Set up Reddit API credentials
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

# Create a folder to store images if it doesn't exist
image_folder = input('insert the name of the folder: ')
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Function to download images
def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)

# Function to collect images from the subreddit
def download_images_from_subreddit(subreddit_name, post_limit=100000000):
    subreddit = reddit.subreddit(subreddit_name)
    
    # Loop through posts and collect images
    downloaded_images = 0
    for submission in subreddit.hot(limit=post_limit):  # Fetch posts
        # Check if the submission has an image link
        if submission.url.endswith(('jpeg', 'png', 'gif', 'mp4')):
            file_name = os.path.join(image_folder, submission.url.split('/')[-1])
            
            # Download the image
            download_image(submission.url, file_name)
            downloaded_images += 1
            print(f"Downloaded: {file_name}")

            # Stop if we've downloaded the desired number of images
            if downloaded_images >= post_limit:
                break
        
        # Avoid hitting Reddit API rate limits
        time.sleep(2)

# Ask the user to input a subreddit name
subreddit_name = input("Enter the subreddit name to download images from: ")

# Ask the user for the number of images to download
post_limit = int(input("Enter the number of images to download: "))

# Download images from the specified subreddit
download_images_from_subreddit(subreddit_name, post_limit)
# Download images from the specified subreddit
download_images_from_subreddit(subreddit_name, post_limit)
