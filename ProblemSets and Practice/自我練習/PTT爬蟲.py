# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:36:24 2018

@author: Asus
"""
#PTT爬蟲練習
from bs4 import BeautifulSoup as bs
import re
import requests

def mainfunction(Current_Soup,author_Name =None, key_Word=None):
#finding author keyword or both
#    regular_expression = re.compile()
    if key_Word!=None and author_Name==None:
        for item in Current_Soup:
            if key_Word in item.select(".title")[0].text:
                print(item.select(".title")[0].text, "https://www.ptt.cc"+item.select("div.title a")[0]["href"])

    elif key_Word == None and author_Name != None:
        for item in Current_Soup:
            if item.select(".author")[0].text == author_Name:    
                print(author_Name,item.select(".title")[0].text,"https://www.ptt.cc"+item.select("div.title a")[0]["href"])
    else:
        for item in Current_Soup:
            if item.select(".author")[0].text == author_Name and key_Word in item.select(".title")[0].text:
                print(author_Name, item.select(".title")[0].text,"https://www.ptt.cc"+item.select("div.title a")[0]["href"])
    
    
def Crawler(start_Url, author_Name =None, key_Word=None, Max_Number_Of_Pages= None):
#    看是要找作者還是關鍵字
    Current_Url = "https://www.ptt.cc/bbs/"+start_Url+"/index.html"
    if key_Word==None and author_Name==None:
        print("You need to give author or keywords")
    else:
        try:
            if Max_Number_Of_Pages == None:
                while True:
                    Request_Current_Url = requests.get(Current_Url)
                    next_Url ="https://www.ptt.cc" +bs(Request_Current_Url.text,"lxml").select("div.btn-group-paging a")[1]["href"]
                    Current_Soup = bs(Request_Current_Url.text,"lxml").select(".r-ent")
                    mainfunction(Current_Soup,author_Name, key_Word)
                    Current_Url = next_Url
            else:
                for i in  range(Max_Number_Of_Pages):
                    Request_Current_Url = requests.get(Current_Url)
                    next_Url ="https://www.ptt.cc" +bs(Request_Current_Url.text,"lxml").select("div.btn-group-paging a")[1]["href"]
                    Current_Soup = bs(Request_Current_Url.text,"lxml").select(".r-ent")
                    mainfunction(Current_Soup,author_Name, key_Word)
                    Current_Url = next_Url
        except KeyError:
            pass
        
        finally:
            print("\nCrawling Finished")