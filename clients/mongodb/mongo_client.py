import urllib.parse
import pymongo

#Mongo client
class MongoClient():
    def __init__(self, user: str, password: str, database: str):
        """
        Initiate the pymongo to use with the MongoClient

        :param user: the mongo user to authenticate
        :param password: the mongo password to authenticate
        :param database: the database to write to
        """

        #encode the password into url
        # pass_urlencoded = urllib.parse.quote(password)

        #Setup the pymongo mongo client
        # self.client = pymongo.MongoClient(
        #     f"mongodb+srv://{user}:{pass_urlencoded}@missingchildrenukraine.nzlsq.mongodb.net/{database}?retryWrites=true&w=majority"
        # )
        aws_arn = "arn:aws:iam::240357374981:role/service-role/missingChildrenBackend-role-6nltq0fh"
        self.client = pymongo.MongoClient(
            f"mongodb+srv://missingchildrenukraine.nzlsq.mongodb.net/{database}?authSource=%24external&authMechanism=MONGODB-AWS&retryWrites=true&w=majority"
        )

        self.db = self.client[database]
        self.db["MissingReports"]

        for i in self.db.find({"address": "ssss"}):
            print(i)
