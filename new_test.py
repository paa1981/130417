print('Gluuuuuuu')
# 1. Given the workers list, divide it in two lists: males and females.
# 2. Given the workers list, sort it by age.
# 3. Find and return the dict which contains data related to Robert.
# 4. Create .csv file and write all this rows and header there*
# 5. Given the workers list, create the list of managers*
# 6. Return the length of workers list.
# 7. Remove Masha from workers list and return the list.
# 8. Add new person (data doesn’t matter) and return the list.

workers_list = [
    {'name': 'Lisa', 'age': 30, 'gender': 'f', 'position': 'Accountant'},
    {'name': 'Mike', 'age': 45, 'gender': 'm', 'position': 'Manager'},
    {'name': 'Nick', 'age': 25, 'gender': 'm', 'position': 'Office Manager'},
    {'name': 'Vera', 'age': 21, 'gender': 'f', 'position': 'Support Manager '},
    {'name': 'Masha', 'age': 33, 'gender': 'f', 'position': 'Accountant'},
    {'name': 'Igor', 'age': 50, 'gender': 'm', 'position': 'Manager'},
    {'name': 'John', 'age': 25, 'gender': 'm', 'position': 'Support'},
    {'name': 'Silvia', 'age': 38, 'gender': 'f', 'position': ' Support  Manager'},
    {'name': 'Robert', 'age': 31, 'gender': 'm', 'position': 'Head of department'}

]



def gender_workers(workers_list):
    # males = []
    # females = []
    # for worker in workers_list:
    #     if worker['gender'] == 'f'
    #         females.append(worker)
    #     else:
    #         males.append(worker)
    # return females, males
    males = [worker for worker in workers_list if worker['gender'] == 'm']
    females = [worker for worker in workers_list if worker['gender'] == 'f']
    return females, males
gender_workers(workers_list)
print('1) Females and Males')
for i in gender_workers(workers_list):
    print(i)


def age_workers(workers_list):
    from21to30 =[]
    from31to40 = []
    from41to50 = []
    for worker in workers_list:
        if worker['age'] <= 30:
            from21to30.append(worker)
        elif worker['age'] <=40:
            from31to40.append(worker)
        else:
            from41to50.append(worker)
    return from21to30, from31to40, from41to50

age_workers(workers_list)
print()
print ('2) Age groups: up to 30, 40, others')
for i in age_workers(workers_list):
    print (i)


def sort_workers(workers_list):
    man = []
    for worker in workers_list:
        if worker['name'] == 'Robert':
            man.append(worker)

    return man
sort_workers(workers_list)
print()
print('3) Who is Robert?')
for i in sort_workers(workers_list):
    print(i)

def write_csv(workers_list):
    import csv
    with open('vikaquiz.csv', 'w') as csvfile:
        for worker in workers_list:
            csvfile.write(worker)

def manager_list(workers_list):
    manager = []
    for worker in workers_list:
        if 'Manager' in worker['position']:
            manager.append(worker)
    return  manager
manager_list(workers_list)
print()
print('5) All managers here: ')
for i in manager_list(workers_list):
    print(i)


def lenth_list(workers_list):
    return len(workers_list)

print()
print('6) the length of workers list is ', lenth_list(workers_list))


def masha_remove(workers_list):
    for worker in workers_list:
        if worker['name'] == 'Masha':
            workers_list.remove(worker)
    return workers_list

masha_remove(workers_list)
print()
print('7) Nobody loves Masha...')
for i in masha_remove(workers_list):
    print(i)

def add_worker(workers_list):
    fresher = {'name': 'Dexter', 'age': 38, 'gender': 'm', 'position': 'Cereal Killer'}
    workers_list.append(fresher)
    return workers_list

x = add_worker(workers_list)
print()

print ('8) There is a fresher!')
for i in x:
    print(i)

################ 2nd ########################


