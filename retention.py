# def get_action(prob, clv, engagement, cart):
#
#     if prob > 0.8:
#         if clv > 3000:
#             return " High-value: 25% discount + personal call"
#         return "Medium value: 15% discount"
#
#     elif prob > 0.6:
#         return " Re-engagement email + product recommendations"
#
#     elif cart > 0.7:
#         return " Cart reminder + coupon"
#
#     elif engagement < 0.3:
#         return " Low engagement: win-back campaign"
#
#     else:
#         return "No action needed"
def get_action(prob, clv, engagement, cart):

    if prob > 0.8:
        return "30% Discount + Personal Call"
    elif prob > 0.6:
        return "Re-engagement Email"
    elif cart > 0.7:
        return " Cart Reminder Offer"
    elif engagement < 0.3:
        return " Win-back Campaign"
    else:
        return " No Action Needed"