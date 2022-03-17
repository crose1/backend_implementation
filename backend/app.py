import base64
import csv
import json
from codecs import encode
from crypt import methods

from flask import Flask, jsonify, request

from backend.exceptions import (DataTypeException, MissingDataFieldException,
                                OperationTypeMissingExeception,
                                ShortDataException)
from backend.model.operation_request import OperationRequest
from backend.processor.operation_processor import OperationProcessor

app = Flask(__name__)

#Only has one method /operation to complete some math on input data
@app.route("/operation", methods=['POST'])
def return_operation():
    try:
        #Create internal object type
        operation_request = OperationRequest.from_json(request=request.json)
        
        #Perform mathematical operation on it
        result = OperationProcessor.process_operation_request(operation_request=operation_request)
        
        return {'result': result},  200 
    except (
        DataTypeException,
        MissingDataFieldException,
        OperationTypeMissingExeception,
        ShortDataException
    ) as e:
        return {'error': e.message}, e.status_code

@app.route("/healthcheck", methods=['GET'])
def return_test():
    return {"health": "OK"}, 200