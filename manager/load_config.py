import os
from base64 import b64decode

import boto3
import yaml

# Make local configuration dictionary
CONFIG = {}

# Load configuration dependent on environment
if "AWS_LAMBDA_FUNCTION_NAME" in os.environ:
    # Load lambdas configuration
    CONFIG["MODE"] = "LAMBDAS"

    try:
        # Load all enviornment variables
        CONFIG.update({key: value for key, value in os.environ.items()})

        # Add kms dependent enviornment variables
        # MONGO_PASSWORD = boto3.client('kms').decrypt(
        #     CiphertextBlob=b64decode(os.environ['MONGO_PASSWORD']),
        #     EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
        # )['Plaintext'].decode('utf-8')
        #
        # MONDO_USER = boto3.client('kms').decrypt(
        #     CiphertextBlob=b64decode(os.environ['MONGO_USER']),
        #     EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
        # )['Plaintext'].decode('utf-8')

    except Exception as e:
        raise Exception(f"Unable to load lambdas configuration environment:\t{e}")

else:
    # Load local configuration
    CONFIG["MODE"] = "LOCAL"

    try:
        # Load the local config.yaml file and save into the config dictionary
        LOCAL = os.path.dirname(os.path.dirname(__file__))
        CONFIG_FILE = open(os.path.join(LOCAL, 'config.yaml'))
        CONFIG.update(yaml.load(CONFIG_FILE, Loader=yaml.FullLoader))
        
    except Exception as e:
        raise Exception(f"Unable to load local configuration:\t{e}")
