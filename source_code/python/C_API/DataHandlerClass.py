from EvaluateClass import *
import pickle
import math

class DataHandler:
    #클래스 변수 : 클래스의 모든 인스턴스들이 공유하는 변수
    evaluator = Evaluate()
    
    #static method : 전역함수처럼 쓸 수 있다
    @staticmethod
    def GetItemsFromFile(filename):
        items = []
        with open(filename, 'rb') as f:
            while 1:
                try: 
                    data = pickle.load(f)
                except EOFError:
                    break    
                items.append(data)
        return items

    @staticmethod
    def GetScores(items):
        scores = []
        for item in items:
            scores.append(list(item.values())[0])
        return scores

    @staticmethod
    def GetRawdataInDic(items):
        rawdata={}
        for dic in items:
            a = list(dic.items())
            #print(a)
            rawdata[a[0][0]] = a[0][1]
        return rawdata

    @staticmethod
    def GetTheHighest(rawdata):
        highest =''
        highscore = 0
        for ele in rawdata:
            if highscore < rawdata[ele]:
                highest = ele
                highscore = rawdata[ele]
        return highest

    @staticmethod
    def GetTheLowest(rawdata):
        lowest = ''
        lowscore = 0
        for key in rawdata.keys():
            if rawdata[key] > 0 :
                lowscore = rawdata[key]
                break
				
        for ele in rawdata:
            if lowscore>= rawdata[ele]:
                lowest = ele
                lowscore = rawdata[ele]          
        return lowest


    #생성자 : 객체 변수 모두 초기화
    def __init__(self, filename, clsname):        
        #객체 변수
        self.items = DataHandler.GetItemsFromFile(filename)
        self.scores = DataHandler.GetScores(self.items)
        
        self.average = round(DataHandler.evaluator.average(self.scores), 1)
        self.variance = round(DataHandler.evaluator.variance(self.scores), 1)
        self.std_dev = round(math.sqrt(self.variance), 1)
        self.clsname = clsname
        #ex2
        self.rawdata = DataHandler.GetRawdataInDic(self.items)
        #ex2
        self.highest = DataHandler.GetTheHighest(self.rawdata)
        #ex2
        self.lowest = DataHandler.GetTheLowest(self.rawdata)
        
    def GetAverage(self):
        return self.average

    def GetVariance(self):
        return self.average

    def GetStandardDeviation(self):
        return self.std_dev

    def GetEvaluation(self):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print("{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".format(self.clsname, self.average, self.variance, self.std_dev))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        DataHandler.evaluator.evaluateClass(self.average, self.std_dev)
        
    def WhoIsTheHighest(self):
        return self.highest

    def WhoIsTheLowest(self):
        return self.lowest

    def GetScoreByName(self, name):
        return self.rawdata[name]
    
    
