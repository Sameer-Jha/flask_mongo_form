import pymongo
import db_config

class db:
    def __init__(self):
        client = pymongo.MongoClient(f"{db_config.mongodb_url}:{db_config.mongodb_port}/")
        db_list = client.list_database_names()
        if db_config.db_name in db_list:
            self.cursor = client[db_config.db_name]
            self.collection = self.cursor[db_config.col_name]
        else:
            prompt = input(f"The DataBase {db_config.db_name} doesn't exit. Should I set it up for you (Y/n): ")
            if(prompt[0].lower() == "y"):
                self.cursor = client[db_config.db_name]
                self.collection = self.cursor[db_config.col_name]
            else:
                print("Aborting ......")

    def store_data(self, data):
        x = self.collection.insert_one(data)
        print(f'Insertion Successful {x}')


    def retrieve_data(self):
        data = self.collection.find()
        return list(data)



