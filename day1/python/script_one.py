import sys, pandas
import matplotlib.pyplot as plt
col = sys.argv[2]
input_file = sys.argv[1]
df=pandas.read_csv(input_file,sep='\t')
plt.hist(df[col])
plt.show()