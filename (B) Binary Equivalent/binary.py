# -*- coding: utf-8 -*-
'''
Python 3.9.1
[MSC v.1916 64 bit (AMD64)]
30 / 01 / 2021
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from itertools import combinations

'''

################################################### '''


def convertBin(x): return format(x, 'b')  # bin(x).replace("0b", "")


def convertingInOnes(nums):
    ''' returns a list with the number of ones on each number (in binary), and the number of bits of the maximum number
    ############################################### '''

    maxBits = 0  # prealloc
    nums_1 = []  # converting the numbers in the num of ones

    def howManyOnes(x): return x.count("1")
    for x in nums:
        data = convertBin(x)
        y = howManyOnes(data)
        nums_1.append(y)

        nBits = len(data)
        if maxBits < nBits:
            maxBits = nBits

    return nums_1, maxBits


def countingCombinations(vals, maxBits):
    ''' returns the number of combinations that fullfil the binary equivalence
    ############################################### '''

    nSolutions = 0

    # D: for a given vector x returns true when the nmber of ones is equal the number of zeros!
    def validateEquivalence(x): return sum(x)*2 == maxBits*len(x)

    for i in range(1, len(vals) + 1):
        for comb in combinations(vals, i):
            if validateEquivalence(comb):
                nSolutions += 1

    return nSolutions


def main():
    '''
    
    ############################################### '''
    _ = input()
    nums = map(int, input().split())

    # --- Converting!
    vals, maxBits = convertingInOnes(nums)

    # --- Conuintg solutions
    nSolutions = countingCombinations(vals, maxBits)

    # --- Printing!
    resp = format(nSolutions, '0' + str(maxBits) + 'b')
    print(resp)
    return


if __name__ == "__main__":
    main()
