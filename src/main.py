from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import sys


def add_text_to_image(input, out, top_t = "SAMPLE TEXT", bottom_t = "SAMPLE TEXT"):

    img = Image.open(input)
    img_fraction = 0.5
    draw = ImageDraw.Draw(img)

    font_size = img.size[0] * 0.15
    font = ImageFont.truetype('fonts/Impact.ttf', font_size)
    #top text
    top_text = top_t

    top_text_width = font.getbbox(top_text)[2]
    while(top_text_width >= img.size[0]):
        font_size-=1
        font = ImageFont.truetype('fonts/Impact.ttf', font_size)
        top_text_width=font.getbbox(top_text)[2]




    #bottom text
    bottom_text = bottom_t
    bottom_text_width = font.getbbox(bottom_text)[2]
    while(bottom_text_width >= img.size[0]):
        font_size-=1
        font = ImageFont.truetype('fonts/Impact.ttf', font_size)
        bottom_text_width=font.getbbox(bottom_text)[2]

    top_text_width=font.getbbox(top_text)[2]

    #draw
    x, y = (img.size[0] - top_text_width)/2 , img.size[1] * 0.05

    draw.text((x-1, y-1), top_text, font=font, fill="black")
    draw.text((x+1, y-1), top_text, font=font, fill="black")
    draw.text((x-1, y+1), top_text, font=font, fill="black")
    draw.text((x+1, y+1), top_text, font=font, fill="black")

    draw.text((x, y), top_text, font=font, fill = (255, 255, 255))


    #draw bottom

    x, y = (img.size[0] - bottom_text_width)/2 , img.size[1] - (img.size[1] * 0.20)

    draw.text((x-1, y-1), bottom_text, font=font, fill="black")
    draw.text((x+1, y-1), bottom_text, font=font, fill="black")
    draw.text((x-1, y+1), bottom_text, font=font, fill="black")
    draw.text((x+1, y+1), bottom_text, font=font, fill="black")

    draw.text((x, y), bottom_text, font=font, fill = (255, 255, 255))

    img.save(out)



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Input file and output file need to be in command line arguments")
    else:
        try:
            if sys.argv[3] != None and sys.argv[4] != None:
                add_text_to_image(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
            else:
                add_text_to_image(sys.argv[1], sys.argv[2])
        except IndexError:
            add_text_to_image(sys.argv[1], sys.argv[2])
        







            