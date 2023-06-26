from pygame import image

element_size = 32
big_element_size = 64
face_size = 50
border = 16
top_border = 100


class RectangularResources:
    img_empty_field = image.load("img/rectangularGrid/empty.png")
    img_flag = image.load("img/rectangularGrid/flag.png")
    img_element = image.load("img/rectangularGrid/Grid.png")
    img_element1 = image.load("img/rectangularGrid/grid1.png")
    img_element2 = image.load("img/rectangularGrid/grid2.png")
    img_element3 = image.load("img/rectangularGrid/grid3.png")
    img_element4 = image.load("img/rectangularGrid/grid4.png")
    img_element5 = image.load("img/rectangularGrid/grid5.png")
    img_element6 = image.load("img/rectangularGrid/grid6.png")
    img_element7 = image.load("img/rectangularGrid/grid7.png")
    img_element8 = image.load("img/rectangularGrid/grid8.png")
    img_mine = image.load("img/rectangularGrid/mine.png")
    img_mineClicked = image.load("img/rectangularGrid/mineClicked.png")
    img_mineFalse = image.load("img/rectangularGrid/mineFalse.png")


class HexagonalResources:
    img_empty_field = image.load("img/hexagonalGrid/empty.png")
    img_flag = image.load("img/hexagonalGrid/flag.png")
    img_element = image.load("img/hexagonalGrid/Grid.png")
    img_element1 = image.load("img/hexagonalGrid/grid1.png")
    img_element2 = image.load("img/hexagonalGrid/grid2.png")
    img_element3 = image.load("img/hexagonalGrid/grid3.png")
    img_element4 = image.load("img/hexagonalGrid/grid4.png")
    img_element5 = image.load("img/hexagonalGrid/grid5.png")
    img_element6 = image.load("img/hexagonalGrid/grid6.png")
    img_mine = image.load("img/hexagonalGrid/mine.png")
    img_mineClicked = image.load("img/hexagonalGrid/mineClicked.png")
    img_mineFalse = image.load("img/hexagonalGrid/mineFalse.png")


class ControlElementsResources:
    img_big_element = image.load("img/Grid_64.png")
    img_big_empty_element = image.load("img/empty_64.png")
    img_face_smiling = image.load("img/face_smile_50.png")
    img_face_dead = image.load("img/face_dead_50.png")
    img_face_sunglasses = image.load("img/face_sunglasses_50.png")
    img_face_considering = image.load("img/face_considering_50.png")
