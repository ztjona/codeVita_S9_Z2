# -*- coding: utf-8 -*-
'''
Python 3.9.1
[MSC v.1916 64 bit (AMD64)]
30 / 01 / 2021
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

'''

################################################### '''



def main():
    '''
    
    ############################################### '''
    N, M = map(int, input().split())
    matrix = []

    for _ in range(N):
        vals = input().split()
        matrix.append(vals)
    

        
    def moveLayer(idLayer, rots, direction):
        ''' idLayer: 0indexed
        ############################################### '''
        colsLayer = M - 2*idLayer
        rowsLayer = N - 2*idLayer

        nLayer = max(colsLayer, rowsLayer)
        numElementsInLayer = 2*(colsLayer - 1) + 2*(rowsLayer - 1)

        rots = rots % numElementsInLayer

        if rots > numElementsInLayer // 2:
            # too many rotations in this direction, we reverse it
            rots = numElementsInLayer - rots
            # reversing
            if direction == 'counter_clockwise':
                direction = 'clockwise'
            else:
                direction = 'counter_clockwise'

        if rots == 0:
            # layer does not change
            return

        
        # --- at least 1 rotation
        rUp = idLayer
        rDown = N - idLayer - 1

        cLeft = idLayer
        cRight = M - idLayer - 1

        if direction == 'counter_clockwise':
            # counterclockwise
            for _ in range(rots):
                # - saving corners
                valDownLeft = matrix[rDown][cLeft]
                valUpLeft = matrix[rUp][cLeft]
                valDownRight = matrix[rDown][cRight]
                valUpRight = matrix[rUp][cRight]

                # -- rotating! (no corners)
                for j in range(nLayer - 1):
                    if cLeft + j + 1 <= cRight:
                        # - side up
                        matrix[rUp][cLeft + j] = matrix[rUp][cLeft + j + 1]
                        # - side down
                        matrix[rDown][cRight - j] = matrix[rDown][cRight - j - 1]
                    if rUp + j + 1 <= rDown:
                        # - side left
                        matrix[rDown - j][cLeft] = matrix[rDown - j - 1][cLeft]
                        # - side right
                        matrix[rUp + j][cRight] = matrix[rUp + j + 1][cRight]

                # -- completing corners
                matrix[rDown][cLeft + 1] = valDownLeft
                matrix[rUp + 1][cLeft] = valUpLeft
                matrix[rDown - 1][cRight] = valDownRight
                matrix[rUp][cRight - 1] = valUpRight
        else:
            # clockwise
            for _ in range(rots):
                # - saving corners
                valDownLeft = matrix[rDown][cLeft]
                valUpLeft = matrix[rUp][cLeft]
                valDownRight = matrix[rDown][cRight]
                valUpRight = matrix[rUp][cRight]

                # -- rotating!(no corners)
                for j in range(nLayer - 1):
                    if cLeft + j + 1 <= cRight:
                        # - side up
                        matrix[rUp][cRight - j] = matrix[rUp][cRight - j - 1]
                        # - side down
                        matrix[rDown][cLeft + j] = matrix[rDown][cLeft + j + 1]
                    
                    if rUp + j + 1 <= rDown:
                        # - side left
                        matrix[rUp + j][cLeft] = matrix[rUp + j + 1][cLeft]
                        # - side right
                        matrix[rDown - j][cRight] = matrix[rDown -j - 1][cRight]
                
                # -- completing corners
                matrix[rDown - 1][cLeft] = valDownLeft
                matrix[rUp][cLeft + 1] = valUpLeft
                matrix[rDown][cRight - 1] = valDownRight
                matrix[rUp + 1][cRight] = valUpRight
        return

    # rotations by layer
    rots = list(map(int, input().split()))

    nLayers = min(N, M)//2
    for i in range(nLayers):
        if i % 2 == 0:
            # counter clockwise
            direction = 'counter_clockwise'
        else:
            # clockwise
            direction = 'clockwise'
        moveLayer(i, rots[i], direction)

    for x in matrix:
        print(*x, sep=' ')

    return


if __name__ == "__main__":
    main()
