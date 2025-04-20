# person.py

from datetime import date, datetime

class Person:
    def __init__(self, last_name = '', first_name = ''):
        self.last_name = last_name
        self.first_name = first_name
        self.last_sacrament_prayer_date = None

    def to_json(self):
        data = {
            'last_name': self.last_name,
            'first_name': self.first_name
        }
        if self.last_sacrament_prayer_date is not None:
            date['last_sacrament_prayer_date'] = self.last_sacrament_prayer_date.strftime('%m-%d-%Y')
        else:
            date['last_sacrament_prayer_date'] = None
        return data

    def from_json(self, data):
        self.last_name = data['last_name']
        self.first_name = data['first_name']
        if 'last_sacrament_prayer_date' in data:
            self.last_sacrament_prayer_date = datetime.strptime(data['last_sacrament_prayer_date'], "%m-%d-%Y").date()
        else:
            self.last_sacrament_prayer_date = None
        return self