import math


def ceaser_cipher(data: str, key: int):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    szyfr = []
    for l in data:
        szyfr.append(l.lower())
    print(szyfr)
    for i in range(0, len(szyfr)):
        for l in range(0, len(alphabet)):
            print(i," ", szyfr[i]," ",alphabet[l])
            if szyfr[i] == alphabet[l]:
                if l + key >= len(alphabet):
                    szyfr[i] = alphabet[abs(len(alphabet) - key - l)]
                    break
                else:
                    szyfr[i] = alphabet[l + key]
                    break
    print(szyfr)


def count_tiles(fl, fw, tl, tw, ti):
    return math.ceil((fl * fw / (tl * tw * ti)))


def is_prime(*numbers):
        for n in range(0, len(numbers)):
            flag = 0
            for k in range(2, int(math.sqrt(numbers[n])) +1):
                if numbers[n] % k == 0:
                    flag = 1
                break
            if flag == 0:
                print(numbers[n], " is a prime number")
            else:
                print(numbers[n], " is not prime ")


ceaser_cipher("Ananas", 2)

print("Potrzeba " + str(count_tiles(3, 10, 3, 1, 3)))

is_prime(3, 7, 8, 23)
