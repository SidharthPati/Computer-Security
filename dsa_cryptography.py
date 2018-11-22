# __author__ = 'spati'
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
import os
import time

# Recording start time for  key generation
start_time_private_key = int(round(time.time() * 1000000))
private_key = dsa.generate_private_key(
    key_size=2048,
    backend=default_backend()
)
# Printing the time taken for key generation
print("Time taken to 2048 create private key in micro seconds: %s" %
      (int(round(time.time() * 1000000)) - start_time_private_key))

# Recording start time for 3072 bit key generation
start_time_private_key_3072 = int(round(time.time() * 1000000))
private_key_3072 = dsa.generate_private_key(
    key_size=3072,
    backend=default_backend()
)
# Printing the time taken for key generation
print("Time taken to create 3072 private key in micro seconds: %s" %
      (int(round(time.time() * 1000000)) - start_time_private_key_3072))

# Generate Signature for 1 MB file
print ("######################## Signature generation for 1MB file 2048 key ##########################################")
file_name_plaintext = os.path.expanduser("~/Desktop/testdata.txt")
with open(file_name_plaintext, mode='r') as f:
    data = f.read()
    f.close()

# Start time for signature
start_time_signature = int(round(time.time() * 1000000))
signature = private_key.sign(
    data,
    hashes.SHA256()
)
# Printing the time taken for signature
time_taken = int(round(time.time() * 1000000)) - start_time_signature
print("Time taken to sign in micro seconds: %s" % time_taken)
file_size = 1000000
sign_per_byte_time = round((time_taken/file_size), 9)
print("Signature generation per byte time: %s" % sign_per_byte_time)

# Signature verification
start_time_verification = int(round(time.time() * 1000000))
public_key = private_key.public_key()
try:
    public_key.verify(signature, data, hashes.SHA256())
except Exception:
    print ("Verification failed")
    exit()
print ("Verification successful")
# Printing the time taken for signature
time_taken = int(round(time.time() * 1000000)) - start_time_verification
print("Time taken to verify in micro seconds: %s" % time_taken)

# Generate Signature for 1 KB file
print ("######################## Signature generation for 1KB file 2048 bit key ##########################################")
small_file_name_plaintext = os.path.expanduser("~/Desktop/smallfile.txt")
with open(small_file_name_plaintext, mode='r') as f:
    data = f.read()
    f.close()

# Start time for signature
start_time_signature = int(round(time.time() * 1000000))
signature = private_key.sign(
    data,
    hashes.SHA256()
)
# Printing the time taken for signature
time_taken = int(round(time.time() * 1000000)) - start_time_verification
print("Time taken to sign in micro seconds: %s" % time_taken)
file_size = 1000
sign_per_byte_time = round((time_taken/file_size), 9)
print ("Signature generation per byte time: %s" % sign_per_byte_time)

# Signature verification
start_time_verification = int(round(time.time() * 1000000))
public_key = private_key.public_key()
try:
    public_key.verify(signature, data, hashes.SHA256())
except Exception:
    print ("Verification failed")
    exit()
print ("Verification successful")
# Printing the time taken for signature
time_taken = int(round(time.time() * 1000000)) - start_time_verification
print("Time taken to verify in micro seconds: %s" % time_taken)

# Generate Signature for 1 MB file using 3072 bit key
print ("######################## Signature generation for 1MB file 3072 bit key ######################################")
file_name_plaintext = os.path.expanduser("~/Desktop/testdata.txt")
with open(file_name_plaintext, mode='r') as f:
    data = f.read()
    f.close()

# Start time for signature
start_time_signature = int(round(time.time() * 1000000))
signature = private_key.sign(
    data,
    hashes.SHA256()
)
# Printing the time taken for signature
time_taken = int(round(time.time() * 1000000)) - start_time_signature
print("Time taken to sign in micro seconds: %s" % time_taken)
file_size = 1000000
sign_per_byte_time = round((time_taken/file_size), 9)
print("Signature generation per byte time: %s" % sign_per_byte_time)

# Signature verification
start_time_verification = int(round(time.time() * 1000000))
public_key = private_key.public_key()
try:
    public_key.verify(signature, data, hashes.SHA256())
except Exception:
    print ("Verification failed")
    exit()
print ("Verification successful")
# Printing the time taken for signature verification
time_taken = int(round(time.time() * 1000000)) - start_time_verification
print("Time taken to verify in micro seconds: %s" % time_taken)

# Generate Signature for 1 KB file using 3072 bit key
print ("######################## Signature generation for 1KB file 3072 bit key ######################################")
file_name_plaintext = os.path.expanduser("~/Desktop/smallfile.txt")
with open(file_name_plaintext, mode='r') as f:
    data = f.read()
    f.close()

# Start time for signature
start_time_signature = int(round(time.time() * 1000000))
signature = private_key.sign(
    data,
    hashes.SHA256()
)
# Printing the time taken for signature
time_taken = int(round(time.time() * 1000000)) - start_time_signature
print("Time taken to sign in micro seconds: %s" % time_taken)
file_size = 1000
sign_per_byte_time = round((time_taken/file_size), 9)
print("Signature generation per byte time: %s" % sign_per_byte_time)

# Signature verification
start_time_verification = int(round(time.time() * 1000000))
public_key = private_key.public_key()
try:
    public_key.verify(signature, data, hashes.SHA256())
except Exception:
    print ("Verification failed")
    exit()
print ("Verification successful")
# Printing the time taken for signature verification
time_taken = int(round(time.time() * 1000000)) - start_time_verification
print("Time taken to verify in micro seconds: %s" % time_taken)
