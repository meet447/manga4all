import json
import requests
import json

def top_mangas():
    url = "https://api.comick.app/top?accept_mature_content=true"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://comick.app/",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return response.status_code
    
def hot_managas(page):
    url = f"https://api.comick.app/chapter?lang=en&accept_erotic_content=true&page={page}&device-memory=4&order=hot"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://comick.app/",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return response.status_code
    
    
def new_managas(page):
    url = f"https://api.comick.app/chapter?lang=en&accept_erotic_content=true&page={page}&device-memory=4&order=new"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://comick.app/",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return response.status_code
    
def details_manga(slug):
    url = f"https://api.comick.app/comic/{slug}/?tachiyomi=false"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://comick.app/",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return response.status_code
    
def get_chapters(hid):
    url = f"https://api.comick.app/comic/{hid}/chapters?lang=en"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://comick.app/",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return response.status_code

def get_images(hid):
    url = f"https://api.comick.app/chapter/{hid}/?tachiyomi=false"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://comick.app/",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return response.status_code
    
def comick_search(page, query):
    url = f"https://api.comick.app/v1.0/search/?type=comic&page={page}&limit=15&tachiyomi=false&q={query}&t=false"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://comick.app/",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return response.status_code
    
def most_viewed():
    url = "https://api.comick.app/v1.0/search?advanced=1&sort=view&limit=49&page=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": "https://comick.app/",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return response.status_code