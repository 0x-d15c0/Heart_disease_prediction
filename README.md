# Heart Disease Prediction 
### ACM SIGAI TASK 
#### Context : <br>
Trained a model using logistic regression to detect whether the patient has a heart disease or not . <br>

#### Attributes : 
- age
- sex
- chest pain type (4 values)
- resting blood pressure
- serum cholestoral in mg/dl
- fasting blood sugar > 120 mg/dl
- resting electrocardiographic results (values 0,1,2)
- maximum heart rate achieved
- exercise induced angina
- oldpeak = ST depression induced by exercise relative to rest
- the slope of the peak exercise ST segment
- number of major vessels (0-3) colored by flourosopy
- thal: 0 = normal; 1 = fixed defect; 2 = reversable defect

## Steps :
### (1) Understanding the problem  <br>
I chose a dataset with 14 columns providing different information about a person . The last column is the target column.
The goal is to predict the target column using the other 13 columns.
Imported the needed python modules. Using  `pd.read_csv()` read the csv file data into a dataframe named dataset . 
### (2) Data analysis <br>
Used `dataset.describe()` , `dataset.shape()`,`dataset.head()`,`dataset.tail()`
and `dataset.info` to get an idea of the data . 
