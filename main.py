import random
import numpy as np
from PIL import Image, ImageShow
from scipy import ndimage


# Transformação de intensidade
def intensity(op=1):
  if (op == 1):
    city_image = Image.open('images/city.png')
    city_image = np.array(city_image)
    negative_image = np.invert(city_image)
    negative_image = Image.fromarray(negative_image)
    negative_image.save('results/intensity.png')
  elif op == 2:
    tranf_img = Image.open('images/city.png')
    tranf_img = np.array(tranf_img)
    tranf_img = np.interp(tranf_img, (0, 255), (100, 200))
    tranf_img = Image.fromarray(tranf_img.astype(np.uint8))
    tranf_img.save('results/intensity.png')
  elif op == 3:  
    odd_invert = Image.open('images/city.png')
    odd_invert = np.array(odd_invert)
    odd_invert[::2] = np.fliplr(odd_invert[::2])
    odd_invert = Image.fromarray(odd_invert)
    odd_invert.save('results/intensity.png')
  elif op == 4:
    half_img = Image.open('images/city.png')
    half_img = np.array(half_img)
    size = int(len(half_img)/2)
    up_half_img = half_img[:size]
    up_half_img = np.flipud(up_half_img)

    half_img[size:] = up_half_img
    half_img = Image.fromarray(half_img)
    half_img.save('results/intensity.png')
  elif op == 5:
    mirror_img = Image.open('images/city.png') 
    mirror_img = np.flipud(mirror_img)
    mirror_img = Image.fromarray(mirror_img)
    mirror_img.save('results/intensity.png')

# Ajuste de brilho
def brightness(y):
  baboon_image = Image.open('images/baboon.png')
  baboon_image = np.array(baboon_image)
  baboon_image = (baboon_image/255) ** (1/y)
  baboon_image = baboon_image * 255
  baboon_image = Image.fromarray(baboon_image.astype(np.uint8))
  baboon_image.save('results/brightness.png')

# Planos de bits
def bits_plan(bit):
  baboon_image = Image.open('images/baboon.png')
  baboon_image = np.array(baboon_image)
  baboon_image = ((baboon_image >> bit) & 1) * 255
  baboon_image = Image.fromarray(baboon_image.astype(np.uint8))
  baboon_image.save('results/bits_plan.png')
  
def mosaic_chunks(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

# Mosaico
def mosaic():
  baboon_image = Image.open('images/baboon.png')
  baboon_image = np.array(baboon_image)

  n_divisions = 4
  sequence = np.arange(n_divisions ** 2)
  height, width = baboon_image.shape
  random.shuffle(sequence)

  block_list = []
  block_height = int(height / n_divisions)
  block_width = int(width / n_divisions)

  for block in sequence:
      line = block % n_divisions
      column = int(block / n_divisions)
      
      block_list.append(baboon_image[
              (line * block_height) : ((line * block_height) + block_height),
              (column * block_width) : ((column * block_width) + block_width)
          ])

  imgs_lines_gen = [np.array(i) for i in mosaic_chunks(block_list, n_divisions)]
  mosaic_img = np.concatenate(np.concatenate(imgs_lines_gen, axis=1), axis=1)

  mosaic_img = Image.fromarray(mosaic_img.astype(np.uint8))
  mosaic_img.save('results/mosaic.png')


# Combinação de imagens 
def image_combinator(a=0.5, b=0.5):
  baboon_image = Image.open('images/baboon.png')
  baboon_image = np.array(baboon_image)

  butterfly_image = Image.open('images/butterfly.png')
  butterfly_image = np.array(butterfly_image)

  img_combination = baboon_image * a + butterfly_image * b
  img_combination = Image.fromarray(img_combination.astype(np.uint8))
  img_combination.save('results/combination.png')


def image_filter(filter='h1'):
  baboon_image = Image.open('images/baboon.png')
  baboon_image = np.array(baboon_image, dtype=np.float64)
  filter_array = np.array([])
  
  if(filter == 'h1'):
    # h1
    filter_array = np.array([
      [0, 0, -1, 0, 0],
      [0, -1, -2, -1, 0],
      [-1, -2, -16, -2, -1],
      [0, -1, -2, -1, 0],
      [0, 0, -1, 0, 0]
    ])

  if(filter == 'h2'):
    # h2
    filter_array = (1/256) * np.array([
      [1, 4, 6, 4, 1],
      [4, 16, 24, 16, 4],
      [6, 24, 36, 24, 6],
      [4, 16, 24, 16, 4],
      [1, 4, 6, 4, 1]
    ])
  
  if(filter == 'h3'):
    # h3
    filter_array = np.array([
      [-1, 0, 1], 
      [-2, 0, 2],
      [-1, 0, 1]
    ])
  
  if(filter == 'h4'):
    # h4
    filter_array = np.array([
      [-1, 2, 1], 
      [0, 0, 0], 
      [1, 2, 1]
    ])
  
  if(filter == 'h5'):
    # h5
    filter_array = np.array([
      [-1, -1, -1], 
      [-1, 8, -1], 
      [-1, -1, -1]
    ])
  
  if(filter == 'h6'):
    # h6
    filter_array = (1/9) * np.array([
      [1, 1, 1], 
      [1, 1, 1], 
      [1, 1, 1]
    ])
  
  if(filter == 'h7'):
    # h7
    filter_array = np.array([
      [-1, -1, 2], 
      [-1, 2, -1], 
      [2, -1, -1]
    ])
  
  if(filter == 'h8'):
    # h8
    filter_array = np.array([
      [2, -1, -1,],
      [-1, 2, -1],
      [-1, -1, 2]
    ])
  
  if(filter == 'h9'):
    # h9
    filter_array = (1/9) * np.array([
      [1,0,0,0,0,0,0,0,0], 
      [0,1,0,0,0,0,0,0,0], 
      [0,0,1,0,0,0,0,0,0], 
      [0,0,0,1,0,0,0,0,0], 
      [0,0,0,0,1,0,0,0,0], 
      [0,0,0,0,0,1,0,0,0], 
      [0,0,0,0,0,0,1,0,0], 
      [0,0,0,0,0,0,0,1,0], 
      [0,0,0,0,0,0,0,0,1]
    ])
  
  if(filter == 'h10'):
    # h10
    filter_array = (1/8) * np.array([
      [-1, -1, -1, -1, -1], 
      [-1, 2, 2, 2, -1], 
      [-1, 2, 8, 2, -1], 
      [-1, 2, 2, 2, -1], 
      [-1, -1, -1, -1, -1]
    ])
  
  if(filter == 'h11'):
    # h11
    filter_array = np.array([
      [-1, -1, 0],
      [-1, 0, 1], 
      [0, 1, 1]
    ])

  if(filter == 'h3+h4'):
    # h3 + h4
    filter_array = (np.array([
      [-1, 0, 1], 
      [-2, 0, 2], 
      [-1, 0, 1]]
    ) ** 2 + np.array([
      [-1, 2, 1], 
      [0, 0, 0], 
      [1, 2, 1]
    ]) ** 2) ** (1/2)
  
  filter_img = ndimage.convolve(baboon_image, filter_array)
  filter_img = ((filter_img - filter_img.min()) * (255 / (filter_img.max() - filter_img.min())))
  filter_img = Image.fromarray(filter_img.astype(np.uint8))
  filter_img.save('results/filter_img.png')


def main():
  intensity(1) 
  bits_plan(7)
  brightness(3.5)
  mosaic()
  image_combinator()
  image_filter('h3+h4')

main()