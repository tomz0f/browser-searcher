import sys
import os

x = ""
browser_queries = {
    "google": "google.com/search?q=",
    "g": "google.com/search?q=",
    "duckduckgo": "ducduckgo.com/?q=",
    "ddg": "duckduckgo.com/?q=",
    "yandex": "yandex.com/search/?text=",
    "y": "yandex.com/search/?text=",
    "yahoo": "https://search.yahoo.com/search?p="
}
browser_lists = [x for x in browser_queries.keys()]
def getLink(browser_name = "google", search_query = ""):
    search_query = search_query.replace(' ', '+')
    full_link = f'{browser_queries[browser_name]}{search_query}'
    if os.name == "nt":
        os.system(f"explorer https://{full_link}")
    if os.name == "posix" or os.name == "darwin":
        os.system(f"open https://{full_link}")
def checkBrowser():
    run = True
    while(run):
        print("Browser Choices:\n-----------------\n1) Google (google/g)\n2) DuckDuckGo (ddg/duckduckgo)\n3) Yandex (yandex/y)\n4) Yahoo (yahoo)", end = "\n")
        browser_choice = input("Give a browser name for search: ")
        if browser_choice in browser_lists:
            run = False
    return browser_choice
try:
    query = sys.argv[1]
    if (query in browser_lists and (sys.argv[-1] not in browser_lists)):
        browser_choice = query
        search_query = sys.argv[-1]
        getLink(browser_choice, search_query)

    if (query not in browser_lists and (sys.argv[-1] != "" or sys.argv[-1] != None)):
        search_query = sys.argv[-1]
        browser_choice = checkBrowser()
        getLink(browser_choice, search_query)
    

except IndexError:
    browser_choice = checkBrowser()
    search_query = input("Give a search query for search: ")
    getLink(browser_choice, search_query)

