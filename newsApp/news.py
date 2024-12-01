from newsapi import NewsApiClient

def content():
    newsapi = NewsApiClient(api_key='1d17a9374065434a9f3230d3771bd147')

    sources = newsapi.get_everything(sources='bbc-news,the-verge',)
    news= []
    for article in sources['articles']:
        if article["author"] is not None:
            if article["title"] not in news:
                news.append(article['title'])
    return news             