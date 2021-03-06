"""
Name: Vo Thanh Hai
Class: INT3404 20
MSSV: 18020452
"""

import cv2

def q_0(input_file, output_file, delay = 1):
    """
    :param input_file:
    :param output_file:
    :param delay:
    :return:
    """
    img = cv2.imread(input_file, cv2.IMREAD_COLOR)

    cv2.imshow('0', img)
    cv2.waitKey(delay)

    cv2.imwrite(output_file, img)

def q_1_YCrCb(input_file, output_file, delay = 1):
    # print("Task 1")
    BGRimg = cv2.imread(input_file)

    height, width, channel = BGRimg.shape
    print('Height: ', height, 'pixels')
    print('Width: ', width, 'pixels')
    print('Number of channels: ', channel)

    YCrCbimg = cv2.cvtColor(BGRimg, cv2.COLOR_BGR2YCrCb)

    meanChannel = cv2.mean(YCrCbimg)
    print('Average value of each color channels: ', meanChannel)

    cv2.imshow('q_1_YCrCb', YCrCbimg)
    cv2.waitKey(delay)

    cv2.inwrite(output_file, YCrCbimg)

def q_1_RGB(input_file, output_file, delay=1):
    #print("Task 1")
    BGRimg = cv2.imread(input_file)

    height, width, channel = BGRimg.shape
    print('Height: ', height, 'pixels')
    print('Width: ', width, 'pixels')
    print('Number of channels: ', channel)

    RGBimg = cv2.cvtColor(BGRimg, cv2.COLOR_BGR2RGB)

    meanChannel = cv2.mean(RGBimg)
    print('Average value of each color channels: ', meanChannel)

    cv2.imshow('q_1_RGB', RGBimg)
    cv2.waitKey(delay)

    cv2.inwrite(output_file, RGBimg)

def q_2(input_file, clear_apple, blurred_apple, delay = 1):
    #print("Task 2")
    img = cv2.imread(input_file)

    nearApple = img[297:297+178, 362:362+178]
    farApple = img[38:38+88, 89:89+88]

    cv2.imshow('clear_apple.png', nearApple)
    cv2.imwrite(clear_apple, nearApple)

    cv2.imshow('blurred_apple', farApple)
    cv2.imwrite(blurred_apple, farApple)

    cv2.waitKey(delay)

def q_3_font(input_file, output_file, delay = 1):
    BGRimg = cv2.imread(input_file)
    GRAYimg = cv2.cvtColor(BGRimg, cv2.COLOR_BGR2GRAY)

    cv2.imshow('0', GRAYimg)
    cv2.waitKey(delay)

    cv2.imwrite(output_file, GRAYimg)

    # width, height = BGRimg.shape
    # resizedBGRimg = cv2.resize(BGRimg, (width/2, height/2)
    # T????ng t??? v???i c??c tr?????ng h???p k/i kh??c.


    # ????? ???nh qu??? t??o n??t h??n, theo kh??a c???nh nhi???p ???nh, c?? th??? ??i???u ch???nh ti??u ??i???m
    # c???a m??y ???nh (??i???u ch???nh v???t l??), th??m ??nh s??ng ??? m??i tr?????ng ch???p v?? gi???m kh???u
    # ????? ????? c?? th??m ????? s??u. ?????t v??? tr?? ch???p ???nh sao cho v??? tr?? c??c qu??? t??o c??ch ?????u
    # m??y ???nh (thay v?? nh??n d???c theo h??ng s???p x???p c??c qu??? t??o).

if __name__ == "__main__":

    q_0('apple.png', 'test_apple.png', 999999)
    q_1_YCrCb('chromatic_aberration.png', 'q_1_YCrCb', 999999)
    q_1_RGB('chromatic_aberration.png', 'q_1_RGB', 999999)
    q_2('apple.png', 'clear_apple.png', 'blurred_apple.png', 999999)
    q_3_font('font.png', 'test.png', 999999)
