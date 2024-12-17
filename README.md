# Using yt-dlp to download all your saved, liked, and shared TikToks

**With TikTok potentially disappearing I wanted to download my saved vids for future reference. But I couldn't get some existing tools to work, so I made my own!**

Be mindful! You might have A LOT of liked/shared videos. Check the files from step 2 for an estimate on how many videos you will end up with. 10k vids ~= 40GB from my testing.

1. Get your Account Data from TikTok (example file `user_data_tiktok.json`). You can download "All" data or just "Activity" which doesn't include shared videos. From [TikTok KB](https://support.tiktok.com/en/account-and-privacy/personalized-ads-and-data/requesting-your-data):

    You can request a copy of your TikTok data, which may include but is not limited to your username, watch video history, comment history, and privacy settings.
    
    To request your TikTok data:
    1. In the TikTok app, tap Profile at the bottom.
    2. Tap the Menu ☰ button at the top, then tap Settings and privacy.
    3. Tap Account.
    4. Tap Download your data.
    5. Choose which information you want to include in your file to download and select a file format.
    6. Tap Request data.
    
    After you submit your request, we'll create a file of your data that you can download from the download data tab. We'll notify you in the app when it's ready to download. Please note that it may take a few days to prepare the file.
    
    To download your TikTok data:
    1. In the TikTok app, tap Profile at the bottom.
    2. Tap the Menu ☰ button at the top, then tap Settings and privacy.
    3. Tap Account.
    4. Tap Download your data.
    5. Tap Download data to see the status of your request, and tap Download if it's ready. Your file will be available for up to 4 days.
  

2. Extract the links from the json file.
   * Run `convert.py` from the same folder as your `user_data_tiktok.json` file
   * You will get three files, one each for Liked, Saved, and Shared items.
  
3. Download via yt-dlp
   * Get yt-dlp from <https://github.com/yt-dlp/yt-dlp>
   * This command will just put the files in the same folder as yt-dlp but it can be modified as desired. REPLACE `PATH_TO_LINKS.TXT` (keep the apostrophes)
   * TikTok videos end up with the entire description as the file name which is a nightmare. So instead, this will name the files using the video ID# and create a .description file (its just a text file) with the entire video descrip/name
   * Run the command once per file from step 2
   
   `yt-dlp -a 'PATH_TO_LINKS.TXT' --write-description --output '[%(id)s].%(ext)s'`
