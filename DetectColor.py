import cv2

#Given the coordinates of the corners of the pattern
#Detects each of the colors in the pattern and where
#Colors stored in a list, snake style starting in upper left and ending in lower left

topLeft = (0, 0)
topRight = (100, 0)
botLeft = (0, 100)
botRight = (100, 100)

topMiddle = ((topRight[0] - topRight[0]) / 2, (topRight[1] - topLeft[1]) / 2)
leftMiddle = ((botLeft[0] - topLeft[0]) / 2, (botLeft[1] - topLeft[1]) / 2)
rightMiddle = ((botRight[0] - topRight[0]) / 2, (botRight[1] - topRight[1]) / 2)
botMiddle = ((botRight[0] - botRight[0]) / 2, (botRight[1] - botLeft[1]) / 2)

center = findCoords(leftMiddle, rightMiddle)

topMiddle = ((topRight[0] - topRight[0]) / 2, (topRight[1] - topLeft[1]) / 2)
leftMiddle = ((botLeft[0] - topLeft[0]) / 2, (botLeft[1] - topLeft[1]) / 2)
rightMiddle = ((botRight[0] - topRight[0]) / 2, (botRight[1] - topRight[1]) / 2)
botMiddle = ((botRight[0] - botRight[0]) / 2, (botRight[1] - botLeft[1]) / 2)

class Quadrilateral:
  def __init__(TL, TR, BL, BR):
      topLeft = TL
      topRight = TR
      botLeft = BL
      botRight = BR


def centroid(vertexes):
     _x_list = [vertex [0] for vertex in vertexes]
     _y_list = [vertex [1] for vertex in vertexes]
     _len = len(vertexes)
     _x = sum(_x_list) / _len
     _y = sum(_y_list) / _len
     return(_x, _y)

def findCoords(point1, point2):
    return ((point2[0] - point1[0]) / 2, (point2[1] - point1[1]) / 2)
