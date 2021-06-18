from . import timeHelper

wait_time = 1800 #seg


def add_member(person_name, command):
    time = timeHelper.get_unix_time()
    f = open("features/blacklist.txt", "a")
    f.write(person_name + "\t" + str(time) + "\t" + command +"\n")
    f.close()


def free_members():
    actual_hour = timeHelper.get_unix_time()
    blacklist = open("features/blacklist.txt", "r")
    new_black_list = []
    lines = blacklist.readlines()
    for line in lines:
        if line is not None:
            separated_data = line.split("	")
            dif = actual_hour - int(separated_data[1])
            if dif < wait_time:
                new_black_list.append(line)
    f = open("features/blacklist.txt", "w")
    for line in new_black_list:
        f.write(line)
    f.close()


def is_member_in_blacklist(person_name, command):
    #print(person_name)
    is_name_in_blacklist = False
    blacklist = open("features/blacklist.txt", "r")
    lines = blacklist.readlines()
    for line in lines:
        if line is not None:
            if (person_name in line) and (command in line):
                is_name_in_blacklist = True
                break
    return is_name_in_blacklist