# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

counts_list = [
    8, 8, 9, 3, 10, 10, 13, 6, 11, 7, 1, 10, 16, 17,
    15, 17, 12, 15, 13, 15, 10, 10, 7, 6, 12,
    6, 2, 6, 7, 1, 1, 1, 6, 1, 2, 1, 1, 3, 2, 3, 1
]

zoom_count = 0
zoom_factor = 0

if __name__ == '__main__':
    attendance = float(sum(counts_list)) + float(zoom_count) * zoom_factor
    print("Attendance: " + str(attendance))