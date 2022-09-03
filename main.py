# Implementation of matplotlib function
import numpy as np
from PIL import Image, ImageShow
from skimage import filters, exposure
  
# Transformação de intensidade
def intensity():
  city_image = Image.open('images/city.png')
  city_image = np.array(city_image)
  negative_image = np.invert(city_image)
  negative_image = Image.fromarray(negative_image)
  negative_image.save('results/intensity01.png')

  tranf_img = Image.open('images/city.png')
  tranf_img = np.array(tranf_img)
  tranf_img = ((tranf_img / 255) * 100) + 100
  print(tranf_img > 200)
  tranf_img = Image.fromarray(tranf_img.astype(np.uint8))
  tranf_img.save('results/intensity02.png')

  odd_invert = Image.open('images/city.png')
  odd_invert = np.array(odd_invert)
  odd_invert[::2] = np.fliplr(odd_invert[::2])
  odd_invert = Image.fromarray(odd_invert)
  odd_invert.save('results/intensity03.png')

  half_img = Image.open('images/city.png')
  half_img = np.array(half_img)
  size = int(len(half_img)/2)
  up_half_img = half_img[:size]
  up_half_img = np.flipud(up_half_img)

  half_img[size:] = up_half_img
  half_img = Image.fromarray(half_img)
  half_img.save('results/intensity04.png')

  mirror_img = Image.open('images/city.png') 
  mirror_img = np.flipud(mirror_img)
  mirror_img = Image.fromarray(mirror_img)
  mirror_img.save('results/intensity05.png')

# Ajuste de brilho
def brightness():
  baboon_image = Image.open('images/baboon.png')
  baboon_image = np.array(baboon_image)
  baboon_image = (baboon_image/255) ** (1/1.5)
  baboon_image = baboon_image * 255
  baboon_image = Image.fromarray(baboon_image.astype(np.uint8))
  baboon_image.save('results/brightness01.png')

# Planos de bits
def bits_plan():
  baboon_image = Image.open('images/baboon.png')
  baboon_image = np.array(baboon_image)
  baboon_image = (baboon_image % 2) * 255
  baboon_image = Image.fromarray(baboon_image.astype(np.uint8))
  baboon_image.save('results/bits_plan01.png')

# Mosaico
def mosaic():
  baboon_image = Image.open('images/baboon.png')

# Combinação de imagens 
def image_combinator():
  baboon_image = Image.open('images/baboon.png')
  butterfly_image = Image.open('images/butterfly.png')

def image_filter():
  baboon_image = Image.open('images/baboon.png')

bits_plan()
intensity()
brightness()