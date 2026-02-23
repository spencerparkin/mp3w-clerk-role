# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

count_list = [
    9, 10, 15, 9, 12, 8, 10, 10, 7, 5, 7, 15,
    4, 1, 1, 2, 8, 3, 8, 5, 7, 5, 7
]

if __name__ == '__main__':

    attendance_count = sum(count_list)
    print('Attendance: %d' % attendance_count)