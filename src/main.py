import time, json
from pumpControl import pumpControl
from temperatureControl import temperatureControl 

def loadEnvironmentalControls():    
    controls = []
    with open('config.json', 'r') as reader:
        config = json.load(reader)
 
        for envSetting in config['controls']:
            name = envSetting['name']
            if 'pump' in name:
                controls.append(pumpControl)
            if 'temperature' in name:
                controls.append(temperatureControl)
            
    return controls
            

controls = loadEnvironmentalControls()  

WAIT_SECONDS = 1 
while True:
         
    for c in controls:
        if c.Check():
            print(f'Executing control: {c.Name}')
            c.Action()
            
    time.sleep(WAIT_SECONDS)