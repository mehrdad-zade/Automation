'''
personalize images
'''


from PIL import Image, ImageDraw, ImageFilter


im2 = Image.open('/Users/mehrdadalemzadeh/Pictures/Matrix.jpg')
im1 = Image.open('/Users/mehrdadalemzadeh/Pictures/Bull.jpg').resize(im1.size)

mask = Image.new("L", im1.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((120, 30, 600, 550), fill=255)
im = Image.composite(im1, im2, mask)

mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
im = Image.composite(im1, im2, mask_blur)

#mask = Image.open('/Users/mehrdadalemzadeh/Pictures/Bull.jpg').convert('L').resize(im1.size)
#im = Image.composite(im1, im2/2, mask)

im.save('/Users/mehrdadalemzadeh/Pictures/Blend.jpg')




