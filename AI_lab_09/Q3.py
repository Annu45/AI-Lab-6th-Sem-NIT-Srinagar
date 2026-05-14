# Program 3: MNIST Digit Classification
from keras.datasets import mnist
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
# Load dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# Normalize data
X_train = X_train / 255.0
X_test = X_test / 255.0
# Flatten images
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
# Reduce size for faster SVM training
X_train_small = X_train[:10000]
y_train_small = y_train[:10000]
# Models
lr = LogisticRegression(max_iter=1000)
svm = SVC(kernel='rbf')
rf = RandomForestClassifier()
# Train models
lr.fit(X_train_small, y_train_small)
svm.fit(X_train_small, y_train_small)
rf.fit(X_train_small, y_train_small)
# Predictions
lr_pred = lr.predict(X_test)
svm_pred = svm.predict(X_test)
rf_pred = rf.predict(X_test)
# Function for metrics
def evaluate(name, y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    pre = precision_score(y_true, y_pred, average='macro')
    rec = recall_score(y_true, y_pred, average='macro')
    f1 = f1_score(y_true, y_pred, average='macro')
    print("\n", name)
    print("Accuracy :", acc)
    print("Precision :", pre)
    print("Recall :", rec)
    print("F1 Score :", f1)
    return acc
# Evaluate
acc1 = evaluate("Logistic Regression", y_test, lr_pred)
acc2 = evaluate("SVM", y_test, svm_pred)
acc3 = evaluate("Random Forest", y_test, rf_pred)
# Bar chart
models = ["Logistic Regression", "SVM", "Random Forest"]
accuracies = [acc1, acc2, acc3]
plt.bar(models, accuracies)
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.title("Accuracy Comparison")
plt.show()