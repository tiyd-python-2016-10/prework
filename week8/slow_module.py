import requests
import time

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


def crawl_to_a_halt(data):
    time.sleep(5)
    return "I did something slow with my data: {}".format(data)
