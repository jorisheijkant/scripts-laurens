import requests

page_name = "marktplaats"
data_folder = "data"
site_url = "https://marktplaats.nl"

response = requests.get(site_url)
response.raise_for_status()
html_content = response.text

file_name = f"../{data_folder}/{page_name}.html"
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(html_content)