"""
Instance of a validation result of given message type e.g. state
"""

import os
import re
from error import Error
import json
import datetime
import dateutil.parser

class ValidationResult:
    
    seen = False
    timestamp = None
    errors = []
    
    def __init__(self, device, schema):
        # load json file .. if exists seen = true
        
        # load out file .. if errors exist, read errors into errors list as error
        # read line by line appending strings .. IF line is a tab its conntunuation, if a word then it's a new error
        self.device = device

        device_folder_path = f"{os.path.normpath(device.site_path)}/out/devices/{device.device_id}"
        message_path = f"{device_folder_path}/{schema}.json"
        error_path = f"{device_folder_path}/{schema}.out"

        if os.path.isfile(message_path):
            self.seen = True

            try:
                with open(message_path) as f:
                    payload = json.load(f)
                    self.timestamp = dateutil.parser.parse(payload['timestamp'])
            except Exception as e:
                exit(e)

        self.errors = self._read_errors(schema, error_path)
 
    def _read_errors(self, schema, file_path):
    # read line by line appending strings .. IF line is a tab its conntunuation, if a word then it's a new error
        errors = []
        error_str = ''

        try:
            with open(file_path) as f:
                # read first line into error str and then loop
                errors = self._coalesce_errors(f.readlines())
        except FileNotFoundError:
            pass
        
        return errors

    def _coalesce_errors(self, errors):
        # Coalesce errors 
        # given an errors list 
        # any line not
        # append to error_str except if not start with white space in which cas
        # append error_Str to errors and reset error_str

        new_list = []
        for line in errors:
            if re.search(r"^\w", line):
                new_list.append(line)
                continue
            new_list[len(new_list) - 1] += line
        
        return new_list
            