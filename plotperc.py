import numpy as np
import random as rand
import matplotlib.pyplot as plt

tstmat1 = [[1,0,0,0,0,1],
                [1,1,1,0,0,0],
                [0,0,1,1,0,0],
                [1,0,0,1,1,1],
                [1,1,1,0,0,0],
                [0,0,1,1,1,1]]

tstmat2 = [[0,1,0],[0,0,0],[0,1,0]]

tstmat3 = [[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
plt.imshow(tstmat3, 'binary')
plt.savefig('noperc2.pdf')
