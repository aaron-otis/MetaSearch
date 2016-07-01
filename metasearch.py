import requests
from lxml import html

search_engines = ["google.com", "yahoo.com", "bing.com", "ixquick.com"]

def trim(link):
    if link[0] == '/':
        link = link[link.find("http"):]
    if '&' in link:
        link = link.split('&')[0]
    return link


def scrape(query):
    results = []
    for site in search_engines:
        search_page = html.fromstring(requests.get("https://" + site).content)
        form_action = search_page.xpath("//form/@action")[0]

        if ';' in form_action:
            form_action = form_action.split(";")[0]

        input_name = search_page.xpath("//input[not(@type='hidden') and not(@type='submit')]/@name")[0]

        if "http" in form_action:
            url = form_action + '?' + input_name + '=' + query
        else:
            url = "https://" + site + form_action + '?' + input_name + '=' + query
        links = html.fromstring(requests.get(url).content).xpath("//h3//a/@href")
        if len(links) == 0:
            links = html.fromstring(requests.get(url).content).xpath("//a/@href")
            for link in links:
                if "http" in link:
                    link = trim(link)
                    if "javascript" not in link and "proxy" not in link:
                        results.append(link)
        else:
            for link in links:
                if "http" in link:
                    link = trim(link)
                    results.append(link)

    return list(set(results))
