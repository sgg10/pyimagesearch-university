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

    # Construct a rectangular kernel (13x5) and apply blackhat
    # operation which enables us to find dark regions on a light background
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rect_kernel)

    # Similarly, a tophat (also called a "whitehat") operation will
    # enable us to find light regions on a dark background
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rect_kernel)

    cv2.imshow("Original", image)
    cv2.imshow("Blackhat", blackhat)
    cv2.imshow("Tophat", tophat)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()

