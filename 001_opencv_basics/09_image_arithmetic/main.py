import cv2
import click
import numpy as np
from cv2 import Mat


@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]))
def main(image, env):
    image = cv2.imread(image)
    cv2.imshow("Original", image)


    """
    Images are NumPy array stored as unsigned 8-bit integer (uint8)
    with values in the range [0, 255]; when using the add/subtract
    function in OpenCV, these values will be *clipped* to this range,
    even if they fall outside the range [0,255] after applying the operation
    """

    added = cv2.add(np.uint8([200]), np.uint8([100]))
    subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
    print(f"""
        Max of 255: {added}
        Min of 0: {subtracted}
    """)


    """
    Using NumPy arithmetic operations (rather than OpenCV operations)
    will result in modulo ("wrap around") instead of being clipped to
    the range [0, 255]
    """
    added = np.uint8([200]) + np.uint8([100])
    subtracted = np.uint8([50]) - np.uint8([100])
    print(f"""
        Wrap around (add): {added}
        Wrap around (sub): {subtracted}
    """)

    """
    Increasing the pixel intensities in input image by 100 is
    accomplished by constructing a NumPy array that has the *same
    dimensions* as input image, filling it with ones, multiplying it
    by 100, and then adding the input image and matrix together
    """
    M = np.ones(image.shape, dtype="uint8") * 100
    # M[:M.shape[0]//2, :M.shape[1]//2] = M[:M.shape[0]//2, :M.shape[1]//2] / 100
    added = cv2.add(image, M)
    cv2.imshow("Ligther", added)


    # Similarly, we can subtract 50 from all pixels in image and make it darker
    M = np.ones(image.shape, dtype="uint8") * 50
    subtracted = cv2.subtract(image, M)
    cv2.imshow("Darker", subtracted)

    M = np.ones(image.shape, dtype="uint8") * 2
    multiply = cv2.multiply(image, M)
    cv2.imshow("multiply", multiply)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()