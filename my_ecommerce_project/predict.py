# =========================================================
# READING .PKL ARTIFACTS IN VS CODE FOR NEW PREDICTIONS
# =========================================================
import os
import pandas as pd
import joblib

# 1. Define paths to where your pkl files are stored
# If your script is running directly in the root directory, use these paths:
MODEL_PATH = "models/final_model.pkl"
PREPROCESSOR_PATH = "models/final_preprocessor.pkl"

# 2. LOAD THE PKL FILES (This reads the binary back into python objects)
print("Loading saved pipeline components...")
loaded_model = joblib.load(MODEL_PATH)
loaded_preprocessor = joblib.load(PREPROCESSOR_PATH)
print("Components loaded successfully!\n")

# 3. CREATE NEW MOCK DATA (Simulating a brand new customer transaction)
# The dictionary keys must match your original dataset column structures exactly!
new_transaction = {
    'product_category': ['Electronics'],
    'region': ['South'],
    'quantity': [3],
    'unit_price': [450.00],
    'discount': [0.15],
    'payment_method': ['Card'],
    'delivery_days': [5],
    'revenue': [1147.50],
    'order_month': [5],
    'order_day': [24],
    'order_dow': [6] # Sunday
}

# Convert our raw sample transaction into a pandas DataFrame DataFrame
df_new = pd.DataFrame(new_transaction)
print("--- NEW RAW DATA ENTRY ---")
print(df_new)

# 4. PREPROCESS THE NEW DATA USING THE LOADED PREPROCESSOR
# Crucial: Use .transform(), NEVER use .fit_transform() here!
X_new_transformed = loaded_preprocessor.transform(df_new)

# 5. GENERATE THE FINAL PREDICTION USING THE LOADED MODEL
predicted_rating = loaded_model.predict(X_new_transformed)

print("\n=========================================")
print(f" Predicted Customer Rating: {predicted_rating[0]:.2f} Stars")
print("=========================================")