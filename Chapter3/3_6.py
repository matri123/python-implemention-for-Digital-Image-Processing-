import numpy as np
from skimage.io import imread, imsave
from scipy.signal import convolve2d

# 3.6.1
def first_order_sharpening(image):
	h, w = image.shape
	ans = np.zeros((h, w))
	for i in range(h):
		for j in range(w - 1):
			ans[i][j] = image[i][j + 1] - image[i][j]
	ans = np.clip(ans, 0, 255)
	return ans

def second_order_sharpening(image):
	h, w = image.shape
	ans = np.zeros((h, w))
	for i in range(h):
		for j in range(1, w - 1):
			ans[i][j] = image[i][j + 1] + image[i][j - 1] - 2 * image[i][j]
	ans = np.clip(ans, 0, 255)
	return ans

# 3.6.2 Second order differential
def laplace_operator(image):
	kernel1 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
	kernel2 = np.array([[1,1,1],[1,-8,1],[1,1,1]])
	kernel3 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
	kernel4 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
	ans = convolve2d(image, kernel4, mode='same')
	return ans

# 3.6.3
def unsharp_masking(image, mask, k=1):
	return image + k * mask

# 3.6.4 First order differential
def image_gradient(image):
	kernel1 = np.array([[-1,0],[0,1]])
	kernel2 = np.array([[0,-1],[1,0]])
	kernel3 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
	kernel4 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
	ans = convolve2d(image, kernel2, mode='same')
	return ans

if __name__ == '__main__':
	image = imread("gray.png")

	first_order = first_order_sharpening(image)
	# imsave("first_order.png", first_order)

	second_order = second_order_sharpening(image)
	# imsave("second_order.png", second_order)

	laplaced = laplace_operator(image)
	# imsave("laplaced.png", laplaced)

	masking = unsharp_masking(image, laplaced, k = 0.1)
	# imsave("masking.png", masking)

	gradient = image_gradient(image)
	# imsave("gradient.png", gradient)

