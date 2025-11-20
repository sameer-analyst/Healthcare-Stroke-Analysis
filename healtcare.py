import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("healthcare-dataset-stroke-data.csv")

# Step 2: Explore basic details

#preview first 5 row 
print(df.head())   
# summary of numerical column     
print(df.describe())   
# data type and non-null info
df.info()               

# Step 3: Check data quality
print("Missing values:\n", df.isnull().sum())
print("Duplicate records:", df.duplicated().sum())

# Step 4: Clean data - remove rows where missing values 
df.dropna(subset=["bmi"], inplace=True)

# Step 5: Identify stroke patients
stroke_pnt = df[df['stroke'] == 1]
print("Total stroke patients:", len(stroke_pnt))

# Step 6: Calculate overall stroke ratio and percentage
stroke_ratio = round(len(stroke_pnt) / len(df), 4)
print("Overall stroke ratio:", stroke_ratio)
print("Overall stroke percentage:", round(stroke_ratio * 100, 2), "%")

# Step 7: Filter stroke patients by gender
male_strk = df[(df['gender'] == "Male") & (df['stroke'] == 1)]
female_strk = df[(df['gender'] == "Female") & (df['stroke'] == 1)]

# Step 8: Display gender-wise counts
print("Male stroke patients:", len(male_strk))
print("Female stroke patients:", len(female_strk))

# Step 9: Calculate gender-wise stroke percentages
male_avg = round(len(male_strk) / len(df) * 100, 2)
female_avg = round(len(female_strk) / len(df) * 100, 2)

print("Male stroke percentage:", male_avg, "%")
print("Female stroke percentage:", female_avg, "%")

# identify hypertension patient 
hypertension_pnt = df[df["hypertension"]==1]
print("Total hypertension patient",len(hypertension_pnt))

# calculate overall hypertension ratio
hypertension_ratio = round(len(hypertension_pnt)/len(df)*100,2)
print("overall hypertension ratio",hypertension_ratio,"%")

# Gender-wise hypertension ratio
male_hyper = df[(df['gender'] == "Male") & (df['hypertension'] == 1)]
female_hyper = df[(df['gender'] == "Female") & (df['hypertension'] == 1)]
male_hyper_ratio = round(len(male_hyper) / len(df) * 100, 2)
female_hyper_ratio = round(len(female_hyper) / len(df) * 100, 2)
print("Male hypertension ratio:", male_hyper_ratio, "%")
print("Female hypertension ratio:", female_hyper_ratio, "%")

#overall smoking counts 
print(df["smoking_status"].value_counts())

#identify smoker patient
smoke_pnt = df[df["smoking_status"]=="smokes"]
print("Toal smoker patient",len(smoke_pnt))

#non smoker 
non_smoker = df[df["smoking_status"]=="never smoked"]
print("Toal non - smoker ",len(non_smoker))

# ratio in persentage 
non_smoker_ratio = round(len(non_smoker)/len(df)*100,2)
smoker_ratio = round(len(smoke_pnt)/len(df)*100,2)
print("non smoker ratio ",non_smoker_ratio,"%")
print("smoker ratio",smoker_ratio,"%")

#male smoker vs non-smoker
male_smoker = df[(df["gender"]=="Male")&(df["smoking_status"]=="smokes")]
male_non_smoker = df[(df["gender"]=="Male")&(df["smoking_status"]=="never smoked")]
print("Toatl Male smoker",len(male_smoker))
print("Total Male non smoker",len(male_non_smoker))

#female smoker vs non-smoker
print(df.head())
female_smoker = df[(df["gender"]=="Female")&(df["smoking_status"]=="smokes")]
female_non_smoker = df[(df["gender"]=="Female")&(df["smoking_status"]=="never smoked")]
print("Total female smoker",len(female_smoker))
print("Total female non-smoker",len(female_non_smoker))

#male smoker ratio in persentage
male_smoke_ratio = round(len(male_smoker)/len(df)*100,2)

#female smoker ratio in persentage
female_smoke_ratio = round(len(female_smoker)/len(df)*100,2)

print("Male smoker ratio",male_smoke_ratio,"%")
print("Female smoker ratio",female_smoke_ratio,"%")

if male_smoke_ratio > female_smoke_ratio:
    print("Smoking is more common among males.")
else:
    print("Smoking is more common among females.")


def age_group(age):
    if age<=12:
        return "Child"
    elif age<=19:
        return "Teen"
    elif age<=35:
        return "Young Adult"
    elif age<=55:
        return "Adult"
    elif age<=75:
        return "Senior"
    else:
        return "Elderly"
    
df["age_group"] = df["age"].apply(age_group)
print(df["age_group"].value_counts())
age_stroke_ratio = df.groupby("age_group")["stroke"].mean() * 100
print(age_stroke_ratio)

#smoke ratio with age
df["is_smoker"] = df["smoking_status"].apply(lambda x: 1 if x == "smokes" else 0)
age_smoke_ratio = df.groupby("age_group")["is_smoker"].mean()*100
print(age_smoke_ratio)  

#hypertension ratio with age
age_hyper_ratio = df.groupby("age_group")['hypertension'].mean()*100
print(age_hyper_ratio)

def group_bmi(bmi):
    if bmi<=18.5:
        return "Underweight"
    elif bmi<=24.9:
        return "Normalweight"
    elif bmi<=29.9:
        return "Overweight"
    else:
        return "Obese"

df["group_bmi"] = df["bmi"].apply(group_bmi)
print(df["group_bmi"].value_counts())
bmi_stroke = df.groupby("group_bmi")["stroke"].mean()*100
print(bmi_stroke)

#check stroke patient average
stroke_glucose = df[df['stroke']==1]['avg_glucose_level'].mean()
non_stroke_glucose = df[df['stroke']==0]['avg_glucose_level'].mean()
print("Stroke patient avg glucose",round(stroke_glucose,2))
print("Nonstroke patient avg glucose",round(non_stroke_glucose,2))

def glucose_group(glu):
    if glu<100:
        return "Normal"
    elif glu<150:
        return "Prediabetic"
    else:
        return "Diabetic"
    
df["glucose_group"] = df['avg_glucose_level'].apply(glucose_group)
print(df["glucose_group"].value_counts())
glucose_stroke_ratio = df.groupby("glucose_group")["stroke"].mean()*100
print(glucose_stroke_ratio)

import matplotlib.pyplot as plt
import seaborn as sns
ratio = [male_smoke_ratio,female_smoke_ratio]
catogries = ["Male","Female"]
plt.figure(figsize=(6,4))
sns.barplot(x=catogries,y=ratio,color='orange',edgecolor='black') 
for i in range(len(catogries)):
    plt.text(i,ratio[i],str(ratio[i])+"%",ha='center',va='bottom')
plt.title("Gender-wise smoke ratio")
plt.xlabel("Gender")
plt.ylabel("ratio (%)")
plt.grid(axis='y')
plt.show()

#Gender wise hypertension
ratio = [male_hyper_ratio,female_hyper_ratio]
catogries = ["Male","Female"]
plt.figure(figsize=(6,4))
sns.barplot(x=catogries,y=ratio)
for i in range(len(catogries)):
    plt.text(i,ratio[i],str(ratio[i])+"%",ha='center',va='bottom')

plt.title("Gender-wise-hypertension")
plt.xlabel("Gender")
plt.ylabel("ratio(%)")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

#Age-wise-stroke-ratio
plt.figure(figsize=(8,5))
sns.barplot(
    x=age_stroke_ratio.index,
    y=age_stroke_ratio.values,
    palette="viridis"
)

for i, v in enumerate(age_stroke_ratio.values):
    plt.text(i, v, f"{round(v,2)}%", ha='center', va='bottom')

plt.title("Age-wise Stroke Ratio")
plt.xlabel("Age Group")
plt.ylabel("Stroke Ratio (%)")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#Age Wise Smoke Ratio
plt.figure(figsize=(8,4),dpi=150)
sns.lineplot(x=age_smoke_ratio.index,y=age_smoke_ratio.values,color='orange',marker='o',markersize=8)
for i,v in enumerate(age_smoke_ratio.values):
    plt.text(i,v,f"{round(v,2)}%",ha='center',va='bottom')

plt.title("Age_Wise_Smoke_ratio")
plt.xlabel("Age_group")
plt.ylabel("Smoke_ratio(%)")
plt.tight_layout()
plt.grid(axis="y")
plt.xticks(rotation=10)
plt.show()

# Age-wise Hypertension Ratio
plt.figure(figsize=(5,4),dpi=150)
sns.lineplot(x=age_hyper_ratio.index,y=age_hyper_ratio.values,color='red',marker='s',markersize=6)
for i,v in enumerate(age_hyper_ratio.values):
    plt.text(i,v,f"{round(v,2)}%",ha='center',va='bottom')

plt.title("Age-Wise Hypertension Ratio")
plt.xlabel("Age_group")
plt.ylabel("Hypertension Ratio(%)")
plt.tight_layout()
plt.grid(axis='y')
plt.show()

#BMI STROKE RATIO(%)
plt.figure(figsize=(5,4),dpi=150)
sns.barplot(x=bmi_stroke.index,y=bmi_stroke.values,palette="viridis")
for i,v in enumerate(bmi_stroke.values):
    plt.text(i,v,f"{round(v,2)}%",va='bottom',ha='center')
plt.title("BMI_STROKE_RATIO(%)")
plt.xlabel("Bmi_Group")
plt.ylabel("Bmi_Ratio(%)")
plt.tight_layout()
plt.grid(axis="y")
plt.show()

#Glucose Group vs Stroke Ratio
plt.figure(figsize=(5,4),dpi=150)
sns.barplot(x=glucose_stroke_ratio.index,y=glucose_stroke_ratio.values,palette='viridis')
for i,v in enumerate(glucose_stroke_ratio.values):
    plt.text(i,v,f"{round(v,2)}%",va='bottom',ha='center')

plt.title('Glucose_Group v/s Stroke Ratio(%)')
plt.xlabel('Glucose_Group')
plt.ylabel('Glucose_Ratio(%)')
plt.tight_layout()
plt.grid(axis='y')
plt.show()

# Final Insights Summary — Stroke Prediction Analysis
# 1. Age vs Stroke

# Stroke ka risk age ke sath continuously increase hota hai.
# Senior aur Elderly group me stroke ratio sabse high mila.
# Young aur Teen groups me stroke cases comparatively bahut kam mile.

# 2.Age vs Smoking

# Smoking ratio Young Adult aur Adult group me highest mila.
# Elderly logon me smoking kam hui, lekin phir bhi unka stroke risk high raha —
# matlab age ek strong risk factor hai.

# 3. Age vs Hypertension

# Hypertension bhi age ke sath badhta hua mila.
# Senior aur Elderly category me hypertension ratio highest tha.
# Hypertension present hone par stroke probability sharply increase hoti hai.

# 4. BMI vs Stroke

# Underweight aur Normal weight walon ka stroke percentage low tha.
# Overweight aur Obese people ka stroke risk noticeably high mila.
# Obese group sabse vulnerable category ke roop me identify hua.

# 5. Average Glucose Level
# High glucose values wale patients me stroke ka risk significantly zyada paya gaya.
# Data indicate karta hai ki prediabetic + diabetic level glucose stroke chances ko increase karte hain.

# 6.Gender-Based Analysis

# Males ka smoking ratio females ke compare me high tha.
# Hypertension ratio dono genders me similar mila, but
# Stroke distribution male-female roughly balanced raha —
# matlab lifestyle + medical factors gender ke effect se zyada important hain.

# 7. Key Risk Factors Identified
# Project ne clearly show kiya ki ye 4 factors stroke ke most powerful indicators hain
# Age (higher age → higher risk)
# Blood Pressure (Hypertension)
# BMI (especially Overweight & Obese)
# Average Glucose Level
# Ye pattern real-world medical research se bhi match karta hai