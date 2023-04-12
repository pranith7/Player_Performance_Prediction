from pycaret.regression import *
import pandas as pd 
import numpy as np

print("Hello world Pranith \n")
pd.set_option('display.max_columns', None)
train = pd.read_csv("/workspace/Player_Performance_Prediction/Data/training_Data.csv")
validation = pd.read_csv("/workspace/Player_Performance_Prediction/Data/validation_data.csv")

columns = ['striker','Batsman_runs','strike_rate','bowler']

train = train[columns]
validation = validation[columns]
train = train[:550].copy()
# validation = validation[300:320].copy()
print(f'Top five rows of the taining data \n {train.head()}')
print(f'Columns of training data \n {train.columns}')
print(f'Number of rows in training data {train.shape} \n Number of rows in validation data {validation.shape} \n')
s = setup(train, target = 'Batsman_runs')

best = compare_models()

print(best)

# print(evaluate_model(best))

# print(plot_model(best, plot = 'residuals'))
# print(plot_model(best, plot = 'feature'))

print(predict_model(best))

# predictions = predict_model(best, data=validation)
# print(predictions.head())

