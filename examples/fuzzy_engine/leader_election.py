from cProfile import label
from turtle import color
from uavlink.drone import parent_drone
import pandas as pd
from uavlink.drone import drone
import yaml
from uavlink.fuzzyparameters.charge_factor import cf
from uavlink.fuzzyparameters.stabilityfactor import sf
from uavlink.fuzzyparameters.primary_link_factor import plf
from uavlink.fuzzyparameters.secondary_link_factor import slf
import matplotlib.pyplot as plt
from uavlink.engine.intersection import intersection
from uavlink.engine.union import union


file_name =  '../values/Drones.xlsx'
config_path = '../values/compression_dilation.yaml'

df = pd.read_excel(io=file_name)

with open(config_path) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)['fuzzy_parameters']

PD = []
CD = []


for index, row in df.iterrows():
    if row['Parent drone']:
        PD.append(parent_drone(row['ID'], row['Charge[out of 100]'],
        [row['X[m]']/1000, row['Y[m]']/1000, row['Z[m]']/1000], [row['Vx[m/s]'],
         row['Vy[m/s]'], row['Vz[m/s]']], row['Reliability_factor']))
    else:
        CD.append(drone(row['ID'], row['Charge[out of 100]'],
        [row['X[m]']/1000, row['Y[m]']/1000, row['Z[m]']/1000], [row['Vx[m/s]'],
         row['Vy[m/s]'], row['Vz[m/s]']]))

cf(PD, CD, data[2]['charge_factor'])
sf(PD, CD, 20,data[3]['stability_factor'])
plf(PD, CD, c_d = data[0]['primary_link_factor'])
slf(PD, CD, cd1 = data[1]['secondary_link_factor'], cd2 = data[4]['connection_factor'])

cf = []
sf = []
plf = []
slf = []
rf = []
Cf = []
inter = []

c = []

for i in PD:
    cf.append(i.cf)
    sf.append(i.sf)
    plf.append(i.plf)
    slf.append(i.slf)
    rf.append(i.rf)
    Cf.append(i.Cf)
    c.append(i.id)
    inter.append(intersection(i.plf, i.slf, i.cf, i.sf, i.rf, i.Cf))


plt.plot(c,cf, linestyle='dotted', label = 'Charge factor')
plt.plot(c,sf, linestyle='dotted', label = 'Stability factor')
plt.plot(c,plf, linestyle='dotted', label = 'Primary link factor')
plt.plot(c,slf, linestyle='dotted', label = 'Secondary link factor')
plt.plot(c,rf, linestyle='dotted', label = 'Reliability factor')
plt.plot(c,Cf, linestyle='dotted', label = 'Connection factor')
plt.plot(c,inter,label = 'Intersection', color = 'red')
plt.plot(c,[0]*len(PD))

leader_drone_ID = c[inter.index(union(inter))]
plt.plot(leader_drone_ID, union(inter), marker="o", markersize=10, markeredgecolor="white", markerfacecolor="black")
print(leader_drone_ID)



plt.legend(['Charge factor', 'Stability factor',
'Primary link factor', 'Secondary link factor',
'Reliability factor', 'Connection factor', 'leader drone']
, loc='lower right')

plt.show()

