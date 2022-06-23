"""
Instance of device with both metadata and validation results
"""

class Device:

    device_id = ''
    site_path = ''

    metadata = None
    event_pointset = None
    state = None

    errors = []


    def __init__(self, site_path, device_id):
        # check if metadata exists
        self.site_path = site_path
        self.device_id = device_id
        # load test results

    def _load_test_results(self):
        # s
