""" Module with helper methods for reading UDMI validation report
"""
from site_report import SiteReport
from jinja2 import Template

# function to read arguments and site dir


# main function to generate report

# load iot config 
# load validation report for details of run 
# LOAD report instance
# load template


test = SiteReport("/Users/nournew/downloads/KGX-17-05-22")
device_id = 'BMS-5'


"""print(test.devices)
print(test.devices[device_id])
print(test.devices[device_id].errors)
print(test.devices[device_id].state.seen)
print(test.devices[device_id].state.errors)
print(test.devices[device_id].event_pointset.seen)
print(test.devices[device_id].event_pointset.errors)

"""

with open('template.html') as f:
    template = Template(f.read())
output = template.render(test=test)

with open("report.html", "w") as f:
    f.write(output)