def get_action(churn_prob, clv):

    if churn_prob > 0.7:
        if clv > 3000:
            return " High-value: 25% discount + call"
        return "️ Medium: 15% discount"

    elif churn_prob > 0.4:
        return " Re-engagement email"

    return " No action needed"