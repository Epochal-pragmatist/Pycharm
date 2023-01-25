import datetime, random


def getBithdays(numberOfBirthdays):
    """Возвращаем список объектов дат для случайных дней рождения."""
    birthdays = []
    for i in range(numberOfBirthdays):
        starOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = starOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Возвращает объект даты дня рождения, встречающегося несколько раз в списке дней рождения."""
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


print("""The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.""")

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and 0 < int(response) <= 100:
        numBDays = int(response)
        break
print()

print('Here are', numBDays, 'birthdays:')
birthdays = getBithdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = f'{monthName} {match.day}'
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

print('Generating', numBDays, 'random birthdays 100,000 times ...')
input('Press enter o begin ...')

print('Let\'s run another 100,000 simulation.')
simMatch = 0
for i in range(100_000):
    if i % 5000 == 0:
        print(i, 'simulation run...')
    birthdays = getBithdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulation run.')

probability = round(simMatch/100_000 * 100, 2)
print('Out of 100,000 simulation', numBDays, 'people, there was a')
print('matching birthday in the group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think')
