//smoke sensor with raspberry pi 
import time 
import botbook_mcp3002 as mcp  
 
smokeLevel= 0 
 
def readSmokeLevel(): 
global smokeLevel 
smokeLevel= mcp.readAnalog() 
 
def main(): 
    while True:  
        readSmokeLevel()   
        if smokeLevel > 120: 
        print("Smoke detected") 
        print(" Smoke value: ",smokeLevel) 
        time.sleep(0.5) 
 
if__name__=="__main__": 
  main()
