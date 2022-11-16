from bs4 import BeautifulSoup as bs
import requests
import re
from urllib.parse import unquote
import json

def parse_html(id):
    response = {}
    url = "https://www.youtube.com/watch?v=" + id
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    response["title"] = soup.find("meta", property="og:title")["content"]
    response["author"] = soup.find("span", itemprop="author").find("link", itemprop="name")["content"]
    tmp = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data = json.loads(tmp)
    try:
        likes_txt = data["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["videoActions"]["menuRenderer"]["topLevelButtons"][0]["segmentedLikeDislikeButtonRenderer"]["likeButton"]["toggleButtonRenderer"]["defaultText"]["accessibility"]["accessibilityData"]["label"]
        response["likes"] = "".join(likes_txt.split(u"\u00A0")[:-1]).replace(u"\u202F", "")
    except:
        print("error while parsing likes, restart the program")
        response["likes"] = "unexpected error"
    try:
        desc = data["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][1]["videoSecondaryInfoRenderer"]["description"]["runs"]
        description = ""
        links = []
        for t in desc:
            description += t["text"].replace('\n','\\n')
            if "navigationEndpoint" in t.keys():
                t = t["navigationEndpoint"]
                if "urlEndpoint" in t:
                    tmp_link = t["urlEndpoint"]["url"]
                    if "redirect" in tmp_link:
                        links.append(unquote(tmp_link.split("&q=")[1].split("&v=")[0]).replace(u"\u200b", ""))
                    else:
                        links.append(unquote(tmp_link))
                elif "commandMetadata" in t:
                    tmp_link = t["commandMetadata"]["webCommandMetadata"]["url"]
                    links.append(unquote("https://youtube.com"+tmp_link))
        response["description"] = description
        response["links"] = links
    except:
        response["description"] = "Pas de description"
        response["links"] = []
    response["id"] = id
    return response
