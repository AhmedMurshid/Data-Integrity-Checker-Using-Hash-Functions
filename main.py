# CSE CSE 564 Cryptography
import hashlib

def calculate_hash(input_data, algorithm='sha256'):
    """Calculate the hash of input data using the specified algorithm."""
    hash_function = getattr(hashlib, algorithm)()
    hash_function.update(input_data.encode('utf-8'))
    return hash_function.hexdigest()

def main():
    print("Welcome to the Hash Data Integrity Checker App!")
    while True:
        print("\nMenu:")
        print("1. Calculate hash for text input")
        print("2. Verify integrity of data")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter the text to calculate hash for: ")
            algorithm = input("Choose the algorithm (sha256/md5/sha1): ")
            hash_value = calculate_hash(text, algorithm)
            print(f"{algorithm.upper()}: {hash_value}")

        elif choice == '2':
            stored_hash = input("Enter the stored hash value: ")
            input_data = input("Enter the data to verify: ")
            algorithm = input("Choose the algorithm (sha256/md5/sha1): ")
            calculated_hash = calculate_hash(input_data, algorithm)
            if stored_hash == calculated_hash:
                print("Integrity verified: Data is not tampered.")
            else:
                print("Data integrity check failed: Data may be tampered!")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
