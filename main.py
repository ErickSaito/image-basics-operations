import random
import numpy as np
from PIL import Image
from scipy import ndimage
import inquirer


# Transformação de intensidade
def intensity(img, op='Negativo da imagem', output_path='results/intensity.png'):
  if intensity_choise == 'Negativo da imagem':
    img = np.invert(img)
  elif intensity_choise == 'Imagem transformada':
    img = np.interp(img, (0, 255), (100, 200))
  elif intensity_choise == 'Linhas pares invertidas':
    img[::2] = np.fliplr(img[::2])
  elif intensity_choise == 'Reflexao de linhas':
    size = int(len(img)/2)
    up_img = img[:size]
    up_img = np.flipud(up_img)
    img[size:] = up_img  
  elif intensity_choise == 'Espelhamento vertical':
    img = np.flipud(img)

  img = Image.fromarray(img.astype(np.uint8))
  img.save(output_path)

# Ajuste de brilho
def brightness(img, y=1.5, output_path='results/brightness.png'):
  img = (img/255) ** (1/y)
  img = img * 255
  img = Image.fromarray(img.astype(np.uint8))
  img.save(output_path)

# Planos de bits
def bits_plan(img, bit=1, output_path='results/bits_plan.png'):
  img = ((img >> bit) & 1) * 255
  img = Image.fromarray(img.astype(np.uint8))
  img.save(output_path)
  
def mosaic_chunks(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

# Mosaico
def mosaic(img, output_path='results/mosaic.png'):
  n_divisions = 4
  sequence = np.arange(n_divisions ** 2)
  height, width = img.shape
  random.shuffle(sequence)

  block_list = []
  block_height = int(height / n_divisions)
  block_width = int(width / n_divisions)

  for block in sequence:
      line = block % n_divisions
      column = int(block / n_divisions)
      
      block_list.append(img[
              (line * block_height) : ((line * block_height) + block_height),
              (column * block_width) : ((column * block_width) + block_width)
          ])

  imgs_lines_gen = [np.array(i) for i in mosaic_chunks(block_list, n_divisions)]
  mosaic_img = np.concatenate(np.concatenate(imgs_lines_gen, axis=1), axis=1)

  mosaic_img = Image.fromarray(mosaic_img.astype(np.uint8))
  mosaic_img.save(output_path)


# Combinação de imagens 
def image_combinator(img_a, img_b, a=0.5, b=0.5, output_path='results/combination.png'):
  if a + b > 1:
    print('A soma dos pesos deve ser menor ou igual a 1')
  else:
    img_combination = img_a * a + img_b * b
    img_combination = Image.fromarray(img_combination.astype(np.uint8))
    img_combination.save(output_path)


def image_filter(img, filter='h1', output_path='results/filter_img.png'):
  filter_array = np.array([])
  
  if filter == 'h1':
    # h1
    filter_array = np.array([
      [0, 0, -1, 0, 0],
      [0, -1, -2, -1, 0],
      [-1, -2, -16, -2, -1],
      [0, -1, -2, -1, 0],
      [0, 0, -1, 0, 0]
    ])

  if filter == 'h2':
    # h2
    filter_array = (1/256) * np.array([
      [1, 4, 6, 4, 1],
      [4, 16, 24, 16, 4],
      [6, 24, 36, 24, 6],
      [4, 16, 24, 16, 4],
      [1, 4, 6, 4, 1]
    ])
  
  if filter == 'h3':
    # h3
    filter_array = np.array([
      [-1, 0, 1], 
      [-2, 0, 2],
      [-1, 0, 1]
    ])
  
  if filter == 'h4':
    # h4
    filter_array = np.array([
      [-1, 2, 1], 
      [0, 0, 0], 
      [1, 2, 1]
    ])
  
  if filter == 'h5':
    # h5
    filter_array = np.array([
      [-1, -1, -1], 
      [-1, 8, -1], 
      [-1, -1, -1]
    ])
  
  if filter == 'h6':
    # h6
    filter_array = (1/9) * np.array([
      [1, 1, 1], 
      [1, 1, 1], 
      [1, 1, 1]
    ])
  
  if filter == 'h7':
    # h7
    filter_array = np.array([
      [-1, -1, 2], 
      [-1, 2, -1], 
      [2, -1, -1]
    ])
  
  if filter == 'h8':
    # h8
    filter_array = np.array([
      [2, -1, -1,],
      [-1, 2, -1],
      [-1, -1, 2]
    ])
  
  if filter == 'h9':
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
  
  if filter == 'h10':
    # h10
    filter_array = (1/8) * np.array([
      [-1, -1, -1, -1, -1], 
      [-1, 2, 2, 2, -1], 
      [-1, 2, 8, 2, -1], 
      [-1, 2, 2, 2, -1], 
      [-1, -1, -1, -1, -1]
    ])
  
  if filter == 'h11':
    # h11
    filter_array = np.array([
      [-1, -1, 0],
      [-1, 0, 1], 
      [0, 1, 1]
    ])

  if filter == 'h3+h4':
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
  
  filter_img = ndimage.convolve(img, filter_array)
  filter_img = ((filter_img - filter_img.min()) * (255 / (filter_img.max() - filter_img.min())))
  filter_img = Image.fromarray(filter_img.astype(np.uint8))
  filter_img.save(output_path)


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


print("MC920 - Introdução ao Processamento de Imagem Digital - Trabalho 1")
print("Feito por Erick Saito")
print("Todas as imagens processadas serão salvas na pasta /results")

while(True): 
  print()
  image_path = inquirer.list_input("Escolha a imagem que deseja realizar o filtro:",
                                choices=['baboon.png', 'butterfly.png', 'city.png'])
  img = Image.open(f'images/{image_path}')
  img = np.array(img)

  process_choise = inquirer.list_input("Qual processamento deseja aplicar na imagem?",
                                choices=['Transformação de Intensidade', 'Ajuste de Brilho', 'Planos de bits', 'Mosaico', 'Combinação de Imagens', 'Filtragem de Imagens'])

  if process_choise == 'Transformação de Intensidade':
    intensity_choise = inquirer.list_input("Qual transformação deseja realizar?",
                                choices=['Negativo da imagem', 'Imagem transformada', 'Linhas pares invertidas', 'Reflexao de linhas', 'Espelhamento vertical'])
    intensity(img=img, op=intensity_choise) 

  elif process_choise == 'Ajuste de Brilho':
    gamma = inquirer.text(message="Qual o valor Gamma gostaria de aplicar na imagem?")
    if not is_float(gamma):
      print('Este valor não é numérico')
    else:
      gamma = float(gamma)
      brightness(img=img, y=gamma)

  elif process_choise == 'Planos de bits':
    bit = inquirer.text(message="Qual bit deseja exibir o plano?")
    if not bit.isnumeric():
      print('Este valor não é numérico')
    else:
      bits_plan(img=img, bit=int(bit))

  elif process_choise == 'Mosaico':
    mosaic(img=img)
  elif process_choise == 'Combinação de Imagens':
    image_path_b = inquirer.list_input("Escolha a segunda imagem que irá mesclar",
                                choices=['baboon.png', 'butterfly.png', 'city.png'])
    img_b = Image.open(f'images/{image_path_b}')
    img_b = np.array(img_b)

    weight_a = inquirer.text(message='Qual o peso para a imagem A?')
    weight_b = inquirer.text(message='Qual o peso para a imagem B?')

    if not is_float(weight_a) or not is_float(weight_b):
      print('Algum dos valores não é numérico')
    else:
      image_combinator(img=img, img_b=img_b, a=float(weight_a), b=float(weight_b))
    
  elif process_choise == 'Filtragem de Imagens':
    filter_img = inquirer.list_input("Qual filtro deseja aplicar?",
                            choices=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h3+h4'])
    image_filter(img=img, filter=filter_img)
    

  redo_process = inquirer.confirm('Fazer outro processamento?', default=False)

  if not redo_process:
    break