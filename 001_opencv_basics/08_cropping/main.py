import cv2
import click
import numpy as np
from cv2 import Mat


colors = { "green": (0,255,0), "blue": (255,0,0), "red": (0,0,255), "white": (255,255,255) }

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

def draw_rectangle(canvas, pt1: tuple, pt2: tuple, color:str, thickness:int=1):
    cv2.rectangle(canvas, pt1, pt2, colors[color], thickness)

@click.command()
@click.option('-i', '--image', required=True)
@click.option('-e', '--env', type=click.Choice(["script", "jupyter"]))
def main(image, env):
    image = cv2.imread(image)
    cv2.imshow("Original", image)

    for _, data in assassins.items():
        face = data["face"]
        body = data["body"]
        draw_rectangle(image, (face["x0"], face["y0"]), (face["x1"], face["y1"]), "green")
        draw_rectangle(image, (body["x0"], body["y0"]), (body["x1"], body["y1"]), "blue")
    cv2.imshow("Assassins", image)

    for assassin, data in assassins.items():
        face_data = data["face"]
        body_data = data["body"]
        """
        Cropping an image with OpenCV is accomplished via simple NumPy array slices in
        startY:endY, startX:endX order. Here we are cropping the face from the image
        (these coordinates were determinad using photo editing software such as Photoshop,
        GIMP, Paint, etc.)
        """
        face = image[face_data["y0"]:face_data["y1"], face_data["x0"]:face_data["x1"]]
        body = image[body_data["y0"]:body_data["y1"], body_data["x0"]:body_data["x1"]]
        cv2.imshow(f"{assassin}'s Face", face)
        cv2.imshow(f"{assassin}'s Body", body)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()