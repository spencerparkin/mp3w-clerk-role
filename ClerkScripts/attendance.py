# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
]

if __name__ == '__main__':

    zoom = 6
    zoom_factor = 1.5

    attendance_count = int(round(float(sum(count_list)) + float(zoom) * zoom_factor))
    print('Attendance: %d' % attendance_count)