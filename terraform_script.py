#!/usr/bin/python

import requests
import pprint
from optparse import OptionParser
import subprocess
from subprocess import PIPE

parser = OptionParser()

parser.add_option("-f", "--filepath", dest="filepath", help="path to request.json")
parser.add_option("-t", "--terraform_endpoint", dest="terraform_endpoint", help="endpoint of terraform API")
parser.add_option("-c", "--control_endpoint", dest="control_endpoint", help="endpoint of control API")
parser.add_option("-a", "--action", dest="action", help="action to be performed: create_stack, list_stack,delete_stack, power_on, power_off, reboot")
parser.add_option("-s", "--stackid", dest="stackid", help="stackId for specific operation")
parser.add_option("-n", "--stackname", dest="stackname", help="stackName for specific operation")
parser.add_option("-v", "--vmid", dest="vmid", help="vmid for specific operation")

(options, args) = parser.parse_args()

filepath = options.filepath
tf_end = options.terraform_endpoint
ctrl_end = options.control_endpoint
action = options.action
stackid = options.stackid
vmid = options.vmid
stackname = options.stackname


#Extract filename
if filepath != None:
  filepath_split = filepath.split('/')
  filepath_length = len(filepath_split)
  filename = filepath_split[filepath_length-1]
  print filename
  print filepath

print tf_end


def create_stack():
 # files = { 'file': (filename, open(filepath, 'rb'), 'application/json')}
 # response = requests.post(tf_end+'/tenantId/stacks', files=files)
 # print response.content
  
  
  cmd = "curl -X POST " + tf_end + "/tenantId/stacks -d @" + filepath
  print cmd
  p = subprocess.Popen([cmd], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
  (out, err) = p.communicate()
  print out

def list_stack():
  response = requests.get(tf_end+'/tenantId/stacks')
  print response.content

def delete_stack():
  cmd = "curl -X DELETE " + tf_end + "/tenantId/stacks/" + stackname + "/" + stackid
  print cmd
  p = subprocess.Popen([cmd], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
  (out, err) = p.communicate()
  print out

def control_stack():
  print stackid
  print vmid
  print stackname
  cmd = "curl -X PATCH " + tf_end + "/tenantId/stacks/" + stackname + "/" + stackid + "/vms/" + vmid + " -d @" + filepath
  print cmd
  p = subprocess.Popen([cmd], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
  (out, err) = p.communicate()
  print out

if action == 'create_stack':
    create_stack()
elif action == 'delete_stack':
    delete_stack()
elif action == 'list_stack':
    list_stack()
elif action == 'control_stack':
    control_stack()
else:
    print('Undefined Action given')
