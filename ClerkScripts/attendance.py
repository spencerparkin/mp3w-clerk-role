# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    5, 10, 16, 13, 14, 16, 11, 9, 8, 9, 7, 5, 1, 13,
    2, 2, 3, 3, 4, 3, 9, 10, 11, 6, 4, 2
]

if __name__ == '__main__':

    zoom = 11
    zoom_factor = 1.5

    attendance_count = int(round(float(sum(count_list)) + float(zoom) * zoom_factor))
    print('Attendance: %d' % attendance_count)