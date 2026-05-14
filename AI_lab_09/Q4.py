# Program 4: Multiclass Classification
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt
import time
# Load dataset
data = load_wine()
X = data.data
y = data.target
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
# Standardization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Models
models = {
    "SVM": SVC(kernel='rbf'),
    "Random Forest": RandomForestClassifier(),
    "MLP": MLPClassifier(max_iter=1000)
}
accuracies = []
f1_scores = []
times = []
# Train and evaluate
for name, model in models.items():
    start = time.time()
    model.fit(X_train, y_train)
    end = time.time()
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro')
    training_time = end - start
    accuracies.append(acc)
    f1_scores.append(f1)
    times.append(training_time)
    print("\n", name)
    print("Accuracy :", acc)
    print("F1 Score :", f1)
    print("Training Time :", training_time)
# Plot Accuracy
plt.bar(models.keys(), accuracies)
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.title("Accuracy Comparison")
plt.show()