from images import Image

def blur(listofcolor):
    r=listofcolor[0][0]+listofcolor[1][0]+listofcolor[2][0]+listofcolor[3][0]+listofcolor[4][0]
    g=listofcolor[0][1]+listofcolor[1][1]+listofcolor[2][1]+listofcolor[3][1]+listofcolor[4][1]
    b=listofcolor[0][2]+listofcolor[1][2]+listofcolor[2][2]+listofcolor[3][2]+listofcolor[4][2]
    r=r//5
    g=g//5
    b=b//5
    return (r,g,b)


path=input("Enter the path to the gif image:")
img=Image(path)
for y in range(1,img.getHeight()-1):
    for x in range(1,img.getWidth()-1):
        old=img.getPixel(x,y)
        left=img.getPixel(x-1,y)
        right=img.getPixel(x+1,y)
        up=img.getPixel(x,y-1)
        down=img.getPixel(x,y+1)
        average=blur([old,left,right,up,down])
        img.setPixel(x,y,average)

img.draw()