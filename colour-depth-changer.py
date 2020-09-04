from PIL import Image
import imageio

# This function uses an adaptive palette
def image_depth_gif(pathToImage, frameDuration=500): 
    originalImage = Image.open(pathToImage)
    frames = []
    amountOfColours = 256
    while amountOfColours >= 2:
        imageWithColourPalette = originalImage.convert("P", palette=Image.ADAPTIVE, colors=amountOfColours)
        amountOfColours = int(amountOfColours / 2) # Program reads amountOfColours as float with /= 2 which doesn't work
        frames.append(imageWithColourPalette)
    frames[0].save('color-depth-change.gif', format='GIF', append_images=frames[1:], save_all=True, duration=frameDuration, loop=0) # To do - change save name to based on pathToImage file name

# Changes colour depth of GIF
def gif_depth_change(pathToGIF):
    originalGIF = Image.open(pathToGIF)
    ### to do

# Changes colour depth of image
def image_depth_change(pathToImage, colourDepth):
    originalImage = Image.open(pathToImage)
    depthChangedImage = originalImage.convert("P", palette=Image.ADAPTIVE, colors=colourDepth)
    depthChangedImage.show()
