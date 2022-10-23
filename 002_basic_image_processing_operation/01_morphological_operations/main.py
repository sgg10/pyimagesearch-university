import cv2
import click


def clear(image):
    cv2.destroyAllWindows()
    cv2.imshow("Original", image)


@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]))
def main(image, env):
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original", image)

    # Apply a series of erosions
    for i in range(3):
        eroded = cv2.erode(gray.copy(), None, iterations=i+1)
        cv2.imshow(f"Eroded {i+1} times", eroded)
        cv2.waitKey(0)

    clear(image)

    # Apply series of dilations
    for i in range(3):
        dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
        cv2.imshow(f"Dilated {i+1} times", dilated)
        cv2.waitKey(0)

    clear(image)

    kernel_sizes = ((3,3), (5,5), (7,7))

    # Loop over the kernel size
    for kernel_size in kernel_sizes:
        # Construct a rectangular kernel from the current size and then apply an "opening" operation
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        cv2.imshow(f"Opening: {kernel_size[0]}, {kernel_size[1]}", opening)
        cv2.waitKey(0)

    clear(image)

    # Loop over the kernel size
    for kernel_size in kernel_sizes:
        # Construct a rectangular kernel from the current size and then apply an "closing" operation
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
        closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
        cv2.imshow(f"Closing: {kernel_size[0]}, {kernel_size[1]}", closing)
        cv2.waitKey(0)

    clear(image)

    # Loop over the kernel size
    for kernel_size in kernel_sizes:
        # Construct a rectangular kernel from the current size and then apply an "morphological gradient" operation
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
        gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
        cv2.imshow(f"Gradient: {kernel_size[0]}, {kernel_size[1]}", gradient)
        cv2.waitKey(0)


if __name__ == '__main__':
    main()
