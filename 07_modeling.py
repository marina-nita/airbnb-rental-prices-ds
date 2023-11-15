X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_safe, y_train, y_safe = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
