import hashlib
import os

def generate_hash(text, algorithm='sha256'):
    """Generate a hash for the given text using the specified algorithm."""
    hash_function = getattr(hashlib, algorithm)()
    hash_function.update(text.encode('utf-8'))
    return hash_function.hexdigest()

def hash_file(file_path, algorithm='sha256'):
    """Generate a hash for the content of the specified file using the specified algorithm."""
    hash_function = getattr(hashlib, algorithm)()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_function.update(chunk)
    return hash_function.hexdigest()

# use examples 
# ----
# sha256_hash = generate_hash("Ahmed Abdullahi", algorithm='sha256')
# md5_hash = generate_hash("Ahmed Abdullahi", algorithm='md5')
# sha1_hash = generate_hash("Ahmed Abdullahi", algorithm='sha1')
# ---- 
# sha256_hash = hash_file("test.txt", algorithm='sha256')
# md5_hash = hash_file("test.txt", algorithm='md5')
# sha1_hash = hash_file("test.txt", algorithm='sha1')


