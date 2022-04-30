import time
import json
import random
import base64
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import re
import urllib.parse


class Drugsy(object):
    def __init__(self):
        self.gecko_driver_path = "includes/geckodriver.exe"
        self.binary = FirefoxBinary(r"includes\tor\firefox.exe")
        self.profile = FirefoxProfile(r"includes\tor\TorBrowser\Data\Browser\profile.default")
        # self.profile.set_preference('network.proxy.type', 1)
        # self.profile.set_preference('network.proxy.socks', '127.0.0.1')
        # self.profile.set_preference('network.proxy.socks_port', 9150)
        self.driver = webdriver.Firefox(self.profile,self.binary,executable_path=self.gecko_driver_path)
        # Default wait time
        self.rest = 3
        # WebDriverWait(self.driver, timeout=20)

    def wait_for_tor(self):
        self.driver.implicitly_wait(30)
        self.base_url = "about:tor"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get("http://check.torproject.org/")
        self.assertEqual("Congratulations. This browser is configured to use Tor.", driver.find_element_by_css_selector("h1.on").text)

    def base64_double_decode(self,s):
        one = base64.b64decode(s).decode('utf-8')
        return base64.b64decode(one).decode('utf-8')

    def scrape_ahmia(self,query):
        search_engine = "ahmia"
        base = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q="
        url = base + query
        list_title = []
        list_url = []
        links = []
        self.driver.get(url)

        try:
            get_list_url = self.driver.find_elements_by_css_selector('li.result cite')
            get_list_title = self.driver.find_elements_by_css_selector('li.result h4 a')
        except NoSuchElementException:
            print("Element not found")

        for t in get_list_url:
            try:
                for t in get_list_url:
                    t_url = "http://" + t.get_attribute("textContent").strip()
                    list_url.append(t_url)
            
                for t in get_list_title:
                    title = re.sub("<.*?>", "", t.get_attribute("textContent").strip().replace(",", "|"))
                    title = re.sub(r"[\n\t]*", "", title)
                    list_title.append(title)
            except IndexError():
                    print("Out of index")

        for i in range(len(list_url)):
            try:
                data = {
                    "url": (list_url[i]),
                    "title": str(list_title[i])
                }

                data_csv = "\n{},{},{},{},{}".format(list_url[i], list_title[i], query, search_engine, time.time())
                with open("./output/links.csv", "a") as f:
                    f.write(data_csv)
                    links.append(data)
            except UnicodeEncodeError:
                print("Codec can't encode")
        
        res = {
            "search_engine": search_engine,
            "query": query,
            "total": len(links),
            "links": links
        }

        return res

    def scrape_devil_search(self,query):
        search_engine = "devil search"
        base = "http://search65pq2x5oh4o4qlxk2zvoa5zhbfi6mx4br4oc33rpxuayauwsqd.onion/index.php?word="
        url = base + query
        list_title = []
        list_url = []
        links = []
        self.driver.get(url)

        try:
            ele_last_li = self.driver.find_elements_by_css_selector('div.pagination a.page-link:nth-last-child(1)')
            total_page = ele_last_li[0].get_attribute("textContent")
        except IndexError:
            total_page = 1

        page = 1

        while(page<=int(total_page)):
            self.driver.get(url+"&p="+str(page))

            get_list_title = self.driver.find_elements_by_css_selector('div.card-body')
            get_list_url = self.driver.find_elements_by_css_selector('div.card-body small a.text-success')

            for t in get_list_url:
                list_url.append(t.get_attribute("href").strip())
            
            for t in get_list_title:
                title = re.sub("<.*?>", "", t.get_attribute("textContent").strip().replace(",", "|"))
                title = re.sub(r"[\n\t]*", "", title)
                list_title.append(title)

            page = page + 1

        for i in range(len(list_url)):
                try:
                    data = {
                        "url": (list_url[i]),
                        "title": str(list_title[i])
                    }

                    data_csv = "\n{},{},{},{},{}".format(list_url[i], list_title[i], query, search_engine, time.time())
                    with open("./output/links.csv", "a") as f:
                        f.write(data_csv)
                    links.append(data)
                except UnicodeEncodeError:
                    print("Codec can't encode")

        res = {
            "search_engine": search_engine,
            "query": query,
            "total": len(list_url),
            "links": links
        }

        return res

        
    def scrape_torch(self,query):
        search_engine = "torch"
        base = "http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/search?query="
        url = base + query + "&action=search"
        list_title = []
        list_url = []
        links = []
        self.driver.get(url)

        get_list_url = self.driver.find_elements_by_css_selector('div.result h5 a')

        for t in get_list_url:
            try:
                t_url = "http://" + t.get_attribute("host")
                t_title = t.get_attribute("textContent").strip().replace(",", "|")
                t_title = re.sub("<.*?>", "", t_title)
                t_title = re.sub(r"[\n\t]*", "", t_title)

                data = {
                    "url": t_url,
                    "title": t_title
                }

                print(data)

                links.append(data)

                data_csv = "\n{},{},{},{},{}".format(t_url, t_title, query, search_engine, time.time())
                with open("./output/links.csv", "a") as f:
                    f.write(data_csv)
            except UnicodeEncodeError:
                    print("Codec can't encode")
        
        res = {
            "search_engine": search_engine,
            "query": query,
            "total": len(links),
            "links": links
        }

        return res


    def scrape_onion_index(self, query):
        search_engine = "onion index"
        base = "http://oniondxjxs2mzjkbz7ldlflenh6huksestjsisc3usxht3wqgk6a62yd.onion/search?query="
        url = base + query + "&submit=Search"
        list_title = []
        list_url = []
        links = []
        self.driver.get(url)

        try:
            ele_last_li = self.driver.find_elements_by_css_selector('.paginations > a:nth-last-child(3)')
            total_page = ele_last_li[0].get_attribute("textContent")
            if(ele_last_li[0].get_attribute("class") == "disabled"):
                total_page = 1
        except IndexError:
            total_page = 1

        page = 1

        while(page<=int(total_page)):
            self.driver.get(url+"&page="+str(page))

            get_list_url = self.driver.find_elements_by_css_selector('div#results a')
            get_list_title = self.driver.find_elements_by_css_selector('div#results h5.text-primary.text-break')

            c = 1
            for t in get_list_url:
                if (c%2 == 0):
                    print(t.get_attribute("href"))
                    list_url.append(t.get_attribute("href"))
                c = c + 1
            
            for t in get_list_title:
                t_title = t.get_attribute("textContent").strip().replace(",", "|")
                t_title = re.sub("<.*?>", "", t_title)
                t_title = re.sub(r"[\n\t]*", "", t_title)
                list_title.append(t_title)

            page = page + 1

        for i in range(len(list_url)):
                try:
                    try:
                        data = {
                            "url": (list_url[i]),
                            "title": str(list_title[i])
                        }

                        data_csv = "\n{},{},{},{},{}".format(list_url[i], list_title[i], query, search_engine, time.time())
                        with open("./output/links.csv", "a") as f:
                            f.write(data_csv)
                        links.append(data)
                    except UnicodeEncodeError:
                        print("Codec can't encode")
                except IndexError:
                    print("Out of range")

        res = {
            "search_engine": search_engine,
            "query": query,
            "total": len(list_url),
            "links": links
        }

        return res