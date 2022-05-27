from typing import Any
import json

from models import models

def submitReport(event: Any, context: Any):
    """
    Handle the submition of a report on the api call

    :param event: the event containing the POST request body and headers
    :param context: the context object descrbing the context of the call
    """
    body = json.loads(event["body"])
    print("SUCCESSFULKY PARSED THE JSON DATA")
    new_event = models.Event.from_dict(body)
    print("CREATED NEW EVENT")

    return new_event
