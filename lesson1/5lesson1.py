#Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

earn = input('Введите сумму выручки компании\n')
costs = input('Введите сумму расходов компании\n')
if int(earn) > int(costs):
    print('Компания работает с прибылью')
    prof = (int(earn) - int(costs)) / int(earn)
    employees = input('Веедите количество сотрудников компании\n')
    prof_employees = (int(earn) - int(costs)) / int(employees)
    print(f'Рентабельность выручки составляет -\n{round(prof, 2)}')
    print(f'Прибыль компании в расчете на одного сотрудника составляет -\n{round(prof_employees, 2)}')
else:
    print('Компания работает в убыток')
