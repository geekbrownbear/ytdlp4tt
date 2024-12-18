import json
import csv

def extract_liked(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    links = []
    for video in data['Activity']['Like List']['ItemFavoriteList']:
        link_key = next((key for key in video if key.lower() == 'link'), None)  # Find the key ignoring case
        if link_key:
            links.append(video[link_key])

    return links

def extract_favs(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    links = []
    for video in data['Activity']['Favorite Videos']['FavoriteVideoList']:
        link_key = next((key for key in video if key.lower() == 'link'), None)  # Find the key ignoring case
        if link_key:
            links.append(video[link_key])

    return links

def extract_shared(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    links = []
    for video in data['Activity']['Share History']['ShareHistoryList']:
        link_key = next((key for key in video if key.lower() == 'link'), None)  # Find the key ignoring case
        if link_key:
            links.append(video[link_key])

    return links    

def write_to_csv(links, csv_file):
    """
    Writes a list of links to a CSV file.

    Args:
        links (list): List of Link entries.
        csv_file (str): Path to the CSV file.
    """

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Link'])  # Write header row
        for link in links:
            writer.writerow([link])

if __name__ == '__main__':
    json_file = 'user_data_tiktok.json'  # Replace with your JSON file name
    liked_file = 'liked_links.txt'  # Name of the output CSV file
    favs_file = 'favorited_links.txt'  # Name of the output CSV file
    shared_file = 'shared_links.txt'  # Name of the output CSV file

    links = extract_liked(json_file)
    write_to_csv(links, liked_file)
    print(f"Liked links extracted and saved to {liked_file}")

    links = extract_favs(json_file)
    write_to_csv(links, favs_file)
    print(f"Favorite links extracted and saved to {favs_file}")
    
    links = extract_shared(json_file)
    write_to_csv(links, shared_file)
    print(f"Shared links extracted and saved to {shared_file}")
