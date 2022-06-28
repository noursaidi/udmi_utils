"""
Instance of device with both metadata and validation results
"""

from validation_result import ValidationResult

class Device:

    device_id = ''
    site_path = ''

    metadata = None
    
    registered_schema = []

    derrors = []
    seen = False

        # Errors assosciated with a file


    def __init__(self, device_id, site_path):
       
        self.site_path = site_path
        self.device_id = device_id
        
        # load test results (validator results)
        self._load_test_results()
        #self._merge_results()
        self.seen = self.state.seen or self.event_pointset.seen
        self.errors = self.state.errors + self.event_pointset.errors

        # check if metadata exists and errors

        # register message types?


    # load all test items
    # merges all schema results into a single error type
    def _merge_results(self):
        print(self.device_id)
        for schema in self.registered_schema:
            print(schema)
            if getattr(self, schema).seen:
                self.errors += getattr(self, schema).errors



    def _load_test_results(self):
        self._register_schema('state')
        self._register_schema('event_pointset')

    def _register_schema(self, schema):
        setattr(self, schema, self._load_test_result(schema))
        self.registered_schema.append(schema)

    # load specific test item
    def _load_test_result(self, schema):
        return ValidationResult(self, schema)
