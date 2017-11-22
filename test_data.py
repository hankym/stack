import pickle

from datetime import datetime

SAVE_DB_PATH = './db/data.pkl'

from Stack_getData import format_day,get_days


def show_last_five_data():


    db = open(SAVE_DB_PATH,"rb")

    totle = pickle.load(db)

    db.close()

    todays = get_days(datetime.today(),5)

    for t in todays:

        if t in totle:

            names = []

            for i in totle[t]:
                names.append(i["stack_name"])

            print(t + str(names))


if __name__ == "__main__":

    show_last_five_data()