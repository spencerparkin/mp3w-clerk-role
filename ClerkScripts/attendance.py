# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    10, 8, 12, 12, 11, 3, 14, 16,
    12, 8, 8, 19, 4, 4, 2, 3, 2, 7, 1, 11, 9, 6, 7
]

if __name__ == '__main__':

    attendance_count = sum(count_list)
    print('Attendance: %d' % attendance_count)