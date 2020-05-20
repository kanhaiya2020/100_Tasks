import pythainlp  # this is a search engine library for thai language
import sys
import datetime
import time
from random import randint
import requests
from bs4 import BeautifulSoup
import pandas as pd
from newspaper import Article
from lxml.html import fromstring


class NewsScraper:

    def news_scraper(self):

        # Read a CSV file to take input such as search keyword and language.
        input_file = sys.argv[1]
        data_frame = pd.read_csv(input_file)

        return self.get_article(data_frame)

    def get_article(self, data_frame):

        # Get Date and Time of scraping.
        scrape_date = datetime.datetime.now().strftime("%Y%m%d")
        scrape_time = datetime.datetime.now().time().strftime("%H:%M:%S")
        scrape_date_time = scrape_date + scrape_time

        scrape_data_list = []
        for index, row in data_frame.iterrows():

            pause_time = randint(0, 30)
            time.sleep(pause_time)

            search_query = "https://www.google.com/search?&q=" + row['Keyword'] + \
                           "&tbs=qdr:h24&tbo=1&source=lnms&tbm=nws&cad=h&hl=" + \
                           row['Language']

            result = requests.get(search_query)
            soup = BeautifulSoup(result.text, "html.parser")
            search_news_article = soup.find_all("div", attrs={'class': 'kCrYT'})
            search_news_article = list(search_news_article)
            link_list = []

            # if Keyword has special keyword then Split-up the keyword

            if len(search_news_article) == 0:
                special_character_list = ['.', '_', '@', '&', '%', '#']
                for var in special_character_list:
                    if var in row['Keyword']:
                        x = row['Keyword'].split(var)[0]
                        search_query = "https://www.google.com/search?&q=" + x + \
                                       "&tbs=qdr:h24&tbo=1&source=lnms&tbm=nws&cad=h&hl=" + \
                                       row['Language']

                        result = requests.get(search_query)
                        soup = BeautifulSoup(result.text, "html.parser")
                        search_news_article = soup.find_all("div", attrs={'class': 'kCrYT'})
                        search_news_article = list(search_news_article)
                        if search_news_article:
                            break
            # if no search result available then add the "No Result Found" in the text file

            if len(search_news_article) == 0:
                link_list = ["No Result Found"]
            else:
                for a in search_news_article:
                    try:
                        link = a.find("a")
                        data_link = link.get('href')[7:].split('&')[0].split('%')[0]
                        link_list.append(data_link)
                    except:
                        pass

            link_set = list(set(link_list))

            for data_link in link_set:
                try:
                    article = Article(data_link, language=row['Language'])
                    article.download()
                    article.parse()
                    full_news = article.text.replace('\n', '')
                except:
                    full_news = " "
                    # pass

                # Create a dictionary of single news article with all details.
                data_dict = {"Scrape Date & Time": scrape_date_time,
                             "Language": row['Language'],
                             "Ticker": row['Keyword'],
                             "News Link": data_link,
                             "Full News Article": full_news
                             }

                scrape_data_list.append(data_dict)
        return self.save_data(scrape_data_list)

    # Method to save data into MongoDB Database or write to a text file
    def save_data(self, scrape_data_list):

        # Get Date and Time of scraping.
        scrape_date = datetime.datetime.now().strftime("%Y%m%d")
        scrape_time = datetime.datetime.now().time().strftime("%H:%M:%S")
        scrape_date_time = scrape_date + scrape_time
        scrape_date_time = scrape_date_time.replace(':', '_')
        # Create a file name with date and time stamp to save data.
        file_name = sys.argv[2] + scrape_date_time + ".txt"
        # file_name=file_name.replace(':','_')
        print(file_name)
        # Full News: Write into text file
        # print(file_name)
        file = open(file_name, "w", encoding="utf-8")
        file.write(scrape_date_time[0:8] + "\n")
        ticker_list = set()

        for idx in scrape_data_list:

            if idx["Ticker"] not in ticker_list:
                file.write("\n\n")
                ticker = idx["Ticker"]
                file.write("**" + ticker[2:len(ticker) - 2] + "\n")
                file.write("****" + idx["Language"] + "\n")
                file.write("\n\n")

            file.write(idx["News Link"] + "\n")
            file.write(idx["Full News Article"] + "\n")

            ticker_list.add(idx["Ticker"])

        file.close()


# Make the object of class NewsScraper
news_scraper_obj = NewsScraper()
# Call the news_scraper() method using object
news_scraper_obj.news_scraper()