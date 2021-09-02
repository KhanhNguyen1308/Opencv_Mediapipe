import numpy as np
import math
from function import khoang_cach, mid_point


def head_pose_ratio(nose, left_eye, right_eye):
    g_t = mid_point(left_eye[0][0], left_eye[0][3])
    g_p = mid_point(right_eye[0][0], right_eye[0][3])
    x2 = (g_t[0], nose[1])
    x1 = (g_p[0], nose[1])
    y2 = (nose[0], g_t[1])
    y1 = (nose[0], g_p[1])
    kc_gt_x2 = khoang_cach(g_t, x2)
    if kc_gt_x2 == 0:
        kc_gt_x2 = 1
    kc_gp_x1 = khoang_cach(g_p, x1)
    if kc_gp_x1 == 0:
        kc_gp_x1 = 1
    kc_gt_y2 = khoang_cach(g_t, y2)
    if kc_gt_y2 == 0:
        kc_gt_y2 = 1
    kc_gp_y1 = khoang_cach(g_p, y1)
    if kc_gp_y1 == 0:
        kc_gp_y1 = 1
    n_ratio_1 = kc_gp_x1/kc_gt_x2
    n_ratio_2 = kc_gp_y1/kc_gt_y2
    c_ratio_1 = kc_gp_x1/kc_gp_y1
    c_ratio_2 = kc_gt_x2/kc_gt_y2
    if n_ratio_1 < 0:
        n_ratio_1 = n_ratio_1 * (-1)
    if n_ratio_2 < 0:
        n_ratio_2 = n_ratio_2 * (-1)
    if c_ratio_1 < 0:
        c_ratio_1 = c_ratio_1 * (-1)
    if c_ratio_2 < 0:
        c_ratio_2 = c_ratio_2 * (-1)
    n = (g_p[1] - nose[1])/(g_p[0] - nose[0])
    m = (g_t[1] - nose[1])/(g_t[0] - nose[0])
    x5 = int(math.degrees(math.atan(n)))
    x6 = int(math.degrees(math.atan(m)))*(-1)
    return n_ratio_1, n_ratio_2, c_ratio_1, c_ratio_2, x5, x6

