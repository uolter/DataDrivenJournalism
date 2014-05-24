# -*- coding: utf-8 -*-


import requests
import bs4
import csv

players_list = {
    'Brasile': ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_del_Brasile', 0),
    'Giappone': ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_del_Giappone',0),
    'Austria' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Australia',0),
    'Iran': ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Iran',0),
    'Corea del Sud' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Corea_del_Sud',0),
    'Olanda' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Olanda',0),
    'Italia' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Italia',4),
    'Stati Uniti' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_degli_Stati_Uniti_d%27America',0),
    'Costa Rica' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Costa_Rica',2),
    'Argentina' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Argentina',0),
    'Belgio' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_del_Belgio',3),
    'Svizzera' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Svizzera',0),
    'Germania' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Germania',0),
    'Colombia' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Colombia',0),
    'Russia' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Russia',0),
    'Bosnia Erzegovina' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Bosnia_ed_Erzegovina',0),
    'Inghilterra' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Inghilterra',2),
    'Spagna' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Spagna',0),
    'Cile' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_del_Cile',0),
    'Ecuador' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Ecuador',0),
    'Honduras': ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Honduras',0),
    'Costa d’Avorio' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Costa_d%27Avorio',0),
    'Nigeria' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Nigeria',0),
    'Camerun' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_del_Camerun',0),
    'Gana' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_del_Ghana',0),
    'Algeria' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Algeria',0),
    'Grecia' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Grecia',0),
    'Croazia' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Croazia',1),
    'Portogallo' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_del_Portogallo',0),
    'Francia' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_della_Francia',3),
    'Messico': ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_del_Messico',0),
    'Uruguai' : ('http://it.wikipedia.org/wiki/Nazionale_di_calcio_dell%27Uruguay',0)
} 


def replace_unicode(txt):

    return txt.replace(u'\xa0', u' ').encode('utf-8', 'ignore')

def get_header(row):

    head = bs4.BeautifulSoup(str(row))
    th =  head.select('th')
    return [
        th[1].text,
        th[2].text,
        replace_unicode(th[3].text),
        th[4].text,
        th[5].text
    ]


def get_player(row):

    r = bs4.BeautifulSoup(str(row))
    return [
        r.select('td a')[0].text,
        replace_unicode(r.select('td a')[1].text),
        replace_unicode(r.select('td')[3].text),
        replace_unicode(r.select('td')[4].text),
        replace_unicode(r.select('td')[5].text)
    ]


def save_csv(file_name, data):

    with open(file_name, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(data)


is_header = True

players = []

for t in players_list:

    response = requests.get(players_list[t][0])

    soup = bs4.BeautifulSoup(response.text)
    table = soup.select('table.wikitable')[players_list[t][1]].select('tr')


    if is_header:
        header = get_header(table[0])
        #print header
        is_header = False
        header.append('Nazionale')
        players.append(header)

    for r in table[1:]:
        try:
            player = get_player(r)
            player.append(t)
            #print player
            players.append(player)
        except IndexError:
            pass


save_csv('player.csv', players)
