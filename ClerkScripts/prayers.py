# payers.py

import datetime
import json

from person import Person

if __name__ == '__main__':
    with open('ward_members.json', 'r') as handle:
        json_text = handle.read()
        json_data = json.loads(json_text)

    ward_member_list = json_data['ward_members']
    ward_member_list = [Person().from_json(ward_member) for ward_member in ward_member_list]

    # TODO: Sort ward member list by prayer date.

    for ward_member in ward_member_list:
        print('Ward member: %s %s' % (ward_member.first_name, ward_member.last_name))