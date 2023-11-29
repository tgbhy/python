import matplotlib.pyplot as plt
from PIL import Image

image = 0
while image != 1 and image != 2:
    image = input("Quel image voulez-vous faire ? ")
    if image.isdigit():
        image = int(image)

maneer = ""
while maneer != 1 and maneer != 2:
    maneer = input("Choisissez votre méthode de remplissage des pixels [1/2]\n- 1 : Pixel par pixel\n- 2 : Depuis un tableau de pixels\n")
    if maneer.isdigit():
        maneer = int(maneer)


if image == 1:
    # pixel art n°36 en 5x5
    
    #Creation d'une image blanche RGB 5x5
    img = Image.new("RGB",(5,5),(255,255,255))
    
    # definition des couleurs
    blue = (56, 75, 196)
    pink = (251, 131, 170)
    light_pink = (251, 172, 201)

    if maneer == 1:
        #remplissage de l'image pixel par pixel
        img.putpixel((1,1), blue)
        img.putpixel((1,2), blue)
        img.putpixel((3,1), blue)
        img.putpixel((3,2), blue)

        img.putpixel((0,3), light_pink)
        img.putpixel((1,3), light_pink)
        img.putpixel((3,3), light_pink)
        img.putpixel((4,3), light_pink)

        img.putpixel((0, 0), pink)
        img.putpixel((1, 0), pink)
        img.putpixel((2, 0), pink)
        img.putpixel((3, 0), pink)
        img.putpixel((4, 0), pink)
        img.putpixel((0, 1), pink)
        img.putpixel((2, 1), pink)
        img.putpixel((4, 1), pink)
        img.putpixel((0, 2), pink)
        img.putpixel((2, 2), pink)
        img.putpixel((4, 2), pink)
        img.putpixel((2, 3), pink)
        img.putpixel((0, 4), pink)
        img.putpixel((1, 4), pink)
        img.putpixel((2, 4), pink)
        img.putpixel((3, 4), pink)
        img.putpixel((4, 4), pink)
    else:
        # remplissage de l'image via plusieurs tableau de pixels selon les couleurs
        blue_pixels = [(1,1),(1,2),(3,1),(3,2)]
        light_pink_pixels = [(0,3),(1,3),(3,3),(4,3)]
        pink_pixels = [(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(2,1),(4,1),(0,2),(2,2),(4,2),(2,3),(0,4),(1,4),(2,4),(3,4),(4,4)]

        for pixel in blue_pixels:
            img.putpixel(pixel, blue)

        for pixel in light_pink_pixels:
            img.putpixel(pixel, light_pink)

        for pixel in pink_pixels:
            img.putpixel(pixel, pink)
else:
    #Creation d'une image blanche RGB 8x8
    img = Image.new("RGB",(8,8),(255,255,255))

    # définition des couleurs
    green = (0, 114, 54)
    beige = (255, 199, 148)
    orange = (247, 148, 29)
    brown = (117, 76, 36)
    light_blue = (109, 207, 246)
    black = (37, 37, 37)
    gray = (54, 54, 54)

    if maneer == 1:
        # background
        img.putpixel((0, 0), green)
        img.putpixel((0, 1), green)
        img.putpixel((0, 2), green)
        img.putpixel((0, 3), green)
        img.putpixel((0, 4), green)
        img.putpixel((0, 6), green)
        img.putpixel((0, 7), green)
        img.putpixel((1, 0), green)
        img.putpixel((1, 5), green)
        img.putpixel((1, 6), green)
        img.putpixel((1, 7), green)
        img.putpixel((3, 7), green)
        img.putpixel((5, 5), green)
        img.putpixel((5, 6), green)
        img.putpixel((5, 7), green)
        img.putpixel((6, 0), green)
        img.putpixel((6, 1), green)
        img.putpixel((6, 2), green)
        img.putpixel((6, 3), green)
        img.putpixel((6, 4), green)
        img.putpixel((6, 6), green)
        img.putpixel((6, 7), green)
        img.putpixel((7, 0), green)
        img.putpixel((7, 1), green)
        img.putpixel((7, 2), green)
        img.putpixel((7, 3), green)
        img.putpixel((7, 4), green)
        img.putpixel((7, 5), green)
        img.putpixel((7, 6), green)
        img.putpixel((7, 7), green)

        img.putpixel((2, 7), gray)
        img.putpixel((4, 7), gray)

        img.putpixel((2, 6), black)
        img.putpixel((3, 6), black)
        img.putpixel((4, 6), black)

        img.putpixel((1, 4), orange)
        img.putpixel((2, 5), orange)
        img.putpixel((3, 5), orange)
        img.putpixel((4, 5), orange)
        img.putpixel((5, 4), orange)

        img.putpixel((0, 5), beige)
        img.putpixel((1, 3), beige)
        img.putpixel((2, 4), beige)
        img.putpixel((2, 3), beige)
        img.putpixel((2, 2), beige)
        img.putpixel((2, 1), beige)
        img.putpixel((3, 4), beige)
        img.putpixel((3, 3), beige)
        img.putpixel((3, 1), beige)
        img.putpixel((4, 4), beige)
        img.putpixel((4, 3), beige)
        img.putpixel((4, 2), beige)
        img.putpixel((4, 1), beige)
        img.putpixel((5, 3), beige)
        img.putpixel((5, 1), beige)
        img.putpixel((6, 5), beige)

        img.putpixel((3, 2), light_blue)
        img.putpixel((5, 2), light_blue)

        img.putpixel((1, 2), brown)
        img.putpixel((1, 1), brown)
        img.putpixel((2, 0), brown)
        img.putpixel((3, 0), brown)
        img.putpixel((4, 0), brown)
        img.putpixel((5, 0), brown)
    else:
        # pixel art n°4 en 8x8
        
        # pixels : Liste de liste qui contient (liste) la couleur en première positions et les pixels correspondant sur les autres positions de la liste.
        # pixels : list[list[tuple[int, int, int], tuple[int, int], tuple[int, int], ...]]
        pixels = [
            [green, (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 6), (0, 7), (1, 0), (1, 5), (1, 6), (1, 7), (3, 7), (5, 5), (5, 6), (5, 7), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)],
            [gray, (2, 7), (4, 7)],
            [black, (2, 6), (3, 6), (4, 6)],
            [orange, (1, 4), (2, 5), (3, 5), (4, 5), (5, 4)],
            [beige, (0, 5), (1, 3), (2, 4), (2, 3), (2, 2), (2, 1), (3, 4), (3, 3), (3, 1), (4, 4), (4, 3), (4, 2), (4, 1), (5, 3), (5, 1), (6, 5)],
            [light_blue, (3, 2), (5, 2)],
            [brown, (1, 2), (1, 1), (2, 0), (3, 0), (4, 0), (5, 0)]
        ]

        for pixelList in pixels:
            color = pixelList[0]
            for pixel in pixelList[1:]:
                img.putpixel(pixel, color)

        # d'après ce code, nous pouvons penser (ce qui est vrai) qu'il est possible de faire correspondre ceci avec le cours sur les données structurées et les fichier CSV.

#-----------------------
# NE PAS MODIFIER LES DEUX LIGNES CI-DESSOUS
plt.imshow(img)
plt.show()