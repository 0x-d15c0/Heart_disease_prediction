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
and `dataset.info` to get an idea of the data . Didnt have much data preprocessing to perform since there were no null values and the target value is binary .
### (3) Data visualisation <br>
Using matplotlib and seaborn plotted a histogram graph of all columns to their count.
Using seaborn plotted a pie chart to check the ratio between males and females in the given dataset.
### (4) Making the model
Split the model into training and testing data (80:20) and trained it used logistic regression and fit the data in the dataframe into the model.
### Accuracy of the current model : 0.8048780487804879

## Using streamlit to deploy a website  
The websaite takes attributes as inputs and returns whether the patient has a heart disease or not 80% accurately. 
 #### testing data : <br>
![image](https://github.com/0x-d15c0/Heart_disease_prediction/assets/117750351/19b8430c-f45c-41c7-83ca-7ca7cf028c01)

#### website : <br>
![image](https://github.com/0x-d15c0/Heart_disease_prediction/assets/117750351/4451a665-799b-4e8d-9735-8fb38f903801)
