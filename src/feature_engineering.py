import pandas as pd

def create_features(df):
    df = df.copy()

    # RFM scores
    df["recency_score"] = pd.qcut(df["recency_days"], 5, labels=[5,4,3,2,1])
    df["frequency_score"] = pd.qcut(df["frequency"], 5, labels=[1,2,3,4,5])
    df["monetary_score"] = pd.qcut(df["monetary"], 5, labels=[1,2,3,4,5])

    df["rfm_score"] = (
        df["recency_score"].astype(int) +
        df["frequency_score"].astype(int) +
        df["monetary_score"].astype(int)
    )

    # Engagement score
    df["engagement_score"] = (
        df["email_open_rate"] * 0.4 +
        (1 - df["cart_abandonment_rate"]) * 0.3 +
        (df["page_views_30d"] / df["page_views_30d"].max()) * 0.3
    )

    # Risk score
    df["risk_score"] = (
        df["support_tickets_30d"] * 1.5 +
        (5 - df["sentiment_score"]) * 2 +
        df["refund_requests"] * 1.2
    )

    return df