import pandas as pd

# Sample dataset
data = {
    "name": ["Aryan", "John", "Lisa", "Emma"],
    "salary": [50000, 60000, 70000, 80000],
    "department": ["ml", "backend", "ml", "devops"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# USING .map()
# ---------------------------------------------------

department_map = {
    "ml": "Machine Learning",
    "backend": "Backend Engineering",
    "devops": "DevOps Engineering"
}

df["department_full"] = df["department"].map(department_map)

# ---------------------------------------------------
# USING .apply()
# ---------------------------------------------------

def bonus_calculation(salary):
    return salary * 1.10

df["new_salary"] = df["salary"].apply(bonus_calculation)

# ---------------------------------------------------
# VECTORIZE DIRECTLY (FASTEST)
# ---------------------------------------------------

df["tax"] = df["salary"] * 0.20

print("\nUpdated DataFrame:")
print(df)




Vectorized Scaling
df["normalized"] = df["salary"] / df["salary"].max()


Feature Engineering
df["log_salary"] = df["salary"].apply(np.log)


Label Encoding
df["label"] = df["category"].map({
    "spam": 1,
    "ham": 0
}
