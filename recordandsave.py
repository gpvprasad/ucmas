import csv
import pandas as pd

class recordandsave:

    def __init__(self,columns:list ) -> None:
        self.maths_answersheet = {}
        for column in columns:
            self.maths_answersheet[column] = []
        pass
    
    def printData(self):
        for column in self.maths_answersheet.keys():
            print(column,self.maths_answersheet[column])
    
    def addData(self,**kwargs):
        for key, value in kwargs.items():
            self.maths_answersheet[key].append(value)
    
    def modifyLatest(self,**kwargs):
        for key, value in kwargs.items():
            self.maths_answersheet[key][-1] = (value)

    def saveData(self):
        df = pd.DataFrame(self.maths_answersheet)
        df.to_csv('test.csv', index = False)


