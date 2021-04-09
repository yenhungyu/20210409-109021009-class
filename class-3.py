import requests
import time
import csv
from bs4 import BeautifulSoup
URL ="https://www.majortests.com/word-lists/word-list-0{0}.html"

def generate_urls(url, start_page , end_page):
    urls = []
    for page in range(start_page , end_page):
        urls.append(url.format(page))
    return urls

def get_resource(url):   #假真人爬蟲
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    return requests.get(url , headers = headers)

def parse_html(html_str):
    return BeautifulSoup(html_str, "lxml")

def get_word(soup , file):
    words = []
    count = 0
    for wordlist_table in soup.find_all(class_="wordlist"):
        count += 1
        for word_entry in wordlist_table.find_all("tr"):
            new_word = []
            new_word.append(file)
            new_word.append(str(count))
            new_word.append(word_entry.th.text)
            new_word.append(word_entry.td.text)
            words.append(new_word)
    return words

def web_scraping_bot(urls):
    eng_words = []
    for url in urls:
        file = url.split("/")[-1]
        print("catching: " , file , " web data...")
        r = get_resource(url)
        if r.status_code == requests.codes.ok: #後者等於參數200,網頁連結成功,若為404網頁不存在500則為伺服器有問題
            soup = parse_html(r.text)
            words = get_word(soup,file)
            eng_words = eng_words + words
            print("sleep 5 second")
            time.sleep(5) #先睡個幾秒再繼續抓   
        else:
            print("HTTP request error")
    return eng_words

def save_to_csv(words, file): #存檔
    with open(file, "w+" , newline="" , encoding="utf-8") as fp: #newline不要加換行
        writer = csv.writer(fp)
        for word in words:
            writer.writerow(word)

if __name__ == "__main__":
    urlx = generate_urls(URL , 1 , 10)
    eng_words = web_scraping_bot(urlx)
    for item in eng_words: #可有可無
        print(item)
    save_to_csv(eng_words,"engWordList_1.csv")