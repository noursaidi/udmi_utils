""" Module with helper methods for reading UDMI validation report
"""
import json
import re
import os

from device import Device

from collections import Counter

#from nmap_results_reader import NmapResultsReader
#from nmap_test_result import NmapTestResult


class ValidationReport:
    
    devices = {}
    cloud_config = {}
    errors = None
    devices_seen = 0 
    devices_model = 0 # sum .. filter .. device.seen = True

    def __init__(self, site_path):
       
        # read cloud_iot_config

        # list devices in site model
        try:
            model_devices_dir = os.path.join(site_path, 'devices')
            model_devices = [os.path.basename(f.path) for f in os.scandir(model_devices_dir) 
                if f.is_dir()]
        except Exception:
            model_devices = []

        # list devices in validator out
        try:
            validated_devices_dir = os.path.join(site_path, 'out/devices')
            validated_devices = [os.path.basename(f.path) for f in os.scandir(validated_devices_dir) 
                if f.is_dir()]  
        except Exception:
            validated_devices = []
        # merge lists
        device_ids = set(validated_devices + model_devices)

        # initialise device by device ID -- it checks if metadata exists and if 
        for device_id in device_ids:
            self.devices[device_id] = Device(device_id, site_path)

        self.errors = self._read_errors()
        self.topErrors = self.errors.most_common(5)

    def _read_errors(self):
        errors = Counter()
        # read all errors, store unique errors and counts in dictionary
        for device in self.devices.values():
            errors.update(device.state.errors)
            errors.update(device.event_pointset.errors)
        return errors
