from newspaper import Article
data_link = input('Enter the link to scrap the data: ')
article = Article(data_link, language='en')
article.download()
article.parse()
full_news = article.text()
print(full_news)