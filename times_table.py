# 掛け算するための関数
def calc_times(value):
    times_list = []
    for i in range(1, 10):
        times_list.append(value * i)
    return times_list

def times_table():
    times_table = []
    for i in range(1, 10):
        times_table.append(calc_times(i))
    return times_table

def show_times_table():
    tt = times_table()
    print("##########################")
    for i in tt:
        for j in i:
            print(j, end=" ")
        print()
    print("##########################")
    
show_times_table()
