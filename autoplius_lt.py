
import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
import pickle
import random
import re
from funkcijos_autoplius import *
import pandas as pd

psl_nr = 1
psl_limit = 20
dabar = datetime.today().strftime("%Y-%m-%d %H_%M_%S")
markes = []
svarios_markes = []
varikliu_kubatura = []
kainos = []
k_tipas = []
pav_deze = []
pag_data = []

adresas = 'https://autoplius.lt/skelbimai/naudoti-automobiliai?make_date_from=&make_date_to=&sell_price_from=&sell_' \
          'price_to=&engine_capacity_from=&engine_capacity_to=&power_from=&power_to=&kilometrage_from=&kilometrage_to=' \
          '&qt=&qt_autocomplete=&has_damaged_id=10924&category_id=2&older_not=-1&slist=1393607654&page_nr='


while True:
    try:
        html = requests.get(adresas+str(psl_nr)).text
        print(f"Nuskaitomas puslapis {psl_nr}")
        soup = BeautifulSoup(html, 'html.parser')
        markes += [a.text.strip() for a in soup.select('.announcement-title')]
        kainos += [a.text.strip() for a in soup.select('div.announcement-pricing-info > strong')]
        k_tipas += [a.text.strip() for a in soup.find_all("span", attrs={"title": "Kuro tipas"})]
        pag_data += [a.text.strip() for a in soup.find_all("span", attrs={"title": "Pagaminimo data"})]
        pav_deze += [a.text.strip() for a in soup.find_all("span", attrs={"title": "Pavarų dėžė"})]
    except:
        print(f"Nepavyko nuskaityti {psl_nr} puslapio")
        break
    # if psl_nr >= psl_limit:
    if soup.select('ul.paging > li')[-1].text.strip() == "":
        print(f"{psl_nr} puslapių nuskaitymas baigtas")
        break
    psl_nr += 1
    sleep(random.randint(1, 7))


for marke in markes:
    try:
        kubatura_pattern = re.compile(r'\d\.\d')
        kubatura_res = kubatura_pattern.search(marke)
        if kubatura_res is None:
            varikliu_kubatura.append("None")
        else:
            varikliu_kubatura.append(kubatura_res.group())
        markes_pattern = re.compile(r'[a-zA-Z0-9-]+\s[a-zA-Z0-9-]+')
        markes_res = markes_pattern.search(marke)
        svarios_markes.append(markes_res.group())
    except:
        print("Nepavyko išfiltruoti duomenų")


svarios_markes = isvalyk(svarios_markes)
varikliu_kubatura = isvalyk(varikliu_kubatura)
kainos = isvalyk(kainos)
kainos = sutvarkyk_kaina(kainos)
pag_data = sutvarkyk_data(pag_data)

with open(f"duomenu_sarasai.pkl", "wb") as failas:
    pickle.dump(svarios_markes, failas)
    pickle.dump(varikliu_kubatura, failas)
    pickle.dump(k_tipas, failas)
    pickle.dump(pag_data, failas)
    pickle.dump(pav_deze, failas)
    pickle.dump(kainos, failas)


df = pd.DataFrame({'Markė': svarios_markes, 'Variklio kubatūra': varikliu_kubatura, 'Kuro tipas': k_tipas, 'Metai':
                   pag_data, 'Pavarų dėžė': pav_deze, 'Kaina': kainos})
df.to_csv(f'autoplius {dabar}.csv', index=False, encoding='UTF-8')
