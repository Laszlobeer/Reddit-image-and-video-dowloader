
# Reddit Image Downloader

This script allows you to download images from a specific subreddit using Reddit's API and stores them in a local folder. You can specify the subreddit name and the number of images to download.

## Features
- Downloads images (`jpeg`, `png`, `gif`, `mp4`) from the **hot** posts of a subreddit.
- Stores images in a user-specified local folder.
- Automatically handles rate-limiting to avoid being blocked by Reddit.

## Prerequisites

1. **Python 3.x** should be installed. You can download it from [python.org](https://www.python.org/).
2. Install the following Python libraries:
   - `praw`: Python Reddit API Wrapper for interacting with Reddit.
   - `requests`: For downloading the image files.

You can install the required libraries using:

```bash
pip install praw requests
```

## Reddit API Setup

Before running the script, you need to set up a Reddit app to obtain API credentials. Follow these steps:

1. Go to [Reddit Developer Apps](https://www.reddit.com/prefs/apps).
2. Click **Create App**.
3. Fill in the required details and make sure to select **script** as the app type.
4. After creating the app, you'll receive:
   - `client_id`
   - `client_secret`
   - `user_agent`

Update the following part of the script with your credentials:

```python
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')
```

## How to Use

1. Clone this repository:

```bash
git clone https://github.com/yourusername/reddit-image-downloader.git
cd reddit-image-downloader
```

2. Run the script:

```bash
python image_downloader.py
```

3. Enter the folder name where you'd like to save the images.

4. Provide the subreddit name (e.g., `pics`, `wallpapers`) and the number of images to download.

## Example

If you want to download 10 images from the `EarthPorn` subreddit:

```bash
Enter the name of the folder: nature_images
Enter the subreddit name to download images from: EarthPorn
Enter the number of images to download: 10
```

The images will be saved in the `nature_images` folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

import praw
import requests
import os
import time

# Set up Reddit API credentials
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

# Create a folder to store images if it doesn't exist
image_folder = input('Insert the name of the folder: ')
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Function to download images
def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)

# Function to collect images from the subreddit
def download_images_from_subreddit(subreddit_name, post_limit=100):
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
