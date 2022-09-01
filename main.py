# Implementation of matplotlib function
import numpy as np
from PIL import Image as img, ImageShow
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
  city_image = img.open('images/city.png')
  negative_image = np.invert(city_image)
  negative_image = img.fromarray(negative_image)
  negative_image.save('results/intensity01.png')

# Ajuste de brilho
def brightness():
  baboon_image = plt.imread('images/baboon.png')

# Planos de bits
def bits_plan():
  baboon_image = plt.imread('images/baboon.png')

# Mosaico
def mosaic():
  baboon_image = plt.imread('images/baboon.png')

# Combinação de imagens 
def image_combinator():
  baboon_image = plt.imread('images/baboon.png')
  butterfly_image = plt.imread('images/butterfly.png')


intensity()