from typing import Any, Dict
import json
from datetime import datetime

from manager.load_config import CONFIG
from apihandlers import submit_report
from clients.mongodb.mongo_client import MongoClient

from pprint import pprint

# Initialize variables globally that will be reused if lambdas container isn't recycled
# Initialize the mongo client depending on the LOCAL or LAMBDAS configuration
mc = None
if CONFIG["MODE"] == "LOCAL":
    mc = MongoClient(
        user=CONFIG["MONGO_USER"],
        password=CONFIG["MONGO_PASSWORD"],
        database=CONFIG["MONGO_DATABASE"],
        atlas_host_name=CONFIG["ATLAS_HOST_NAME"],
        mode=CONFIG["MODE"]
    )
elif CONFIG["MODE"] == "LAMBDAS":
    mc = MongoClient(
        user=None,
        password=None,
        database=CONFIG["MONGO_DATABASE"],
        atlas_host_name=CONFIG["ATLAS_HOST_NAME"],
        mode=CONFIG["MODE"]
    )

# Start the lambda handler that will be invoked on the call of the lambdas function
def lambda_handler(event: Any, context: Any):
    """
    The handler that will be called when the lambda function is run

    :param event: Event can be anything the calling service decides to pass in
    :param context: the context is an object describing what the context of the call is. It's typing is a special AWS type
    """

    # Determine the event that must be processed
    if event["requestContext"]["httpMethod"] == "POST":
        if event["requestContext"]["resourcePath"] == "/submitreport":
            n_event = submit_report.submitReport(mc, event, context)

            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'message': 'Successfully saved report'})
            }

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'Execution started successfully!'})
    }


if __name__ == "__main__":
    lambda_handler(event=None, context=None)
