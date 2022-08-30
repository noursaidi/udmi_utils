""" Master clas for validation report  .. probably call it report
"""
from atexit import register
import json
import re
import os

from device import Device
from collections import Counter
from google.cloud import iot_v1
from google.protobuf import field_mask_pb2 as gp_field_mask

#from nmap_results_reader import NmapResultsReader
#from nmap_test_result import NmapTestResult


class SiteReport:
    
    devices = {}
    iot_config = {}
    
    validation_report = {} # to check points and also get some report data
    errors = None

    devices_seen = 0 
    devices_model = 0 # sum .. filter .. device.seen = True
    devices_clean = 0
    total_errors = 0

    def __init__(self, site_path):
    
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

        # read cloud_iot_config
        try:
            config_path = f"{os.path.normpath(site_path)}/cloud_iot_config.json"
            with open(config_path) as f:
                self.iot_config = json.load(f)
        except Exception as err:
            raise err

        # read validator summary
        try:
            report_path = f"{os.path.normpath(site_path)}/out/validation_report.json"
            with open(report_path) as f:
                self.validation_report = json.load(f)
        except Exception as err:
            raise err

        # initialise device by device ID -- it checks if metadata exists and if 
        for device_id in device_ids:
            self.devices[device_id] = Device(device_id, site_path)
        self.errors = self._read_errors()
        self.topErrors = self.errors.most_common(5)
        self._gen_statistics()

    def _read_errors(self):
        errors = Counter()
        # read all errors, store unique errors and counts in dictionary
        for device in self.devices.values():
            errors.update(device.state.errors)
            errors.update(device.event_pointset.errors)
        return errors

    def _gen_statistics(self):

        for device in self.devices.values():
            if device.seen:
                self.devices_seen += 1

            if len(device.errors) == 0 and device.seen:
                self.devices_clean += 1
            
            self.total_errors += len(device.errors)


    def sample_list_devices():
        field_mask = gp_field_mask.FieldMask(
            paths=[
                "id",
                "name",
                "num_id",
                "last_heartbeat_time",
                "last_event_time",
                "last_state_time",
                "last_config_ack_time",
                "last_config_send_time",
                "blocked",
                "last_error_time",
                "last_error_status",
                "gateway_config"
            ]
        )

        # Create a client
        client = iot_v1.DeviceManagerClient()
        registry_path = client.registry_path('daq1-273309', 'us-central1', 'registrar_test')
        # Initialize request argument(s)
        request = iot_v1.ListDevicesRequest(
            parent=registry_path,
        )

        # Make the request
        page_result = client.list_devices(request={"parent": registry_path, "field_mask": field_mask})

        # Handle the response
        for device in page_result:
            print(device)


