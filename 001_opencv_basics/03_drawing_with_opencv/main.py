import cv2
import numpy as np

colors = { "green": (0,255,0), "blue": (255,0,0), "red": (0,0,255), "white": (255,255,255) }

def draw_line(canvas, pt1: tuple, pt2: tuple, color:str, thickness:int=1):
    cv2.line(canvas, pt1, pt2, colors[color], thickness)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

def draw_rectangle(canvas, pt1: tuple, pt2: tuple, color:str, thickness:int=1):
    cv2.rectangle(canvas, pt1, pt2, colors[color], thickness)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)


if __name__ == '__main__':
    # Initialize our canvas as a 300x300 with 3 channels with a black background.
    canvas = np.zeros((300,300,3), dtype="uint8")

    # Draw a green line from the top-left corner of our canvas to the bottom_rigth
    draw_line(canvas, (0,0), (300,300), "green")

    # Draw a 3 pixel thick red line from the top right corner to the bottom left
    draw_line(canvas, (300,0), (0,300), "red", 3)

    # Draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
    draw_rectangle(canvas, (10,10), (60,60), "green")

    # Draw another rectangle, this one red with 5 pixel thickness
    draw_rectangle(canvas, (50,200), (200,225), "red", 5)

    # Draw a final rectangle (blue and filled in)
    draw_rectangle(canvas, (200,50), (225,125), "blue", -1)

    # Re-Initialize canvas as an empty array, then compute the center
    canvas = np.zeros((300,300,3), dtype="uint8")
    centerX, centerY = canvas.shape[1] // 2, canvas.shape[0] // 2

    # Loop over increasing radio, from 25 pixels to 150 pixels in 25 pixel increments
    for r in range(0, 175, 25):
        # Draw a white circle with the current radius size
        cv2.circle(canvas, (centerX, centerY), r, colors["white"])
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

    # Re-Initialize canvas as an empty array, again
    canvas = np.zeros((300,300,3), dtype="uint8")

    for _ in range(25):
        """
        Randomly generate a radius size between 5 and 200, generate a
        random color. and then pick a random point on our canvas where
        the cricule will be drawn.
        """
        radius = np.random.randint(low=5, high=200)
        color = np.random.randint(low=0, high=256, size=(3,)).tolist()
        pt = np.random.randint(low=0, high=300, size=(2,))

        # Draw random circle on the canvas
        cv2.circle(canvas, tuple(pt), radius, color, 1)

    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)