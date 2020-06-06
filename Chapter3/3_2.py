import numpy as np

from skimage.io import imread, imsave

# 3.2.1
def image_reversal(image):
	image = 255 - 1 - image
	return image

# 3.2.2 Logarithmic transformation
# s = c * log(1 + r)
def log_trans(image, c=255/np.log(256)):
	image = c * np.log(1 + image)
	return image

# 3.2.3 Gamma transformation
# s = c * r ^ gamma
def gamma_trans(image, gamma, c = 1):
	image = c * np.power(image, gamma)
	return image

# 3.2.4
# Contrast stretch
def contrast_stretch(image, point1, point2):
	w, h = image.shape

	def left(x):
		k = point1[1] / point1[0]
		ans = k * x
		return ans
	def middle(x):
		k = (point2[1] - point1[1]) / (point2[0] - point1[0])
		y = k * x + point1[1] - k * point1[0]
		return y
	def right(x):
		k = (1 - point2[1]) / (1 - point2[0])
		y = k * x + 1 - k
		return y

	if point1[0] == 0 and point2[0] == 1:
		for i in range(w):
			for j in range(h):
				image[i][j] = middle(image[i][j])
	elif point1[0] == 0:
		for i in range(w):
			for j in range(h):
				if image[i][j] < point2[0]:
					image[i][j] = middle(image[i][j])
				else:
					image[i][j] = right(image[i][j])
	elif point2[0] == 1:
		for i in range(w):
			for j in range(h):
				if image[i][j] < point1[0]:
					image[i][j] = left(image[i][j])
				else:
					image[i][j] = middle(image[i][j])
	elif point1[0] == point2[0]:
		for i in range(w):
			for j in range(h):
				if image[i][j] < point1[0]:
					image[i][j] = left(image[i][j])
				else:
					image[i][j] = right(image[i][j])
	else :
		for i in range(w):
			for j in range(h):
				if image[i][j] < point1[0]:
					image[i][j] = left(image[i][j])
				elif image[i][j] < point2[0]:
					image[i][j] = middle(image[i][j])
				else:
					image[i][j] = right(image[i][j])
	return image

# Gray scale layering
def gray_scale_layering(image, left, right, value):
	w, h = image.shape
	for i in range(w):
		for j in range(h):
			if left <= image[i][j] and image[i][j] <= right:
				image[i][j] = value
	return image

# Bit plane layering
# 0 <= bit <= 7
def bit_plane_layering(image, bit):
	w, h = image.shape
	for i in range(w):
		for j in range(h):
			image[i][j] = 1 if image[i][j] & 1 << bit else 0
	return image


if __name__ == '__main__':
	image = imread("gray.png")

	image_reversed = image_reversal(image)
	# imsave("image_reversed.png", image_reversed)

	log_transed = log_trans(image).astype(np.uint8)
	# imsave("log_transed.png", log_transed)

	gamma_transed = gamma_trans(image / 255, 0.5)
	# imsave("gamma_transed.png", gamma_transed)

	stretch = contrast_stretch(image / 255, (0.1, 0.2), (0.9, 0.8))
	# imsave("stretch.png", stretch)

	gray_layered = gray_scale_layering(image / 255, 0.4, 0.6, 0)
	# imsave("gray_layered.png", gray_layered)

	bit_layered = bit_plane_layering(image, 7)
	# imsave("bit_layered.png", bit_layered * 255)

