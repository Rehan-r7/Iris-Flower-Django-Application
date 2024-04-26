from django.shortcuts import render
import pandas as pd
from joblib import load
model = load('./SavedModel/model.joblib')
# Create your views here.
def predictor(request):
    
    if request.method == 'POST':
        
        # sepal_length = float(request.POST.get('sepal_length'))
        # sepal_width = float(request.POST.get('sepal_width'))
        # petal_length = float(request.POST.get('petal_length'))
        # petal_width = float(request.POST.get('petal_width'))
        # y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        # Assuming you have extracted input values from user input and converted them to floats
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        # Construct the input data with correct column names and order
        input_data = pd.DataFrame({
            'SepalLengthCm': [sepal_length],
            'SepalWidthCm': [sepal_width],
            'PetalLengthCm': [petal_length],
            'PetalWidthCm': [petal_width]
        })

        # Now you can use this input_data for prediction
        y_pred = model.predict(input_data)


        
        if y_pred[0] == 0 :
            y_pred = 'Setosa'
            
        elif y_pred[0] == 1 :
            y_pred = 'Versicolor'
        else :
            y_pred = 'Virginica'
        return render(request, 'index.html',{'result':y_pred})

    return render(request, 'index.html')

    
    