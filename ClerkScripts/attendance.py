# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    6, 6, 15, 15, 11, 14, 9, 13, 11, 13, 23,
    5, 5, 8, 9, 12, 11, 6, 10
]

if __name__ == '__main__':

    zoom = 0
    zoom_factor = 1.5

    attendance_count = int(round(float(sum(count_list)) + float(zoom) * zoom_factor))
    print('Attendance: %d' % attendance_count)