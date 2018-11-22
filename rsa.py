# __author__ = 'spati'
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
from Crypto import Random
import time


def encryption_RSA(plaintext, publickey):
    encryptor = PKCS1_OAEP.new(publickey)
    encrypted = encryptor.encrypt(plaintext)
    return encrypted


def decryption_RSA(ciphertext, p_key):
    decryptor = PKCS1_OAEP.new(p_key)
    decrypted = decryptor.decrypt(ciphertext)
    return decrypted


file_name_plaintext = os.path.expanduser("~/Desktop/testdata.txt")
small_file_name_plaintext = os.path.expanduser("~/Desktop/smallfile.txt")
rsa_encrypted_file = os.path.expanduser("~/Desktop/rsa_encrypted.txt")
rsa_decrypted_file = os.path.expanduser("~/Desktop/rsa_decrypted.txt")

random_generator = Random.new().read
start_time_2048 = int(round(time.time() * 1000))
key_2048 = RSA.generate(2048, random_generator)
print("Time taken to create 2048 bit key in milli seconds: %s" % (int(round(time.time() * 1000)) - start_time_2048))
publickey_2048 = key_2048.publickey()

random_generator = Random.new().read
start_time_2048 = int(round(time.time() * 1000))
key_3072 = RSA.generate(3072, random_generator)
print("Time taken to create 3072 bit key in milli seconds: %s" % (int(round(time.time() * 1000)) - start_time_2048))
publickey_3072 = key_3072.publickey()

print ("\n ############ Encrypt and Decrypt 1MB file with 2048 bit key #######")
file_plaintext = open(file_name_plaintext, 'rb')
encrypted_file = open(rsa_encrypted_file, 'wb')
decrypted_file = open(rsa_decrypted_file, 'wb')

encrypt_time = 0
while True:
    data = file_plaintext.read(214)
    if not data:
        break
    start_time_2048 = int(round(time.time() * 1000))
    enc_data = encryption_RSA(data, publickey_2048)
    final_time = int(round(time.time() * 1000)) - start_time_2048
    encrypt_time = encrypt_time + final_time
    encrypted_file.write(enc_data)
print("Time taken to encrypt using 2048 bit key in milli seconds: %s" % encrypt_time)
file_plaintext.close()
encrypted_file.close()

file_encrypted = open(rsa_encrypted_file, 'rb')
decrypted_file1 = open(rsa_decrypted_file, 'wb')
start_time_2048 = int(round(time.time() * 1000))
while True:
    data = file_encrypted.read(256)
    if not data:
        break
    dec_data = decryption_RSA(data, key_2048)
    time1 = (int(round(time.time() * 1000)) - start_time_2048)
    decrypted_file1.write(dec_data)
print("Time taken to decrypt using 2048 bit key in milli seconds: %s" % time1)
decrypted_file1.close()
file_encrypted.close()

print ("\n ############ Encrypt and Decrypt 1MB file with 3072 bit key #######")
file_plaintext = open(file_name_plaintext, 'rb')
encrypted_file = open(rsa_encrypted_file, 'wb')
decrypted_file = open(rsa_decrypted_file, 'wb')

start_time_3072 = int(round(time.time() * 1000))
while True:
    data = file_plaintext.read(342)
    if not data:
        break
    enc_data = encryption_RSA(data, publickey_3072)
    encrypted_file.write(enc_data)
print("Time taken to encrypt using 3072 bit key in milli seconds: %s" %(int(round(time.time() * 1000)) - start_time_3072))
file_plaintext.close()
encrypted_file.close()

file_encrypted = open(rsa_encrypted_file, 'rb')
decrypted_file1 = open(rsa_decrypted_file, 'wb')
start_time_3072 = int(round(time.time() * 1000))
while True:
    data = file_encrypted.read(384)
    if not data:
        break
    dec_data = decryption_RSA(data, key_3072)
    decrypted_file1.write(dec_data)
print("Time taken to decrypt using 3072 bit key in milli seconds: %s" % (int(round(time.time() * 1000)) - start_time_3072))
decrypted_file1.close()
file_encrypted.close()

print ("\n ############ Encrypt and Decrypt 1KB file with 2048 bit key #######")
file_plaintext = open(small_file_name_plaintext, 'rb')
encrypted_file = open(rsa_encrypted_file, 'wb')
decrypted_file = open(rsa_decrypted_file, 'wb')

start_time_2048 = int(round(time.time() * 1000))
while True:
    data = file_plaintext.read(214)
    if not data:
        break
    enc_data = encryption_RSA(data, publickey_2048)
    encrypted_file.write(enc_data)
print("Time taken to encrypt using 2048 bit key in milli seconds: %s" %(int(round(time.time() * 1000)) - start_time_3072))
file_plaintext.close()
encrypted_file.close()

file_encrypted = open(rsa_encrypted_file, 'rb')
decrypted_file1 = open(rsa_decrypted_file, 'wb')
start_time_3072 = int(round(time.time() * 1000))
while True:
    data = file_encrypted.read(256)
    if not data:
        break
    dec_data = decryption_RSA(data, key_2048)
    decrypted_file1.write(dec_data)
print("Time taken to decrypt using 3072 bit key in milli seconds: %s" % (int(round(time.time() * 1000)) - start_time_3072))
decrypted_file1.close()
file_encrypted.close()

print ("\n ############ Encrypt and Decrypt 1MB file with 3072 bit key #######")
file_plaintext = open(small_file_name_plaintext, 'rb')
encrypted_file = open(rsa_encrypted_file, 'wb')
decrypted_file = open(rsa_decrypted_file, 'wb')

start_time_3072 = int(round(time.time() * 1000))
while True:
    data = file_plaintext.read(342)
    if not data:
        break
    enc_data = encryption_RSA(data, publickey_3072)
    encrypted_file.write(enc_data)
print("Time taken to encrypt using 3072 bit key in milli seconds: %s" %(int(round(time.time() * 1000)) - start_time_3072))
file_plaintext.close()
encrypted_file.close()

file_encrypted = open(rsa_encrypted_file, 'rb')
decrypted_file1 = open(rsa_decrypted_file, 'wb')
start_time_3072 = int(round(time.time() * 1000))
while True:
    data = file_encrypted.read(384)
    if not data:
        break
    dec_data = decryption_RSA(data, key_3072)
    decrypted_file1.write(dec_data)
print("Time taken to decrypt using 3072 bit key in milli seconds: %s" % (int(round(time.time() * 1000)) - start_time_3072))
decrypted_file1.close()
file_encrypted.close()
