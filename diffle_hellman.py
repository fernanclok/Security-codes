import random

def generate_private_key(n, g):

    #random number for Alice where  x<n-1
    x = random.randint(1, n)

    #random number for Bob where  y<n-1
    y = random.randint(1, n)

    #calculate g^x mod n which is Alice's k1
    k1 = pow(g, x, n)

    #calculate g^y mod n which is Bob's k2
    k2 = pow(g, y, n)

    #print the private keys
    print("Alice's private key: %s" % (pow(k2, x, n)))
    print("Bob's private key: %s" % (pow(k1, y, n)))

if __name__ == "__main__":
    n = 2347
    g = 750
    generate_private_key(n, g)