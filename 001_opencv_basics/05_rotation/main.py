import cv2
import click
import imutils


@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]), default="script")
def main(image, env):
    image = cv2.imread(image)
    cv2.imshow("Original", image)

    # Grab the dimensions of the image and calculate the center
    h, w = image.shape[:2]
    cX, cY = w // 2, h // 2

    # Rotate image by 45 degrees aroud the center of the image
    M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 45 degrees", rotated)

    # Rotate image by -90 degrees aroud the image
    M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by -90 degrees", rotated)

    # Rotate image aroud an arbitrary point rather than the center
    M = cv2.getRotationMatrix2D((10,10), 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by arbitrary point", rotated)

    # Use imutils function to rotate an image 180 degrees
    rotated = imutils.rotate(image, 180)
    cv2.imshow("Rotated by 180 degrees", rotated)

    """
    Rotated image by 33 degrees counterclockwise, ensuring the
    entire rotated image still views in the viewing area
    """
    rotated = imutils.rotate_bound(image, -33)
    cv2.imshow("Rotate without Cropping", rotated)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
