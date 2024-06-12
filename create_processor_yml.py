#!/bin/env python3

import yaml
import os

deminput_jobid = os.environ['param_input_path']
input_path = f'/compute_scratch/{deminput_jobid}'

processor_dict = {'$1': {'DEMMerge': {'input_path':input_path,'site_id':os.environ['param_site_id'],'merged_filename':os.environ['param_merged_filename']}}}

with open('/job/executable/demmerge.yml','w') as demfile:
    yaml.dump(processor_dict,demfile)
