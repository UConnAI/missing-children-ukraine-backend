from typing import Any, Dict
import json
from datetime import datetime

from manager.load_config import CONFIG
from apihandlers import submit_report

from pprint import pprint


def lambda_handler(event: Any, context: Any):
    """
    The handler that will be called when the lambda function is run

    :param event: Event can be anything the calling service decides to pass in
    :param context: the context is an object describing what the context of the call is. It's typing is a special AWS type
    """

    if event["requestContext"]["httpMethod"] == "POST":
        if event["requestContext"]["resourcePath"] == "/submitreport":
            n_event = submit_report.submitReport(event, context)

            pprint(n_event)

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'Execution started successfully!'})
    }


if __name__ == "__main__":
    lambda_handler(event=None, context=None)
