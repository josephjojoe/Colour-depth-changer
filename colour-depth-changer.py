from PIL import Image

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
def gif_depth_change(pathToGIF, colourDepth):
    originalGIF = Image.open(pathToGIF)
    newFrames = []
    for frame in range(0, originalGIF.n_frames):
        originalGIF.seek(frame)
        x = originalGIF.convert("P", palette=Image.ADAPTIVE, colors=colourDepth)
        newFrames.append(x)
    for frame in range(0, len(newFrames)):
        newFrames[frame] = newFrames[frame].convert("P", palette=Image.ADAPTIVE, colors=colourDepth)
    newFrames[0].save('changed-depth-gif.gif', format='GIF', append_images=newFrames[1:], save_all=True)

# Changes colour depth of image
def image_depth_change(pathToImage, colourDepth):
    originalImage = Image.open(pathToImage)
    depthChangedImage = originalImage.convert("P", palette=Image.ADAPTIVE, colors=colourDepth)
    depthChangedImage.show()
