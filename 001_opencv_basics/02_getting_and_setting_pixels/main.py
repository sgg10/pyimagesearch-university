import cv2
import click


@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]), default="script")
def main(image, env):

    image = cv2.imread(image)
    h, w = image.shape[:2]

    cv2.imshow("Original", image)

    # Images are simply Numpy arrays -- with the origin (0, 0) located at
    # the top-left of the image
    b, g, r = image[0, 0] # RGB -> BGR
    print(f"Pixel at (0, 0) - RED: {r}, GREEN: {g}, BLUE: {b}")

    # Acces to pixel located at x=50, y=20 | y->rows x->columns
    b, g, r = image[20, 50]
    print(f"Pixel at (50, 20) - RED: {r}, GREEN: {g}, BLUE: {b}")

    # Update the pixel at (50,20) and set it to pruple
    image[20, 50] = (216,28,131)
    b, g, r = image[20, 50]
    print(f"Pixel at (50, 20) - RED: {r}, GREEN: {g}, BLUE: {b}")

    cv2.imshow("With purple pixel", image)

    # Compute the center od the image, which is simply the width and heigth divided by two
    cX, cY = w // 2, h // 2

    """
    Since we are using NumPy Arrays, we can apply array slicing to grab
    large chunks/regions of interest from the image. Here we grab the
    top-left corner of the image
    """
    top_left = image[0:cY, 0:cX]
    cv2.imshow("Top-Left Corner", top_left)

    # Get all parts
    top_right = image[0:cY, cX:w]
    bottom_rigth = image[cY:h, cX:w]
    bottom_left = image[cY:h, 0:cX]

    cv2.imshow("Top-Right Corner", top_right)
    cv2.imshow("Bottom-Right Corner", bottom_rigth)
    cv2.imshow("Bottom-Left Corner", bottom_left)

    # Set the top-left corner of the original image to be green
    image[0:cY, 0:cX] = (0,255,0)
    cv2.imshow("Green corner", image)

    # Change color for all corners
    image[0:cY, 0:cX] = (0,255,0)
    image[0:cY, cX:w] = (216,28,131)
    image[cY:h, cX:w] = (255,0,0)
    image[cY:h, 0:cX] = (0,0,255)
    cv2.imshow("Multi color", image)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()