from backend.app import app

class TestCreateOperation:
    def test_create_operation_with_positive_numbers_returns_mean(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'mean',
                'data': [1, 2, 3],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['result'] == 2.0
            assert response.status_code == 200

    def test_create_operation_with_negative_numbers_returns_mean(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'mean',
                'data': [1, 0, -1],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['result'] == 0.0
            assert response.status_code == 200
    
    def test_create_operation_with_list_of_even_length_returns_median(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'median',
                'data': [1.0,2,2,3.0,4,3],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['result'] == 2.5
            assert response.status_code == 200
    
    def test_create_operation_with_list_of_odd_length_returns_median(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'median',
                'data': [1, -4, 6.0],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['result'] == 1
            assert response.status_code == 200
    
    def test_create_operation_with_numbers_returns_range_(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'range',
                'data': [1, -4, 6.0],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['result'] == 10.0
            assert response.status_code == 200
        
    def test_create_operation_with_numbers_returns_stddev(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'standard_deviation',
                'data': [0.8,0.4,1.2,3.7,2.6,5.8],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['result'] == 2.0634114147853952
            assert response.status_code == 200
        
    def test_create_operation_with_numbers_returns_variance(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'variance',
                'data': [0.8,0.4,1.2,3.7,2.6,-5.8],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['result'] == 10.985666666666667
            assert response.status_code == 200

    def test_throw_operation_type_missing_exception_when_operation_type_field_missspelt(self):
        with app.test_client() as c:
            operation_request = {
                'operation_typex': '',
                'data': [1, -4, 6.0],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['error'] == 'Operation type missing'
            assert response.status_code == 400
    
    def test_throw_operation_type_missing_exception_when_operation_type_body_empty(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': '',
                'data': [1, -4, 6.0],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['error'] == 'Operation type missing'
            assert response.status_code == 400
    
    def test_throw_data_type_exception_when_data_field_contains_str(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'mean',
                'data': [1, -4, 'str'],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['error'] == 'Data body contains invalid types, must be float or int'
            assert response.status_code == 400
    
    def test_throw_missing_data_field_exception_when_data_field_misspelt(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'mean',
                'datad': [1, -4, 4000],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['error'] == 'Data body missing'
            assert response.status_code == 400
    
    def test_throw_short_data_exception_when_only_one_number_computing_variance(self):
        with app.test_client() as c:
            operation_request = {
                'operation_type': 'variance',
                'data': [1],
                'metadata': 'some string'
            }
            response = c.post('/operation', json=operation_request)

            assert response.json['error'] == 'Data body too short, must have at least two data points for operation'
            assert response.status_code == 400