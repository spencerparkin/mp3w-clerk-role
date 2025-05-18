# attendance_stats.py

if __name__ == '__main__':
    attendance_list = [220.0, 252.0, 178.0, 220.0, 212.0, 195.0, 212.0, 204.0, 218.0, 316.0, 212.0, 193.0, 240.0, 257.0, 212.0]
    attendance_avg = sum(attendance_list) / float(len(attendance_list))
    attendance_easter = 257.0
    percentage = (attendance_easter / attendance_avg) * 100.0
    print('Average attendance: %f' % attendance_avg)
    print('Easter attendance: %f' % attendance_easter)
    print('Easter precentage of average: %f%%' % percentage)