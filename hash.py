import os
from Crypto.Hash import SHA3_256, SHA256, SHA512
import time

file_name_plaintext = os.path.expanduser("~/Desktop/testdata.txt")
with open(file_name_plaintext, mode='rb') as f:
    data1 = f.read()
    f.close()

small_file_name_plaintext = os.path.expanduser("~/Desktop/smallfile.txt")
with open(small_file_name_plaintext, mode='rb') as f:
    data_small = f.read()
    f.close()


print("######## Hashing 1MB file ########")
print ("\n ########### SHA256 ########")
start_time = int(round(time.time() * 1000000))
hash_object = SHA256.new(data=data1)
time_taken = round(time.time() * 1000000) - start_time
print("Time taken to hash using SHA256 in micro seconds: %s" % time_taken)
print("SHA256- speed per byte for 1MB: %s" % (time_taken/1000000))
print ("SHA256 Hash:")
print (hash_object.hexdigest())


print ("\n ########### SHA512 ########")
start_time = int(round(time.time() * 1000000))
hash_object = SHA512.new(data=data1)
time_taken = round(time.time() * 1000000) - start_time
print("Time taken to hash using SHA512 in micro seconds: %s" % time_taken)
print("SHA512- speed per byte for 1MB: %s" % (time_taken/1000000))
print ("SHA512 Hash:")
print (hash_object.hexdigest())

print ("\n ########### SHA3-256 ########")
start_time = int(round(time.time() * 1000000))
hash_object = SHA3_256.new(data=data1)
time_taken = round(time.time() * 1000000) - start_time
print("Time taken to hash using SHA3-256 in micro seconds: %s" % time_taken)
print("SHA3-256 speed per byte for 1MB: %s" % (time_taken/1000000))
print ("SHA3-256 Hash:")
print (hash_object.hexdigest())

print("######## Hashing 1KB file ########")
print ("\n ########### SHA256 ########")
start_time = int(round(time.time() * 1000000))
hash_object = SHA256.new(data=data_small)
time_taken = round(time.time() * 1000000) - start_time
print("Time taken to hash using SHA256 in micro seconds: %s" % time_taken)
print("SHA256- speed per byte for 1KB: %s" % (time_taken/1000))
print ("SHA256 Hash:")
print (hash_object.hexdigest())

print ("\n ########### SHA512 ########")
start_time = int(round(time.time() * 1000000))
hash_object = SHA512.new(data=data_small)
time_taken = round(time.time() * 1000000) - start_time
print("Time taken to hash using SHA512 in micro seconds: %s" % time_taken)
print("SHA512- speed per byte for 1KB: %s" % (time_taken/1000))
print (hash_object.hexdigest())

print ("\n ########### SHA3-256 ########")
start_time = int(round(time.time() * 1000000))
hash_object = SHA3_256.new(data=data_small)
time_taken = round(time.time() * 1000000) - start_time
print("Time taken to hash using SHA3-256 in micro seconds: %s" % time_taken)
print("SHA3-256- speed per byte for 1KB: %s" % (time_taken/1000))
print ("SHA3-256 Hash:")
print (hash_object.hexdigest())
