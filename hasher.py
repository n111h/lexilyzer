#!/usr/bin/python3
#
#  Noah Olmstead Harvey
#  04102021
#
#  lexical analyzer for pl0

####  IMPORTS  #################################################################################################################

import matplotlib                                               #  for hash testing
from matplotlib import pyplot as plt                            #  for hash testing
import seaborn as sns                                           #  for hash testing

####  GLOBALS  #################################################################################################################

primes = [                                                      #  primes up to 1000
      2,  3,  5,  7, 11, 13, 17, 19, 23, 29,
     31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
     73, 79, 83, 89, 97,101,103,107,109,113,
    127,131,137,139,149,151,157,163,167,173,
    179,181,191,193,197,199,211,223,227,229,
    233,239,241,251,257,263,269,271,277,281,
    283,293,307,311,313,317,331,337,347,349,
    353,359,367,373,379,383,389,397,401,409,
    419,421,431,433,439,443,449,457,461,463,
    467,479,487,491,499,503,509,521,523,541,
    547,557,563,569,571,577,587,593,599,601,
    607,613,617,619,631,641,643,647,653,659,
    661,673,677,683,691,701,709,719,727,733,
    739,743,751,757,761,769,773,787,797,809,
    811,821,823,827,829,839,853,857,859,863,
    877,881,883,887,907,911,919,929,937,941,
    947,953,967,971,977,983,991,997
]

largePrimes = [
    9999463, 9999469, 9999481, 9999511, 9999533, 9999593, 9999601, 9999637, 9999653, 9999659,
    9999667, 9999677, 9999713, 9999739, 9999749, 9999761, 9999823, 9999863, 9999877, 9999883,
    9999889, 9999901, 9999907, 9999929, 9999931, 9999937, 9999943, 9999971, 9999973, 9999991
]

firstPrimes = [primes[i] for i in range(30)]                    #  the first 30 primes (used in hasher0)

primePrimes = [primes[(prime-1)] for prime in firstPrimes]      #  the first 30 prime/primes (used in hasher0)

####  FUNCTIONS  ###############################################################################################################

def hasher(identifier="testString", factor="primePrimes", modulo=499):
    hashCode = 0
    if(factor not in ["firstPrimes","primePrimes","index","number","largePrimes"]):
        print("!!!!  UNKNOWN FACTOR PASSED  !!!!")
        return(None)
    for e,char in enumerate(identifier):                        #  for each char in the identifier and it's index
        if(factor=="firstPrimes"): hashCode+=(ord(char)*firstPrimes[e])     #  multiply each char by the prime at index
        elif(factor=="primePrimes"): hashCode+=(ord(char)*primePrimes[e])   #  multiply each char by the primePrime at index
        elif(factor=="largePrimes"): hashCode+=(ord(char)*largePrimes[e])   #  multiply each char by the big prime at index
        elif(factor=="index"): hashCode+=(ord(char)*e)          #  multiply each char by the index
        elif(factor=="number"): hashCode+=(ord(char)*(e+1))     #  multiply each char by the index plus one
    return(hashCode%modulo)                                     #  return the sum of those values modulo the symbol table size

####  MAIN  ####################################################################################################################

def main():
    with open("engDict.txt", 'r') as f:
        engDict = f.read().split()                              #  list of 370102 english words (<=30 chars)

    print("\nNumber of test words:",len(engDict),'\n')
    print("Hashing Factors:")
    print(f"{'index':<12}{'number':<12}{'firstPrimes':<12}{'primePrimes':<12}{'largePrimes':<12}")
    for e,p in enumerate(firstPrimes):
        print(f"{e:<12}{(e+1):<12}{p:<12}{primePrimes[e]:<12}{largePrimes[e]:<12}")
    print()
    print("'testString' hash:",hasher(),'\n')

    firstPrimesHash = []
    primePrimesHash = []
    largePrimesHash = []
    indexHash = []
    numberHash = []
    numberHash500 = []

    for word in engDict:
        firstPrimesHash.append(hasher(word,"firstPrimes"))
        primePrimesHash.append(hasher(word,"primePrimes"))
        largePrimesHash.append(hasher(word,"largePrimes"))
        indexHash.append(hasher(word,"index"))
        numberHash.append(hasher(word,"number"))
        numberHash500.append(hasher(word,"number",500))

    # plt.figure(figsize=(11,8.5))
    # sns.distplot(indexHash, color='r', label="index", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # sns.distplot(numberHash, color='r', label="number", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # sns.distplot(primeHash, color='g', label="prime", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # sns.distplot(largePrimes, color='b', label="largePrime", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # sns.distplot(primePrimeHash, color='b', label="primePrime", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # plt.xlim(-1,500)
    # plt.legend()
    # plt.savefig("allHashes.pdf")

    # plt.figure(figsize=(11,8.5))
    # sns.distplot(primeHash, color='b', label="prime", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # plt.xlim(-1,500)
    # plt.legend()
    # plt.savefig("primeHash.pdf")

    # plt.figure(figsize=(11,8.5))
    # sns.distplot(primePrimeHash, color='b', label="primePrime", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # plt.xlim(-1,500)
    # plt.legend()
    # plt.savefig("primePrimeHash.pdf")

    # plt.figure(figsize=(11,8.5))
    # sns.distplot(indexHash, color='b', label="index", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # plt.xlim(-1,500)
    # plt.legend()
    # plt.savefig("indexHash.pdf")

    # plt.figure(figsize=(11,8.5))
    # sns.distplot(numberHash, color='b', label="number", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # plt.xlim(-1,500)
    # plt.legend()
    # plt.savefig("numberHash.pdf")

    # plt.figure(figsize=(11,8.5))
    # sns.distplot(numberHash, color='b', label="number", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # sns.distplot(numberHash500, color='r', label="number % 500", bins=500, kde_kws={"shade":True, "bw_method":.01})
    # plt.xlim(-1,501)
    # plt.legend()
    # plt.savefig("numberModCompare.pdf")

    # plt.figure(figsize=(11,8.5))
    # sns.distplot(primeHash, color='r', label="prime", bins=499, kde_kws={"shade":True,"bw_method":.01})
    # sns.distplot(primePrimeHash, color='b', label="primePrime", bins=499, kde_kws={"shade":True, "bw_method":.01})
    # plt.xlim(-1,500)
    # plt.legend()
    # plt.savefig("primeVprimePrime.pdf")

if(__name__=="__main__"): main()