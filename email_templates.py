def generate_email(name, segment):

    if segment == "Critical":
        return f"""
Subject: We Value You – An Exclusive Offer Just for You

Dear {name},

We hope this message finds you well.

At Dhurandar Enterprise, we truly value your association with us. We noticed that your recent activity has reduced, and we wanted to personally reach out to ensure everything is going smoothly.

As a valued customer, your experience matters greatly to us. To express our appreciation and to welcome you back, we are pleased to offer you an exclusive 30% discount on your next purchase.

This is a limited-time offer created specifically for you.

If there is anything we can do to improve your experience or assist you in any way, please do not hesitate to reach out. Our support team is always here to help.

We look forward to serving you again.

Warm regards,  
Customer Success Team  
Dhurandar Enterprise
"""

    elif segment == "High Risk":
        return f"""
Subject: Special Offer Inside – We Would Love to See You Again

Dear {name},

Greetings from Dhurandar Enterprise.

We noticed that you have not been as active recently, and we wanted to reconnect with you. Your continued support is very important to us.

To make your next shopping experience even better, we are offering you an exclusive 20% discount on your next order.

We have also introduced several new products and improvements that we believe you will find valuable.

We invite you to visit our platform and explore what’s new.

Thank you for being a part of our journey.

Best regards,  
Customer Engagement Team  
Dhurandar Enterprise
"""

    elif segment == "Medium Risk":
        return f"""
Subject: Discover What’s New at Dhurandar Enterprise

Dear {name},

We hope you are doing well.

At Dhurandar Enterprise, we continuously strive to enhance your shopping experience by bringing you the latest products and exciting updates.

We would like to invite you to explore our newest collections and features that have been designed keeping your preferences in mind.

We are confident that you will find something that interests you.

Thank you for choosing Dhurandar Enterprise.

Sincerely,  
Product Experience Team  
Dhurandar Enterprise
"""

    else:
        return f"""
Subject: Thank You for Being a Valued Customer

Dear {name},

We sincerely appreciate your continued trust and support in Dhurandar Enterprise.

It is customers like you who motivate us to consistently improve and deliver better services and products.

As a token of our appreciation, we will continue to bring you exclusive benefits, priority updates, and special rewards.

We look forward to serving you in the future.

Warm regards,  
Customer Relations Team  
Dhurandar Enterprise
"""