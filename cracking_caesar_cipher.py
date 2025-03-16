import string
from colorama import Fore
#filter
def find(wanted,color,type):
    for word in wanted:
        if word in translated.lower():
            print(f"{color}Key: {key} | Message:{translated} | {type}:{word}{Fore.RESET}")
        else: continue

#main
def main():
    global key
    global wanted_words
    global wanted_numbers
    global wanted_chars
    global translated

    #input
    count=0
    message = ""
    while len(message) == 0:
        message = input("Enter Message: ")

    symbols = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation+" "
    print("All filters are separated by space")
    wanted_words = input("Enter Wanted Words(RED): ").split(" ")
    wanted_numbers = input("Enter Wanted Numbers(YELLOW): ").split(" ")
    wanted_chars = input("Enter wanted Chars(GREEN): ").split(" ")

    #brute force decrypt 
    for key in range(len(symbols)):
        translated = ""
        for letter in message:
            if letter in symbols:
                symbolIndex = symbols.find(letter)

                translated_index = symbolIndex-key

                if translated_index<0:
                    translated_index+=len(symbols)
                
                translated+=symbols[translated_index]
            else:
                print("Sorry there was a error in trying to crack caesar cipher")
        
        #filters

        if not (len(wanted_words) == 0 or wanted_words == ['']):
            find(wanted_words,Fore.RED,"Word")
        if not (len(wanted_numbers) == 0 or wanted_numbers == ['']):
            find(wanted_numbers,Fore.YELLOW,"Number")
        if not (len(wanted_chars) == 0 or wanted_chars == ['']):
            find(wanted_chars,Fore.GREEN,"Character")
        if (len(wanted_chars) == 0 or wanted_chars == ['']) and (len(wanted_numbers) == 0 or wanted_numbers == ['']) and (len(wanted_words) == 0 or wanted_words == ['']):
            while count == 0: print(f"{Fore.RED}No options were typed, printing all tries.{Fore.RESET}"); count+=1
            print(f"Key: {key} Message:{translated}")


if __name__ == '__main__':
    main() 
