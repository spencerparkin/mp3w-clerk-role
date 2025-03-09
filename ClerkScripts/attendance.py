# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    11, 13, 16, 15, 14, 1,
	10, 16, 8, 13, 30, 5, 4, 7, 4, 14,
	8, 19, 4
]

if __name__ == '__main__':

    zoom = 4
    zoom_factor = 1.5

    attendance_count = int(round(float(sum(count_list)) + float(zoom) * zoom_factor))
    print('Attendance: %d' % attendance_count)