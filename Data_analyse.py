from datetime import datetime
import pickle

import os

print(os.getcwd())


from Stack_getData import format_day,SAVE_DB_PATH,STACK_NAME,get_days


import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams

class Data_Analyse():

    def __init__(self):




        pass



    def get_one_day(self,day):


        sday = format_day(day)

        return self.totle[sday]


    def get_all_data(self):


        db = open(SAVE_DB_PATH,"rb")

        totle = pickle.load(db)

        db.close()

        self.totle = totle

        return totle

    def cmp_day(self,num_day = 5):

        totle_data = self.get_all_data()

        today_data = self.get_one_day(datetime.today())



        last_days = get_days(datetime.today(),num_day)

        print(last_days)
        self.myset = set([])

        self.result = {}

        for i in  range(num_day):

            if  last_days[i] not in totle_data:
                continue

            one = totle_data[last_days[i]]



            if last_days[i] == format_day(datetime.today()):
                print("jump today")
                continue

            for one_data in today_data:

                for t in  one:

                    if one_data[STACK_NAME] == t[STACK_NAME]:

                        self.myset.add(t[STACK_NAME])
                        if t[STACK_NAME] not in self.result.keys():

                            self.result[t[STACK_NAME]] = 1
                        else:
                            self.result[t[STACK_NAME]] += 1










        self.sort_result()

        print(self.l_result)


    def sort_result(self):


        self.l_result = []
        for key,value in self.result.items():

            self.l_result.append({key:value})


        print(self.l_result)
        self.l_result.sort(key = lambda x:list(x.values())[0])

    def show_result(self):

        x_name = []
        y_value = []
        print(len(self.l_result))
        for item in self.l_result:

            x_name.append(list(item.keys())[0])
            y_value.append(list(item.values())[0])


        x_l = []

        print(x_name)
        for i in range(len(x_name)):

            x_l.append(i + 1)

        print(x_l)
        if len(x_name) > 0:

            fg = plt.figure(10)

            rects = plt.bar(left= x_l,height=y_value,width=0.2)

            plt.xticks(x_l,x_name)

            plt.show()


    def _test_show(self):


        for i in range(5):

            self.l_result.append({str(i):i})

        self.show_result()



def test_matlib():

    fg = plt.figure(10)
    rects = plt.bar(left=(1,2),height=(2,4),width=0.2)

    plt.xticks((1,2),("one","two"))

    plt.show()


if __name__ == "__main__":


    a = Data_Analyse()

    a.cmp_day()

    a.show_result()

    #a._test_show()
    #test_matlib()
    print("end!!")