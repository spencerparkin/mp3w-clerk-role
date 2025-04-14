# person.py

from datetime import date

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
            date['last_sacrament_prayer_date'] = date.strftime('%Y-%m-%d')
        else:
            date['last_sacrament_prayer_date'] = None
        return data

    def from_json(self, data):
        self.last_name = data['last_name']
        self.first_name = data['first_name']
        if 'last_sacrament_prayer_date' in data:
            self.last_sacrament_prayer_date = date.fromisoformat(data['last_sacrament_prayer_date'])
        else:
            self.last_sacrament_prayer_date = None
        return self