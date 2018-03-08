import numpy as np
import cv2
import cv2.aruco as aruco

aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

#Draw Single Marker
#id_num = 2
#img_size = 700
#image = aruco.drawMarker(aruco_dict, id_num, img_size)

#Draw a Grid Board
horLength = 2
verLength = 2
markerLength = 0.03
markerSep = 0.01

gridBoard = aruco.GridBoard_create(horLength, verLength, markerLength, markerSep, aruco_dict)
image = gridBoard.draw((400,400), 10, 1)
#image = aruco.drawPlanarBoard(gridBoard, 700, 10, 1)
#image = gridBoard.draw()
cv2.imwrite("testMarker.jpg", image)

cv2.imshow('frame', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
