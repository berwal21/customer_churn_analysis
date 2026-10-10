import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Customer-Churn.csv')

# replace blanks with 0 as tenure is 0 and no totalcharges is recorded
df['TotalCharges'] = df['TotalCharges'].replace(" ","0")
df['TotalCharges'] = df['TotalCharges'].astype("float")

# converted values 0 and 1 of  seniorcitizen to yes/no to make it easier to understand 
def conv(values):
    if values == 1:
        return "yes"
    else:
        return "no"

df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv)

#print(df.info())
# ax = sns.countplot(x='Churn', data= df)
# ax.bar_label(ax.containers[0])
#plt.title("Count of Churned customer")
# plt.show()

# plt.figure(figsize=(3,4))
# gb = df.groupby('Churn').agg({'Churn':'count'})
# plt.pie(gb['Churn'], labels=gb.index, autopct='%1.2f%%')
# plt.title('Percentage of Churned Customer', fontsize=10)
# plt.show()
# from the given pie chart we can conclude that 26.54% of our customer have churned out 

# now let's figure out the reason

# plt.figure(figsize=(4,4))
# sns.countplot(x = "gender" , data=df, hue="Churn")
# plt.title("Churn By Gender")
# plt.show()



# comparitive a greater percentage of people in senior citizen have churned
# plt.figure(figsize=(4,4))
# sns.countplot(x = "SeniorCitizen" , data=df, hue="Churn")
# plt.title("Churn By SeniorCitizen")
# plt.show()

plt.figure(figsize=(4,4))
sns.histplot(x='tenure', data=df, bins=30, hue='Churn')
plt.show()

#people who have used our services for long time have stayed and people who have used for 1 or 2 months have churned


plt.figure(figsize=(4,4))
ax =sns.countplot(x = "Contract" , data=df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churn By Contract")
plt.show()

#people who have month to month contract are likley to churn then those who have 1 or 2 years of contract