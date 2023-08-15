import pyshorteners

def short_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)


if __name__ == "__main__":
    url_to_short = input("URL: ")
    print(short_url(url_to_short))
