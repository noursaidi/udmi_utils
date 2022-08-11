# udmi_utils

3rd party utilities for UDMI.

## Install Instructions
1. Install [gcloud sdk](https://cloud.google.com/sdk/docs/install)
2. Authenticate [application default credentials](https://cloud.google.com/sdk/gcloud/reference/auth/application-default)
3. Install dependancies `pip3 -i requirements.txt`


## Report
Outputs HTML file which can be viewed in the browser.

`python3 report/generate.py <FULL PATH TO SITE MODEL> <OUTPUT FILE PATH>` 
e.g. `python3 report/generate.py /home/ubuntu/site_model /home/ubuntu/report.html`


