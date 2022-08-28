# OpenCV Basics

## 04. Translation

Translating (shifting) and image is given by Numpy matrix in the form:

```python
[
    [1, 0, shiftX],
    [0, 1, shiftY],
]
```
You simply need to specify how many pixels you want to shift the image in the X and Y direction.

Let's translate the image 25 pixels to the right and 50 pixels down.

```python
M = np.float32([[1, 0, 25], [0, 1, 50]])
```