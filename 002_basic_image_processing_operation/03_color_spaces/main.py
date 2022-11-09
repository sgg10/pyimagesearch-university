import cv2
import click


def clear(image):
    cv2.destroyAllWindows()
    cv2.imshow("Original", image)

def show_split_image(names, image):
    for name, channel in zip(names, cv2.split(image)):
        cv2.imshow(name, channel)
    cv2.waitKey(0)


@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]))
def main(image, env):
    image = cv2.imread(image)
    cv2.imshow("Original", image)

    # Lop over each of the individual channels and displat them
    show_split_image(("B", "G", "R"), image)
    clear(image)

    # Convert the image to the HVS color space and show it
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)
    show_split_image(("H", "S", "V"), hsv)
    clear(image)

    # Convert the image to the L*a*b* color space and show it
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    cv2.imshow("L*a*b*", lab)
    show_split_image(("L*", "a*", "b*"), lab)
    clear(image)

    # Show the original and grayscale version of the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
