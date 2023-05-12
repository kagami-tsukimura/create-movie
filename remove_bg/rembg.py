#!/usr/bin/env python
# coding: utf-8

# In[2]:


from google.colab import drive
drive.mount('/content/drive')
get_ipython().run_line_magic('cd', './drive/MyDrive')


# In[3]:


get_ipython().system('pip install rembg')


# In[4]:


import os
from glob import glob

from rembg import remove
import cv2


# In[5]:


INPUT = './input/overlay'
OUTPUT = './output/overlay'
IN_BLUR = f'{INPUT}/Blur'
OUT_BLUR = f'{OUTPUT}/Blur'


# In[27]:


# outputディレクトリの作成
os.makedirs(OUTPUT, exist_ok=True)


# In[31]:


# Blurディレクトリの作成
os.makedirs(IN_BLUR, exist_ok=True)
os.makedirs(OUT_BLUR, exist_ok=True)


# In[7]:


input_path = glob(f'{INPUT}/*')
print(input_path)


# In[8]:


# outputディレクトリの中身作成
for input in input_path:
  output = input.replace(INPUT,OUTPUT)
  os.makedirs(output, exist_ok=True)
  print(output)


# In[17]:


imgs = glob(f'{INPUT}/*/*')
print(imgs)


# In[32]:


img_blurs = glob(f'{IN_BLUR}/*')
print(img_blurs)


# In[35]:


for img in imgs:
  input_img = cv2.imread(img)
  output_img = remove(input_img)
  cv2.imwrite(img.replace(INPUT,OUTPUT).replace('jpg', 'png').replace('jpeg', 'png'), output_img)


# In[ ]:


for img in img_blurs:
  input_img = cv2.imread(img)
  output_img = remove(input_img)
  cv2.imwrite(img.replace(IN_BLUR,OUT_BLUR).replace('jpg', 'png').replace('jpeg', 'png'), output_img)


# In[6]:


from matplotlib import pyplot as plt


imgs = glob(f'{OUTPUT}/ペンギン/*.png')

for img in imgs:
  img = cv2.imread(img)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  plt.imshow(img)
  plt.show()


# In[20]:





# In[24]:


# Gaussian Blur
imgs = glob(f'{IN_BLUR}/*')
for i, img in enumerate(imgs):
  input_img = cv2.imread(img)
  img_blur = cv2.GaussianBlur(input_img,     # 入力画像
                               (9,9),    # カーネルの縦幅・横幅
                                10,10        # 横方向の標準偏差（0を指定すると、カーネルサイズから自動計算）
                            )
  cv2.imwrite(f'{IN_BLUR}/{i}.png', img_blur)


# In[25]:


from matplotlib import pyplot as plt


imgs = glob(f'{INPUT}/Blur/*.png')

for img in imgs:
  img = cv2.imread(img)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  plt.imshow(img)
  plt.show()


# In[36]:


from matplotlib import pyplot as plt


imgs = glob(f'{OUTPUT}/Blur/*.png')

for img in imgs:
  img = cv2.imread(img)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  plt.imshow(img)
  plt.show()

