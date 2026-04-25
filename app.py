# import streamlit as st
# import pandas as pd
# import pickle
# import plotly.express as px
# import plotly.graph_objects as go
#
# from retention import get_action
# # Load model
# model = pickle.load(open("models/model.pkl", "rb"))
# features = pickle.load(open("models/features.pkl", "rb"))
# imp_df = pd.read_csv("models/feature_importance.csv")
#
# st.set_page_config(page_title="Churn System", layout="wide")
#
# st.title("🛡️ Customer Churn Prediction Dashboard")
#
# # -------------------------------
# # INPUT SECTION
# # -------------------------------
# col1, col2 = st.columns(2)
#
# with col1:
#     recency = st.number_input("Recency (days)", 1, 365, 30)
#     frequency = st.number_input("Frequency", 1, 50, 5)
#     monetary = st.number_input("Monetary", 50.0, 10000.0, 500.0)
#     page_views = st.number_input("Page Views", 1, 200, 20)
#
# with col2:
#     cart = st.slider("Cart Abandonment", 0.0, 1.0, 0.4)
#     tickets = st.number_input("Support Tickets", 0, 10, 1)
#     sentiment = st.slider("Sentiment Score", 1.0, 5.0, 3.5)
#     email = st.slider("Email Open Rate", 0.0, 1.0, 0.3)
#     discount = st.slider("Discount Dependency", 0.0, 1.0, 0.4)
#
# clv = st.number_input("Predicted CLV", 0.0, 10000.0, 1000.0)
#
# # -------------------------------
# # PREDICTION
# # -------------------------------
# if st.button("Predict Churn"):
#
#     # Feature engineering
#     engagement = email * 0.6 + (1 - cart) * 0.4
#     rf_ratio = recency / (frequency + 1)
#
#     input_data = pd.DataFrame([[
#         recency, frequency, monetary,
#         page_views, cart,
#         tickets, sentiment,
#         email, discount,
#         engagement, rf_ratio
#     ]], columns=features)
#
#     prob = model.predict_proba(input_data)[0][1]
#
#     st.subheader(f"🎯 Churn Probability: {prob:.2f}")
#
#     action = get_action(prob, clv, engagement, cart)
#     st.success(action)
#
#     st.divider()
#
#     # -------------------------------
#     # GRAPH 1: GAUGE CHART
#     # -------------------------------
#     st.subheader("📈 Churn Risk Gauge")
#
#     fig_gauge = go.Figure(go.Indicator(
#         mode="gauge+number",
#         value=prob * 100,
#         title={"text": "Churn %"},
#         gauge={
#             "axis": {"range": [0, 100]},
#             "bar": {"color": "red"},
#             "steps": [
#                 {"range": [0, 30], "color": "green"},
#                 {"range": [30, 60], "color": "yellow"},
#                 {"range": [60, 100], "color": "red"},
#             ],
#         },
#     ))
#
#     st.plotly_chart(fig_gauge, use_container_width=True)
#
#     # -------------------------------
#     # GRAPH 2: FEATURE IMPORTANCE
#     # -------------------------------
#     st.subheader("📊 Feature Importance")
#
#     fig_imp = px.bar(
#         imp_df.sort_values("importance"),
#         x="importance",
#         y="feature",
#         orientation="h",
#         title="Feature Importance"
#     )
#
#     st.plotly_chart(fig_imp, use_container_width=True)
#
#     # -------------------------------
#     # GRAPH 3: INPUT COMPARISON
#     # -------------------------------
#     st.subheader("🔍 Your Input vs Typical Values")
#
#     avg_values = {
#         "recency_days": 180,
#         "frequency": 15,
#         "monetary": 3000,
#         "cart_abandonment_rate": 0.5,
#         "email_open_rate": 0.4
#     }
#
#     compare_df = pd.DataFrame({
#         "Feature": list(avg_values.keys()),
#         "Your Value": [
#             recency, frequency, monetary, cart, email
#         ],
#         "Typical": list(avg_values.values())
#     })
#
#     fig_compare = px.bar(
#         compare_df,
#         x="Feature",
#         y=["Your Value", "Typical"],
#         barmode="group",
#         title="Comparison"
#     )
#
#     st.plotly_chart(fig_compare, use_container_width=True)

import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go
import smtplib
from email.mime.text import MIMEText

from retention import get_action
from email_templates import generate_email

# -------------------------------
# LOAD FILES
# -------------------------------
model = pickle.load(open("models/model.pkl", "rb"))
features = pickle.load(open("models/features.pkl", "rb"))
imp_df = pd.read_csv("models/feature_importance.csv")

st.set_page_config(page_title="Churn System", layout="wide")
st.title("Customer Churn Prediction Dashboard")

# -------------------------------
# INPUT SECTION
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    recency = st.number_input("Recency (days)", 1, 365, 30)
    frequency = st.number_input("Frequency", 1, 50, 5)
    monetary = st.number_input("Monetary", 50.0, 10000.0, 500.0)
    page_views = st.number_input("Page Views", 1, 200, 20)

with col2:
    cart = st.slider("Cart Abandonment", 0.0, 1.0, 0.4)
    tickets = st.number_input("Support Tickets", 0, 10, 1)
    sentiment = st.slider("Sentiment Score", 1.0, 5.0, 3.5)
    email = st.slider("Email Open Rate", 0.0, 1.0, 0.3)
    discount = st.slider("Discount Dependency", 0.0, 1.0, 0.4)

clv = st.number_input("Predicted CLV", 0.0, 10000.0, 1000.0)

# -------------------------------
# SESSION STATE INIT
# -------------------------------
if "email_sent" not in st.session_state:
    st.session_state.email_sent = False
if "last_user" not in st.session_state:
    st.session_state.last_user = ""
if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("Predict Churn"):

    st.session_state.prediction_done = True

    # Feature engineering
    engagement = email * 0.6 + (1 - cart) * 0.4
    rf_ratio = recency / (frequency + 1)

    input_data = pd.DataFrame([[
        recency, frequency, monetary,
        page_views, cart,
        tickets, sentiment,
        email, discount,
        engagement, rf_ratio
    ]], columns=features)

    prob = model.predict_proba(input_data)[0][1]

    st.session_state.prob = prob
    st.session_state.engagement = engagement
    st.session_state.rf_ratio = rf_ratio

# -------------------------------
# SHOW RESULTS (NO REFRESH EFFECT)
# -------------------------------
if st.session_state.prediction_done:

    prob = st.session_state.prob
    engagement = st.session_state.engagement

    st.subheader(f"Churn Probability: {prob:.2f}")

    action = get_action(prob, clv, engagement, cart)
    st.success(action)

    # -------------------------------
    # GRAPH 1
    # -------------------------------
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={"text": "Churn Percentage"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "red"},
            "steps": [
                {"range": [0, 30], "color": "green"},
                {"range": [30, 60], "color": "yellow"},
                {"range": [60, 100], "color": "red"},
            ],
        },
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)

    # -------------------------------
    # FEATURE IMPORTANCE
    # -------------------------------
    fig_imp = px.bar(
        imp_df.sort_values("importance"),
        x="importance",
        y="feature",
        orientation="h"
    )
    st.plotly_chart(fig_imp, use_container_width=True)

    # -------------------------------
    # SEGMENT
    # -------------------------------
    if prob > 0.8:
        seg = "Critical"
    elif prob > 0.6:
        seg = "High Risk"
    elif prob > 0.4:
        seg = "Medium Risk"
    else:
        seg = "Low Risk"

    st.subheader(f"Customers in {seg} Segment")

    df_all = pd.read_csv("models/final_data.csv")
    segment_df = df_all[df_all["segment"] == seg].head(10)

    st.dataframe(segment_df[["name", "email_id", "predicted_clv"]])

    # -------------------------------
    # EMAIL SYSTEM
    # -------------------------------
    selected_customer = segment_df.iloc[0]
    name = selected_customer["name"]
    email_id = selected_customer["email_id"]

    generated_email = generate_email(name, seg)

    edited_email = st.text_area(
        "Edit Email Before Sending",
        generated_email,
        height=300,
        key="email_editor"
    )

    # -------------------------------
    # SEND EMAIL
    # -------------------------------
    def send_email(receiver_email, message_text):
        try:
            sender_email = "your_email@gmail.com"
            password = "your_app_password"

            msg = MIMEText(message_text)
            msg["Subject"] = "Dhurandar Enterprise"
            msg["From"] = sender_email
            msg["To"] = receiver_email

            # Uncomment later for real sending
            # with smtplib.SMTP("smtp.gmail.com", 587) as server:
            #     server.starttls()
            #     server.login(sender_email, password)
            #     server.send_message(msg)

            return True
        except:
            return False

    if st.button("Send Email", key="send_btn"):

        with st.spinner("Sending email..."):
            success = send_email(email_id, edited_email)

        if success:
            st.session_state.email_sent = True
            st.session_state.last_user = name
        else:
            st.session_state.email_sent = False

    # -------------------------------
    # NOTIFICATION (NO REFRESH FEEL)
    # -------------------------------
    if st.session_state.email_sent:
        st.success(f"Email sent successfully to {st.session_state.last_user}")
    # -------------------------------
    # CHURN REASON
    # -------------------------------
    if engagement < 0.3:
        reason = "Low customer engagement"
    elif cart > 0.7:
        reason = "High cart abandonment"
    elif recency > 200:
        reason = "Customer inactivity"
    else:
        reason = "General behavioral decline"

    st.subheader("Churn Reason")
    st.info(reason)
    # -------------------------------
    # CLV PRIORITY
    # -------------------------------
    st.subheader("Customer Value")

    if clv > 5000:
        st.success("High Value Customer")
    elif clv > 2000:
        st.warning("Medium Value Customer")
    else:
        st.info("Low Value Customer")
    # -------------------------------
    # REVENUE IMPACT
    # -------------------------------
    st.subheader("Revenue Impact")

    saved_revenue = clv * (1 - prob)

    col1, col2 = st.columns(2)

    col1.metric("Predicted CLV", f"{clv:.2f}")
    col2.metric("Expected Revenue Saved", f"{saved_revenue:.2f}")
    # -------------------------------
    # PRODUCT RECOMMENDATION
    # -------------------------------
    st.subheader("Recommended Strategy")

    if cart > 0.7:
        st.write("Offer discount on items left in cart")
    elif engagement < 0.3:
        st.write("Recommend trending products")
    elif clv > 5000:
        st.write("Recommend premium products")
    else:
        st.write("Recommend popular products")
    # -------------------------------
    # RFM SCORE
    # -------------------------------
    st.subheader("RFM Analysis")

    r_score = 5 if recency < 60 else 3 if recency < 180 else 1
    f_score = 5 if frequency > 30 else 3 if frequency > 10 else 1
    m_score = 5 if monetary > 5000 else 3 if monetary > 2000 else 1

    rfm_total = r_score + f_score + m_score

    st.write(f"Recency Score: {r_score}")
    st.write(f"Frequency Score: {f_score}")
    st.write(f"Monetary Score: {m_score}")
    st.write(f"Total RFM Score: {rfm_total}")