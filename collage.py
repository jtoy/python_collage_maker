from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 50, encoding="unic")
# for mac, need to change for linux

# images are labeled 1_1.jpg 1_2.jpg etc for as many rows and cols you want.
# images will automatically be resided to 512x512 or whatever size you set

def generate_collage(rows, cols,width=512,height=512):
    new_img = Image.new('RGB', ((width  + 10)*cols+90, (height+10)*rows-10), color=(255,255,255))
    draw = ImageDraw.Draw(new_img)
    for i in range(0, rows):
        for ii in range(0, cols):
            file = f'{i+1}_{ii+1}.jpg'
            img = Image.open(file)
            img = img.resize((width, height))
            offset = i*10
            if ii == 0:
                start_center = (img.width/2, img.height/2)
                x = (start_center[0] + start_center[0])  + 30
                y = (start_center[1] + start_center[1] + (i*img.width*2) ) / 2 
                blue = (70,102,255)
                draw.line([(x-20,y), (x+35,y)], fill=blue, width=50)
                draw.polygon([(x+20, y-40), (x+20, y+40), (x+60, y)], fill=blue)
                draw.text((x,y-30), f"to", fill=(255,255,255), font=font)
            if ii > 0:
               new_img.paste(img, (100+ii*(width+10),(i*height)+offset))
            else:
               new_img.paste(img, (ii*width,(i*height)+offset))
    new_img.save('collage.jpg')



generate_collage(3,5)
