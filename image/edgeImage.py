from images import Image

def average(colors):
    (r,g,b)=colors
    return (r+g+b)//3


path=input("Enter the path to the gif image:")
amount=int(input("Enter the amount:"))
blackpixel=(0,0,0)
whitepixel=(255,255,255)
img=Image(path)
for y in range(1,img.getHeight()-1):
    for x in range(1,img.getWidth()-1):
        old=img.getPixel(x,y)
        left=img.getPixel(x-1,y)
        down=img.getPixel(x,y+1)
        oldavg=average(old)
        leftavg=average(left)
        downavg=average(down)
        if ((abs(oldavg-leftavg)>amount)or(abs(oldavg-downavg)>amount)):
            img.setPixel(x,y,blackpixel)
        else:
            img.setPixel(x,y,whitepixel)
img.draw()