# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:36:24 2018

@author: Asus
"""
#PTT爬蟲練習
from bs4 import BeautifulSoup
import re
import requests

def mainfunction(Current_Soup,author_Name =None, key_Word=None):
#finding author keyword or both
#    regular_expression = re.compile()
#    印出要求的keyword或是作者名稱
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
#                未設定上限頁數
                while True:
                    Request_Current_Url = requests.get(Current_Url)#解析網址
                    next_Url ="https://www.ptt.cc" +BeautifulSoup(Request_Current_Url.text,"lxml").select("div.btn-group-paging a")[1]["href"]
#                    抓取下一頁的TAG
                    Current_Soup = BeautifulSoup(Request_Current_Url.text,"lxml").select(".r-ent")
#                    用BeautifulSoup選所要元素
                    mainfunction(Current_Soup,author_Name, key_Word)
#                    用mainfunction找keyword跟author
                    Current_Url = next_Url
#                    把現在網址替換到下一頁
            else:
#                設定上限頁數
                for i in  range(Max_Number_Of_Pages):
                    Request_Current_Url = requests.get(Current_Url)
                    next_Url ="https://www.ptt.cc" +BeautifulSoup(Request_Current_Url.text,"lxml").select("div.btn-group-paging a")[1]["href"]
#                    Current_Soup = BeautifulSoup(Request_Current_Url.text,"lxml").select(".r-ent")
                    mainfunction(Current_Soup,author_Name, key_Word)
                    Current_Url = next_Url
        except KeyError:
#            有錯誤就跳過(通常是因為到底了)，到最後一個會跳到fianlly印出結束
            pass
        
        finally:
            print("\nCrawling Finished")