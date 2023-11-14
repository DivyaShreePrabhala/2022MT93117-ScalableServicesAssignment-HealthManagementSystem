import unittest
from unittest.mock import Mock, patch
from lambda_function import (
    lambda_handler,
    handle_get,
    handle_getItemId,
    handle_post,
    handle_put,
    handle_delete,
    get_health_record,
    get_all_health_records,
    delete_health_record,
)

class TestLambdaFunction(unittest.TestCase):
    @patch('lambda_function.table')
    def test_handle_get(self, mock_table):
        # Mock DynamoDB response
        mock_response = {'Item': {'recordId': '123', 'attribute1': 'value1', 'attribute2': 'value2'}}
        mock_table.get_item.return_value = mock_response

        # Create a sample event
        event = {'routeKey': 'GET /health-records', 'pathParameters': {'recordId': '123'}}

        # Call the Lambda handler
        result = handle_get(event)

        # Assert the expected response
        expected_response = {'statusCode': 200, 'body': '{"recordId": "123", "attribute1": "value1", "attribute2": "value2"}'}
        self.assertEqual(result, expected_response)

    # Add similar test cases for other functions

if __name__ == '__main__':
    unittest.main()
