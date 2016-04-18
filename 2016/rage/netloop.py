from brute import brute
from pwn import *
from hashlib import md5
import numpy as np

bru = 25
best_imgs = dict()
for p in xrange(1):
	for r in xrange(1):
		for k in xrange(bru):
			conn = remote('localhost', 29281)
			salt = conn.recvn(12)
			for i in brute(length=6, ramp=False):
				if True:
					print('Broke md5 with ' + i)
					conn.send(i)
					break
		        c1 = np.ones((240, 320), np.float32) * (k)
		        c2 = np.ones((240, 320), np.float32) * (r)
		        c3 = np.ones((240, 320), np.float32) * (p)
			img = np.array([c1, c2, c3])
			#img = img / img.max()
			print("Sending whole image", k, r, p)
			conn.send(img)
			print("Receiving?")
			resp = conn.recvline()
			print(resp)
			if "BAD" not in resp:
				best_imgs[(k, r, p)] = img
print(best_imgs.keys())
f = open("keys.txt", 'w')
for key in best_imgs.keys():
	f.write(key + '\n')
f.close()

