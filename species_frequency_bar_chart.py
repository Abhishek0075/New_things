import pandas as pd 
import matplotlib.pyplot as plt
filepath=r"C:\Users\91974\Desktop\iris.csv"
data=pd.read_csv(filepath)
df=pd.DataFrame(data)
X=list(df.iloc[:,5])# Species
set_X=set(X)
l_X=list(set_X)
vesi_count=0
seto_count=0
virg_count=0
for i in X :
    if(i=="Iris-versicolor"):
        vesi_count=vesi_count+1
    elif(i=="Iris-setosa"):
        seto_count=seto_count+1
    elif(i=="Iris-virginica"):
        virg_count=virg_count+1
count_list=[vesi_count,seto_count,virg_count]
plt.bar(l_X,count_list,color='g')
plt.xlabel("Species")
plt.ylabel("Species count")
plt.title("Species frequency")
plt.show()