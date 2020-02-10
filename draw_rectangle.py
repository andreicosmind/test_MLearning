import cv2
import argparse


def arg_parser():
	parser = argparse.ArgumentParser(description="input photo path")
	parser.add_argument("-path", "--input_path", type=str, required=True, help="input photo path")
	argument = vars(parser.parse_args())
	return argument


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
	cv2.namedWindow("view", cv2.WINDOW_NORMAL)
	cv2.imshow('view', img)

	k = cv2.waitKey(0)
	if k == 27:
		cv2.destroyAllWindows()
	elif k == ord('s'):
		cv2.imwrite('process.png', img)
		cv2.destroyAllWindows()


if __name__ == '__main__':
	pars = arg_parser()
	draw_rectangle(pars['input_path'], 12, 200, 400, 450)
