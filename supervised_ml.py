from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]

X = [[h] for h in hours]
y = scores

# Model
model = LinearRegression()
model.fit(X, y)

# User input
hours_input = float(input("Enter hours studied: "))
predicted_score = model.predict([[hours_input]])

print(f"Predicted exam score: {predicted_score[0]:.2f}")

# --- BONUS: Graph ---
plt.figure()
plt.scatter(hours, scores, color='blue', label='Actual Data')
plt.plot(hours, model.predict(X), color='red', label='Regression Line')
plt.scatter([hours_input], predicted_score, color='green', s=100, label=f'Your Prediction ({hours_input}h)')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Relationship between Study Hours and Exam Scores")
plt.legend()
plt.grid(True)
plt.show()