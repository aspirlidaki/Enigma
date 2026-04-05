def caesar_encrypt(text, shift):
    """Encrypts a string using the Caesar cipher."""
    result = ""
    
    # Go through each character in the message one by one
    for char in text:
        # Check if the character is a letter (ignore spaces, numbers, !? etc.)
        if char.isalpha():
            # Figure out if it is an uppercase or lowercase letter
            start = ord('A') if char.isupper() else ord('a')
            
            # 1. Convert the letter to a number (0-25)
            # 2. Add the shift key
            # 3. Use modulo (%) 26 to wrap around (so 'Z' shifted by 1 becomes 'A')
            # 4. Convert back to a letter
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # If it's a space or punctuation, leave it exactly as is
            result += char
            
    return result


def main():
    print("Welcome to Enigma: The Cipher Toolkit! 🔐")
    
    # The 'while True' loop keeps the menu running forever, 
    # until the user explicitly chooses to exit.
    while True:
        print("\n--- Main Menu ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute-force a Caesar Cipher")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("Choose an option (1-4): ")
        
        # Handle the user's choice using if/elif statements
        if choice == '1':
            print("\n--- Encryption ---")
            message = input("Enter the message you want to encrypt: ")
            
            # We use int() to convert the user's typed input into a math number
            try:
                key = int(input("Enter your shift key (e.g., 3): "))
                
                # Call our function and store the result
                ciphertext = caesar_encrypt(message, key)
                
                print(f"\n🔒 Your encrypted message is: {ciphertext}")
            except ValueError:
                print("\n⚠️ Error: The shift key must be a whole number!")
            
        elif choice == '2':
            print("\n--- Decryption ---")
            message = input("Enter the message you want to decrypt: ")
            
            try:
                key = int(input("Enter the shift key it was encrypted with: "))
                
                # The magic trick: we use a negative key (-key) to shift backward!
                plaintext = caesar_encrypt(message, -key)
                
                print(f"\n🔓 Your decrypted message is: {plaintext}")
            except ValueError:
                print("\n⚠️ Error: The shift key must be a whole number!")

        elif choice == '3':
            print("\n--- Brute-Force Cracker ---")
            message = input("Enter the encrypted message to crack: ")
            
            print("\n[Cracking] Trying all possible shifts...")
            print("-" * 30)
            
            # The range(1, 26) function generates numbers from 1 up to 25.
            for shift in range(1, 26):
                # We use -shift because we are trying to reverse (decrypt) the message
                attempt = caesar_encrypt(message, -shift)
                
                # The :02d formats the number to always have two digits (e.g., 01, 02)
                print(f"Key {shift:02d}: {attempt}")
                
            print("-" * 30)
            print("Look through the results above to find the readable message!")
            
        elif choice == '4':
            print("\nExiting Enigma. Goodbye!")
            break # This stops the 'while' loop and ends the program
            
        else:
            # Catch-all for if they type '5' or letters by mistake
            print("\n⚠️ Invalid choice. Please type a number between 1 and 4.")

# Tells the script to run 
# the main() function when you start the file.
if __name__ == "__main__":
    main()
