import cv2
import click
import numpy as np

assassins = {
    "Altair": {
        "face": { "x0": 162, "y0": 383, "x1": 233, "y1": 466 },
        "body": { "x0": 107, "y0": 382, "x1": 316, "y1": 918 }
    },
    "Connor": {
        "face": { "x0": 418, "y0": 376, "x1": 497, "y1": 480 },
        "body": { "x0": 350, "y0": 376, "x1": 630, "y1": 972 }
    },
    "Ezio": {
        "face": { "x0": 736, "y0": 345, "x1": 814, "y1": 442 },
        "body": { "x0": 645, "y0": 345, "x1": 956, "y1": 999 }
    }
}

@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]))
def main(image, env):
    image = cv2.imread(image)
    cv2.imshow("Original", image)

    """
    A mask is the same size as our image, but has only two pixel
    values, 0 and 255. Pixels with a value of 0 (background) are
    ignored in the original image while mask pixels with a value of
    255 (foreground) are allowed to be kept
    """
    mask = np.zeros(image.shape[:2], dtype="uint8")
    for _, data in assassins.items():
        face = data["face"]
        cv2.rectangle(mask, (face["x0"], face["y0"]), (face["x1"], face["y1"]), 255, -1)
    cv2.imshow("Rectangular Mask", mask)


    # Apply mask. Notice how only the faces in the image is cropped out
    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Mask Applied to Image", masked)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
