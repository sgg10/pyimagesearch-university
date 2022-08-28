import cv2
import click
import imutils
import numpy as np


@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]), default="script")
def main(image, env):
    image = cv2.imread(image)
    cv2.imshow("Original", image)

    # Shift the image 25 pixels to the right and 50 pixels down
    M = np.float32([[1, 0, 25], [0, 1, 50]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted down and right", shifted)

    """
    Now, let's shift the image 50 pixels to the left and 90 pixels
    up by specifying negative values for the x and y directions respectively.
    """
    M = np.float32([[1, 0, -50],[0, 1, -90]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted up and left", shifted)


    """
    Now, use the imutils helper function to translate the image 100 pixels
    down in a single function call
    """
    shifted = imutils.translate(image, 0, 100)
    cv2.imshow("Shifted Down", shifted)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()
