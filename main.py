# Implementation of matplotlib function
import numpy as np
from PIL import Image, ImageShow
import matplotlib.pyplot as plt
from skimage import filters, exposure
  
# image = plt.imread('images/city.png')

# fig, ax = plt.subplots()
# ax.imshow(image)
# ax.axis('off')
  
# plt.title('matplotlib.pyplot.imread() function Example', fontweight ="bold")
# plt.show()

# Transformação de intensidade
def intensity():
  city_image = Image.open('images/city.png')
  city_image = np.array(city_image)
  negative_image = np.invert(city_image)
  negative_image = Image.fromarray(negative_image)
  negative_image.save('results/intensity01.png')

  odd_invert = Image.open('images/city.png')
  odd_invert = np.array(odd_invert)
  odd_invert[::2] = np.fliplr(odd_invert[::2])
  odd_invert = Image.fromarray(odd_invert)
  odd_invert.save('results/intensity03.png')
  
  mirror_img = Image.open('images/city.png') 
  mirror_img = np.flipud(mirror_img)
  mirror_img = Image.fromarray(mirror_img)
  mirror_img.save('results/intensity05.png')

# Ajuste de brilho
def brightness():
  baboon_image = Image.open('images/baboon.png')

# Planos de bits
def bits_plan():
  baboon_image = Image.open('images/baboon.png')

# Mosaico
def mosaic():
  baboon_image = Image.open('images/baboon.png')

# Combinação de imagens 
def image_combinator():
  baboon_image = Image.open('images/baboon.png')
  butterfly_image = Image.open('images/butterfly.png')


intensity()