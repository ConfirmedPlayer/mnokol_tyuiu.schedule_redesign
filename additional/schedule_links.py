schedule_menu_url = 'http://mnokol.tyuiu.ru/rtsp/index2.php'

group_schedule_url = 'http://mnokol.tyuiu.ru/rtsp/shedule/show_shedule.php? \
    action=group&union=0&sid={sid}&gr={gr}&year={year}&vr=1'

teachers_schedule_url = 'http://mnokol.tyuiu.ru/rtsp/shedule/show_shedule.php? \
        action=prep&prep={teacher_id}&vr=1&count=4&shed[0]=244&union[0]=0&year[0]={year}& \
            shed[1]=245&union[1]=0&year[1]={year}&shed[2]=246&union[2]=0&year[2]={year}& \
                shed[3]=247&union[3]=0&year[3]={year}'

cabinets_schedule_url = 'http://mnokol.tyuiu.ru/rtsp/shedule/show_shedule.php? \
        action=cab&prep={cabinet_id}&vr=1&count=4&shed[0]=244&union[0]=0&year[0]={year}& \
            shed[1]=245&union[1]=0&year[1]={year}&shed[2]=246&union[2]=0&year[2]={year}& \
                shed[3]=247&union[3]=0&year[3]={year}'
