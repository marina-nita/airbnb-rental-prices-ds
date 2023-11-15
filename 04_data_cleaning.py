# drop columns id name host_id host last_review number_of_reviews last_review reviews_per_month
df = df.drop(['id', 'name', 'host_id', 'host_name', 'last_review', 'number_of_reviews', 'last_review', 'reviews_per_month', 'neighbourhood'], axis=1)
df.duplicated().sum()
# converting the following columns into numerical data since predictive model can only have numerical data and the following columns are directly related to the rental price of the AirBnB. Therefore we can not drop these columns 
X = df.drop('price', axis=1)
