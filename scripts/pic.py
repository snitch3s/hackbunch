#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image, ImageFilter, ImageFont, ImageDraw
import requests


# In[2]:


avatarLinkList = ['https://avatars1.githubusercontent.com/u/52825668?v=4', 'https://avatars2.githubusercontent.com/u/25265451?v=4', 'https://avatars2.githubusercontent.com/u/43813386?v=4', 'https://avatars0.githubusercontent.com/u/43090559?v=4', 'https://avatars0.githubusercontent.com/u/21276922?v=4', 'https://avatars0.githubusercontent.com/u/20596763?v=4', 'https://avatars2.githubusercontent.com/u/43813629?v=4', 'https://avatars2.githubusercontent.com/u/21018149?v=4', 'https://avatars0.githubusercontent.com/u/30266744?v=4', 'https://avatars2.githubusercontent.com/u/43827236?v=4', 'https://avatars1.githubusercontent.com/u/45566277?v=4', 'https://avatars0.githubusercontent.com/u/52889867?v=4', 'https://avatars1.githubusercontent.com/u/41968785?v=4', 'https://avatars3.githubusercontent.com/u/43822585?v=4', 'https://avatars0.githubusercontent.com/u/52251306?v=4', 'https://avatars2.githubusercontent.com/u/52925407?v=4', 'https://avatars0.githubusercontent.com/u/43814992?v=4', 'https://avatars0.githubusercontent.com/u/32199592?v=4', 'https://avatars2.githubusercontent.com/u/20839661?v=4', 'https://avatars0.githubusercontent.com/u/32136294?v=4', 'https://avatars1.githubusercontent.com/u/48018942?v=4', 'https://avatars2.githubusercontent.com/u/43813630?v=4', 'https://avatars1.githubusercontent.com/u/44905238?v=4', 'https://avatars3.githubusercontent.com/u/41850468?v=4', 'https://avatars0.githubusercontent.com/u/40494926?v=4', 'https://avatars2.githubusercontent.com/u/32234113?v=4', 'https://avatars3.githubusercontent.com/u/43813624?v=4', 'https://avatars3.githubusercontent.com/u/20722967?v=4', 'https://avatars3.githubusercontent.com/u/50765423?v=4', 'https://avatars0.githubusercontent.com/u/43849008?v=4', 'https://avatars0.githubusercontent.com/u/23553776?v=4', 'https://avatars0.githubusercontent.com/u/43813460?v=4', 'https://avatars2.githubusercontent.com/u/40348358?v=4', 'https://avatars2.githubusercontent.com/u/42376739?v=4', 'https://avatars3.githubusercontent.com/u/43094266?v=4', 'https://avatars3.githubusercontent.com/u/42903659?v=4', 'https://avatars0.githubusercontent.com/u/43814493?v=4', 'https://avatars3.githubusercontent.com/u/41234408?v=4', 'https://avatars2.githubusercontent.com/u/10833993?v=4', 'https://avatars3.githubusercontent.com/u/53488062?v=4', 'https://avatars1.githubusercontent.com/u/53133634?v=4', 'https://avatars2.githubusercontent.com/u/53230977?v=4', 'https://avatars0.githubusercontent.com/u/53400471?v=4', 'https://avatars0.githubusercontent.com/u/53221628?v=4', 'https://avatars3.githubusercontent.com/u/52829712?v=4', 'https://avatars1.githubusercontent.com/u/52847620?v=4', 'https://avatars3.githubusercontent.com/u/53134591?v=4', 'https://avatars2.githubusercontent.com/u/33775493?v=4', 'https://avatars1.githubusercontent.com/u/44433208?v=4', 'https://avatars1.githubusercontent.com/u/52834709?v=4', 'https://avatars1.githubusercontent.com/u/29457764?v=4', 'https://avatars2.githubusercontent.com/u/21082378?v=4', 'https://avatars1.githubusercontent.com/u/43813666?v=4', 'https://avatars0.githubusercontent.com/u/52852877?v=4']
print(len(avatarLinkList))


# In[3]:


def refineImage(avatarLink):
    avatar = Image.open(requests.get(avatarLink, stream=True).raw).convert("RGBA")
    canvas = Image.new('RGBA', avatar.size, (255,255,255,255))
    canvas.paste(avatar, mask=avatar)
    canvas.thumbnail(avatar.size, Image.ANTIALIAS)
    avatar = canvas.resize((100, 100))
    return avatar


# In[4]:


avatarList = []


# In[5]:


for avatarLink in avatarLinkList:
    avatarList.append(refineImage(avatarLink))


# In[6]:


logo = Image.open("../images/amfoss.png")
logo = logo.resize((150,150))
logoWidth, logoHeight = logo.size


# In[7]:


hacklogo = Image.open("../images/hacktoberfest.png")
hlogoWidth, hlogoHeight = hacklogo.size


# In[8]:


font_fname = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
font_size = 60
font = ImageFont.truetype(font_fname, font_size)


# In[9]:


width, height = 900, 600


# In[10]:


dim = []
for left in range(0, width, 100):
    for top in range(0, height, 100):
        dim.append((left, top))


# In[11]:


plainImage = Image.new('RGB', (width, height), (255, 255, 255))


# In[12]:


for avatar, (left, top) in zip(avatarList, dim):
    plainImage.paste(avatar, (left, top))


# In[13]:


plainImage = plainImage.filter(ImageFilter.GaussianBlur(radius = 4))


# In[14]:


draw = ImageDraw.Draw(plainImage)

draw.text((250, 210), "Total PRs: 263", font=font, fill='rgb(0, 0, 0)')
draw.text((200, 290), "+2109014", font=font, fill='rgb(40, 167, 69)')
draw.text((500, 290), "-12484", font=font, fill='rgb(203, 36, 49)')


# In[15]:


plainImage.paste(logo, (width - logoWidth, height - logoHeight), logo)
plainImage.paste(hacklogo, (0, 0), hacklogo)


# In[16]:


plainImage.save("pic.png")


# In[ ]:




