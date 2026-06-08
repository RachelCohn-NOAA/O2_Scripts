### Testing TRT file read in ###

import pandas as pd

trt_file = r"C:\Users\rachel.cohn\Downloads\HG26081_001.dat_ABR_TRT"

#this works but is still a little messy
#from Gemini AI and then altered

#reads file into data frame with one column where everything is a string
trt = pd.read_csv(trt_file, sep='|', names=['raw'], engine='python')

#it also works to just split by comma but the data frame looks a bit messier than filtering out non-comma rows
test = trt['raw'].str.split(',', expand=True)

#Filter: keep only rows that have a comma
trt = trt[trt['raw'].str.contains(',', na=False)]

#split that single column into multiple columns based on the comma
trt_clean = trt['raw'].str.split(',', expand=True)


test = trt['raw'].str.split(',', expand=True)
