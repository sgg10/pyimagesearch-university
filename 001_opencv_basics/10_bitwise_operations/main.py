import cv2
import click
import numpy as np

@click.command()
@click.option('-i', '--image', default=None)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]))
def main(image, env):
    if image:
        image = cv2.imread(image)
        cv2.imshow("Original", image)

        not_image = cv2.bitwise_not(image)
        cv2.imshow("NOT", not_image)
        cv2.waitKey(0)
    else:
        # Draw a rectangle
        rectangle = np.zeros((300, 300), dtype="uint8")
        cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
        cv2.imshow("Rectangle", rectangle)

        # Draw a circle
        circle = np.zeros((300, 300), dtype = "uint8")
        cv2.circle(circle, (150, 150), 150, 255, -1)
        cv2.imshow("Circle", circle)

        """
        A bitwise 'AND' is only 'True' when both inputs have a value that
        is "ON'. In this case, the cv2.bitwise_and function examines
        every pixel in the rectangle and circle; if *BOTH* pixels have a
        value greater than zero then the pixel is turned 'ON (i.e., 255)
        in the output image; otherwise, the output value is set to
        'OFF' (i.e., 0)
        """
        bitwise_and = cv2.bitwise_and(rectangle, circle)
        cv2.imshow("AND", bitwise_and)
        cv2.waitKey(0)

        """
        A bitwise 'OR' examines every pixel in the two inputs, and if
        *EITHER* pixel in the rectangle or circle is greater than zero,
        then the output pixel has a value of 255, otherwise it is 0
        """
        bitwise_or = cv2.bitwise_or(rectangle, circle)
        cv2.imshow("OR", bitwise_or)
        cv2.waitKey(0)

        """
        The bitwise 'XOR' is identical to the 'OR' function, with one
        exception: both the rectangle and circle are not allowed to *BOTH*
        have values greater than 0 (only one can be 0)
        """
        bitwiseXor = cv2.bitwise_xor(rectangle, circle)
        cv2.imshow("XOR", bitwiseXor)
        cv2.waitKey(0)

        """
        Finally, the bitwise 'NOT' inverts the values of the pixels; pixels
        with a value of 255 become 0, and pixels with a value of 0 become 255
        """
        bitwiseNot = cv2.bitwise_not(circle)
        cv2.imshow("NOT", bitwiseNot)
        cv2.waitKey(0)


if __name__ == '__main__':
    main()