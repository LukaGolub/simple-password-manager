FIRST LABORATORY ASSIGNMENT: SYMMETRIC CRYPTOGRAPHY
1. PASSWORD PROTECTION MECHANISM

The system secures stored passwords using a combination of modern cryptographic algorithms:

a) PBKDF2:
The master password is not used directly as a key. Instead, the system utilizes PBKDF2 with a fixed salt to derive a 128-bit AES key. This protects the system against
brute-force attacks.

b) AES-EAX:
AES in EAX mode is used for encryption. EAX provides authenticated encryption, meaning that in addition to confidentiality (ensuring no one can see the password), the system also guarantees integrity (ensuring no one has tampered with the data). Each entry has its own unique 'nonce' and 'tag'.

c) SHA-256:
Service addresses (e.g., google.com) are stored as SHA-256 hashes with an appended secret string (salt). This prevents an attacker from discovering which services the user is using by simply inspecting the storage file.

2. SECURITY REQUIREMENTS

The system satisfies the following security requirements:

PASSWORD CONFIDENTIALITY: Passwords are encrypted using the AES algorithm. Without knowing the master password, the content remains unreadable. An attacker cannot determine if passwords for two different addresses are identical, cannot determine the password length, and cannot determine whether a password remained the same after an update.

ADDRESS CONFIDENTIALITY: An attacker cannot determine the service addresses because they are stored as SHA-256 hashes.

ANALYSIS RESISTANCE: Due to the use of a randomized nonce, saving the exact same password for two different services will result in completely different ciphertexts in the storage file.

3. STORAGE STRUCTURE

Data is stored in lab1passwords.txt using the following format:
[Address Hash] [Password Ciphertext] [Tag] [Nonce]

4. USAGE INSTRUCTIONS AND AUTOMATED TESTING

The master password is lab1mp.

The system supports the following commands:

get [Master password] [address] (Retrieve a password)

put [Master password] [address] [password] (Add/update a password in the database)

delete [Master password] (Reset/wipe the database)

exit (Exit the application)

For automated testing, navigate to the project directory and run automatic.sh using the command: ./automatic.sh.
