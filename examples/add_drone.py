from random import randint
import pandas as pd


file_name =  '../values/Drones.xlsx'

cont = True

dict = {'ID': [],
        'Charge[out of 100]': [], 
        'Parent drone' : [], 
        'Vx[m/s]' : [],
        'Vy[m/s]' : [],
        'Vz[m/s]' : [],
        'X[m]' : [],
        'Y[m]': [], 
        'Z[m]' : [],
        'Reliability_factor' : [],
}

while(cont):
    type = input('Enter type of drone (1 for parent, 2 for child): ')
    if type == '1':
        dict['ID'].append('PD'+str(randint(0,100)) +input('Enter ID no: '))
        dict['Parent drone'].append(True)
        dict['Reliability_factor'].append(input('Enter Reliability_factor(max 1): '))
    elif type == '2':
        dict['ID'].append('CD'+str(randint(0,100)) +input('Enter ID no: '))
        dict['Parent drone'].append(False)
    else:
        print('Invalid input')
        continue
    dict['Charge[out of 100]'].append(input('Enter charge(Out of 100): '))
    dict['Vx[m/s]'].append(input('Enter Vx[m/s]: '))
    dict['Vy[m/s]'].append(input('Enter Vy[m/s]: '))
    dict['Vz[m/s]'].append(input('Enter Vz[m/s]: '))
    dict['X[m]'].append(input('Enter X[m]: '))
    dict['Y[m]'].append(input('Enter Y[m]: '))
    dict['Z[m]'].append(input('Enter Z[m](max 49.9): '))
    cont = input('Do you want to continue? (y/n): ')
    if cont == 'n':
        cont = False




df = pd.read_excel(io=file_name)

df2 = pd.DataFrame.from_dict(dict)

df3 = pd.concat([df, df2], ignore_index = True)
df3.reset_index()
df3.to_excel(file_name, index=False)
