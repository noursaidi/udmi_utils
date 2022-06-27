"""
Instance of device with both metadata and validation results
"""

from validation_result import ValidationResult

class Device:

    device_id = ''
    site_path = ''

    metadata = None
    event_pointset = None
    state = None

    errors = []
        # Errors assosciated with a file


    def __init__(self, device_id, site_path):
       
        self.site_path = site_path
        self.device_id = device_id
        
        # load test results (validator results)
        self._load_test_results()

        # check if metadata exists and errors
        

    # load all test items
    def _load_test_results(self):
        self.state = self._load_test_result('state')
        self.event_pointset = self._load_test_result('event_pointset')

    # load specific test item
    def _load_test_result(self, schema):
        return ValidationResult(self, schema)
