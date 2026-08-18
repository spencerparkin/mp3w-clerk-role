# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    6, 10, 10, 13, 8, 13, 10, 11, 3, 12, 7, 14, 5, 3, 5, 6, 7, 6, 11,
    11, 9, 5, 8
]

if __name__ == '__main__':

    attendance_count = sum(count_list)
    print('Attendance: %d' % attendance_count)