import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "s65wg1",
        "typeId": "new",
        "deviceId":"100"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    print(type(cmd.data['command']))
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    Temp=random.randint(20,125)
    Hum=random.randint(25,100)
    ship=random.randint(3,27)
    gt=random.randint(289,8379)
    gt_rat=random.randint(1364,3560)
    gg_rate=random.randint(92,644)
    sp_trq=random.randint(7,644)
    pp_trq=random.randint(7,644)
    hpt_temp=random.randint(635,1114)
    gt_c_o_temp=random.randint(559,788)
    hpt_prs=random.randint(1,4)
    
    
    
    
    
    
    myData={'Temperature':Temp, 'Humidity':Hum, 'Ship_speed':ship, 'Gt_shaft':gt, 'Gt_rate':gt_rat, 'Gg_rate':gg_rate, 'Sp_torque':sp_trq, 'Pp_torque':pp_trq, 'Hpt_temp':hpt_temp, 'Gt_c_o_temp':gt_c_o_temp,'Hpt_pressure':hpt_prs}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
