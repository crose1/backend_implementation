class OperationTypeMissingExeception(Exception):
    message = 'Operation type missing'
    status_code = 400

class MissingDataFieldException(Exception):
    message = 'Data body missing'
    status_code = 400

class DataTypeException(Exception):
    message = 'Data body contains invalid types, must be float or int'
    status_code = 400

class ShortDataException(Exception):
    message = 'Data body too short, must have at least two data points for operation'
    status_code = 400


