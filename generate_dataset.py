# import numpy as np
# import pandas as pd
# import os
#
# np.random.seed(42)
# N = 5000
#
# def generate_data():
#     rows = []
#
#     for _ in range(N):
#
#         # ---------------------------
#         # 1. Customer Type (KEY FIX)
#         # ---------------------------
#         customer_type = np.random.choice(
#             ["loyal", "regular", "at_risk"],
#             p=[0.3, 0.4, 0.3]
#         )
#
#         # ---------------------------
#         # 2. Feature generation per type
#         # ---------------------------
#         if customer_type == "loyal":
#             recency = np.random.randint(1, 60)
#             frequency = np.random.randint(20, 50)
#             monetary = np.random.uniform(2000, 10000)
#             email_open = np.random.uniform(0.5, 1.0)
#             cart_abandon = np.random.uniform(0.1, 0.4)
#
#         elif customer_type == "regular":
#             recency = np.random.randint(30, 180)
#             frequency = np.random.randint(5, 25)
#             monetary = np.random.uniform(500, 5000)
#             email_open = np.random.uniform(0.2, 0.6)
#             cart_abandon = np.random.uniform(0.3, 0.7)
#
#         else:  # at_risk
#             recency = np.random.randint(120, 365)
#             frequency = np.random.randint(1, 10)
#             monetary = np.random.uniform(50, 2000)
#             email_open = np.random.uniform(0.0, 0.3)
#             cart_abandon = np.random.uniform(0.6, 1.0)
#
#         # Common features
#         page_views = np.random.randint(1, 200)
#         tickets = np.random.randint(0, 10)
#         sentiment = np.random.uniform(1, 5)
#         discount = np.random.uniform(0, 1)
#
#         # ---------------------------
#         # 3. Add noise
#         # ---------------------------
#         recency += np.random.normal(0, 5)
#         sentiment += np.random.normal(0, 0.3)
#
#         recency = np.clip(recency, 1, 365)
#         sentiment = np.clip(sentiment, 1, 5)
#
#         # ---------------------------
#         # 4. Interaction features
#         # ---------------------------
#         engagement = (email_open * 0.6 + (1 - cart_abandon) * 0.4)
#         rf_ratio = recency / (frequency + 1)
#
#         # ---------------------------
#         # 5. Churn logic (STRONG but real)
#         # ---------------------------
#         churn_score = (
#             0.5 * (recency / 365) +
#             0.2 * cart_abandon +
#             0.15 * (1 - engagement) +
#             0.1 * (rf_ratio / 50) +
#             0.05 * (tickets / 10)
#         )
#
#         churn_score += np.random.normal(0, 0.04)
#         churn_score = np.clip(churn_score, 0, 1)
#
#         churned = np.random.rand() < churn_score
#
#         # CLV
#         clv = monetary * np.random.uniform(1.5, 4)
#
#         rows.append([
#             recency, frequency, monetary,
#             page_views, cart_abandon,
#             tickets, sentiment,
#             email_open, discount,
#             clv, int(churned)
#         ])
#
#     columns = [
#         "recency_days",
#         "frequency",
#         "monetary",
#         "page_views_30d",
#         "cart_abandonment_rate",
#         "support_tickets_30d",
#         "sentiment_score",
#         "email_open_rate",
#         "discount_dependency",
#         "predicted_clv",
#         "churned_30d"
#     ]
#
#     return pd.DataFrame(rows, columns=columns)
#
#
# if __name__ == "__main__":
#     print("Generating improved dataset...")
#
#     df = generate_data()
#
#     os.makedirs("data", exist_ok=True)
#     df.to_csv("data/ecommerce_customers.csv", index=False)
#
#     print("Dataset:", df.shape)
#     print("Churn rate:", round(df["churned_30d"].mean(), 3))
import numpy as np
import pandas as pd
import os
import random
import string

np.random.seed(42)
N = 5000

def generate_name(i):
    first = random.choice(["Amit","Rahul","Priya","Sneha","Arjun","Neha","Ravi","Anjali","Kiran","Pooja"])
    last = random.choice(["Sharma","Das","Roy","Verma","Singh","Paul","Gupta","Nair"])
    return f"{first} {last} {i}"

def generate_email(name):
    base = name.replace(" ", "").lower()
    rand = ''.join(random.choices(string.digits, k=3))
    return f"{base}{rand}@gmail.com"

def generate_data():
    rows = []

    for i in range(N):

        name = generate_name(i)
        email_id = generate_email(name)

        customer_type = np.random.choice(["loyal","regular","at_risk"], p=[0.3,0.4,0.3])

        if customer_type == "loyal":
            recency = np.random.randint(1,60)
            frequency = np.random.randint(20,50)
            monetary = np.random.uniform(2000,10000)
            email_open = np.random.uniform(0.5,1.0)
            cart = np.random.uniform(0.1,0.4)
        elif customer_type == "regular":
            recency = np.random.randint(30,180)
            frequency = np.random.randint(5,25)
            monetary = np.random.uniform(500,5000)
            email_open = np.random.uniform(0.2,0.6)
            cart = np.random.uniform(0.3,0.7)
        else:
            recency = np.random.randint(120,365)
            frequency = np.random.randint(1,10)
            monetary = np.random.uniform(50,2000)
            email_open = np.random.uniform(0.0,0.3)
            cart = np.random.uniform(0.6,1.0)

        page_views = np.random.randint(1,200)
        tickets = np.random.randint(0,10)
        sentiment = np.random.uniform(1,5)
        discount = np.random.uniform(0,1)

        engagement = email_open * 0.6 + (1 - cart) * 0.4
        rf_ratio = recency / (frequency + 1)

        churn_score = (
            0.5*(recency/365) +
            0.2*cart +
            0.15*(1-engagement) +
            0.1*(rf_ratio/50) +
            0.05*(tickets/10)
        )

        churned = np.random.rand() < np.clip(churn_score,0,1)
        clv = monetary * np.random.uniform(1.5,4)

        rows.append([
            name, email_id,
            recency, frequency, monetary,
            page_views, cart,
            tickets, sentiment,
            email_open, discount,
            clv, int(churned)
        ])

    cols = [
        "name","email_id",
        "recency_days","frequency","monetary",
        "page_views_30d","cart_abandonment_rate",
        "support_tickets_30d","sentiment_score",
        "email_open_rate","discount_dependency",
        "predicted_clv","churned_30d"
    ]

    return pd.DataFrame(rows, columns=cols)

if __name__ == "__main__":
    df = generate_data()
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/ecommerce_customers.csv", index=False)
    print("Dataset created:", df.shape)