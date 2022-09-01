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

def reportDefinition(mc: MongoClient, event: Any, context: Any):
    """
    Define the report needed for the current report
    """

    mc.saveReport(event.json["context"])

    mc.close() # TODO: finish the close function for memory safety

    return mc

def reportDefinitionExtended(mc: MongoCLient, event: Any, context: Any):
    """
    Report definition extended 

    :param mc: mc the class to extended Mongoclient decided
    :param event: the event that the lambda class passes
    :param context: the context of the lambda function 
    """

    for i in mc.saveReport():
        pprint(i)
        i["children"] = models.to_dict([models.dataclass])

    return i

def extendedReportDefinition(mc: MongoClient, event: Any, context: Any):
    """
    jReport definition extended

    :param mc: mc extended project
    :param event: the event returned by the lambda function
    :param context: the context pf the event called by the lambda function
    """
    
    for i in mc.saveReport():
        pprint(i)
        pprint(i["children"])

    return