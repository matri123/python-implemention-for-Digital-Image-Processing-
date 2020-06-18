import numpy as np
from skimage.io import imread, imsave
from skimage.util import random_noise

# 5.2.2
def Guassion_noise(image, sigma=0.01):
	return image + sigma * np.random.normal(size=image.shape)

def Rayleigh_noise(image, scale=0.1):
	return image + np.random.rayleigh(scale=scale, size=image.shape)

def Gamma_noise(image, scale=0.1):
	return image + np.random.gamma(shape=2, scale=scale, size=image.shape)

def Exp_noise(image, scale=0.05):
	return image + np.random.exponential(scale=scale, size=image.shape)

def Uniform_noise(image):
	return image + np.random.uniform(low=0, high=0.1, size=image.shape)

def SaltPepper_noise(image):
	return image + random_noise(image, mode="s&p")

if __name__ == '__main__':
	image = imread("gray.png")

	Guassion_noised = Guassion_noise(image / 255.0, 0.05)
	# imsave("Guassion_noised.png", Guassion_noised)

	Rayleigh_noised = Rayleigh_noise(image / 255.0)
	# imsave("Rayleigh_noised.png", Rayleigh_noised)

	Gamma_noised = Gamma_noise(image / 255.0)
	# imsave("Gamma_noised.png", Gamma_noised)

	Exp_noised = Exp_noise(image / 255.0)
	# imsave("Exp_noised.png", Exp_noised)

	Uniform_noised = Uniform_noise(image / 255.0)
	# imsave("Uniform_noised.png", Uniform_noised)

	SaltPepper_noised = SaltPepper_noise(image / 255.0)
	# imsave("SaltPepper_noised.png", SaltPepper_noised)