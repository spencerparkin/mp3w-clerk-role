# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    10, 7, 20, 17, 16, 14, 10, 10, 17, 13, 12,
    9, 19, 1, 4, 8, 4, 9, 10, 12, 6, 11
]

if __name__ == '__main__':

    zoom = 0
    zoom_factor = 1.5

    attendance_count = int(round(float(sum(count_list)) + float(zoom) * zoom_factor))
    print('Attendance: %d' % attendance_count)