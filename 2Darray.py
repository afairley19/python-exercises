# HackerRank practice 2D Array - DS

def hourglassSum(arr):

    hourglass_max = -1000
    s = []
    sub_array = []

    for i in range(4):
        for col in range(4):
            for row in range(3):
                sub_array.append(arr[row + i] [col:col + 3])
                s = sub_array
            hourglass_sum = sum_list(s[0]) + s [1][1] + sum_list(s[2])
            if (hourglass_max < hourglass_sum):
                hourglass_max = hourglass_sum
            sub_array = []
    return hourglass_max

def sum_list(list1):

    total = 0

    for value in range(0, len(list1)):
        total = total + list1[value]
    return total
