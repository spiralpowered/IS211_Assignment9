import requests
from bs4 import BeautifulSoup

def scrape_table(url):
    # Get and parse webpage from URL
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')

    # Pull all text from the table
    super_bowl_table = soup.find_all('table', class_="wikitable sortable")

    # Extract all rows and headers from the table and formats the headers text
    rows = super_bowl_table[0].find_all('tr')
    headers = rows[0].find_all('th')
    game_header = headers[0].text.strip()
    winner_header = headers[2].text.strip()
    score_header = headers[3].text.strip()
    loser_header = headers[4].text.strip()
    venue_header = headers[5].text.strip()
    attendance_header = headers[7].text.strip()
    print(f"{game_header:<15} - {winner_header:<35} - {score_header:<15} - {loser_header:<35} - {venue_header:<35} - {attendance_header:<15}")


    # Extract text from each cell in the table and format it
    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        game = cells[0].text.strip()
        winner = cells[2].text.strip()
        score = cells[3].text.strip()
        loser = cells[4].text.strip()
        venue = cells[5].text.strip()
        attendance = cells[7].text.strip()
        print(f"{game:<15} - {winner:<35} - {score:<15} - {loser:<35} - {venue:<35} - {attendance:<15}")


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
    scrape_table(url)
