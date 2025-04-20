# payers.py

import json
import argparse

from person import Person

if __name__ == '__main__':
    # TODO: There should be a way to update our list of ward members from CVS.  I think that LCR can export a CSV of all members.

    arg_parser = argparse.ArgumentParser(prog='Players', description='A program that can help you determine who hasn\'t prayed in a while in church.')
    arg_parser.add_argument('-n', '--never', action='store_true', help='Show all those, and only those, who have never prayed in church according to records.')
    arg_parser.add_argument('-c', '--count', default=10, help='Show given number of people who have prayed in church, starting with the oldest.')

    args = arg_parser.parse_args()

    with open('ward_members.json', 'r') as handle:
        json_text = handle.read()
        json_data = json.loads(json_text)

    ward_member_list = json_data['ward_members']
    ward_member_list = [Person().from_json(ward_member) for ward_member in ward_member_list]

    if args.count is not None:
        prayed_list = list(filter(lambda ward_member: ward_member.last_sacrament_prayer_date is not None, ward_member_list))
        ward_member_list = sorted(prayed_list, key=lambda member: member.last_sacrament_prayer_date)
        print('Showing %d ward members...' % args.count)
        for i in range(args.count):
            ward_member = ward_member_list[i]
            print('%s: %s %s' % (ward_member.last_sacrament_prayer_date.strftime('%m-%d-%Y'), ward_member.first_name, ward_member.last_name))
    elif args.never is not None:
        never_list = list(filter(lambda ward_member: ward_member.last_sacrament_prayer_date is None, ward_member_list))
        print('Showing %s ward members who\'ve never prayed in church according to the record.' % len(never_list))
        for ward_member in never_list:
            print('%s %s' % (ward_member.first_name, ward_member.last_name))
    else:
        print('Oops!')