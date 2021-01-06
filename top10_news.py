from newsapi import NewsApiClient
import json
newsapi = NewsApiClient(api_key='35003889278240c486c9a9ca51b47c19')
top_headlines = newsapi.get_top_headlines(q="https://timesofindia.indiatimes.com/business/india-business/rbi-announces-special-liquidity-facility-of-rs-50000-crore-for-mutual-funds/articleshow/75400260.cms",
                                          sources='India.com',
                                          language='en',
                                          )
print(top_headlines)
'''import pandas as pd
print(dir(pd))'''




