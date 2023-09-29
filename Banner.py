# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Banner:

    def __init__(self, image, locStart, locEnd,  tekst):
        # font = ImageFont.truetype(<font-file>, <font-size>)
        self.font = ImageFont.truetype("OpenSans-Regular.ttf", 18)
        self.reset(image)
        self.set_waarde(tekst)
        self.locStart = locStart
        self.locEnd = locEnd

    def reset(self, image):
        self.img = Image.open(image).convert('RGB')
        self.draw = ImageDraw.Draw(self.img, 'RGB')

    def set_waarde(self, tekst):
        self.tekst = str(tekst.replace('\r',''))

    def schrijf(self):
        _, _, text_width, text_height = self.draw.textbbox((0, 0), self.tekst, font=self.font)

        text_width -= 0
        lefttop = (
            int((self.locEnd[0]+self.locStart[0]-text_width)/2),
            int((self.locEnd[1]+self.locStart[1]-text_height)/2)
        )

        self.draw.text(lefttop, self.tekst, (0, 0, 0), font=self.font)

    def save(self, uit='out.jpeg'):
        self.img.save(uit, "jpeg")

    def run(self):
        self.schrijf()
        self.save()

    def get_image(self):
        return self.img
if __name__ == "__main__":
    banner = Banner("img\\1.jpg", "Test\nFoo\nBar")
    banner.run()
