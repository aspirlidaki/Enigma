def main():
    print("Welcome to Enigma: The Cipher Toolkit! 🔐")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute-force a Caesar Cipher")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            print("\n[+] Encryption module selected. (Coming soon...)")
            
        elif choice == '2':
            print("\n[-] Decryption module selected. (Coming soon...)")
            
        elif choice == '3':
            print("\n[*] Brute-force module selected. (Coming soon...)")
            
        elif choice == '4':
            print("\nExiting Enigma. Goodbye!")
            break
            
        else:
            print("\n⚠️ Invalid choice. Please type a number between 1 and 4.")

if __name__ == "__main__":
    main()
