
import pickle

with open("duomenu_sarasai.pkl", "rb") as failas:
    markes = pickle.load(failas)
    varikliu_kubatura = pickle.load(failas)
    kuro_tipas = pickle.load(failas)
    pag_data = pickle.load(failas)
    pav_deze = pickle.load(failas)
    kainos = pickle.load(failas)
print(len(kainos))
