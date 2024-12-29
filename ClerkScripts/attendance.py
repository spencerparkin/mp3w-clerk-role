# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    5, 13, 11, 12, 10, 9, 6, 17, 6, 9, 6, 17,
    4, 8, 9, 10, 5, 7, 7, 6
]

if __name__ == '__main__':

    zoom = 16
    zoom_factor = 1.5

    attendance_count = int(round(float(sum(count_list)) + float(zoom) * zoom_factor))
    print('Attendance: %d' % attendance_count)