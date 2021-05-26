 temp = []
max_t = ''
min_t = ''
days = 0
min_error = 0
max_error = 0
t_error = 0
avg_max_temp = 0
avg_min_temp = 0
error_days = 0

# Creation of the list containing the temperatures
while max_t != '0' or min_t != '0':
    min_t = input('Please enter the minimum temperature for the day: ')
    max_t = input('Please enter the maximum temperature for the day: ')
    tem = (min_t, max_t) 
    temp.append(tem)
temp = temp[0:len(temp)-1]
print(temp)
# Iterating over the list
for pair in temp:
    #Counting number of days of the field trip
    days += 1
print(f'The number of the days the field trip took was {days}')

# Iterating over the pairs
for (index, tuple) in enumerate(temp):
    min_d = int(tuple[0])
    max_d = int(tuple[1])
    if min_d < 5 or max_d > 35:
        error_days += 1
    # Checking for values less than 5
    if min_d < 5:
        min_error += 1
    else:
        avg_min_temp += min_d

    # Checking for values bigger than 35
    if max_d > 35:
        max_error += 1
    else:
        avg_max_temp += max_d

t_error = min_error + max_error 
avg_max_temp = avg_max_temp / (days - max_error)
avg_min_temp = avg_min_temp / (days - min_error)
print(error_days)

print(f'The number of days that the temperatures were less than 5 was {min_error}')
print(f'The number of days that the temperatures were more than 35 was {max_error}')
print(f'The number of days that registered errors during the field trip was {t_error}')
print(f'The average maximum temperature during the field trip was {avg_max_temp}')
print(f'The average minimum temperature during the field trip was {avg_min_temp}')
print(f'The percentage of days that registered error compared to he correct registries is {error_days/days * (100)}%')