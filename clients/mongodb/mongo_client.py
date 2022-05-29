import urllib.parse
import pymongo

#Mongo client
class MongoClient():
    def __init__(self, user: str, password: str, database: str, atlas_host_name: str, mode: str="LOCAL"):
        """
        Initiate the pymongo to use with the MongoClient

        :param user: the mongo user to authenticate
        :param password: the mongo password to authenticate
        :param database: the database to write to
        :param mode: the mode to run the client on (specific for LAMBDAS mode to run on iam auth)
        """

        # initialize empty client and base header parameters
        self.client = None
        base_header_params = "retryWrites=true&w=majority"

        if mode == "LAMBDAS":
            # Select the authorization params as aws iam
            aws_auth_params = "authSource=%24external&authMechanism=MONGODB-AWS"

            # Setup the pymongo client with aws iam auth
            self.client = pymongo.MongoClient(
                f"mongodb+srv://{atlas_host_name}/?{aws_auth_params}&{base_header_params}"
            )
        elif mode == "LOCAL":
            #encode the password into url
            pass_urlencoded = urllib.parse.quote(password)

            #Setup the pymongo mongo client
            self.client = pymongo.MongoClient(
                f"mongodb+srv://{user}:{pass_urlencoded}@{atlas_host_name}/?retryWrites=true&w=majority"
            )

        print(self.client[database].list_collection_names())
