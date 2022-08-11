# udmi_utils

3rd party utilities for UDMI.

## Install Instructions
1. Install [gcloud sdk](https://cloud.google.com/sdk/docs/install)
2. Authenticate [application default credentials](https://cloud.google.com/sdk/gcloud/reference/auth/application-default)
3. Install dependancies `pip3 -i requirements.txt`


## Report
**NOTE** You must be using an older version of the UDMI tools. Do this by running:
`git checkout 5cdec4ec9ab855cc61cf125f46a4371abcd51831` before running the validator

Outputs HTML file which can be viewed in the browser.

`python3 report/generate.py <FULL PATH TO SITE MODEL> <OUTPUT FILE PATH>` 
e.g. `python3 report/generate.py /home/ubuntu/site_model /home/ubuntu/report.html`


