# DODAWANIE DANYCH DO BAZDY DANYCH

def todb():
    from scrap.scraping import autor
    from scrap.models import Author
    dane = []
    l = autor()
    for p in l:
        if p not in dane:
             dane.append(p)
             Author.objects.create(imie=p)



    from scrap.scraping import tekst
    from scrap.models import Text
    l = tekst()
    for inner_l in l:
         for item in inner_l:
             Text.objects.create(slowo=item)




    from django.db import connection
    from scrap.models import Stats
    cursor = connection.cursor()
    cursor.execute('''
     SELECT       slowo,
                  COUNT(slowo) AS liczebnosc
         FROM     scrap_stats
         GROUP BY slowo
         ORDER BY liczebnosc DESC
         LIMIT    10;''')

    row = cursor.fetchall()

    for p in row:
        Stats.objects.create(slowo=p[0],liczebnosc=p[1])