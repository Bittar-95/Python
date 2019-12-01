import statistics as st
# =============================================================================
# Q1
X=[3,1.5,4.5,6.75,2.25,5.75,2.25]
print(st.mean(X))
print(st.harmonic_mean(X))
print(st.median(X))
print(st.median_low(X))
print(st.median_high(X))
print(st.median_grouped(X))
print(st.median_grouped(X))
print(st.mode(X))
print(st.pstdev(X))
print(st.pvariance(X))
print(st.stdev(X))
print(st.variance(X))
# =============================================================================



# =============================================================================
# Q2
import random
print(random.random())
print(random.randrange(10))
print(random.choice(["Ali","Khalid","Hussam"])) 
print(random.sample(range(100) ,10 ))
print(random.choice('Orange Academy' ))
a = [1,5,8,9,2,4]
random.shuffle(a)
print(a)
print(random.randint(20,30))
print(random.randrange(1000,2111,5))
print(random.uniform(10000,11000))
# =============================================================================


# =============================================================================
# Q3
import math
print(math.pi)
print(math.cos(200))
print(math.sin(30))
print(math.tan(180))
print(math.floor(10.8))
print(math.ceil(10.8))


# =============================================================================


# =============================================================================
# Q4
from PIL import Image,ImageDraw,ImageFilter

img =Image.open('Pizza.jpg')
newImage = img
draw = ImageDraw.Draw(img)
#print(img.format , img.size , img.mode , end=" ")
#img = img.transpose(Image.FLIP_TOP_BOTTOM)
#img.show()
#img = img.convert('L')
#img.show()
#img=img.crop((0,0,50,50))
#img.show()
draw.line((0,0)+img.size , fill=(255,255,0))
draw.line((0,img.size[1] , img.size[0] , 0) , fill=(255,255,0))
draw.text((150,150),"Mohammad Albittar",(100,200,100))
img.show()

img = img.filter(ImageFilter.EDGE_ENHANCE)
img.show()
img = img.filter(ImageFilter.FIND_EDGES)
img.show()

img = img.filter(ImageFilter.SMOOTH)
img.show()

img1 = img.filter(ImageFilter.SHARPEN)
img.show()

blend = Image.blend(img , newImage,0.5)
blend.show()
blend = blend.filter(ImageFilter.BLUR)
blend.show()



img.thumbnail((128,128))
img.show()


img = img.rotate(90)
img.show()

pizza =Image.open('Pizza.jpg')

mask = Image.open('horse_r.png').convert('L').resize(img.size)
image_mask = Image.composite(img , pizza , mask)
image_mask.show();





# =============================================================================
