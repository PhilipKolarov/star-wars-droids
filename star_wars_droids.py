def droid_sort(droid_string):
    droid_list = []
    while droid_string != 'End':
        droid_list.append(droid_string)
        droid_string = input()

    list_as_string = ' '.join(droid_list)
    return list_as_string


import re

print("Start entering R2 unit names to check if they are valid. Once you are done, type 'End' to finish your list.")
r2_unit_string = input()
r2_unit_list_as_string = droid_sort(r2_unit_string)

expression = r'R[0-9]\-[A-Z]\d{1,2}'
matches = re.findall(expression, r2_unit_list_as_string)

for match in matches:
    if match == "R2-D2":
        print(f"{match} - Main character included!")
    else:
        print(match)

print("Start entering protocal droid names to check if they are valid. Once you are done, type 'End' to finish your list.")
protocal_droid_string = input()
protocal_droid_list_as_string = droid_sort(protocal_droid_string)

expression = r'([A-Z]{1,2})(\-)([0-9]{1,2})([A-Z]{2})*'
matches = re.findall(expression, protocal_droid_list_as_string)

for match in matches:
    current_droid = ""
    for el in match:
        current_droid += el
    if current_droid == 'C-3PO':
        print(f"{current_droid} - Main character included!")
    else:
        print(current_droid)
