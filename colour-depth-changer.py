from PIL import Image
import imageio


originalImage = Image.open("./painting.jpg")
originalImage.show()


imageWithColorPalette = originalImage.convert("P", palette=Image.ADAPTIVE, colors=128)
imageWithColorPalette.show()
