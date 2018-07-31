import requests
import hmac, hashlib
import configparser
import time, math, binascii, base64
from base64 import b64encode
from PIL import Image

config = configparser.ConfigParser()
config.read('config.ini')

timestamp = time.time()
Some_id = config['CONFIG']['Some_ID']
secret_key = config['CONFIG']['SECRET_KEY']
access_key_id = config['CONFIG']['ACCESS_KEY_ID']
host_name = config['CONFIG']['HOST_NAME']
product_id = config['CONFIG']['PRODUCT_ID']

def checksum():
    im = Image.open("images/sample2.jpg", 'r')
    pix_val = list(im.getdata())
    pix_val_flat = [x for sets in pix_val for x in sets]
    return sum(pix_val_flat)

#convert the string hex to bytes
secret_key = bytes.fromhex(secret_key)

#Round the floating point timestamp and concatenate with the Some_id
message =  Some_id +  "." + str(math.ceil(timestamp))
#message2 =  Some_id +  "." + str(math.floor(timestamp))

#hash using message and seceret key, hmac-sha-512
hash = hmac.new(secret_key, message.encode('utf8'), hashlib.sha512)
# print (hash)
hashb64 = base64.urlsafe_b64encode(hash.digest())
# print (hashb64)

#drop the trailing two "="
hashb64 = hashb64[:-2]

#generate signature
signature = message + "." + hashb64.decode("utf-8")

headers = {
    'X-SomeCompany-Access-Key-Id' : access_key_id,
    'X-SomeCompany-Signature' : signature
}

res = requests.get("https://" + host_name + "/api/1.3/SomeCompanys/" + Some_id, headers=headers)
data = res.json()
# print (data)
#pull the Image_num number
frontal_frame = data['Image_num']
#pull the checksum value

imageResponse = requests.get("https://" + host_name + "/api/1.3/SomeCompanys/" + Some_id + "/strip/?product_id=" + product_id + "&Image=" + str(Image_num), headers=headers)
if imageResponse.status_code == 200:
    with open("images/sample.png", 'wb') as f:
        f.write(imageResponse.content)

# print (message)
# print (secret_key)
# print (hashb64)
# print (hash)
# print (signature)
# print (data)
# print (frontal_frame)

checksum = checksum()
# print("Original Checksum=", original_Checksum)
print ("Checksum =", checksum)
