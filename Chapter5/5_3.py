import numpy as np
from skimage.io import imread, imsave
from skimage.util import random_noise

def Guassion_noise(image, sigma=0.01):
	return image + sigma * np.random.normal(size=image.shape)

def SaltPepper_noise(image):
	return image + random_noise(image, mode="s&p")

# 5.3.1
def Arithmetic_mean_filtering(image, filterSize=3):
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

def Geometric_mean_filtering(image, filterSize=3):
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
			# print(pixel)
			# print(np.prod(pixel))
			result[x][y] = np.power(np.prod(pixel), 1/len(pixel))
	return result

def Harmonic_mean_filtering(image, filterSize=3):
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
						pixel.append(1 / image[i][j])
			result[x][y] = len(pixel) / sum(pixel)
	return result

# 5.3.2
def middle_filter(image, filterSize=3):
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

def max_filter(image, filterSize=3):
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
			result[x][y] = max(pixel)
	return result

def min_filter(image, filterSize=3):
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
			result[x][y] = min(pixel)
	return result

def middle_value_filter(image, filterSize=3):
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
			result[x][y] = (max(pixel) + min(pixel)) / 2
	return result

def alpha_mean_filtering(image, filterSize=3, d=2):
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
			if len(pixel) > 2 * d:
				pixel = pixel[d:-d]
			result[x][y] = sum(pixel) / len(pixel)
	return result

# 5.3.3
def Adaptive_local_denoise(image, var=0.01, filterSize=3):
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
			result[x][y] = image[x][y] - var / np.var(pixel) * (image[x][y] - np.mean(pixel))
	return result


if __name__ == '__main__':
	image = imread("gray.png")

	Guassion_noised = Guassion_noise(image / 255.0, 0.01)
	Arithmetic_mean_denosied = Arithmetic_mean_filtering(Guassion_noised)
	# imsave("Arithmetic_mean_denosied.png", Arithmetic_mean_denosied)

	Geometric_mean_denoised = Geometric_mean_filtering(Guassion_noised)
	# imsave("Geometric_mean_denoised.png", Geometric_mean_denoised)


	SaltPepper_noised = SaltPepper_noise(image / 255.0)
	# imsave("SaltPepper_noised.png", SaltPepper_noised)
	Harmonic_mean_denoised = Harmonic_mean_filtering(SaltPepper_noised)
	# imsave("Harmonic_mean_denoised.png", Harmonic_mean_denoised)

	middle_filtered = middle_filter(Guassion_noised)
	# imsave("middle_filtered.png", middle_filtered)

	max_filtered = max_filter(Guassion_noised)
	# imsave("max_filtered.png", max_filtered)

	min_filtered = min_filter(Guassion_noised)
	# imsave("min_filtered.png", min_filtered)

	middle_value_filtered = middle_value_filter(Guassion_noised)
	# imsave("middle_value_filtered.png", middle_value_filtered)

	alpha_mean_filtered = alpha_mean_filtering(Guassion_noised)
	# imsave("alpha_mean_filtered.png", alpha_mean_filtered)

	Adaptive_local_denoised = Adaptive_local_denoise(Guassion_noised, 0.01, 5)
	# imsave("Adaptive_local_denoised.png", Adaptive_local_denoised)

