import hashlib
import typing
import time

def generate_hash(password, salt: str, iterations: int):
    passwordBytes = password.encode('UTF-8')
    saltBytes = salt.encode('UTF-8')
    derivedHash =  hashlib.pbkdf2_hmac('sha256', passwordBytes, saltBytes, iterations)
    return derivedHash.hex()

def attack_hash(hash: str, dictionary: [str]):
    
    for attack in dictionary:
        print("Attempting " + attack + "...")
        attackList = attack.split(" ")
        iterations = int(attackList[2])
        for i in range(1, iterations+1):
            if (generate_hash(attackList[0], attackList[1], i) == hash):
                print("--------MATCH FOUND--------\n" + attack + "\n------------------------")
                return True
    print("No matches found.")
    return False
    

def main():
    startTime = time.thread_time()
    dictionary = open("dictionary.txt", "r")
    baseHash = open("basehash.txt", "r")
    attack_hash(baseHash.read(), dictionary.read().splitlines())
    endTime = time.thread_time()
    print("Elapsed time: " + str(endTime-startTime) + "s")

main()