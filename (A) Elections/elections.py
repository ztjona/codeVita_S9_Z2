# -*- coding: utf-8 -*-
'''
Python 3.9.1
[MSC v.1916 64 bit (AMD64)]
29 / 01 / 2021
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

'''

################################################### '''


def solveQueue(queue):
    ''' Returns winner for a queue. In the case of a draw returns -.
    # Example:
    --AB--AB---A--
    ############################################### '''

    # ---- Finding decisive votes (viz. '-')
    # Example: AB---B-
    # -> decisivesLocation
    # -> [[2, 5], [6, 7]] # (there is decisive voter between 2-5 and 6-7)

    lastVal = None
    decisivesLocation = []
    votes = {'A': 0, 'B': 0, '-': 0}

    for idx, val in enumerate(queue):
        # -- counting votes for A B and -
        votes[val] += 1

        # -- finding decisives!
        if val == '-':
            if lastVal == '-':
                # - continuing!
                decisivesLocation[-1][1] += 1
            else:
                # - creating new segment!
                # supossing only 1 element
                decisivesLocation.append([idx, idx + 1])

        lastVal = val

    # # simplifying block
    # #ie. AAA--B = 3A, 2-, 1B
    # simpleQueue = []
    # lastVal = None
    # for val in queue:
    #     if lastVal == val:
    #         simpleQueue[-1][1] += 1
    #     else:
    #         simpleQueue.append([val, 1])
    #         lastVal = val

    # --- solving
    # -- does the decisives matter?
    if votes['A'] > votes['B'] + votes['-']:
        # A will win even with B convencing everybody!
        return 'A'
    elif votes['B'] > votes['A'] + votes['-']:
        # B will win even with A convencing everybody!
        return 'B'
    # else

    # -- there is to be decided yet.
    votersConverted = {'A': 0, 'B': 0}  # new votes for A or B
    for i, j in decisivesLocation:

        # - voters on each side
        # * left
        leftBVoter = False  # prealloc
        if i > 0:
            if queue[i - 1] == 'B':
                leftBVoter = True

        # * right
        rightAVoter = False
        if j < len(queue):
            if queue[j] == 'A':
                rightAVoter = True

        # - converting!
        numConversors = j - i
        if leftBVoter:
            if rightAVoter:
                # left and right. dividing
                eachSide = numConversors//2
                votersConverted['A'] += eachSide
                votersConverted['B'] += eachSide
            else:
                # only left, no right! All B
                votersConverted['B'] += numConversors

        else:
            if rightAVoter:
                # only right, no left! All A
                votersConverted['A'] += numConversors
            else:
                # nothing on the sides?!
                pass

        # --- Counting!
        As = votes['A'] + votersConverted['A']
        Bs = votes['B'] + votersConverted['B']
        if As > Bs:
            return 'A'
        elif As < Bs:
            return 'B'
        else:
            return '-'


def main():
    '''

    ############################################### '''
    _ = input()
    votersQueue = input()

    resp = solveQueue(votersQueue)
    if resp == '-':
        print('Coalition government')
    else:
        print(resp)
    return


if __name__ == "__main__":
    main()
