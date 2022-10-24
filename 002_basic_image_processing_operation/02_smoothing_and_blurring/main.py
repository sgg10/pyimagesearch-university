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
    cv2.imshow("Original", image)
    kernel_sizes = [(3, 3), (9, 9), (15, 15), (80, 80), (150,150)]
    # kernel_sizes = [(80, 9), (9, 80)]

    # Loop over the kernel sizes
    for kX, kY in kernel_sizes:
        # Apply an "average" blur to the image using the current kernel size
        blurred = cv2.blur(image, (kX, kY))
        cv2.imshow(f"Average ({kX}, {kY})", blurred)
        cv2.waitKey(0)

    clear(image)

    # Loop over the kernel sizes and apply a "Gaussian" blur to the image using each kernel size
    for kX, kY in kernel_sizes:
        try:
            blurred = cv2.GaussianBlur(image, (kX, kY), 0)
            cv2.imshow(f"Gaussian ({kX}, {kY})", blurred)
            cv2.waitKey(0)
        except:
            continue

    clear(image)

    # Loop over the kernel sizes and apply a "median" blur to the image using each kernel size
    for k, _ in kernel_sizes:
        try:
            blurred = cv2.medianBlur(image, k)
            cv2.imshow(f"Median ({k})", blurred)
            cv2.waitKey(0)
        except:
            continue

    clear(image)

    # Bilateral filtering
    params = [(11,21,7), (11,41,21), (11,61,39)]
    # params = [(120,10,10), (10,120,10), (10,10,120), (120, 10, 120), (120,120,120)]
    # params = [(25, 300, 25), (150, 300, 25), (25, 300, 150)]

    # Loop over the diameter, sigma color and sigma space
    for diameter, sigma_color, sigma_space in params:
        # Apply bilteral filtering to the image using the current set of parameters
        blurred = cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)
        cv2.imshow(f"Blurred d={diameter}, sc={sigma_color}, ss={sigma_space}", blurred)
        cv2.waitKey(0)


if __name__ == '__main__':
    main()