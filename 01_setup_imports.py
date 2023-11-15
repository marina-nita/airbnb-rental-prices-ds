import pandas as pd
import numpy as np
# import data
# removing the following columns from the dataframe because these columns are not direclty or indeirectly related to the targeted value so removing these columns would not have any effect and on the other hand these coulmns contain textual data in order to make a predictive model all the data should in numerical form
# Since the data contains outliers it would have a drastic effect on the model. Since Outliers are data points that are significantly different from the rest of the data, and they can skew the results of the analysis. Therefore the accuracy of the model would be effected
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
# # The target population will benefit from the results of your analysis by gaining a better understanding of the factors that influence AirBnB rental prices. This information can be used to make more informed decisions.
