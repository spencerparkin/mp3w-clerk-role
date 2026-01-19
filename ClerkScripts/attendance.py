# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    13, 9, 11, 17, 11, 9, 10, 10, 12, 11,
    14, 22, 2, 4, 3, 13, 9, 12, 7, 6, 6, 1, 5
]

if __name__ == '__main__':

    attendance_count = sum(count_list)
    print('Attendance: %d' % attendance_count)