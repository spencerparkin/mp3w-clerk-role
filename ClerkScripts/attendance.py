# attendance.py -- Quick script to calculate attendance taken during Sacrament meeting.

from Levenshtein import distance

class Family:
    def __init__(self, name, heads, count):
        self.name = name
        self.heads = heads
        self.count = count

family_list = [
    Family('Anderson', ['Benjamin', 'Tammy'], 8),
    Family('Anderson', ['Chesna'], 1),
    Family('Austin', ['Eugene Paul', 'Jessica'], 1),
    Family('Barker', ['David', 'Darlene'], 2),
    Family('Barker', ['Lee', 'Rachel'], 6),
    Family('Barnes', ['Mary'], 4),
    Family('Bastian', ['Diane'], 1),
    Family('Bates', ['Elizabeth'], 1),
    Family('Bates', ['Janet'], 1),
    Family('Bates', ['John'], 1),
    Family('Bates', ['Suzanne'], 2),
    Family('Bates', ['William'], 1),
    Family('Bean', ['Noriene'], 1),
    Family('Bearnson', ['Rhea'], 1),
    Family('Benett', ['David', 'Lorreen'], 2),
    Family('Bertot', ['Emil', 'Ruth'], 5),
    Family('Bruderer', ['Jacob', 'Nicole'], 5),
    Family('Bryant', ['Aaron', 'Bethany'], 5),
    Family('Budge', ['Michael', 'Kara'], 4),
    Family('Budge', ['Taya'], 1),
    Family('Burr', ['Melanee'], 1),
    Family('Burt', ['Joshua', 'Hanna'], 6),
    Family('Calder', ['David', 'Evelyn'], 3),
    Family('Calder', ['Heather'], 4),
    Family('Callister', ['Mark', 'Carrie'], 2),
    Family('Carter', ['Sam', 'Melissa'], 3),
    Family('Chaffee', ['Philip', 'Stephanie'], 3),
    Family('Christensen', ['David'], 4),
    Family('Clegg', ['Cameron', 'Dusty'], 2),
    Family('Clement', ['Molly'], 2),
    Family('Coleby', ['April Dawn'], 1),
    Family('Cook', ['Mason', 'Emily'], 7),
    Family('Cordon', ['Weston', 'Allie'], 5),
    Family('Craven', ['Brett', 'Shelly'], 3),
    Family('Davies', ['Tyrone', 'Marisa'], 8),
    Family('Doxey', ['Tom', 'Bethani'], 6),
    Family('Duston', ['Mark', 'Tracy'], 2),
    Family('Felix', ['Nathan', 'Kara'], 2),
    Family('Flores', ['Jesus', 'Elizabeth Kailani'], 3),
    Family('Fowler', ['Richard', 'Caitlin'], 6),
    Family('Fratto', ['Wayne'], 2),
    Family('Freckleton', ['Json', 'Haley'], 6),
    Family('Geertgens', ['Christine Audry'], 1),
    Family('Gold', ['Jalynn'], 1),
    Family('Gonzalez', ['Rodrigo', 'Gina Rene'], 2),
    Family('Grieve', ['Cally'], 1),
    Family('Griffin', ['Donald', 'Karen'], 2),
    Family('Guertin', ['Ronald Wayne', 'Dana'], 1),
    Family('Habashi', ['Saeed', 'Judith'], 1),
    Family('Hanks', ['Mike', 'Annette'], 2),
    Family('Hardy', ['Christina'], 1),
    Family('Haviland', ['Kade', 'Jessica'], 6),
    Family('Heiner', ['Jonathan Ray', 'Ali'], 6),
    Family('Howard', ['Jerry', 'Joy'], 2),
    Family('Hughes', ['William', 'Lori'], 3),
    Family('Hulet', ['Stephen', 'Lisa'], 6),
    Family('Jarman', ['Lee', 'Colette'], 3),
    Family('Jaynes', ['Mark', 'Elaine'], 2),
    Family('Jeppson', ['Peter', 'Marj'], 2),
    Family('Jones', ['Jeremy'], 1),
    Family('Kikuchi', ['Yoshihiko', 'Toshiko'], 2),
    Family('Klc', ['Thomas', 'Cydney'], 4),
    Family('Lahn', ['Steve', 'Lucinda'], 7),
    Family('Larson', ['Bert', 'Betty'], 2),
    Family('Leavitt', ['Marth'], 1),
    Family('Ledezma Madrigal', ['Filiberto', 'Magdalena'], 2),
    Family('Ledezma Soto', ['Nefily', 'Rose'], 4),
    Family('Leigh', ['Stephen', 'Sara'], 4),
    Family('Loveless', ['Max', 'Julianne Joyce'], 7),
    Family('Mallet', ['Connie'], 1),
    Family('Randall', ['Fernando', 'Jennie Elizabeth'], 3),
    Family('Martin', ['Jim'], 1),
    Family('McDonald', ['Kerry'], 1),
    Family('Meeks', ['Jessica'], 1),
    Family('Meeks', ['Lee', 'cora'], 3),
    Family('Meono', ['Andrew'], 3),
    Family('Meono', ['Ed', 'Carol'], 2),
    Family('Mercer', ['Gary', 'Susan'], 2),
    Family('Merkley', ['Scott'], 4),
    Family('Miller', ['David'], 1),
    Family('Mills', ['Calvin', 'Ruth'], 2),
    Family('Moore', ['Adam'], 3),
    Family('Morse', ['Patric Nicholas'], 1),
    Family('Moss', ['James'], 2),
    Family('Muir', ['Robbin'], 1),
    Family('Myers', ['Rick', 'Peggy'], 2),
    Family('Nakaya', ['Mas', 'Shauna'], 2),
    Family('Nakaya', ['Ryan', 'Leslie'], 2),
    Family('Nelson', ['Brad'], 1),
    Family('Nelson', ['Matt', 'Kelli'], 6),
    Family('Nelson', ['Neal', 'Roberta'], 2),
    Family('Nielson', ['Joshua', 'Chyrese'], 4),
    Family('Parkin', ['Spencer', 'Melinda'], 4),
    Family('Passey', ['Karen'], 1),
    Family('Pettit', ['Mitch', 'Katelyn'], 3),
    Family('Pitcher', ['Jed', 'MerLynn'], 2),
    Family('Rankin', ['Judy'], 1),
    Family('Reimann', ['Joshua', 'Ali'], 3),
    Family('Rhodes', ['Del', 'Susan'], 2),
    Family('Roach', ['Gloria'], 1),
    Family('Roberts', ['Stan', 'Liz'], 2),
    Family('Rodger', ['Scott', 'Teresa'], 6),
    Family('Sadler', ['Jamie', 'Lori'], 2),
    Family('Schulthies', ['Brad', 'Jane'], 5),
    Family('Shaffer', ['Bonnie'], 1),
    Family('Simon', ['David', 'Mindy'], 3),
    Family('Sims', ['Allen', 'Karen'], 2),
    Family('Smith', ['Peter', 'Alysha'], 1),
    Family('Smith', ['Blaine', 'Becky'], 2),
    Family('Smith', ['Gail'], 1),
    Family('Smith', ['Wally', 'Cecil'], 2),
    Family('Spain', ['Anne'], 1),
    Family('Stagg', ['Brian', 'Stephanie'], 6),
    Family('Staley', ['Jacy'], 6),
    Family('Staples', ['Dona'], 4),
    Family('Staples', ['Kiley'], 1),
    Family('Stapley', ['Ben', 'Cami'], 6),
    Family('Stromberg', ['Ron', 'Helen'], 2),
    Family('Su', ['Erick', 'Olivia'], 4),
    Family('Thomas', ['Brett', 'Jennifer'], 3),
    Family('Thorup', ['Cheryl'], 1),
    Family('Tuttle', ['Eric', 'Kim'], 3),
    Family('Twitchell', ['Joshua', 'Aubrey'], 2),
    Family('Walker', ['Darren', 'Kim'], 5),
    Family('Wangerin', ['June'], 1),
    Family('Wangerin', ['Steven'], 1),
    Family('Watts', ['Joseph', 'Lynette'], 4),
    Family('Wayman', ['Logan Alexander', 'Steph'], 1),
    Family('Weiland', ['Kurt', 'Kathy'], 3),
    Family('West', ['Steve', 'Miriam'], 5),
    Family('Whipple', ['Carol'], 1),
    Family('Wilson', ['Brent', 'Stefani'], 4)
]

count_list = [
    6, 4, 15, 9, 10, 10, 15, 12, 11, 14, 9, 13,
    2, 1, 4, 5, 7, 3, 10, 5, 4, 2
]

zoom_list = [
    'Gail',
    'Hughes',
    'Harmony',
    'Larsons',
    'Howards',
    'Rose Ledezma',
    'Jaynes',
    'Thomas Lahn',
    'Karen',
    'Stella',
    'Kara',
    'Bennett'
]

if __name__ == '__main__':

    average_family_size = 0.0
    for family in family_list:
        average_family_size += float(family.count)
    average_family_size /= float(len(family_list))
    print('Average family size: %f' % average_family_size)

    attendance_count = sum(count_list)
    print('In-person count: %d' % attendance_count)

    zoom_count_list = [1, 3, 1, 2, 2, 4, 2, 1, 1, 1, 1, 2]
    zoom_count = sum(zoom_count_list)
    print('Zoom count: %d' % zoom_count)

    total = zoom_count + attendance_count
    print('Total: %d' % total)