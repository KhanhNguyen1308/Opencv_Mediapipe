def sleep_mode(mode, ear, blink, count):
    if mode == 1:
        if count >= 25:
            status = 'Danger'
        else:
            status = 'Normal'
    else:
        status = 'Normal'
    return status

def color_text(Drowsy_mode):
    if Drowsy_mode == 'Normal':
        color = (0, 255, 0)
    else:
        color = (0, 0, 255)
    return color
