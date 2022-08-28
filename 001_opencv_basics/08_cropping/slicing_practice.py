import numpy as np

if __name__ == '__main__':
    I = np.arange(0, 25)
    print(I)

    I = I.reshape((5, 5))
    print(I)

    print("\nI[0, 2:5] =", I[0, 2:5])

    print("\nI[3:, 3:] =\n\n", I[3:, 3:])

    print("\nI[:, 2] =\n\n", I[:, 2])

    print("\nI[2::2, ::2] =\n\n", I[2::2, ::2])

    print("\nI[0:3, 0:2] =\n\n", I[0:3, 0:2])

    print("\nI[3:5, 1:5] =\n\n", I[3:5, 1:5])