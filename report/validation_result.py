"""
Instance of a validation result of given message type e.g. state
"""

class ValidationResult:
    
    seen = False
    errors = []
    
    def __init__(self, device, type):
        # load json file .. if exists seen = true
        # load out file .. if errors exist, read errors into errors list as error
        # read line by line appending strings .. IF line is a tab its conntunuation, if a word then it's a new error
        self.device = device

    def _read_errors(self, file_path)
    # read line by line appending strings .. IF line is a tab its conntunuation, if a word then it's a new error