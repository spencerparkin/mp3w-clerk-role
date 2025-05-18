# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    11, 8, 13, 11, 10, 13, 13, 3, 18, 12, 10, 8, 8, 18, 3, 1,
    6, 3, 8, 7, 9, 8, 5, 8
]

if __name__ == '__main__':

    zoom = 8
    zoom_factor = 1.5

    attendance_count = int(round(float(sum(count_list)) + float(zoom) * zoom_factor))
    print('Attendance: %d' % attendance_count)