import pprint
from circleclient import circleclient
import json

print('loading')

def loadConfig():
    json_data = open('config.json').read()
    return json.loads(json_data)

def triggerBuild():
    config = loadConfig()
    client = circleclient.CircleClient(config['circle_token'])
    client.build.trigger(config['circle_user'], config['repo'], config['branch'])

def lambda_handler(event, context):
    print('running')
    #pprint.pprint(event)
    #triggerBuild()
    return event