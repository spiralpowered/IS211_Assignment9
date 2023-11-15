import requests
from bs4 import BeautifulSoup
import urllib.request

def download_url(url):
    """
    Reads from a URL and returns the HTML as string

    :param url:
    :return: the content of the URL
    """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response
def scrape_table(url):
    """
    Scrapes webpage for info in the scoring table
    :param url:
    :return:
    """

    # Get and parse webpage from URL
    page = download_url(url)

    soup = BeautifulSoup(page, 'lxml')

    # Pull all text from the table
    scoring_table = soup.find_all('div', class_="Page-colMain")

    # Pull all rows and formats header
    rows = scoring_table[0].find_all('tr')
    headers = rows[0].find_all('th')
    tooltip = headers[0].find(class_="Tablebase-tooltipInner")
    tooltip.decompose()
    player_header = headers[0].text.strip()
    tooltip = headers[2].find(class_="Tablebase-tooltipInner")
    tooltip.decompose()
    rutd_header = headers[2].text.strip()
    print(f"{player_header:<20} - Position{'':<10} - Team{'':<10} - {rutd_header}(Rushing Touchdowns){'':<10}")

    # Pulls info from cells and formats it.
    for row in rows[:21]:
        cells = row.find_all('td')
        if not cells:
            continue
        player_info = cells[0].find_all('span', class_="CellPlayerName--long")
        name = player_info[0].find('a').text.strip()
        position = player_info[0].find(class_="CellPlayerName-position").text.strip()
        team = player_info[0].find(class_="CellPlayerName-team").text.strip()
        rutd = cells[2].text.strip()
        print(f"{name:<20} - {position:<18} - {team:<14} - {rutd:<10}")

if __name__ == "__main__":
    url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/?sortcol=rutd&sortdir=descending"
    scrape_table(url)


