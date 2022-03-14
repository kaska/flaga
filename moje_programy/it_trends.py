import requests

def pobierz_strone_www_jako_text(orangutan):
 # Pobranie tekstu ze strony (jako tafla tesktu).
    surowe_info = requests.get( orangutan)
    text = surowe_info.text
    return text

orangutan = 'https://justjoin.it/offers/sternkraft-poland-data-scientist-poznan'
print (pobierz_strone_www_jako_text( orangutan))