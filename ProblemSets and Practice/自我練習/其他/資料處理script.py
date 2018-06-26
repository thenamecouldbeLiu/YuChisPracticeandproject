# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:10:19 2018

@author: Asus
"""

import pandas as pd
import numpy as np
import pylab
import matplotlib.pyplot as plt

'''找:點閱數大於某個數,中立 正面 負面個數, 正面強度與點閱數的比較, 負面強度與點閱數的比較, 平均點閱數,
平均正面強度,平均負面強度, '''
#file_list=["淘寶.xlsx","蝦皮.xlsx",PChome.xlsx]
class static_describe(object):
    def __init__(self,file):
        self.file_df  =pd.read_excel(file)
        self.emotion_list =['中立', '正面','負面']
    def findStatic(self, save_txt=None):
        
        wanted_infor =['標題', '點閱數', '正面強度', '負面強度', '情緒標記']
        
        
        
        #title_dict={}
        #for title in set(taobao_df["標題"]):
        #    if not title_dict.__contains__(title):
        #        title_dict[title]={}
        
        #selected_df.sort_values(by=["標題"],ascending =False, inplace=True)
        selected_df= self.file_df[wanted_infor] #選出來的DATABASE
        '''情緒種類'''
        self.emotion_list =['中立', '正面','負面']
        '''點閱數Filter'''
        self.non_filted= selected_df['點閱數']
        self.filter_click_bigger_than5000 =selected_df[selected_df["點閱數"]>5000]
        self.filter_click_bigger_than1000 = selected_df[selected_df["點閱數"]>1000]
        self.filter_click_bigger0_smaller1000= selected_df[(selected_df["點閱數"]<1000) & (selected_df["點閱數"]>0)]
        self.filter_click_bigger_than0=selected_df[selected_df["點閱數"]>0]
        self.filter_click_quales_0 =selected_df[selected_df["點閱數"]==0]
        '''filter名稱與字典'''
        self.filted_name= ["未分類平均點擊率:",'點閱數等於0:', '點閱數大於0 :','點閱數大於0 小於1000:','點閱數大於1000:','點閱數大於5000:']
        self.filted_list=[self.non_filted, self.filter_click_quales_0,self.filter_click_bigger_than0,self.filter_click_bigger0_smaller1000, self.filter_click_bigger_than1000, self.filter_click_bigger_than5000,]
        self.filter_dict = dict(zip(self.filted_name, self.filted_list))
        #print('點閱數大於5000:',len(filter_click_bigger_than5000))
        #print('點閱數大於1000:',len(filter_click_bigger_than1000))
        #print('點閱數大於0 小於1000:',len(filter_click_bigger0_smaller1000))
        #print('點閱數大於0 :',len(filter_click_bigger_than0))
        #print('點閱數等於:0:',len(filter_click_quales_0))
        '''算平均與標準差'''
        for f in self.filter_dict:
            print(f,"\n")
            print("限制範圍樣本數:",len(self.filter_dict[f]))
            print("平均值")
            print(self.filter_dict[f].mean(),"\n")
            print("標準差")
            print(self.filter_dict[f].std(),"\n")
            print("-"*10)
        
        print("情緒強度")
        for emo in self.emotion_list:
            filter_emo=selected_df['情緒標記']==emo
            print(emo,"強度個數:",len(selected_df[filter_emo]))
        print("-"*10)
        for emo in self.emotion_list:
            try:
                print("總體平均",emo,"強度:", (selected_df[emo+'強度']).mean())
            except:
                pass
        
        '''relation between 來源與情緒標記'''
        print("-"*10)
        source_set= set(self.file_df["來源"])
        source_mark = self.file_df[["來源","情緒標記"]].sort_values(by=["來源","情緒標記"])
        for source in source_set:
            print("-"*10,)
            print(source)
            
            for emo in self.emotion_list:
                print(emo,":",len(source_mark[(source_mark["來源"]==source) & (source_mark["情緒標記"]==emo)]))
    def getEomtionNumberDict(self, select_filter ="All", click =None):
        '''返回目前用的標籤與總量，用來畫圖'''
        df = self.file_df
        if click!= None:
            df= df[df["點閱數"]>click]
        emotion_dict = {} #選取的標籤為KEY, 取得值為Value
        if select_filter=="All":
            for emo in self.emotion_list:
                filter_emo=df['情緒標記']==emo
                emotion_dict[str(select_filter+emo)+"總和"] = (len(df[(filter_emo)]),)
#                except:
#                    emotion_dict[str(select_filter+emo)+"總和"] = (len(df[(filter_emo)]),)
#        字典的值須為Tuple才能正常繪圖
        else:
            '''假設有再限定來源範圍'''
            for emo in self.emotion_list:
                filter_emo = (df['情緒標記']==emo) & (df["來源"]==select_filter)
                emotion_dict[str(select_filter+emo)+"總和"] = (len(df[filter_emo]),)
        return emotion_dict
    def getEomtionAverageDict(self, source_select_filter ="All", click =None):
        df = self.file_df
        if click !=None:
            df = df[df["點閱數"]>click]
#        return(df)
        '''返回目前用的標籤與平均值，用來畫圖'''
        emotion_dict = {}#選取的標籤為KEY, 取得值為Value
        if source_select_filter=="All":
            for emo in self.emotion_list:
                try:
                    emotion_dict[emo+"強度平均"] = (df[emo+'強度']).mean()
                except:
                    emotion_dict[emo+"強度"] = (0,)
        else:
            filted_df = df[df["來源"]==source_select_filter]
#        字典的值須為Tuple才能正常繪圖
#            print(emo_filted_df)
            for emo in self.emotion_list:
                try:
                    emo_filted_df = filted_df[emo+"強度"]
                    emotion_dict[str(source_select_filter+emo)+"強度平均"] = (emo_filted_df.mean(),)
                except:
                    emotion_dict[str(source_select_filter+emo)+"強度平均"] =0
        return emotion_dict
    def getEomtionStdDict(self, source_select_filter ="All", click =None):
        '''回傳點擊大於某個數的資料的標準差'''
        df = self.file_df
        if click !=None:
            df = df[df["點閱數"]>click]

        '''返回目前用的標籤與平均值，用來畫圖'''
        emotion_dict = {}#選取的標籤為KEY, 篩選後值為Value
        if source_select_filter=="All":
            for emo in self.emotion_list:
                try:
                    emotion_dict[emo+"強度標準差"] =(df[emo+'強度']).std()
                except:
                    emotion_dict[emo+"強度"] = (0,)
        else:
            filted_df = df[df["來源"]==source_select_filter]
#        字典的值須為Tuple才能正常繪圖
            for emo in self.emotion_list:
                try:
                    emo_filted_df = filted_df[emo+"強度"]
                    emotion_dict[str(source_select_filter+emo)+"強度標準差"] =(emo_filted_df.std(),)
                except:
                    emotion_dict[str(source_select_filter+emo)+"強度標準差"] =0
        return emotion_dict
    def getCampareSumDict(self,data_source=["淘寶.xlsx", "蝦皮.xlsx","PChome.xlsx"],select_filter ="All",click = None):
        '''例如:找點擊數5000以上, 並以"討論區", "正面"來篩選總和'''
        compareSum_dict ={}
        for data in data_source:
            data_df = pd.read_excel(data)
            if click!=None:
                data_df= data_df[data_df["點閱數"]>click]
            if select_filter=="All":
                for emo in self.emotion_list:
                    filted_df =data_df[data_df["情緒標記"]==emo]
                    compareSum_dict[data+emo+" 總和"]=(len(filted_df),)
            else:
                filted_df = data_df[data_df["來源"]==select_filter]
                for emo in self.emotion_list:
                    emo_filted_df =filted_df[filted_df["情緒標記"]==emo]
                    compareSum_dict[data+" 點擊大於 "+str(click)+"的"+select_filter+str(emo)+"總和"] = (len(emo_filted_df),)
        return compareSum_dict
                        

    def getCompareMeanDict(self,data_source=["淘寶.xlsx", "蝦皮.xlsx","PChome.xlsx"],select_filter ="All",click = None):
        '''例如:找點擊數5000以上, 並以"討論區", "正面"來篩選之後平均'''
        compareMeanDict ={}
#        print(self.emotion_list)
        for data in data_source:
            data_df = pd.read_excel(data)
            if click!=None:
                data_df= data_df[data_df["點閱數"]>click]
            if select_filter=="All":
#                print(len(data_df))
                for emo in self.emotion_list:
                    try:
#                        print(emo, data)
                        compareMeanDict[data,emo,"強度平均"]=((data_df[emo+"強度"]).mean(),)
                    except:
                        compareMeanDict[data,emo,"強度平均"]=(0,)
            else:
                filted_df = data_df[data_df["來源"]==select_filter]
#                print(filted_df)
                for emo in self.emotion_list:
                    try:
#                        print("suessess")
                        emo_filted_df= filted_df[emo+"強度"]

                        compareMeanDict[data+" 點擊大於 "+str(click)+"的"+select_filter+str(emo)+"強度平均"] = (emo_filted_df.mean(),)
                    except KeyError:
#                        print("fail,Key",emo)
                        compareMeanDict[data+" 點擊大於 "+str(click)+"的"+select_filter+str(emo)+"強度平均"]=(0,)
        return compareMeanDict
    def getCompareStdDict(self,data_source=["淘寶.xlsx", "蝦皮.xlsx","PChome.xlsx"],select_filter ="All",click = None):
        '''例如:找點擊數5000以上, 並以"討論區", "正面"來篩選之後平均'''
        compareMeanDict ={}
#        print(self.emotion_list)
        for data in data_source:
            data_df = pd.read_excel(data)
            if click!=None:
                data_df= data_df[data_df["點閱數"]>click]
            if select_filter=="All":
#                print(len(data_df))
                for emo in self.emotion_list:
                    try:
#                        print(emo, data)
                        compareMeanDict[data,emo,"強度標準差"]=((data_df[emo+"強度"]).std(),)
                    except:
                        compareMeanDict[data,emo,"強度標準差"]=(0,)
            else:
                filted_df = data_df[data_df["來源"]==select_filter]
#                print(filted_df)
                for emo in self.emotion_list:
                    try:
#                        print("suessess")
                        emo_filted_df= filted_df[emo+"強度"]

                        compareMeanDict[data+" 點擊大於 "+str(click)+"的"+select_filter+str(emo)+"強度標準差"] = (emo_filted_df.std(),)
                    except KeyError:
#                        print("fail,Key",emo)
                        compareMeanDict[data+" 點擊大於 "+str(click)+"的"+select_filter+str(emo)+"強度標準差"]=(0,)
        return compareMeanDict
def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    model_result = []
    xVal = np.array(x)
    yVal = np.array(y)
    for degree in degs:
        regression = np.polyfit(xVal, yVal, degree)
        model_result.append(regression)
    return model_result

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    mean_y  = sum(y)/len(y)
    numerator = 0
    denominator = 0
    place = 0
    while place < len(y):
        try:
            denominator+= (y[place]-mean_y)**2
            numerator+= (y[place] - estimated[place])**2
            place+=1
        except:
            continue
    return 1-float(numerator/denominator)

def barGraphPlot(data,xlabel=None,ylabel=None, graphTitle=None,figureName = None,save_graph =False):
    print(data)
    graph = pd.DataFrame(data)
    test_graph=graph.plot(kind="bar", grid=True,legend =True,title = graphTitle, figsize= (8,10), fontsize =15)
    test_graph.set_ylabel(ylabel,fontsize =15)
    test_graph.set_xlabel(xlabel,fontsize =20)
    if figureName!= None and save_graph:
        plt.savefig(figureName)
    plt.title(graphTitle)
    plt.show()

def pieGraphPlot(data,xlabel=None,ylabel=None, graphTitle=None,figureName = None, save_graph =False):
    print(data)
    plt.axes(aspect='equal')
    plt.pie(x= data.values(),labels=data.keys(),autopct='%1.2f%%',pctdistance=0.8, radius = 1.5,textprops = {'fontsize':18, 'color':'k'})
    if figureName!= None and save_graph:
        plt.savefig(figureName)
    plt.title(graphTitle)
    plt.show()
    
testClass =static_describe("淘寶.xlsx")
#    testClass.findStatic()
#print(testClass.getCompareStdDict(select_filter = "討論區"))
#for data in ["淘寶.xlsx", "蝦皮.xlsx","PChome.xlsx"]:
#    print("*"*15,"Now showing data analysis of",data,"*"*15)
#
#    for item in ["All"]:
#        barGraphPlot(testClass.getEomtionNumberDict(item), "Emotion", "Number", graphTitle= (data+" "+item+" "+"Total"), figureName=data+item+"總和直條圖.jpg",save_graph=True)
#        pieGraphPlot(testClass.getEomtionNumberDict(item),graphTitle= "情緒分布圓餅圖",save_graph=True)
#        barGraphPlot(testClass.getEomtionAverageDict(item), "Emotion", "Number", graphTitle=data+" "+item+" "+"Average",figureName=data+item+"情緒強度平均直條圖.jpg",save_graph=True)
#        barGraphPlot(testClass.getEomtionStdDict(item), "Emotion", "Number", graphTitle=data+" "+item+" "+"Std",figureName=data+item+"情緒強度標準差直條圖.jpg",save_graph=True)
#barGraphPlot(testClass.getCampareSumDict(select_filter="All"),"Emotion", "Number", graphTitle=("資料總和比較直條圖.jpg"), figureName="資料總和比較直條圖.jpg",save_graph=True)
#barGraphPlot(testClass.getCompareMeanDict(select_filter="All"),"Emotion", "Number", graphTitle=("資料平均比較直條圖"), figureName="資料平均比較直條圖.jpg",save_graph=True)
#barGraphPlot(testClass.getCompareStdDict(select_filter="All"),"Emotion", "Number", graphTitle=("資料標準差比較直條圖"), figureName="資料標準差比較直條圖.jpg",save_graph=True)

#testClass.findStatic()
#print("click>5000 average",testClass.getEomtionAverageDict(click=5000))
#print("click>5000 Sum",testClass.getEomtionNumberDict(click=5000))
#testClass =static_describe("淘寶.xlsx")
#
#pieGraphPlot(testClass.getEomtionNumberDict())
