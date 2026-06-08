#O2 Profile from Merged File

#example below is from GO-SHIP A13.5 2024
#merged file may change depending on cruise and code needs to be altered

#%%
#import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#%%

#%%

#read in merged file

file_path_merged = r"C:\Users\rc_local\Documents\Jujube\Oxygen\33H320240201_hy1.csv"
df_merged = pd.read_csv(file_path_merged, skiprows = 10, header = [0,1])
#df_merged.head()
#df_merged.info()
#%%

#%%
#plot o2 profile

#convert columns to numpy arrays 
stn = np.array(df_merged['STNNBR'])
prs = np.array(df_merged['CTDPRS'])
o2_ctd = np.array(df_merged['CTDOXY'])
o2 = np.array(df_merged['OXYGEN'])
o2_flag = np.array(df_merged['OXYGEN_FLAG_W'])
sal = np.array(df_merged['SALNTY'])

#figure out how to remove values based on QC flag (i.e. remove if o2_flag == 4)
#remove bad values from array 

#one way
#condition = lambda o2_flag: o2_flag == 9

#o2_filtered = list(filter(lambda o2_flag: not condition(o2_flag), o2))
#o2_filtered_arr = np.array(o2_filtered)

#prs_filtered = list(filter(lambda o2_flag: not condition(o2_flag), prs))
#prs_filtered_arr = np.array(prs_filtered)

#remove negative values from o2 data--won't get rid of all known bad (4), but will get rid of -999 and negative values
o2_pos = o2[o2>=0]
prs_pos = prs[o2>=0]
stn_pos = stn[o2>=0]

#plot
fig, ax = plt.subplots(figsize = (6, 9))
stn_plot = 113
plt.plot(o2_ctd[stn == stn_plot], prs[stn == stn_plot], color = 'blue', marker = 'o', linestyle = 'dotted', label = 'CTD O2')
plt.plot(o2_pos[stn_pos == stn_plot], prs_pos[stn_pos == stn_plot], color = 'orangered', marker = 'o', linestyle = 'dotted', label = 'Discrete O2')
ax.invert_yaxis()

#plot accoutrements 
ax.set_xlabel('O2 (umol/kg)')
ax.set_ylabel('Pressure (dbar)')
ax.legend()
plt.grid()
title_str = 'A13.5 Station {} Oxygen Profile'.format(stn_plot)
plt.title(title_str);

plt.show()
#%%
