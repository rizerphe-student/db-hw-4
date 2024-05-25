from dataclasses import dataclass
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests

bus_types_link = "https://en.wikipedia.org/wiki/List_of_buses"
response = requests.get(bus_types_link)
soup = BeautifulSoup(response.text, "html.parser")


@dataclass
class BusType:
    name: str
    link: str

    @property
    def final_link(self) -> str:
        raw_url = urljoin(bus_types_link, self.link)
        # Some of the links are redirects, so we need to follow them:
        response = requests.get(raw_url)
        return response.url

    @property
    def full_text(self) -> str:
        response = requests.get(urljoin(bus_types_link, self.link))
        soup = BeautifulSoup(response.text, "html.parser")
        body = soup.find("div", {"class": "mw-body-content"})
        # One of these confused MySQL, so I'm just getting rid of both
        return (
            body.get_text()
            .replace("\n", " ")
            .replace('"', "'")
            .replace("'", "")
            .replace(",", "")
            .strip()
        )


# We need to filter out only things in the Bus column, and take the first 20:
bus_types: list[BusType] = []
for row in soup.find_all("tr"):
    cells = row.find_all("td")
    if len(cells) > 0:
        # We want to find a link inside of it:
        link = cells[0].find("a")
        if link and "href" in link.attrs:
            # Add the URL:
            bus_types.append(BusType(name=link.text, link=link["href"]))

# A lot of these are redirects to the same page, so we'll remove duplicates based on the URL
# while counting up the first 20:
used_links = set()
filtered_bus_types: list[BusType] = []
for bus in bus_types:
    if bus.final_link not in used_links:
        filtered_bus_types.append(bus)
        used_links.add(bus.final_link)
    if len(filtered_bus_types) == 20:
        break
