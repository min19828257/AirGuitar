def data_return(onORoff,turn):

    if onORoff == 1:
        print("음악 시작")
        onOff = 1
    else :
        print("음악 끄기")
        onOff = 0

    number = turn

    if number == 1:
        melody = 60
    elif number == 2:
        melody = 62
    elif number == 3:
        melody = 64
    elif number == 4:
        melody = 65
        
##        
##    melody = [[60, 62, 64, 65, 67, 69, 71],
##              [72, 74, 76, 77, 79, 81, 83],
##              [84, 86, 88, 89, 91, 93, 95]]

    return onOff ,melody
