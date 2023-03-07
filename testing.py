import numpy as np
import matplotlib.pyplot as plt


def testMeshGrid():
    nx = np.linspace(-5,5,20)
    ny = np.linspace(-5,5,20)
    X,Y = np.meshgrid(nx,ny)

    # print(X)

    plt.plot(X,Y, 'o')
    plt.show()



testMeshGrid()