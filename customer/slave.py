from operator import attrgetter
from customer.models import State
from airconfig.config import config
TEMP_RATE = config.temp_rate


class Slave:
    def __init__(self, room_id: str, phone_num: str, req_time: int, sp_mode: int):
        self.room_id = room_id
        self.phone_num = phone_num
        # 接受送风服务的开始时间或者 无送风服务的等待开始时间
        self.req_time = req_time
        self.sp_mode = sp_mode
        self.inverse_sp = 2 - sp_mode
        self.temp_rate = TEMP_RATE # 默认的每分钟温度变化率
        self.wait_timer = False

    def init_state(self, room_id, goal_temp, curr_temp, sp_mode, work_mode):
        state, _ = State.objects.get_or_create(room_id=room_id)
        state.goal_temp = goal_temp
        state.curr_temp = curr_temp
        state.sp_mode = sp_mode
        state.work_mode = work_mode
        state.is_on = True
        state.is_work = False
        state.save()

    def set_curr_temp(self, curr_temp):
        state = State.objects.get(room_id=self.room_id)
        state.curr_temp = curr_temp
        state.save()

    def add_fee(self, delta_fee):
        state = State.objects.get(room_id=self.room_id)
        state.total_cost += delta_fee
        state.save()

    def change_fan_spd(self, sp_mode):
        state = State.objects.get(room_id=self.room_id)
        state.sp_mode = sp_mode
        state.save()

    def change_goal_temp(self, goal_temp):
        state = State.objects.get(room_id=self.room_id)
        state.goal_temp = goal_temp
        state.save()

    def change_work_mode(self, work_mode):
        state = State.objects.get(room_id=self.room_id)
        state.work_mode = work_mode
        state.save()

    def set_is_on(self, is_on):
        state = State.objects.get(room_id=self.room_id)
        state.is_on = is_on
        state.save()

    def set_is_work(self, is_work):
        state = State.objects.get(room_id=self.room_id)
        state.is_work = is_work
        state.save()

    def get_is_work(self):
        state = State.objects.get(room_id=self.room_id)
        return state.is_work

    def get_curr_temp(self):
        state = State.objects.get(room_id=self.room_id)
        return state.curr_temp

    def set_goal_temp(self, goal_temp):
        state = State.objects.get(room_id=self.room_id)
        state.goal_temp = goal_temp
        state.save()

    def get_goal_temp(self):
        state = State.objects.get(room_id=self.room_id)
        return state.goal_temp

    def get_poll_state(self):
        state = State.objects.get(room_id=self.room_id)
        return state.curr_temp, state.total_cost, state.is_work

    def get_all_state(self):
        state = State.objects.get(room_id=self.room_id)
        return state

    def __repr__(self):
        return repr((self.room_id, self.sp_mode, self.req_time, self.temp_rate, self.wait_timer))

    __str__ = __repr__


if __name__ == '__main__':
    slist = []
    slist.append(Slave('1001', 999, 1, 0))
    slist.append(Slave('1002', 1000, 2, 0))
    slist.append(Slave('1003', 800, 1, 0))
    slist.append(Slave('1004', 800, 2, 1))
    slist.sort(key=attrgetter('is_pause', 'inverse_sp', 'req_time'))
    print(slist)
