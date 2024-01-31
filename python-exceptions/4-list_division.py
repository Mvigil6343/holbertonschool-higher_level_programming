#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            n_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            n_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            n_list.append(0)
        except IndexError:
            print("out of range")
            n_list.append(0)
        finally:
            pass
    return n_list
