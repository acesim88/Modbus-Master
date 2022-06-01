from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import sendmail

client=ModbusClient(method='rtu',port='/dev/ttyUSB0',stopbits=1,bytesize=8,parity='N',baudrate=9600,timeout=0.3)
connection=client.connect()

while True:	

	value=client.read_input_registers(0,1,unit=0x01)
	print(value.registers)	
	print(sendmail.send_an_email("Value:"+str(value.registers)))
	time.sleep(60)