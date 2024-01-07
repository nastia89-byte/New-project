def staff_min_efficiency(staff):
    min_efficiency = 100  
    min_efficiency_employee = None  

    for employee, data in staff.items():
        if 0 <= data['ефективність'] < min_efficiency:
            min_efficiency = data['ефективність']
            min_efficiency_employee = employee

    return min_efficiency_employee

def staff_max_efficiency(staff):
    max_efficiency = 0  
    max_efficiency_employee = None  

    for employee, data in staff.items():
        if 0 <= data['ефективність'] > max_efficiency:
            max_efficiency = data['ефективність']
            max_efficiency_employee = employee

    return max_efficiency_employee

staff = {
    'Петрик': {'посаду': 'менеджер з продажу', 'ефективність': 86},
    'Ткач': {'посаду': 'менеджер з продажу', 'ефективність': 69},
    'Костін': {'посаду': 'менеджер з продажу', 'ефективність': 78},
    'Костилєв': {'посаду': 'менеджер з продажу', 'ефективність': 91},
    'Борисенко': {'посаду': 'менеджер з продажу', 'ефективність': 99}
}

best_employee = staff_max_efficiency(staff)
worst_employee = staff_min_efficiency(staff)

print('Кращий результат:',  staff[best_employee]['ефективність'])
print('Найгірший результат:', staff[worst_employee]['ефективність'])
