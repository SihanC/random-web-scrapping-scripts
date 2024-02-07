import time
import requests
from bs4 import BeautifulSoup

money_unit_map = { "Million" : 1000000, "Billion" : 1000000000 }
DAY_IN_SEC = 60 * 60 * 12
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'})

while (True): 
    # Scrap Powerball
    powerball_page = requests.get('https://www.powerball.com/', headers=HEADERS)
    print(powerball_page.headers)
    powerball_soup = BeautifulSoup(powerball_page.content, 'html.parser')
    
    p_jackport_price_text = powerball_soup.find("span", "game-jackpot-number text-xxxl lh-1 text-center").text.replace('$', '')
    p_jackport_price_parts = p_jackport_price_text.split(" ")
    p_jackport_price = int(p_jackport_price_parts[0]) * money_unit_map[p_jackport_price_parts[1]]
    print(p_jackport_price)

    # Scrap Mega Millions
    megamillion_page = requests.get('https://www.megamillions.com/', headers=HEADERS)
    megamillion_soup = BeautifulSoup(megamillion_page.content, 'html.parser')
    print(megamillion_soup.contents)
    m_jackport_price_text = megamillion_soup.find("span", "nextEstVal js_estJackpot").text.replace('$', '')
    print(m_jackport_price_text)
    m_jackport_price_parts = m_jackport_price_text.split(" ")
    m_jackport_price = int(m_jackport_price_parts[0]) * money_unit_map[m_jackport_price_parts[1]]
    print(m_jackport_price)

    # Run twice per day
    time.sleep(DAY_IN_SEC)