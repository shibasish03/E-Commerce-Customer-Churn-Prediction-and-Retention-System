# import pandas as pd
# import pickle
# import os
#
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import roc_auc_score
#
# # -------------------------------
# # 1. LOAD DATA
# # -------------------------------
# df = pd.read_csv("data/ecommerce_customers.csv")
#
# print("Dataset Loaded:", df.shape)
# print("Churn Rate:", round(df["churned_30d"].mean(), 3))
#
# # -------------------------------
# # 2. FEATURE ENGINEERING
# # -------------------------------
#
# # Engagement score
# df["engagement"] = (
#     df["email_open_rate"] * 0.6 +
#     (1 - df["cart_abandonment_rate"]) * 0.4
# )
#
# # Recency-Frequency interaction (VERY IMPORTANT)
# df["rf_ratio"] = df["recency_days"] / (df["frequency"] + 1)
#
# # -------------------------------
# # 3. FEATURE SELECTION
# # -------------------------------
# features = [
#     "recency_days",
#     "frequency",
#     "monetary",
#     "page_views_30d",
#     "cart_abandonment_rate",
#     "support_tickets_30d",
#     "sentiment_score",
#     "email_open_rate",
#     "discount_dependency",
#     "engagement",
#     "rf_ratio"
# ]
#
# X = df[features]
# y = df["churned_30d"]
#
# # -------------------------------
# # 4. TRAIN-TEST SPLIT
# # -------------------------------
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )
#
# print("Train Size:", X_train.shape)
# print("Test Size:", X_test.shape)
#
# # -------------------------------
# # 5. MODEL
# # -------------------------------
# model = RandomForestClassifier(
#     n_estimators=300,
#     max_depth=12,
#     min_samples_leaf=5,
#     class_weight="balanced",
#     random_state=42,
#     n_jobs=-1
# )
#
# model.fit(X_train, y_train)
#
# # -------------------------------
# # 6. EVALUATION
# # -------------------------------
#
# # Test AUC
# probs = model.predict_proba(X_test)[:, 1]
# auc = roc_auc_score(y_test, probs)
#
# # Cross Validation AUC
# cv_scores = cross_val_score(model, X, y, cv=5, scoring="roc_auc")
#
# print("\n Model Performance")
# print("Test AUC:", round(auc, 4))
# print("CV AUC:", round(cv_scores.mean(), 4))
#
# # -------------------------------
# # 7. FEATURE IMPORTANCE
# # -------------------------------
# importance = model.feature_importances_
#
# imp_df = pd.DataFrame({
#     "feature": features,
#     "importance": importance
# }).sort_values("importance", ascending=False)
#
# print("\n🔍 Feature Importance:")
# print(imp_df)
#
# # Save importance
# os.makedirs("models", exist_ok=True)
# imp_df.to_csv("models/feature_importance.csv", index=False)
#
# # -------------------------------
# # 8. SAVE MODEL
# # -------------------------------
# pickle.dump(model, open("models/model.pkl", "wb"))
# pickle.dump(features, open("models/features.pkl", "wb"))
#
# print("\n Model saved in /models")

import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

df = pd.read_csv("data/ecommerce_customers.csv")

df["engagement"] = df["email_open_rate"]*0.6 + (1-df["cart_abandonment_rate"])*0.4
df["rf_ratio"] = df["recency_days"]/(df["frequency"]+1)

features = [
    "recency_days","frequency","monetary",
    "page_views_30d","cart_abandonment_rate",
    "support_tickets_30d","sentiment_score",
    "email_open_rate","discount_dependency",
    "engagement","rf_ratio"
]

X = df[features]
y = df["churned_30d"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

model = RandomForestClassifier(n_estimators=300,max_depth=12,class_weight="balanced")
model.fit(X_train,y_train)

probs = model.predict_proba(X_test)[:,1]
print("AUC:",roc_auc_score(y_test,probs))

df["churn_prob"] = model.predict_proba(X)[:,1]

def segment(p):
    if p>0.8: return "Critical"
    elif p>0.6: return "High Risk"
    elif p>0.4: return "Medium Risk"
    else: return "Low Risk"

df["segment"] = df["churn_prob"].apply(segment)

os.makedirs("models", exist_ok=True)
df.to_csv("models/final_data.csv", index=False)

pickle.dump(model, open("models/model.pkl","wb"))
pickle.dump(features, open("models/features.pkl","wb"))