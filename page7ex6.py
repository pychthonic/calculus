import numpy, sympy

def predict_CO2_scientific_american(year):
    t = year - 1960
    return .018*(t**2)+.7*t+316.2

def predict_CO2_2010(year):
    t = year - 1960
    return 1.68*t+303.5


if __name__ == '__main__':
    scientific_american_prediction = predict_CO2_scientific_american(2035)
    linear_model_prediction = predict_CO2_2010(2035)

    print(f"Scientific American prediction: {scientific_american_prediction} CO2 parts per million in 2035")
    print(f"Linear model prediction:        {linear_model_prediction} CO2 parts per million in 2035")
