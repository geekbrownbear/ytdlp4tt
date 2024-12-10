import json

def extract_video_lists(json_file):
    """
    Extracts the 'Like List', 'Favorite Videos', and 'Share History' sections from a JSON file.

    Args:
        json_file (str): Path to the JSON file.

    Returns:
        tuple: Three lists of video links, one each for 'Like List', 'Favorite Videos', and 'Share History'.
    """

    with open(json_file, 'r') as f:
        data = json.load(f)

    liked_vids = [video['Link'] for video in data['Activity']['Like List']['LikeVideoList']]
    favorite_vids = [video['Link'] for video in data['Activity']['Favorite Videos']['FavoriteVideoList']]
    shared_vids = [video['Link'] for video in data['Activity']['Share History']['ShareHistoryList']]

    return liked_vids, favorite_vids, shared_vids

def write_to_txt(video_list, txt_file):
    """
    Writes a list of video links to a text file.

    Args:
        video_list (list): List of video links.
        txt_file (str): Path to the text file.
    """

    with open(txt_file, 'w') as f:
        for link in video_list:
            f.write(link + '\n')

if __name__ == '__main__':
    json_file = 'user_data_tiktok.json'  # Replace with your JSON file name
    liked_vids_file = 'liked_vids.txt'
    favorite_vids_file = 'bookmarked_vids.txt'
    shared_vids_file = 'shared_vids.txt'

    liked_vids, favorite_vids, shared_vids = extract_video_lists(json_file)

    write_to_txt(liked_vids, liked_vids_file,)
    print(f"'Like List' links extracted and saved to {liked_vids_file}")

    write_to_txt(favorite_vids, favorite_vids_file)
    print(f"'Favorite Videos' links extracted and saved to {favorite_vids_file}")

    write_to_txt(shared_vids, shared_vids_file)
    print(f"'Shared Videos' links extracted and saved to {shared_vids_file}")