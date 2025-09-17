from PIL import Image


def ascii(image_path, output_width):
  img = Image.open(image_path)

  aspect_ratio = (img.height/img.width)*0.4
  output_height = int(aspect_ratio * output_width)

  img = img.resize((output_width, output_height))

  ascii_chars = "@%#*+=-:. "

  ascii_image=""

  for y in range(output_height):
    for x in range(output_width):
      r,g,b = img.getpixel((x, y))

      intensity = (r+g+b)/3 #number between 0 and 255

      ascii_char = ascii_chars[int(intensity/255 * (len(ascii_chars) - 1))]

      ascii_image += f"\033[;38;2;{r};{g};{b}m{ascii_char}\033[0m"
    ascii_image += "\n"

  print(ascii_image)
     
