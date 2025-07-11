

# Import to library
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report
)

import joblid



# Create Function 
def creat_df(link):
    # Setup display in pandas
    pd.set_option("display.max_columns", None)
    path = "https://drive.google.com/uc?export=download&id=" + link.split("/")[-2]

    return pd.read_csv(path)


def ohe_convert(df_cal, columns):
    # Encoding by one hot encoding method
    for col in columns:
        df_cal = df_cal.join(pd.get_dummies(df_cal[col], prefix=col))

    return df_cal

def _tunning_model(model, X_train, X_test, y_train, y_test):
    # Train and predict target value
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Confusion matrix and visualize
    cm = confusion_matrix(y_true=y_test, y_pred=y_pred, labels=model.classes_)

    visual_cm = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

    # Evaluate metrics
    acc = round(accuracy_score(y_test, y_pred), 4)
    recall = round(recall_score(y_test, y_pred), 4)
    prec = round(precision_score(y_test, y_pred), 4)
    f1 = round(f1_score(y_test, y_pred), 4)

    return model, acc, recall, prec, f1, classification_report(y_test, y_pred), visual_cm

# Get file from link
link = "https://drive.google.com/file/d/1BDDaPR6nBXyeihV6KJ3rreOEe63GnX5f/view"
df = creat_df(link)
print(df.head(10))



# Summary dataset by pandas
# Make copy data set
df_client = df.copy()

# Display shape of data (rows and columns)
# print(f"Rows of dataset: {df_client.shape[0]}") 
# Rows of dataset: 4521
# print(f"Columns of dataset: {df_client.shape[1]}")
# Columns of dataset: 16

# Information dataset
df_client.info()

# Delete columns not use 
df_client.columns
df_client.drop(columns=df_client.columns[0], axis=1, inplace=True)
# df_client.head(10)

# Check duplicate rows
print(f"Duplicate rows of dataset: {df_client.duplicated().sum()}")
# Duplicate rows of dataset: 0

# Delete duplicate row
# df_employ.drop_duplicates()

# Check missing values
total = df_client.isnull().sum()
percent = df_client.isnull().mean()*100

data = []
for i in range(len(df_client.columns)):
    info_data = [df_client.columns[i], total[i], percent[i]]
    data.append(info_data)

# print(data)
df_missing_data = pd.DataFrame(data, columns=['Features', 'Total Missing', 'Percent Missing'])
# Show sumary table
print(df_missing_data)

# Data distribution numerical and object types
print(df_client.describe())
print(df_client.describe(exclude=[int, float]))



# Check imbalance data
# Application for Target value y(yes/no approved)
print(f'Distribution TARGET VALUE:\n {df_client['y'].value_counts()}')



# Encoding data
# Data type numerical and categorical
categorical_df = df_client.select_dtypes(exclude=[int, float])
list_col = []
for col in categorical_df.columns:
    value = [col, categorical_df[col].nunique()]
    list_col.append(value)

# Show name columns and corresponding value
for i in list_col:
    print(i)

# Make group job feature and encoding by frequency 
job_map = {
    'management': 'White-collar',
    'admin.': 'White-collar',
    'blue-collar': 'Manual labor',
    'housemaid': 'Manual labor',
    'technician': 'Skilled professionals',
    'services': 'Service sector',
    'student': 'Non-working',
    'retired': 'Non-working',
    'unemployed': 'Non-working',
    'self-employed': 'Entrepreneurial/Independent',
    'entrepreneur': 'Entrepreneurial/Independent',
    'unknown': 'Miscellaneous',
    'unknown': 'unknown'
}

df_client['job'] = df_client['job'].map(job_map)
frequency_encoding = df_client['job'].value_counts(normalize=True)
df_client['job'] = df_client['job'].map(frequency_encoding)

# Encoding by One Hot Encoding method
# Function ohe_convert have created
columns_nio = ['marital', 'contact', 'poutcome']
df_client_encod = ohe_convert(df_client, columns_nio)
df_client_encod.drop(columns=columns_nio, inplace=True)

# Replace values features with corresponding code
df_client_encod['education'].replace(['primary', 'secondary', 'tertiary', 'unknown'], [1,2,3,0], inplace=True)

for col in ['default', 'housing', 'loan', 'y']:
    df_client_encod[col].replace({'no':0, 'yes':1}, inplace=True)

# Add calculation columns
df_client_encod['age_group'] = pd.cut(df_client_encod['age'], bins=[18, 30, 40, 50, 60, 100], 
                         labels = ['18-30', '30-40', '40-50', '50-60', '60+'])

df_client_encod['not_contacted_flag'] = (df_client_encod['pdays'] == -1).astype(int)
df_client_encod['high_balance_flag'] = (df_client_encod['balance'] > df_client_encod['balance'].mean()).astype(int)
df_client_encod['contact_duration_bin'] = pd.cut(df_client_encod['duration'], bins=[0, 100, 300, 600, df_client_encod['duration'].max()], 
                                    labels=['short', 'medium', 'long', 'very long'])
df_client_encod['previous_contact_flag'] = (df_client_encod['previous'] > 0).astype(int)
df_client_encod['recently_contacted'] = np.where((df_client_encod['pdays'] > 0) & (df_client_encod['pdays'] < 30), 1, 0)

# Encoding by frequency method
columns_gr = ['age_group', 'contact_duration_bin']
for col in columns_gr:
    frequency_encoding = df_client_encod[col].value_counts(normalize=True)
    df_client_encod[col] = df_client_encod[col].map(frequency_encoding)




# Imbalance 
# Make a copy datafram to avoid errors with post-processing data
# Shuffle dataset
df_client_encod = shuffle(df_client_encod)

# Split dataset to Target value and Feature
X = df_client_encod.drop(columns=['y'])
y = df_client_encod['y']

# Split dataset to train, test group
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Imbalance dataset by Over sample method
oversample = RandomOverSampler(sampling_strategy='minority', random_state=0)
X_train_re, y_train_re = oversample.fit_resample(X_train, y_train)

# Visualize data has processed
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

sns.countplot(x=y_train, ax=ax[0], hue=y_train, palette="viridis", legend=False)
ax[0].set_title("Before Handling Imbalance")
ax[0].set_xlabel("Target Class")
ax[0].set_ylabel("Count")
ax[0].bar_label(ax[0].containers[0], label_type='edge')

sns.countplot(x=y_train_re, ax=ax[1], hue=y_train_re, palette="viridis", legend=False)
ax[1].set_title("After Handling Imbalance with RandomOverSampler")
ax[1].set_xlabel("Target Class")
ax[1].set_ylabel("Count")
ax[1].bar_label(ax[1].containers[0], label_type='edge')

plt.tight_layout()
plt.show()




# Scaling dataset
std_scaler = StandardScaler().fit(X_train_re)

X_train_re = std_scaler.transform(X_train_re)
X_test = std_scaler.transform(X_test)




# Find the best parameters
md_dec_tree_list = []
depth =[5, 9, 15, 20, 30]

for i in range(len(depth)):
    md= {}

    dtc = DecisionTreeClassifier(criterion='gini', max_depth=depth[i])
    model, acc, recall, prec, f1, report, visual_cm = _tunning_model(dtc, X_train_re, X_test, y_train_re, y_test)

    md['name_model'] = model
    md['acc'] = acc
    md['recall'] = recall
    md['prec'] = prec
    md['f1'] = f1
    md['report'] = report
    md['visual'] = visual_cm
    md_dec_tree_list.append(md)

# Create table param model
df_param = pd.DataFrame(md_dec_tree_list, columns=['name_model', 'acc', 'recall', 'prec', 'f1', 'report', 'visual'])
df_param.columns = ['name_model', 'acc', 'recall on GOOD', 'prec on GOOD', 'f1', 'report', 'visual']
# Show table
print(df_param)

# Choose max_depth = 15 and retrain model base on param table
dtc = DecisionTreeClassifier(criterion='gini', max_depth=15)

model, acc, recall, prec, f1, report, visual_cm = _tunning_model(dtc, X_train_re, X_test, y_train_re, y_test)
print(model)
print(acc)
print(recall)
print(prec)
print(f1)
print(report)
visual_cm.plot()



# Create Diagram Decision Tree from model
# Type image
fig = plt.figure(figsize=(50,40))

viz_model = tree.plot_tree(df_param.iloc[2,0],
                           feature_names=X.columns,
                           class_names=['no', 'yes'],
                           fontsize=10,
                           filled=True)
# Type text
text_representation = tree.export_text(model)
with open("decistion_tree.log", "w") as fout:
    fout.write(text_representation)

# Save model
joblib.dump(dtc, "DecisionTree_Model.pkl")

