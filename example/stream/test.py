import usb.core, usb.util
import time

dev = usb.core.find(idVendor=0x9999, idProduct=0xffff)

d1 = range(1, 64*2+1)
print len(d1)

d1[55] = 0
d1[-2] = 0

for i in range(100):
	dev.write(0x02, d1, 0, 100)
	for i in range(3):
		start = time.time()
		d = dev.read(0x81, 64, 0, 100)
		end = time.time()
		print list(d), end-start
