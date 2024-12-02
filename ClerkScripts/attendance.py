# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    8, 14, 5, 10, 10, 17, 13, 12, 7, 12, 7, 12, 7, 19, 2, 5, 2, 10, 6, 8, 5, 5
]

if __name__ == '__main__':

    zoom = 13
    zoom_factor = 1.5

    attendance_count = int(round(float(sum(count_list)) + float(zoom) * zoom_factor))
    print('Attendance: %d' % attendance_count)