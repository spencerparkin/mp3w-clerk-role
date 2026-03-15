# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    9, 7, 15, 13, 12, 16, 12, 12, 8, 7, 8,
    7, 18, 1, 3, 2, 1, 5, 7, 2, 12, 9, 9, 6, 12
]

if __name__ == '__main__':

    attendance_count = sum(count_list)
    print('Attendance: %d' % attendance_count)