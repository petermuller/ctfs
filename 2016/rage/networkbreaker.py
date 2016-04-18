from brute import brute
from pwn import *
from hashlib import md5
import numpy as np
from scipy.ndimage import imread

conn = remote('localhost', 29281)  # server connection
#conn = remote('40.117.46.42', 29281)  # ctf server connection
salt = conn.recvn(12)  # get part of string from server
for i in brute(length=6, ramp=False):  # generated second part of string
	if md5(salt+i).digest().startswith('\x00\x00\x00'):  # get 3 nulls at beginning of hash
		print('Broke md5 with ' + i)
		conn.send(i)  # send second part of string
		break  # and stop the brute forcing
img = imread("plaid/wallpaper_20090122104623_19095694832.jpg").astype(np.float32)  # plaid image via google image search
img = img.transpose((2, 0, 1))  # Keras accepts (CxWxH) images, not the standard (WxHxC)
img = img.copy(order='C')  # get data into contiguous, C-styled data block
print("Sending whole image")
conn.send(img)  # send image to server. it is already in format to send RGB channels in that order
print("Receiving key?")
print(conn.recvline())  # get the key!
