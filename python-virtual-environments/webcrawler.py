import requests

r = requests.get('http://unhackathon.org/')

def crawl_web(initial_url):
    crawled, to_crawl = [], []
    to_crawl.append(initial_url)

    while to_crawl:
        current_url = to_crawl.pop(0)
        r = requests.get(current_url)
        crawled.append(current_url)
        for url in re.findall('<a href="([^"]+)">', str(r.content)):
            if url[0] == '/':
                url = current_url + url
            pattern = re.compile('https?')
            if pattern.match(url):
                to_crawl.append(url)
    return crawled

print(crawl_web('http://unhackathon.org'))

