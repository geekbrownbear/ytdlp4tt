import json
import csv

def extract_links(json_file):
    """
    Extracts the 'Link' values from a JSON file.

    Args:
        json_file (str): Path to the JSON file.

    Returns:
        list: A list of Link entries.
    """

    with open(json_file, 'r') as f:
        data = json.load(f)

    links = []
    for video in data['Activity']['Favorite Videos']['FavoriteVideoList']:
        links.append(video['Link'])

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
    json_file = 'bookmarked_vids.json'  # Replace with your JSON file name
    csv_file = 'bookmarked_links.csv'  # Name of the output CSV file

    links = extract_links(json_file)
    write_to_csv(links, csv_file)

    print(f"Links extracted and saved to {csv_file}")