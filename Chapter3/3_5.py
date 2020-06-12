import numpy as np
from skimage.io import imread, imsave
from skimage.util import random_noise

# 3.5.1
def mean_filter(image, filterSize=3):
	w, h = image.shape
	result = np.ones((w, h))
	for x in range(w):
		for y in range(h):
			x_start = x - int(filterSize/2)
			y_start = y - int(filterSize/2)
			pixel = []

			for i in range(x_start, x_start + filterSize):
				for j in range(y_start, y_start + filterSize):
					if i < 0 or j < 0 or i >= w or j >= h:
						pass
					else :
						pixel.append(image[i][j])
			result[x][y] = sum(pixel) / len(pixel)
	return result

# 3.5.2
def middle_filter(image, filterSize = 5):
	w, h = image.shape
	result = np.ones((w, h))
	for x in range(w):
		for y in range(h):
			x_start = x - int(filterSize/2)
			y_start = y - int(filterSize/2)
			pixel = []

			for i in range(x_start, x_start + filterSize):
				for j in range(y_start, y_start + filterSize):
					if i < 0 or j < 0 or i >= w or j >= h:
						pass
					else :
						pixel.append(image[i][j])
			pixel = sorted(pixel)
			result[x][y] = pixel[int(len(pixel) / 2)]
	return result

if __name__ == '__main__':
	image = imread("gray.png")

	mean_filtered = mean_filter(image)
	imsave("mean_filtered.png", mean_filtered)

	middle_filtered = middle_filter(image)
	imsave("middle_filtered.png", middle_filtered)

	# add salt and pepper noise
	noise = random_noise(image, mode="s&p")
	denoise = middle_filter(noise)
	imsave("noise.png", noise)
	imsave("denoise.png", denoise)
