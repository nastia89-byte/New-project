staff = {
        'Фроленко': {
            'посаду': 'маркетолог',
            'ефективність': 71
        },
        'Палій': {
            'посаду': 'маркетолог',
            'ефективність': 65
        },
        'Ковалець': {
            'посаду': 'маркетолог',
            'ефективність': 49
        },
        'Лисенко': {
            'посаду': 'маркетолог',
            'ефективність': 53
        }
}

def find_inefficient_employee(employees):
    inefficient_employee = None

    for last_name, data in employees.items():
        efficiency = data['ефективність']
        if efficiency < 50:
            inefficient_employee = last_name
            break

    if inefficient_employee:
        print(f"Співробітник {inefficient_employee} рекомендований до звільнення")
    else:
        print("")

    return inefficient_employee

inefficient_employee = find_inefficient_employee(staff)

if inefficient_employee:
    del staff[inefficient_employee]

print("Ефективні співробітники:")
for last_name in staff:
    print(last_name)