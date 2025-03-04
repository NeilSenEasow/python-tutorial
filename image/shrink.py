from images import Image

path=input("Enter the path to the gif image:")
factor=int(input("Enter the factor to shrink:"))
img=Image(path)
height=img.getHeight()
width=img.getWidth()
new=Image(width//factor,height//factor)
oldY=0
newY=0
while oldY<height-factor:
    oldX=0
    newX=0
    while oldX<width-factor:
        oldP=img.getPixel(oldX,oldY)
        new.setPixel(newX,newY,oldP)
        oldX+=factor
        newX+=1
    oldY+=factor
    newY+=1

new.draw()