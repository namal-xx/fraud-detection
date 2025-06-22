# 🚨 Fraud-Detection-App

Welcome to **Fruad Detection App** - A Streamlit-powered web that hpls detect fraudulent transactions using Machine Learning! 🧠💸

<br>

## 📌 Features 

- 🔍 Input key transaction details
- 📊 Intelligent fraud detection using a trained ML model
- ✅ Clean and simple interface
- 🛡️ Based on `BalancedRandomForestClassisfier` from `imabalnced-learn`

<br>

## 🚀 How to use:

1. Visit the [live app here]
2. Enter the requested details
3. Click **Predict**
4. See whether the transation is fruad or not!!

<br>

## 🧠 Model info

- **Algorithm:** BalancedRandomForestClassisfier (handles the class imabalance well).
- **Training libraries:**
   - `scikit-learn`
   - `imabalanced-learn`
   - `pandas`, `numpy`

- **Preprocessing:** Clipping out-of-bound values for robustness

<br>

## 📉 Model Limitations

⚠️ This modle was trained on highly imbalanced dataset (very few fraudulent transactions compared to normal ones). While it does its best to detect fraud, it's not 100% accurate:

- Sometimes it **flags legitimate transation as fruad** (false positive)
- Sometimes it **misses actual fraud** (false negative)

This is a common challenge in fraud detection, and the model may need further tuning and more real-world data to improve accuracy. Use the predictions as a **supporting tool**, not as the final decision. 

<br>

## 🛠 Tech stack

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [imbalanced-learn](https://imbalanced-learn.org/)
- [joblib](https://joblib.readthedocs.io/en/latest/)

 
   

 
