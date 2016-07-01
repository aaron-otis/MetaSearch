import metasearch

search_phrase = raw_input("What do you want to search for? ")

for link in metasearch.scrape(search_phrase):
    print link
