from bs4 import BeautifulSoup

marktplaats_file = "../data/marktplaats.html"

with open(marktplaats_file) as html_file:
    soup = BeautifulSoup(html_file, "html.parser")

all_popular_terms = soup.select(".PopularSearchesBlock-list a")
print(f"{len(all_popular_terms)} popular search terms found:")

for item in all_popular_terms:
    print(item.text)