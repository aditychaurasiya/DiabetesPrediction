# views.py

import os
from pandas import read_csv
from django.shortcuts import render
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler


def home(request):
    return render(request, 'home.html')


def predict(request):
    return render(request, 'predict.html')


def result(request):
    file_path = os.path.join(os.path.expanduser("~"), "Desktop", "MERISKILL", "diabetes.csv")
    data = read_csv(file_path)

    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, stratify=Y)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(max_iter=100000)
    model.fit(X_train_scaled, Y_train)

    val1 = float(request.GET.get('n1', 0.0))
    val2 = float(request.GET.get('n2', 0.0))
    val3 = float(request.GET.get('n3', 0.0))
    val4 = float(request.GET.get('n4', 0.0))
    val5 = float(request.GET.get('n5', 0.0))
    val6 = float(request.GET.get('n6', 0.0))
    val7 = float(request.GET.get('n7', 0.0))
    val8 = float(request.GET.get('n8', 0.0))

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    model.predict_proba([[val1, val2, val3, val4, val5, val6, val7, val8]])

    model.predict(X_test_scaled)

    result2 = "Positive" if pred == [1] else "Negative"

    return render(request, 'predict.html', {"result2": result2})
