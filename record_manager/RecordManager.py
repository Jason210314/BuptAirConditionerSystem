from customer.models import Ticket, Record, get_current_record, get_current_ticket, create_new_ticket, get_all_ticket
import datetime


class RecordManager:
    @staticmethod
    def add_ticket(room_id, phone_num, sp_mode):
        ticket = create_new_ticket(room_id, phone_num, sp_mode)
        ticket.save()

    @staticmethod
    def plus_ticket_schedule_count(room_id, phone_num):
        ticket = get_current_ticket(room_id, phone_num)
        ticket.schedule_count += 1
        ticket.save()

    @staticmethod
    def plus_ticket_cost(room_id, phone_num, delta_fee, duration):
        ticket = get_current_ticket(room_id, phone_num)
        ticket.cost += delta_fee
        ticket.service_duration += duration
        ticket.save()

    @staticmethod
    def finish_ticket(room_id, phone_num):
        ticket = get_current_ticket(room_id, phone_num)
        if ticket.schedule_count == 0:
            ticket.delete()
        else:
            ticket.end_time = datetime.datetime.now()
            ticket.duration = int((ticket.end_time - ticket.start_time).total_seconds())
            ticket.save()

    @staticmethod
    def add_power_on_record(room_id):
        r = Record.objects.create(room_id=room_id, record_type='power_on', at_time=datetime.datetime.now())
        r.save()

    @staticmethod
    def add_power_off_record(room_id):
        r = Record.objects.create(room_id=room_id, record_type='power_off', at_time=datetime.datetime.now())
        r.save()

    @staticmethod
    def add_goal_temp_record(room_id, goal_temp):
        r = Record.objects.create(room_id=room_id, record_type='goal_temp', goal_temp=goal_temp,
                                  at_time=datetime.datetime.now())
        r.save()

    @staticmethod
    def finish_goal_temp_record(room_id):
        r = get_current_record(room_id=room_id, record_type='goal_temp')
        r.duration = int((datetime.datetime.now() - r.at_time).total_seconds())
        r.save()

    @staticmethod
    def add_work_mode_record(room_id):
        r = Record.objects.create(room_id=room_id, record_type='change_mode', at_time=datetime.datetime.now())
        r.save()

    @staticmethod
    def add_reach_goal_record(room_id):
        r = Record.objects.create(room_id=room_id, record_type='reach_goal', at_time=datetime.datetime.now())
        r.save()

    @staticmethod
    def add_form_record(room_id,date_to,date_from,oc_count,common_temp,choice,common_spd,achieve_count,schedule_count,ticket_count,total_cost):
        r = Record.objects.create(room_id=room_id,date_from = date_from, date_to = date_to,record_type='form',common_temp=common_temp,
        choice=choice,common_spd=common_spd,achieve_count=achieve_count,schedule_count=schedule_count,
        ticket_count=ticket_count,total_cost=total_cost)
        r.save()
    def calc_bill(room_id,phone_num,checkin_date):
        tickets = list(Ticket.objects.filter(room_id=room_id,phone_num=phone_num,start_time__gte=checkin_date))
        total_cost = 0.
        total_use = 0
        for ticket in tickets:
            total_cost += ticket.cost
            total_use += ticket.duration
        return total_cost, total_use

    @staticmethod
    def get_tickets(room_id,phone_num,checkin_date):
        return list(Ticket.objects.filter(room_id=room_id,phone_num=phone_num,start_time__gte=checkin_date))
