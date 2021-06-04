import pymongo
class DB:

    def __init__(self):
        try:
            self.DB_NAME = 'PINCODE_DB'
            # self.connection =mg.MongoClient(f"mongodb://cowinDB:cowin_db_1@cluster0-shard-00-00.ftxo4.mongodb.net:27017,cluster0-shard-00-01.ftxo4.mongodb.net:27017,cluster0-shard-00-02.ftxo4.mongodb.net:27017/{self.DB_NAME}?ssl=true&replicaSet=atlas-13pnfs-shard-0&authSource=admin&retryWrites=true&w=majority")
            self.connection = pymongo.MongoClient(f"mongodb+srv://scrapper:12345@scrapperdb.p8wac.mongodb.net/{self.DB_NAME}?retryWrites=true&w=majority")
            self.dataBase = self.connection[self.DB_NAME]

            # print(self.connection.test)
        except Exception as e:
            print(e)

    def create_collection(self, pin_code, number_,age):
        """
        For Creating Collection in the database
        :param pin_code:
        :return:
        """
        try:

            self.COLLECTION_NAME = str(pin_code)
            self.number = int(number_[number_.find('+'):])
            self.age=age
            self.collection = self.dataBase[self.COLLECTION_NAME]
            self.collection.insert_one({"_id": self.number,'age':self.age})
            return f"Your Number is Successfully Registered 📝 !"

        except pymongo.errors.DuplicateKeyError:
            return f"For This Pincode Your Number is Already Registered 📝 With Us 🤷🏻‍♀"


    def get_collection_name(self):
        """
        This is helper funcion so that it's easy to get the name of collection
        :return: list of collection
        """
        return self.dataBase.list_collection_names()

    def get_collection_info(self,coll_name):
        self.collection=self.dataBase[coll_name]
        return list(self.collection.find())
            # print(i['_id'])
            # print(i['age'])


# x.create_table(pin,number)

# if __name__=="__main__":
#     x=DB()
