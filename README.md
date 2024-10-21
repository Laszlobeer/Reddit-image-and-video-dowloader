Reddit Image Downloader
This script allows you to download images from a specific subreddit using Reddit's API and stores them in a local folder. You can specify the subreddit name and the number of images to download.

Features
Downloads images (jpeg, png, gif, mp4) from the hot posts of a subreddit.
Stores images in a user-specified local folder.
Automatically handles rate-limiting to avoid being blocked by Reddit.
Prerequisites
Python 3.x should be installed. You can download it from python.org.
Install the following Python libraries:
praw: Python Reddit API Wrapper for interacting with Reddit.
requests: For downloading the image files.
You can install the required libraries using:

bash
Copy code
pip install praw requests
Reddit API Setup
Before running the script, you need to set up a Reddit app to obtain API credentials. Follow these steps:

Go to Reddit Developer Apps.
Click Create App.
Fill in the required details and make sure to select script as the app type.
After creating the app, you'll receive:
client_id
client_secret
user_agent
Update the following part of the script with your credentials:

python
Copy code
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')
How to Use
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/reddit-image-downloader.git
cd reddit-image-downloader
Run the script:
bash
Copy code
python image_downloader.py
Enter the folder name where you'd like to save the images.

Provide the subreddit name (e.g., pics, wallpapers) and the number of images to download.

Example
If you want to download 10 images from the EarthPorn subreddit:

bash
Copy code
Enter the name of the folder: nature_images
Enter the subreddit name to download images from: EarthPorn
Enter the number of images to download: 10
The images will be saved in the nature_images folder.

License
This project is licensed under the MIT License - see the LICENSE file for details.

