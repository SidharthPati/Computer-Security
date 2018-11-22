# __author__ = 'spati'
import pyaes
import os
import filecmp
import time

# Recording start time for 128 bit key generation
start_time_key_128 = int(round(time.time() * 1000000))
key_128 = os.urandom(16)
# Printing the time taken for 128 bit key generation
print("Time taken to create 128 bit key in milliseconds: %s" % (int(round(time.time() * 1000000)) - start_time_key_128))

# Recording start time for 256 key generation
start_time_key_256 = int(round(time.time() * 1000000))
key_256 = os.urandom(32)
# Printing the time taken for 256 bit key generation
print("Time taken to create 256 bit key in milliseconds: %s" % (int(round(time.time() * 1000000)) - start_time_key_256))

# for encryption
aes128 = pyaes.AESModeOfOperationCTR(key_128)
aes256 = pyaes.AESModeOfOperationCTR(key_256)

# for decryption
aes_decrypt128 = pyaes.AESModeOfOperationCTR(key_128)
aes_decrypt256 = pyaes.AESModeOfOperationCTR(key_256)

# Files containing Plaintext of 1KB and 1MB each
small_file_name_plaintext = os.path.expanduser("~/Desktop/smallfile.txt")
file_name_plaintext = os.path.expanduser("~/Desktop/testdata.txt")

# Files containing Ciphertext of 1KB and 1MB each
small_file_name_ciphertext = os.path.expanduser("~/Desktop/smallciphertext.txt")
file_name_ciphertext = os.path.expanduser("~/Desktop/ciphertext.txt")

# Files containing Decrypted message of 1KB and 1MB each
small_file_name_decrypted_plaintext = os.path.expanduser("~/Desktop/smalldecryptedtext.txt")
file_name_decrypted_plaintext = os.path.expanduser("~/Desktop/decryptedtext.txt")


def encrypt(plaintext_file, aes_mode):
    with open(plaintext_file, mode='r') as f1:
        plaintext = f1.read()
        f1.close()
    ciphertext = aes_mode.encrypt(plaintext)
    return ciphertext


def decrypt(ciphertext_file, aes_mode):
    with open(ciphertext_file, mode='r') as f1:
        ciphertext1 = f1.read()
        f1.close()
    decrypted = aes_mode.decrypt(ciphertext1)
    return decrypted


# small file with 128 bit key
print "\n ############################ Encrypt and Decrypt 1kb file with 128 bit key ##########"
# Encryption time for 1KB file with 128 bit key
start_time_encryption = time.time()
returned_ciphertext = encrypt(small_file_name_plaintext, aes128)
print("Time taken to encrypt 1KB file using 128 bit key in seconds: %s" % (time.time() - start_time_encryption))
# Writing the ciphertext to file
with open(small_file_name_ciphertext, 'w') as f:
    f.write(returned_ciphertext)
    f.close()

# Decryption time for 1KB file with 128 bit key
start_time_decryption = time.time()
returned_decrypted = decrypt(small_file_name_ciphertext, aes_decrypt128)
print("Time taken to decrypt 1KB file using 128 bit key in seconds: %s" % (time.time() - start_time_decryption))
# Writing the decrypted message to file
with open(small_file_name_decrypted_plaintext, 'w') as f:
    f.write(returned_decrypted)
    f.close()

# check if both plaintext message and decrypted message are correct for 1KB file with 128 bit key
print "File comparison result: "
print filecmp.cmp(small_file_name_plaintext, small_file_name_decrypted_plaintext)


# small file with 256 bit key
print "\n ############################ Encrypt and Decrypt 1kb file with 256 bit key ##########"
# Encryption time for 1KB file with 256 bit key
start_time_encryption = time.time()
returned_ciphertext = encrypt(small_file_name_plaintext, aes256)
print("Time taken to encrypt 1KB file using 256 bit key in seconds: %s" % (time.time() - start_time_encryption))
# Writing the ciphertext to file
with open(small_file_name_ciphertext, 'w') as f:
    f.write(returned_ciphertext)
    f.close()

# Decryption time for 1KB file with 256 bit key
start_time_decryption = time.time()
returned_decrypted = decrypt(small_file_name_ciphertext, aes_decrypt256)
print("Time taken to decrypt 1KB file using 256 bit key in seconds: %s" % (time.time() - start_time_decryption))
# Writing the decrypted message to file
with open(small_file_name_decrypted_plaintext, 'w') as f:
    f.write(returned_decrypted)
    f.close()

# check if both plaintext message and decrypted message are correct for 1KB file with 256 bit key
print "File comparison result: "
print filecmp.cmp(small_file_name_plaintext, small_file_name_decrypted_plaintext)

# Large file with 128 bit key
print "\n ############################ Encrypt and Decrypt 1mb file with 128 bit key ##########"
# Encryption time for 1MB file with 128 bit key
start_time_encryption = time.time()
returned_ciphertext = encrypt(file_name_plaintext, aes128)
print("Time taken to encrypt 1MB file using 128 bit key in seconds: %s" % (time.time() - start_time_encryption))
# Writing the ciphertext to file
with open(file_name_ciphertext, 'w') as f:
    f.write(returned_ciphertext)
    f.close()

# Decryption time for 1MB file with 128 bit key
start_time_decryption = time.time()
returned_decrypted = decrypt(file_name_ciphertext, aes_decrypt128)
print("Time taken to decrypt 1MB file using 128 bit key in seconds: %s" % (time.time() - start_time_decryption))
# Writing the decrypted message to file
with open(file_name_decrypted_plaintext, 'w') as f:
    f.write(returned_decrypted)
    f.close()

# check if both plaintext message and decrypted message are correct for 1KB file with 128 bit key
print "File comparison result: "
print filecmp.cmp(file_name_plaintext, file_name_decrypted_plaintext)

# Large file with 256 bit key
print "\n ############################ Encrypt and Decrypt 1mb file with 256 bit key ##########"
# Encryption time for 1MB file with 256 bit key
start_time_encryption = time.time()
returned_ciphertext = encrypt(file_name_plaintext, aes256)
print("Time taken to encrypt 1MB file using 256 bit key in seconds: %s" % (time.time() - start_time_encryption))
# Writing the ciphertext to file
with open(file_name_ciphertext, 'w') as f:
    f.write(returned_ciphertext)
    f.close()

# Decryption time for 1MB file with 256 bit key
start_time_decryption = time.time()
returned_decrypted = decrypt(file_name_ciphertext, aes_decrypt256)
print("Time taken to decrypt 1MB file using 256 bit key in seconds: %s" % (time.time() - start_time_decryption))
# Writing the decrypted message to file
with open(file_name_decrypted_plaintext, 'w') as f:
    f.write(returned_decrypted)
    f.close()

# check if both plaintext message and decrypted message are correct for 1KB file with 256 bit key
print "File comparison result: "
print filecmp.cmp(file_name_plaintext, file_name_decrypted_plaintext)
