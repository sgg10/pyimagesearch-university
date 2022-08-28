import cv2
import click
import imutils
from cv2 import Mat


@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]))
def main(image, env):
    image: Mat = cv2.imread(image)
    cv2.imshow("Original", image)

    """
    Let's resize image to be 150 pixels wide, but in order to
    prevent our resized image from being skewd/distorted, we must
    first calculate the ratio of the *new* width to the *old* width.
    """
    r = 150.0 / image.shape[1]
    dim = (int(150), int(image.shape[0] * r))

    # Perform the actual resizing of the image
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Resized (150 Width)", resized)

    """
    Let's resize the image to width of 50 pixels, again keeping
    in mind the aspect ratio
    """
    r = 50.0 / image.shape[0]
    dim = (int(image.shape[1] * r), 50)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Resized (50 Height)", resized)

    cv2.waitKey(0)

    """
    Calculating the ratio each and every time we want to resize an
    image is a real pain, so let's use the imutils convenience function
    which will *automatically* maintain our aspect ratio for us
    """
    resized = imutils.resize(image, width=100)
    cv2.imshow("Resized via imutils", resized)
    cv2.waitKey(0)

    methods = (
        ("cv2.INTER_BITS", cv2.INTER_BITS),
        ("cv2.INTER_AREA", cv2.INTER_AREA),
        ("cv2.INTER_BITS2", cv2.INTER_BITS2),
        ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
        ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
        ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
        ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4),
        ("cv2.INTER_LINEAR_EXACT", cv2.INTER_LINEAR_EXACT),
    )

    for name, method in methods:
        # Increase the size of the image by 3x using the current interpolation method
        print(f"[INFO] {name}")
        resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
        cv2.imshow(f"Method: {name}", resized)
        cv2.waitKey(0)

if __name__ == "__main__":
    main()
