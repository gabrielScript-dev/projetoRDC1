import network
import time
import gc

gc.collect()

ssid = 'MADMAN_iDnet985635188'
password = 'qwe122448'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while wifi.isconnected() == False:
    print('CONECTANDO...')
    time.sleep(0.2)
    
print('\n--CONEXÃO BEM-SUCEDIDA!-\n')
print('CONECTANDO EM: \nSSID: {}\nIP: {}\n\n'.format(ssid, wifi.ifconfig()[0]))