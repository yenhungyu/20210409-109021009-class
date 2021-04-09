URL = "https://www.majortests.com/word-lists/word-list-0{0}.html"

def generate_urls(url, start_page , end_page):
    urls = []
    for page in range(start_page , end_page):
        urls.append(url.format(page))
    return urls

if __name__ == "__main__":
    urlx = generate_urls(URL , 1 , 10)
    for url in urlx:
        print(url)