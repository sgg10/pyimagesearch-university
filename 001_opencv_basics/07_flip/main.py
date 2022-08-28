import cv2
import click
from cv2 import Mat


@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]))
def main(image, env):
    image = cv2.imread(image)
    cv2.imshow("Original", image)

    # Flip the image horizontally
    print("[INFO] flipping image horizontally...")
    flipped = cv2.flip(image, 1)
    cv2.imshow("Flipped horizontally", flipped)

    # Flip the image vertically
    print("[INFO] flipping image vertically...")
    flipped = cv2.flip(image, 0)
    cv2.imshow("Flipped vertically", flipped)

    # Flip the image along both axes
    print("[INFO] flipping image horizontally and vertically...")
    flipped = cv2.flip(image, -1)
    cv2.imshow("Flipped horizontally and vertically", flipped)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()