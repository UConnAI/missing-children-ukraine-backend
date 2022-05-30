from typing import Any
import json

from models import models
from clients.mongodb.mongo_client import MongoClient

def submitReport(mc: MongoClient, event: Any, context: Any):
    """
    Handle the submition of a report on the api call

    :param mc: MongoClient to be used for storing the report
    :param event: the event containing the POST request body and headers
    :param context: the context object descrbing the context of the call
    """

    body = json.loads(event["body"])
    new_report = models.Report.from_dict(body)

    mc.saveReport(new_report.to_dict())

    return new_report
