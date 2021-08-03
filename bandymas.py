
import requests
from bs4 import BeautifulSoup

psl_nr = 40
adresas = 'https://autoplius.lt/skelbimai/naudoti-automobiliai?make_date_from=&make_date_to=&sell_price_from=&sell_' \
          'price_to=&engine_capacity_from=&engine_capacity_to=&power_from=&power_to=&kilometrage_from=&kilometrage_to=' \
          '&qt=&qt_autocomplete=&has_damaged_id=10924&category_id=2&older_not=-1&slist=1393607654&page_nr='


html = requests.get(adresas+str(psl_nr)).text
soup = BeautifulSoup(html, 'html.parser')
if soup.select('ul.paging > li')[-1].text.strip() == "":
    print("Nieko nera")
