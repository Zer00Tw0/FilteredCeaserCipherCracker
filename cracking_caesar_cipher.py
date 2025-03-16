#02
import string
from colorama import Fore

# Filter
def find(wanted, color, type):
    for word in wanted:
        if word in translated.lower():
            print(f"{color}Key: {key} | Message: {translated} | {type}: {word}{Fore.RESET}")

# Main 
def main():
    global key
    global translated
    
    # Input
    message = ""
    while len(message) == 0:
        message = input("Enter Message: ")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    all_chars = lowercase + uppercase + digits + punctuation + " "
    
    print("All filters are separated by space")
    wanted_words = input("Enter Wanted Words (RED): ").split()
    wanted_numbers = input("Enter Wanted Numbers (YELLOW): ").split()
    wanted_chars = input("Enter Wanted Chars (GREEN): ").split()
    
    count = 0
    
    
    for letter_key in range(26):  
        for digit_key in range(10):  
            translated = ""
            for char in message:
                if char in lowercase:
                    # lowercase letters
                    index = (lowercase.find(char) - letter_key) % 26
                    translated += lowercase[index]
                elif char in uppercase:
                    # uppercase letters
                    index = (uppercase.find(char) - letter_key) % 26
                    translated += uppercase[index]
                elif char in digits:
                    # digits 
                    index = (digits.find(char) - digit_key) % 10
                    translated += digits[index]
                else:
                    # Keep special characters as is
                    translated += char
            

            key = f"{letter_key}.{digit_key}"
            
            # Filters
            if wanted_words and wanted_words != ['']:
                find(wanted_words, Fore.RED, "Word")
            if wanted_numbers and wanted_numbers != ['']:
                find(wanted_numbers, Fore.YELLOW, "Number")
            if wanted_chars and wanted_chars != ['']:
                find(wanted_chars, Fore.GREEN, "Character")
            
            if (not wanted_words or wanted_words == ['']) and (not wanted_numbers or wanted_numbers == ['']) and (not wanted_chars or wanted_chars == ['']):
                if count == 0:
                    print(f"{Fore.RED}No options were typed, printing all tries.{Fore.RESET}")
                    count += 1
                print(f"Key: {key} | Message: {translated}")

if __name__ == '__main__':
    main()
