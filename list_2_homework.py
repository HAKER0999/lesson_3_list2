
# HOMEWORK LIST_2👇👇👇:

def task_1(filter_list, number):
    for x in filter_list:
        if type(x) == int:
            number.append(x)
    return number

print(task_1([1, 2, 3, "a", "b", 4], []))



def task_2(add_indexes, numbers):
    for num, index in enumerate(add_indexes):
        f = num + index
    return f
print(task_2([1, 2, 3, 4, 5], []))



def task_3(list, list2):
    for x in list:
        if 6 < x:
           list2.append(x)
    return list2
print(task_3([7, 4, 17, 14, 12, 3], []))



def task_4(numbers):
    first = numbers[0]
    ortasida = numbers[1: -1]
    end = numbers[-1]
    return first, end
print(task_4([1, 2, 3, 4, 5, 6]))



def task_5(characters):
    spread = len("".join(characters))
    return spread
print(task_5(["###", "###", "###"] ))



def task_6(lst, num):
    lst.append(num)
    return lst
print(task_6([1, 3, 2, 4, 4, 1], int(input("Num: "))))



def task_7(lists, lists2, num):

    if num in lists: 
        if num in lists2:
            return True
        else:
            return False
    else:
        return False
print(task_7([3, 2], [2, 3], 1))



def task_8():
    line = [5, 6, 7, 8, 9]
    num = int(input("Son: "))
    line.pop(0)
    line.append(num)
    print(line)
task_8()



def task_9(list, list2):
    for x in list:
        list2.append(x)
    list.append(list2)
    return list
print(task_9(["x", "y"], []))



def task_10(lst, lst2):
    for x in lst:
        if type(x) == int:
            lst2.append(x)
    return lst2
print(task_10([9, 2, "space", "car", "lion", 16], []))








