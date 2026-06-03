import requests
import xml.etree.ElementTree as ET

def get_news():
    """Fetch top news headlines from BBC RSS feed"""
    try:
        url = "https://feeds.bbci.co.uk/news/rss.xml"
        response = requests.get(url)
        root = ET.fromstring(response.content)
        
        items = root.findall(".//item")
        headlines = []
        for item in items[:5]:
            title = item.find("title").text
            headlines.append(title)
        
        return "Here are the top news headlines. " + ". ".join(headlines[:3])
    except Exception as e:
        return f"Could not fetch news. Error: {str(e)}"