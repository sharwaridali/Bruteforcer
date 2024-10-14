import zipfile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        # Attempt to extract with the given password
        zf_handle.extractall(pwd=password)
        print(f"[+] Password found: {password.decode('utf-8')}")
        print("Extraction successful!")
    except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile) as e:
        # Handle incorrect password or bad zip file
        print(f"Failed to extract: {str(e)}")
def main():
    print("[+] Beginning bruteforce...")
    with zipfile.ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()  # Remove any surrounding whitespace or newlines
                if attempt_extract(zf, password):
                    break  # Stop if the correct password is found
            else:
                print("[+] Password not found in the list.")

if __name__ == "__main__":
    main()

