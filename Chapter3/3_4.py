import numpy as np
from skimage.io import imread, imsave

# 3.4.2
def correlation(image, kernel):
	h, w = image.shape
	kh, kw = kernel.shape
	kh //= 2
	kw //= 2
	res = np.ones(image.shape)
	for i in range(h):
		for j in range(w):
			temp_sum = 0
			for ki in range(-kh, kh + 1):
				for kj in range(-kw, kw + 1):
					if ki + i >= 0 and kj + j >= 0 and ki + i < h and kj + j < w:
						temp_sum += kernel[ki + kh, kj + kw] * image[ki + i, kj + j]
			res[i, j] = temp_sum
	return res 

def filter(image, kernel):
	kernel = np.rot90(kernel, 2)
	return correlation(image, kernel)

# 3.4.4
def smooth(image):
	kernel = np.ones((3, 3)) / 9.0
	return correlation(image, kernel)

if __name__ == '__main__':
	image = imread("gray.png")

	kernel = np.ones((3,3))
	correlationed = correlation(image, kernel)

	filtered = filter(image, kernel)

	smoothed = smooth(image)
	# imsave("smoothed.png", smoothed)