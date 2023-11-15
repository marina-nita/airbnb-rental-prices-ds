#!/usr/bin/env python
# coding: utf-8

# The Notebook seeks to help predict the rental price of the AirBnB based of several features where the targeted value is the price. The insights provided by your predictive model could benefit both AirBnB hosts and guests. Hosts can use the insights to set competitive prices for their listings, while guests can use the insights to find the best deals on rentals. Additionally, the insights could be used by real estate investors and city planners to gain a better understanding of the housing market and make more informed decisions. 

# It is not specified who the target audience is for the analysis you've been working on. It could be any person or organization that is interested in understanding the rental prices of AirBnBs based on various features. Some examples of potential target audiences could be:
# -AirBnB hosts looking to set competitive prices for their listings
# -AirBnB guests looking to find the best deals on rentals
# -Real estate investors and city planners looking to gain a better understanding of the housing market and make more informed decisions
# -Data scientists and researchers looking to explore and understand the relationship between AirBnB rental prices and various features.

# # Importing Libraries

# In[96]:




# # Importing Data

# In[97]:




# # Data Preprocessing


# In[98]:




# In[99]:


# check for missing values
df.isnull().sum()


# In[100]:


# check for duplicates


# In[101]:


# total number of rows and columns


# # Checking For Outliers

# In[102]:


# function to check for outliers
def check_outliers(df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    return df[(df[col] < lower_bound) | (df[col] > upper_bound)]



# In[103]:


# check for outliers
check_outliers(df, 'price')


# # Result of Outliers 
# 

# In[104]:


print(df['room_type'].unique())


# # Label Encoding for converting textual data into numerical data


# In[105]:


# encode categorical variables using label encoder



df['neighbourhood_group'] = le.fit_transform(df['neighbourhood_group'])
df['room_type'] = le.fit_transform(df['room_type'])



# # Spilitting Data into Test and Train set

# In[106]:


# split data into 3 sets: train, test and safe 


y = df['price']



# # Scaling the Data

# In[107]:


# scale data

  
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# # Applying Model of the Data

# In[108]:


# train model

regressor = LinearRegression()


# # Prediction on the Trained Model

# In[109]:


# predict
y_pred  


# # Accuracy of the Model

# In[110]:


# evaluate model

print('R2 score: ', r2_score(y_test, y_pred))


# accuracy of the model is affected since there wer alot of outliers in the dataset. Applying any predictive model would not give have accuracy result.

# In[111]:


# print the accuracy score of the model
print('Accuracy of linear regression classifier on test set: {:.2f}'.format(100*(regressor.score(X_test, y_test))))


# # Visualization

# In[112]:


# exploratory data analysis



# In[114]:


 


# # Summary Statistics

# In[115]:


# summary statistics


# 
# For example:
# -AirBnB hosts can use the insights to set competitive prices for their listings and increase their bookings and revenue.
# -AirBnB guests can use the insights to find the best deals on rentals and save money on their bookings.
# -Real estate investors and city planners can use the insights to gain a better understanding of the housing market and make more informed decisions about where to invest or plan for future housing developments.
# -Data scientists and researchers can use the insights to explore and understand the relationship between AirBnB rental prices and various features and contribute to the research in the field.
