from math import log
from random import SystemRandom, random
import argparse

import pyperclip


def generate_charset(noupper=False, nolower=False, nonumber=False, nosymbol=False):

    charset = {
        "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "lower": "abcdefghijklmnopqrstuvwxyz",
        "numbers": "0123456789",
        "symbols": "!@#$%&*()_-=§+[]{},.<>\|"
    }

    if noupper:
        charset["upper"] = ""
    
    if nolower:
        charset["lower"] = ""
    
    if nonumber:
        charset["numbers"] = ""
    
    if nosymbol:
        charset["symbols"] = ""

    return charset["upper"] + charset["lower"] + charset["numbers"] + charset["symbols"]


def calculate_entropy(length, charset):
    return log(len(charset), 2) * length


def generate_password(length, charset):

    random_engine = SystemRandom()

    password = ""

    for i in range(0, length):

        character = random_engine.choice(charset)

        password = password + character
    
    return password


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("length", help="Characters length of the password")
    parser.add_argument("-l", "--nolower", help="Disable lowercase letters on the password", action="store_true", default=False)
    parser.add_argument("-u", "--noupper", help="Disable uppercase letters on the password", action="store_true", default=False)
    parser.add_argument("-n", "--nonumber", help="Disable numbers on the password", action="store_true", default=False)
    parser.add_argument("-s", "--nosymbol", help="Disable special characters on the password", action="store_true", default=False)
    parser.add_argument("-c", "--copy", help="copy the generated password to clipboard", action="store_true", default=False)

    args = parser.parse_args()

    charset = generate_charset(args.noupper, args.nolower, args.nonumber, args.nosymbol)

    password = generate_password(int(args.length), charset)

    entropy = calculate_entropy(int(args.length), charset)

    if entropy < 50:
        safety = "weak"
    elif entropy < 75:
        safety = "neutral"
    elif entropy < 100:
        safety = "strong"
    else:
        safety = "very strong"

    if not args.copy:
        print(f"Generated password: {password}")
    
    else:
        pyperclip.copy(password)
        print("Password copied sucessfuly!")    
    
    
    print(f"Your password safety is: {safety} (entropy={entropy:.2f})")

if __name__ == "__main__":
    main()
