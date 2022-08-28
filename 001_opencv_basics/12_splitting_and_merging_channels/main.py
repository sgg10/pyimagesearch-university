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

    B, G, R = cv2.split(image)

    # Show each channel individually
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    cv2.waitKey(0)

    # Merge the image back together again
    merged = cv2.merge([B, G, R])
    cv2.imshow("Merged", merged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Visualize each channel in color
    zeros = np.zeros(image.shape[:2], dtype="uint8")
    cv2.imshow("RED", cv2.merge([zeros, zeros, R]))
    cv2.imshow("GREEN", cv2.merge([zeros, G, zeros]))
    cv2.imshow("BLUE", cv2.merge([B, zeros, zeros]))

    cv2.waitKey(0)


if __name__ == '__main__':
    main()