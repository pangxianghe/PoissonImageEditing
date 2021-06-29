from poisson_complete import *

if __name__ == '__main__':
    src = cv2.imread('./images/test6_src.png')
    msk = cv2.imread('./images/test6_mask.png')
    dst = src.copy()

    offset = [0, 0]
    P = Poisson(offset, src, msk, dst)
    out = P.process('Local_color_changes')

    cv2.imshow('', out)
    cv2.waitKey(0)

    cv2.imwrite('./images/test6.png', out)
