import time, json

class IEnvironmentalControl:
    name = 'undefined'
    checkSeconds = -1
    
    def __init__(self, name, checkSeconds):
        self.name = name
        self.checkSeconds = checkSeconds
        
    def CheckCondition(self) -> bool:
        pass
    
    def ActionControl(self):
        pass


def loadEnvironmentalControls():    
    controls = []
    with open('config.json', 'r') as reader:
        config = json.load(reader)
        
        for envControl in config['controls']:
            name = envControl['name']
            checkSeconds = envControl['checkSeconds']
            controls.append(IEnvironmentalControl(name, checkSeconds))
            
    return controls
            

WAIT_SECONDS = 1 

controls = loadEnvironmentalControls()
while True:
 
     for c in controls:
        if c.CheckCondition():
            print('Executing control: {c.name}')
            c.ActionControl()
    
    time.sleep(WAIT_SECONDS)