import cv2
import argparse


def arg_parser():
    parser = argparse.ArgumentParser(description="input photo path")
    parser.add_argument("-path", "--input_path", type=str, required=True, help="input photo path")
    argument = vars(parser.parse_args())
    return argument


def resize_pic(path, x_axis=10, y_axis=10):
    pic = cv2.imread(path, 1)
    x_per = 100 / pic.shape[1] * x_axis
    y_per = 100 / pic.shape[0] * y_axis

    cv2.imshow('view', pic)
    cv2.waitKey(0)
    resized = cv2.resize(pic, (int(pic.shape[0] * 60 / 100), int(pic.shape[1] * 60 / 100)))
    cv2.circle(resized, (int(x_per / 100 * pic.shape[1]), int(y_per / 100 * pic.shape[0])), 10, (0, 0, 255), -1)
    cv2.imshow('view2', resized)
    cv2.waitKey(0)


cv2.destroyAllWindows()

resize_pic('1.jpg')
