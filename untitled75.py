import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\ashmi\\Downloads\\aiproject_with_speeds.csv")
X = data.drop("Accident_Severity", axis=1)
y = data["Accident_Severity"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = GradientBoostingClassifier(n_estimators=20,learning_rate=0.1,max_depth=3,random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred) * 100, "%")
print("Classification Report:\n", classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Heatmap')
plt.show()
log = float(input("Enter Longitude: "))
lat = float(input("Enter latitude: "))
time = float(input("Enter Time_of_Day: "))
speed = float(input("Enter Speed_Limit: "))
uspeed=float(input("Enter Speed:"))
vnum = float(input("Enter Number_of_Vehicles: "))
vtype = float(input("Enter Vehicle_Type: "))

# Column names must match training data exactly
data = pd.DataFrame({
    "longitude": [log],
    "latitude": [lat],
    "Time_of_Day": [time],
    "Speed_Limit": [speed],
    "Speed_Vehical":[uspeed],
    "Number_of_Vehicles": [vnum],
    "Vehicle_Type": [vtype]
})

# Scale the input using the same scaler
data_scaled = scaler.transform(data)

prediction = model.predict(data_scaled)
if prediction[0] == 0:
    print("Accident Severity Prediction: Minor")
elif prediction[0] == 1:
    print("Accident Severity Prediction: Major")
elif prediction[0] == 2:
    print("Accident Severity Prediction: Fatal")
else:
    print("Unknown Prediction")
