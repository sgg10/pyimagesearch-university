import cv2
import click
from matplotlib import pyplot as plt

# Function to display images in Jupyter Notebooks and Google Colab
def plt_imshow(title, image):
	# convert the image frame BGR to RGB color space and display it
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	plt.imshow(image)
	plt.title(title)
	plt.grid(False)
	plt.show()


@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]), default="script")
def main(image, env):
    """
    Load the image from disk via "cv2.imread" and then grab the spatial
    dimensions, including width, height and number of channels
    """
    image_name = image.split('/')[-1]

    image = cv2.imread(image)
    height, width, channels = image.shape[:3]

    print(f"""
    Width: {width} pixels
    Height: {height} pixels
    Channels: {channels}
    """)

    # Show the image and wait for a keypress
    if env == "script":
        cv2.imshow(f"OpenCV | {image_name}", image)
        cv2.waitKey(0)
    else:
        plt_imshow((f"OpenCV | {image_name}", image))

    cv2.imwrite("new_image.jpg", image)


if __name__ == '__main__':
    main()
