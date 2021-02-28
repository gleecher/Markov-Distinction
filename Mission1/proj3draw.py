from PIL import Image, ImageDraw

def create_image(width, height):
  return Image.new("RGB", (width, height), (255, 255, 255))

def draw_point(image, x, y, color):
  ImageDraw.Draw(image).point((x,y), color)

def draw_square(image, x, y, w, color):
  ImageDraw.Draw(image).rectangle([x,y,x+w,y+w], color)

def save_image(image, filename):
  image.save(filename, "PNG")