""" Module with helper methods for reading UDMI validation report
"""
import json
import re

from nmap_results_reader import NmapResultsReader
from nmap_test_result import NmapTestResult


class validationReport:
    
    devices = []
    cloud_config = {}

    def __init__(self, site_path):
       
        # read cloud_iot_config

        # list devices in site model

        # list devices in validator out

        # merge lists

        # initialise device by device ID -- it checks if metadata exists and if 

    def _read_errors(self):
        # read all errors, store unique errors and counts in dictionary