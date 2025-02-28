import utime
import random
from picozero import pico_led
import network
import utime
import urequests
import machine

SSID = "YOUR NETWORK NAME"
PASSWORD = "YOUR NETWORK PASSWORD"
THINGSPEAK_API_WRITE = "YOUR API KEY"

wlan = network.WLAN(network.STA_IF)
adc = machine.ADC(4) 

def upload_to_thingspeak(api_key, value):
    if not wlan.isconnected():
        print("Wi-Fi lost! Reconnecting...")
        connect_wifi()

    try:
        url = f"https://api.thingspeak.com/update?api_key={api_key}&field2={value}"
        response = urequests.get(url)
        print(f"Data sent: {value}. Response: {response.text}")
        response.close()
    except Exception as e:
        print("Error sending data:", e)
        utime.sleep(10)
        upload_to_thingspeak(api_key, value)
        
        
        
def read_temperature():
    adc_value = adc.read_u16()
    volt = (3.3/65535) * adc_value
    temperature = 27 - (volt - 0.706)/0.001721
    return temperature



def connect_wifi(ssid, password):
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.active(True)
        wlan.connect(ssid, password)

        if wlan.isconnected():
            print("Connected to Wi-Fi:", wlan.ifconfig())
        else:
            print("Failed to connect. Retrying...")
            utime.sleep(1)
            connect_wifi(ssid, password)
    else:
        print("Connected to Wi-Fi:", wlan.ifconfig())
        
        

connect_wifi(SSID, PASSWORD)

while True:
    pico_led.on()
    sensor_value = read_temperature() 
    upload_to_thingspeak(THINGSPEAK_API_WRITE, sensor_value)
    
    utime.sleep(5)
    pico_led.off()
    utime.sleep(175)