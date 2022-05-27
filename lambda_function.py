import json
from typing import Any, Dict

import boto3
import json
from datetime import datetime

from pprint import pprint

from manager.load_config import CONFIG


def lambda_handler(event: Any, context: Any):
    """
    The handler that will be called when the lambda function is run

    :param event: Event can be anything the calling service decides to pass in
    :param context: the context is an object describing what the context of the call is. It's typing is a special AWS type
    """
    print("---------------------------------------------")
    print("#")
    print("#")
    print(datetime.now())
    print("#")
    print("#")
    print("---------------------------------------------")
    pprint(event)
    print("#")
    print("#")
    pprint(context)
    print("---------------------------------------------")

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'Execution started successfully!'})
    }


if __name__ == "__main__":
    lambda_handler(event=None, context=None)
