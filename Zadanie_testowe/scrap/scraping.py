# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup


def autor():
    data = []
    quote_page = ['https://teonite.com/blog','https://teonite.com/blog/page/2/','https://teonite.com/blog/page/3/','https://teonite.com/blog/page/4/']
    for pg in quote_page:
        page = urlopen(pg)
        soup = BeautifulSoup(page, 'html.parser')
        all_links = soup.find_all("a", class_="read-more")

        for link in all_links:
            podstrona = link.get("href")
            quote_page = ['https://teonite.com' + podstrona]
            # print(quote_page)
            for pg in quote_page:
                page = urlopen(pg)
                soup = BeautifulSoup(page, 'html.parser')

                for h4 in soup.findAll('h4'):
                    if h4.parent.name == 'span':
                        data.append(h4.get_text())
                        print(h4.get_text())
    return data


def tekst():
    data = []
    quote_page = ['https://teonite.com/blog', 'https://teonite.com/blog/page/2/', 'https://teonite.com/blog/page/3/',
                  'https://teonite.com/blog/page/4/']
    for pg in quote_page:
        page = urlopen(pg)
        soup = BeautifulSoup(page, 'html.parser')
        all_links = soup.find_all("a", class_="read-more")

        for link in all_links:
            podstrona = link.get("href")
            quote_page = ['https://teonite.com' + podstrona]
            # print(quote_page)
            for pg in quote_page:
                page = urlopen(pg)
                soup = BeautifulSoup(page, 'html.parser')
                # name_box = soup.find_all('section', class_= 'post-content')

                for lines in soup.findAll('section', class_='post-content'):
                    slowa = lines.get_text()
                    slowa = slowa.split(' ')
                    slowa = [x.replace('\n', '') for x in slowa]
                    data.append(slowa)

    return data



# TO WPISUJE W KONSOLI ABY DODAC DANE DO BAZY DANYCH


# from scrap.scraping import autor
# from scrap.models import Author
#     dane = []
# l = autor()
# for p in l:
#     if p not in dane:
#         dane.append(p)
#         Author.objects.create(imie=p)

# from scrap.scraping import tekst
# # from scrap.models import Stats
# l = tekst()
# for inner_l in l:
#     for item in inner_l:
#         Stats.objects.create(slowo=item)

