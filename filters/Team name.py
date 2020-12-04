from PIL import Image, ImageFont, ImageDraw

team = "Anaïs, Paul & Walid"

celebration_img = Image.open("../assets/smille.png")

#TELECHARGER TTF POUR LES POLICES D'ECRITURES ou la TTF de la police voulu direct sur google fonts

title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)
    title_text = "Anaïs, Paul & Walid"

image_editable = ImageDraw.Draw(celebration_img)

image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
clebration_img.save("result.jpg")