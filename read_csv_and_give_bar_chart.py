import pandas as pd 
import matplotlib.pyplot as plt
filepath=r"C:\Users\91974\Desktop\iris.csv"
data=pd.read_csv(filepath)
df=pd.DataFrame(data)
X=list(df.iloc[:,3])
Y=list(df.iloc[:,4])
plt.bar(X,Y,color='g')
plt.title("Petal")
plt.xlabel("Petal length")
plt.ylabel("Petalwidth")
plt.show()