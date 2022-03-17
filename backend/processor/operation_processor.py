from backend.exceptions import OperationTypeMissingExeception, ShortDataException
from backend.model.operation_request import OperationRequest

class OperationProcessor:
    def process_operation_request(operation_request: OperationRequest) -> float:
        if operation_request.operation_type == 'mean': 
            return sum(operation_request.data)/len(operation_request.data)

        if operation_request.operation_type == 'median': 
            quotient, remainder = divmod(len(operation_request.data), 2)
            #If odd number in list, return middle number
            if remainder:
                return sorted(operation_request.data)[quotient]
            #Otherwise, interpolate numbers
            return sum(sorted(operation_request.data)[quotient-1:quotient+1]) / 2

        if operation_request.operation_type == 'range': 
            return max(operation_request.data) - min(operation_request.data)
        
        if operation_request.operation_type == 'standard_deviation': 
            if len(operation_request.data) < 2:
                #Require at least two numbers 
                raise ShortDataException()

            mean = sum(operation_request.data)/len(operation_request.data)
            ss = sum((x-mean)**2 for x in operation_request.data) 
            #Always calculating for sample, not population
            pvar = ss/(len(operation_request.data)-1)
            return pvar**0.5

        if operation_request.operation_type == 'variance': 
            if len(operation_request.data) < 2:
                #Require at least two numbers
                raise ShortDataException()

            mean = sum(operation_request.data)/len(operation_request.data)
            ss = sum((x-mean)**2 for x in operation_request.data)
             #Always calculating for sample, not population
            pvar = ss/(len(operation_request.data)-1)
            return pvar
        else: 
            raise OperationTypeMissingExeception