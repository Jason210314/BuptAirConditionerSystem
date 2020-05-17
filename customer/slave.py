from operator import attrgetter


class Slave:
    def __init__(self, room_id: str, req_time: int, sp_mode: int, is_pause: int):
        self.room_id = room_id
        # 接受送风服务的开始时间或者 无送风服务的等待开始时间
        self.req_time = req_time
        self.sp_mode = sp_mode
        self.inverse_sp = 2 - sp_mode
        self.is_pause = is_pause
        self.is_run = False

    def __repr__(self):
        return repr((self.room_id, self.sp_mode, self.req_time, self.is_pause, self.is_run))

    __str__ = __repr__


if __name__ == '__main__':
    slist = []
    slist.append(Slave('1001', 999, 1, 0))
    slist.append(Slave('1002', 1000, 2, 0))
    slist.append(Slave('1003', 800, 1, 0))
    slist.append(Slave('1004', 800, 2, 1))
    slist.sort(key=attrgetter('is_pause', 'inverse_sp', 'req_time'))
    print(slist)
