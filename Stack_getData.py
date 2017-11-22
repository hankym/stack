from bs4 import BeautifulSoup,SoupStrainer


URL_FILE = "default.html"

def test():



    table_id = SoupStrainer(id = "stockList_table")

    f = open(URL_FILE,"r",encoding="UTF-8")
    bs = BeautifulSoup(f.read(),"lxml",parse_only=table_id)

    f.close()


    ll = bs.findAll(class_="sname")
    lup = bs.findAll(class_="up")
    a  = ll[0].findAll("a")


    tr = bs.findAll("tr")
    print(tr)


    print("______________")

    tags = []

    for t in  tr:
        if t is not None:

            if len(t.findAll("td")) > 0:
                tags.append(t)



    td_tags = tags[0].findAll("td")



    for i in td_tags:
        print(i.text)

STACK_NAME    = "stack_name"
NEW_PRICE     = "new_price"
PRICE_LIMIT   = "price_limit" #涨跌幅
PRICE_CHANGE  = "price_change" #涨跌额
LARGE_IN      = "large_in" #主力流入
LARGE_IN_TAKE = "large_in_take" #主力净占比
YESTODAY_LAST = "yestoday_last" #昨收
TODAY_START   = "today_start" #今开
TOP_PRICE     = "top_price" #最高
LOW_PRICE     = "low_price" #最低
SALE_NUM      = "sale_num" #成交量
CHANGE_NUM    = "change_num" #换手率

STACK_NAME_INDEX    = 0
NEW_PRICE_INDEX     = 3
PRICE_LIMIT_INDEX   = 4
PRICE_CHANGE_INDEX  = 5
LARGE_IN_INDEX      = 6
LARGE_IN_TAKE_INDEX = 7
YESTODAY_LAST_INDEX = 8
TODAY_START_INDEX   = 9
TOP_PRICE_INDEX     = 10
LOW_PRICE_INDEX     = 11
SALE_NUM_INDEX      = 12
CHANGE_NUM_INDEX    = 13

INDEX_LIST = [STACK_NAME_INDEX,NEW_PRICE_INDEX,PRICE_CHANGE_INDEX,LARGE_IN_INDEX,LARGE_IN_TAKE_INDEX,YESTODAY_LAST_INDEX,
              TODAY_START_INDEX,TOP_PRICE_INDEX,LOW_PRICE_INDEX,SALE_NUM_INDEX,CHANGE_NUM_INDEX]


KEY_LIST = [None] * 15



def init_key_list():


    global KEY_LIST

    KEY_LIST[STACK_NAME_INDEX] = STACK_NAME
    KEY_LIST[NEW_PRICE_INDEX]  = NEW_PRICE
    KEY_LIST[PRICE_LIMIT_INDEX] = PRICE_LIMIT
    KEY_LIST[PRICE_CHANGE_INDEX] = PRICE_CHANGE
    KEY_LIST[LARGE_IN_INDEX] = LARGE_IN
    KEY_LIST[LARGE_IN_TAKE_INDEX] = LARGE_IN_TAKE
    KEY_LIST[YESTODAY_LAST_INDEX] = YESTODAY_LAST
    KEY_LIST[TODAY_START_INDEX] = TODAY_START
    KEY_LIST[TOP_PRICE_INDEX] = TOP_PRICE
    KEY_LIST[LOW_PRICE_INDEX] = LOW_PRICE
    KEY_LIST[SALE_NUM_INDEX] = SALE_NUM
    KEY_LIST[CHANGE_NUM_INDEX] = CHANGE_NUM


from datetime import datetime,timedelta

import pickle
import os


def format_day(day):

    return str(day.year) + ":" + str(day.month) + ":" + str(day.day)

"""
获取nowday 之前的几天的日期，并按year:month:day 格式返回
"""
def get_days(nowday,daynum = 0):

    days = []

    for i in range(daynum):

        d = nowday - timedelta(i)

        d_format = format_day(d)

        days.append(d_format)

    return days



SAVE_DB_PATH = './db/data.pkl'
class Stack_Data_Save():

    def __init__(self,max_num = 10):

        self.stacks_data = []

        self.bs = None

        self.max_num = max_num

        self.savedb = SAVE_DB_PATH


    def __get_trs(self,soup):

        trs = soup.findAll("tr")

        return trs[1:-1] #过滤掉第一个不是表格项

    def __get_tds(self,trs):

        tds = []

        for t in trs:

            td = t.findAll("td")

            tds.append(td)

        return tds
    def __print_td(self,tds):

        for i in tds:
            for td in i:
                print(td.text)


    def __put_into_list(self,tds):


        self.totle = []

        tempdict = {}

        for i ,td in enumerate(tds):

            if i >= self.max_num:
                break

            tempdict = {}

            for index,value in enumerate(td):

                if index in INDEX_LIST:

                    tempdict[KEY_LIST[index]] = value.text

            self.totle.append(tempdict)

    def save_data(self):

        savefile = {}
        """
        try:

            db = open('data.pkl', 'rb')
            savefile = pickle.load(db)
            db.close()
        except EOFError: #如果文件没
            print("file not create")
        """

        #如果文件不存在则先创建文件，即写文件

        if os.path.exists(self.savedb):
            db = open(self.savedb, 'rb')
            savefile = pickle.load(db)
            db.close()


        db = open(self.savedb,'wb+')

        key = format_day(datetime.today())#str(datetime.today().year) + ":" + str(datetime.today().month) + ":" + str(datetime.today().day - 1)

        savefile[key] = self.totle

        pickle.dump(savefile,db)

        db.close()




    def analyse_file(self,filename):

        table_tag = SoupStrainer(id = "stockList_table")

        if table_tag is None:

            print("get table tag error")
            return

        with open(filename,"r",encoding="UTF-8") as f:

            self.bs = BeautifulSoup(f.read(),"lxml",parse_only=table_tag)

            trs = self.__get_trs(self.bs)


            tds = self.__get_tds(trs)


            #self.__print_td(tds)

            self.__put_into_list(tds)


            print(self.totle)
            print(len(self.totle))



class Stack_data_Load():

    def __init__(self):

        self.savedb = SAVE_DB_PATH

        self.totle = []
    def get_data(self):

        if os.path.exists(self.savedb) == False:

            print("file not exsit")

            return None

        db = open(self.savedb,"rb")

        savefile = pickle.load(db)

        db.close()


        return db






def test_db():

    db = open(SAVE_DB_PATH,"rb")

    file = pickle.load(db)

    print(type(file))

    for key,value in file.items():
        print(str(key) + " : " + str(value))
    print(len(file))


    db.close()


def test_days():


    today = datetime.today()

    print(get_days(today,5))

if __name__ == "__main__":

    #test()

    init_key_list()

    print(KEY_LIST)
    sg = Stack_Data_Save()

    sg.analyse_file(URL_FILE)

    sg.save_data()

    test_db()

    #test_days()
    print("end!!")




