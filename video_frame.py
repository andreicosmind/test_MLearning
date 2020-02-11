import cv2
import os
import argparse
import tqdm


def arg_parser():
    parser = argparse.ArgumentParser(description="input video path")
    parser.add_argument("-path", "--input_path", type=str, required=True, help="input video path")
    argument = vars(parser.parse_args())
    return argument


def video_frame(path_to_video):
    new_dir = os.getcwd() + "/frames"
    if os.path.exists(new_dir):
        pass
    else:
        os.mkdir(new_dir)

    vid = cv2.VideoCapture(path_to_video)
    count_frames = 1
    p_bar = tqdm.tqdm()
    while vid.isOpened():
        p_bar.update(10)
        rest, frame = vid.read()
        if not rest:
            break
        cv2.imwrite(new_dir + "/f_" + str(count_frames).zfill(2) + '.png', frame)
        count_frames += 1

    vid.release()
    p_bar.close()


if __name__ == '__main__':
    pars = arg_parser()
    video_frame(pars['input_path'])
