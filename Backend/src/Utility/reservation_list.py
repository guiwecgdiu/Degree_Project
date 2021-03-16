reservation_list = []

def get_list():
    return reservation_list


def update_list(l):
    global reservation_list
    l = map(eval, l)
    reservation_list = list(l)
    return reservation_list


def add_list(r):
    global reservation_list
    if reservation_list:
        reservation_list.insert(0,r)
        print(reservation_list)
        return reservation_list

def delete_res(id):
    global reservation_list
    if reservation_list and id:
        reservation_list.pop(int(id))
        return reservation_list