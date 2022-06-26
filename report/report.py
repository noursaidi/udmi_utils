""" Module with helper methods for reading UDMI validation report
"""
from validation_report import ValidationReport
from jinja2 import Template

# function to read arguments and site dir


# main function to generate report

# load iot config 
# load validation report for details of run 
# LOAD report instance
# load template


test = ValidationReport("/Users/nournew/udmi_site_model")
device_id = 'AHU-1'

"""
rint(test.devices)
print(test.devices[device_id])
print(test.devices[device_id].errors)
print(test.devices[device_id].state.seen)
print(test.devices[device_id].state.errors)
print(test.devices[device_id].event_pointset.seen)
print(test.devices[device_id].event_pointset.errors)"""

with open('template.html') as f:
    template = Template(f.read())
output = template.render(test=test)

with open("report.html", "w") as f:
    f.write(output)