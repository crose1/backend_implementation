from __future__ import annotations
from ast import literal_eval
import enum

import uuid
from dataclasses import dataclass
from typing import List, Mapping

from backend.exceptions import MissingDataFieldException, OperationTypeMissingExeception, DataTypeException

@dataclass
class OperationRequest:
    operation_type: str
    data: List[float | int]
    metadata: str

    @staticmethod
    def from_json(request: Mapping) -> OperationRequest:
        if 'operation_type' not in request:
            raise OperationTypeMissingExeception()
        if 'data' not in request:
            raise MissingDataFieldException()
        if 'metadata' not in request:
            #Do nothing, structure used if we need to use metadata
            pass

        #Validate data types
        try:
            parsed_data = request['data']
            if not all(isinstance(i, (int, float)) for i in parsed_data):
                raise DataTypeException()
        except: 
            raise DataTypeException()
        
        return OperationRequest(
            operation_type=request['operation_type'],
            data=parsed_data,
            metadata=request['metadata'],
        )
