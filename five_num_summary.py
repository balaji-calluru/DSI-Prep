def mean(lst, trim_by=0):
    lst_ = lst.copy()
    if trim_by > 0:
        lst_ = sorted(lst_)[trim_by: -trim_by]
    return sum(lst_) / len(lst_)

def median(lst):
    lst_ = sorted(lst)
    mid_idx = int(len(lst) / 2)
    if len(lst) % 2 == 1:
        return lst_[mid_idx]
    else:
        return int((lst_[mid_idx-1] + lst_[mid_idx]) / 2)

def q1finder(list_):
    median_ = median(list_)
    mid_idx = 0
    if len(list_) % 2 == 0:
        mid_idx = int(len(list_) / 2)
    else:
        mid_idx = int(len(list_) / 2)
    return list_[0:mid_idx]

def q2finder(list_):
    median_ = median(list_)
    mid_idx = 0
    if len(list_) % 2 == 0:
        mid_idx = int(len(list_) / 2)
    else:
        mid_idx = int(len(list_) / 2)
    print(len(list_), mid_idx)
    return list_[mid_idx:-1]

def five_num_summ(list_of_num):
    sorted_list = sorted(list_of_num)
    min_ = sorted_list[0]
    max_ = sorted_list[-1]
    median_ = median(sorted_list)
    q1 = q1finder(sorted_list)
    q2 = q2finder(sorted_list)
    return min_,q1,median_,q2,max_

a = [1, 2, 4, 9, 3, 5, 25, 6, 10]

print(five_num_summ(a))
