""" Module with helper methods for reading UDMI validation report
"""
from site_report import SiteReport
from jinja2 import Template
import plotly.express as px
import pandas as pd
import argparse
import dateutil.parser

# function to read arguments and site dir


# main function to generate report

# load iot config 
# load validation report for details of run 
# LOAD report instance
# load template

def parse_command_line_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('site_path', type=str,
                        help='path to site model')

    parser.add_argument('output_file', type=str,
                        help='file to save results in ')

    return parser.parse_args()


def timedelta(site_result):
    timestamps = []
    device_labels = []
    for device in site_result.devices.values():
        # TODO there's got to be a better way of doing this ...

        try:
            if device.state.timestamp:
                timestamps.append(device.state.timestamp)
                device_labels.append(device.device_id)
        except:
            pass

        try:
            if device.event_pointset.timestamp:
                timestamps.append(device.event_pointset.timestamp)
                device_labels.append(device.device_id)
        except:
            pass

    print(max(timestamps))
    min_ts = min(timestamps)
    td =  [(ts - min_ts).total_seconds() for ts in timestamps]
    
    df = pd.DataFrame({'ts': timestamps, 'device_id': device_labels})
    fig = px.scatter(df, hover_data=['device_id'])

    #fig.add_hline(y=dateutil.parser.parse("Wed 6 Jul 2022 15:16:25"))
    #fig.add_hline(y=dateutil.parser.parse("Wed 6 Jul 2022 15:22:25"))

    fig.show()


def write_report(site_result, output_file):
    with open('template.html') as f:
        template = Template(f.read())
    output = template.render(test=site_result)

    with open(output_file, "w") as f:
        f.write(output)

def main():
    args = parse_command_line_args()
    site_path = args.site_path
    output_file = args.output_file
    
    test = SiteReport(site_path)

    write_report(test, output_file)
    #timedelta(test)


if __name__ == "__main__":
    main()
