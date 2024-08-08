# Vehicle-Prices-Identifier

# Goal
Develop neural net that defines vehicle prices by them properties.

# Description
Fully-connected neural network is used to resolve nonlinear regression task. The model developed may be use to predict cars price reletive to given inputs.

## Skills:
- Python
- Machine Learning
- Nonlinear Regression
- Data Engineering
- Pytorch

# Data Overview
## Input Properties:
* Brand: `str` - Vehicle brand. 11 unique values.
* Model: `str` - Vehicle model. 58 unique values.
* Year: `int` - Year of manufacture.
* Kilometers_Driven: `int` - Kilometers vehicle driven.
* Fuel_Type: `str` - Type of fuel. 2 unique values.
* Transmission: `str` - Type of transmission. 2 unique values.
* Owner_Type: `str` - Owner sequence number. 3 unique values.
* Mileage: `int` - Vehicle mileage.
* Engine: `int` - Vehicle engine volume.
* Power: `int` - Vehicle horsepower.
* Seats: `int` - Number of seats.

Examples:
| Brand   | Model   | Year | Kilometers_Driven | Fuel_Type | Transmission | Owner_Type | Mileage | Engine | Power | Seats | Price   |
|---------|---------|------|-------------------|-----------|--------------|------------|---------|--------|-------|-------|---------|
| Toyota  | Corolla | 2018 | 50000             | Petrol    | Manual       | First      | 15      | 1498   | 108   | 5     | 800000  |
| Honda   | Civic   | 2019 | 40000             | Petrol    | Automatic    | Second     | 17      | 1597   | 140   | 5     | 1000000 |
| Ford    | Mustang | 2017 | 20000             | Petrol    | Automatic    | First      | 10      | 4951   | 395   | 4     | 2500000 |
| Maruti  | Swift   | 2020 | 30000             | Diesel    | Manual       | Third      | 23      | 1248   | 74    | 5     | 600000  |
| Hyundai | Sonata  | 2016 | 60000             | Diesel    | Automatic    | Second     | 18      | 1999   | 194   | 5     | 850000  |

## Output Property:
- Vehicle Price: `float`

![Avg. Price per Brand](https://github.com/the2roock/Vehicle-Prices-Identifier/blob/main/plots/Avg.%20Price%20per%20Brand.png)

# Network`s Architecture


# Data Preprocessing


# Traning

# Results
