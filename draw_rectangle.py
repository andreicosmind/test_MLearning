import cv2
import numpy


def draw_rectangle(picture_path, ax_x1, ax_y1, ax_x2, ax_y2):
	"""
	The function functionality is to proses and draw a rectangle on a picture.
	It takes 5 parameters.

		1) the path to the picture
		2) the x coordinate of the down-left corner
		3) the y coordinate of the down-left corner
		4) the x coordinate of the up-right corner
		5) the y coordinate of the up-right corner
	"""
	img = cv2.imread(picture_path, 1)
	cv2.rectangle(img, (ax_x1, ax_y1), (ax_x2, ax_y2), (196, 30, 58), 7)
	cv2.imshow('view', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.imwrite('procesata.png', img)

if __name__ == '__main__':
	pass