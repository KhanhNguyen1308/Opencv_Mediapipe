def head_pose_status(n_ratio_1, n_ratio_2,c_ratio_1, c_ratio_2):
    if 0.5 < n_ratio_1 < 1.5:
        if 0.5 <= c_ratio_1 <= 0.95: 
            if 0.5 <= c_ratio_2 <= 0.95:
                head_status = 'Thang'
                mode = 0
            elif c_ratio_2 > 0.95:
                head_status = 'Cui'
                mode = 1
            elif c_ratio_2 < 0.5:
                head_status = 'Cui'
                mode = 1
        elif c_ratio_1 > 0.95:
            if 0.5 <= c_ratio_2 <= 0.95:
                head_status = 'Thang'
                mode = 0
            elif c_ratio_2 > 0.95:
                head_status = 'Cui'
                mode = 1
        elif c_ratio_1 < 0.5:
                head_status = 'Thang'
                mode = 8

    elif n_ratio_1 <= 0.5:
        if c_ratio_1 <= 0.4:
            head_status = 'Nghieng phai'
            mode = 2
        elif c_ratio_1 > 0.4:
            head_status = 'Cui_Nghieng phai'
            mode = 6

    elif n_ratio_1 >= 1.5:
        if c_ratio_2 <= 0.4:
            head_status = 'Nghieng Trai'
            mode = 3
        elif c_ratio_2 > 0.4:
            head_status = 'Cui_Nghieng Trai'
            mode = 7
    # if n_ratio_2 >= 1.4:
    #     head_status = 'Nhin Trai'
    #     mode = 8
    # if n_ratio_2 <= 0.7:
    #     head_status = 'Nhin Phai'
    #     mode = 8
    return head_status, mode



def eye_stat(eye_avg_ratio, count, blink, mode, Alarm):
    try:
        if mode == 0:
            if eye_avg_ratio <= 0.43:
                eye_status = 'Nham'
                count += 1
                if count >= 20:
                    Alarm = True
            else:
                eye_status = 'Mo'
                if count > 0:
                    blink += 1
                count = 0
                Alarm = False
        elif mode == 1:
            if eye_avg_ratio <= 0.6:
                eye_status = 'Nham'
                count += 1
                if count >= 20:
                    Alarm = True
            else:
                eye_status = 'Mo'
                if count > 0:
                    blink += 1
                count = 0
                Alarm = False
        elif mode == 2:
            if eye_avg_ratio <= 0.6:
                eye_status = 'Nham'
                count += 1
                if count >= 20:
                    Alarm = True
            else:
                eye_status = 'Mo'
                if count > 0:
                    blink += 1
                count = 0
                Alarm = False
        elif mode == 3:
            if eye_avg_ratio <= 0.53:
                eye_status = 'Nham'
                count += 1
                if count >= 20:
                    Alarm = True
            else:
                eye_status = 'Mo'
                if count > 0:
                    blink += 1
                count = 0
                Alarm = False
        elif mode == 4:
            if eye_avg_ratio <= 0.67:
                eye_status = 'Nham'
                count += 1
                if count >= 20:
                    Alarm = True
            else:
                eye_status = 'Open'
                if count > 0:
                    blink += 1
                count = 0
                Alarm = False
        elif mode == 5:
            if eye_avg_ratio <= 0.67:
                eye_status = 'Nham'
                count += 1
                if count >= 20:
                    Alarm = True
            else:
                eye_status = 'Open'
                if count > 0:
                    blink += 1
                count = 0
                Alarm = False
        elif mode == 6:
            if eye_avg_ratio <= 0.67:
                eye_status = 'Nham'
                count += 1
                if count >= 20:
                    Alarm = True
            else:
                eye_status = 'Open'
                if count > 0:
                    blink += 1
                count = 0
                Alarm = False
        elif mode == 7:
            if eye_avg_ratio <= 0.67:
                eye_status = 'Nham'
                count += 1
                if count >= 20:
                    Alarm = True
            else:
                eye_status = 'Open'
                if count > 0:
                    blink += 1
                count = 0
                Alarm = False

    except:
        eye_status = 'Loi'
        blink = 0
        count = 0
    return eye_status, blink, count, Alarm


def gat_dau(prev_status, mode, dem, gat_num):
    if mode == 1 or mode == 6 or mode == 7:
        dem += 1
        prev_status = mode
    if mode == 0 and (prev_status == 1 or prev_status == 6 or prev_status == 7):  
        if dem <= 20 and dem != 0:
            gat_num += 1
        dem = 0
    return gat_num, dem, prev_status