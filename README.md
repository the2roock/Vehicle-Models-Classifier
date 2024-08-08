# Vehicle-Prices-Identifier

# Goal
Develop neural net that predicts vehicle prices based on their properties.

# Description
A fully-connected neural network is used to solve a nonlinear regression task. The developed model can be used to predict car prices relative to given inputs.

## Skills:
- Python
- Machine Learning
- Nonlinear Regression
- Supervised Learning
- Data Engineering
- PyTorch


# Data Overview
## Input Features:
* Brand: `str` - Vehicle brand. 11 unique values.
* Model: `str` - Vehicle model. 58 unique values.
* Year: `int` - Year of manufacture.
* Kilometers_Driven: `int` - Kilometers the vehicle has driven.
* Fuel_Type: `str` - Type of fuel. 2 unique values.
* Transmission: `str` - Type of transmission. 2 unique values.
* Owner_Type: `str` - Owner sequence number. 3 unique values.
* Mileage: `int` - Vehicle mileage.
* Engine: `int` - Vehicle engine volume.
* Power: `int` - Vehicle horsepower.
* Seats: `int` - Number of seats.

## Output Feature:
- Vehicle Price: `float`

## Examples:
| Brand   | Model   | Year | Kilometers_Driven | Fuel_Type | Transmission | Owner_Type | Mileage | Engine | Power | Seats | Price   |
|---------|---------|------|-------------------|-----------|--------------|------------|---------|--------|-------|-------|---------|
| Toyota  | Corolla | 2018 | 50000             | Petrol    | Manual       | First      | 15      | 1498   | 108   | 5     | 800000  |
| Honda   | Civic   | 2019 | 40000             | Petrol    | Automatic    | Second     | 17      | 1597   | 140   | 5     | 1000000 |
| Ford    | Mustang | 2017 | 20000             | Petrol    | Automatic    | First      | 10      | 4951   | 395   | 4     | 2500000 |
| Maruti  | Swift   | 2020 | 30000             | Diesel    | Manual       | Third      | 23      | 1248   | 74    | 5     | 600000  |
| Hyundai | Sonata  | 2016 | 60000             | Diesel    | Automatic    | Second     | 18      | 1999   | 194   | 5     | 850000  |



![Avg. Price per Brand](https://github.com/the2roock/Vehicle-Prices-Identifier/blob/main/plots/Avg.%20Price%20per%20Brand.png)


# Network`s Architecture
The model has 105 parameters.

![Model Design](https://github.com/the2roock/Vehicle-Prices-Identifier/blob/main/plots/Model%20Architecture.png)


# Data Preprocessing
1. One-hot encoding of object data columns.
2. Splitting data into input features and expected outputs.
3. MinMax normalization.
4. K-Fold splitting into train and test datasets.
5. Conversion to Tensor.


# Traning
## Hyperparameters:
- Learning Rate: 0.0001
- Epochs: 50,000
- Loss Function: Mean Squared Error
- Optimization Algorithm: Adam
## Accuracy Dynamic:
The best loss: 3.99e-06
![Train-Test Losses](https://github.com/the2roock/Vehicle-Prices-Identifier/blob/main/plots/Training%20Results.png)


# Results
## Simulate Prediction
![Comparison of Predicted and Real Values](https://github.com/the2roock/Vehicle-Prices-Identifier/blob/main/plots/Comparison%20of%20Predicted%20and%20Real%20Values.png)
## Final Accuracy Score
Model`s Absolute Error is 4,221.95$
