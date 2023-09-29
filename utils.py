# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 29 Sep 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com

"""


def get_intent(user_query):
    user_query = user_query.lower()

    # Define keywords associated with different intents
    product_keywords = ["product", "item", "buy"]
    inventory_keywords = ["inventory", "stock", "quantity"]
    price_keywords = ["price", "cost", "how much"]

    # Check for keywords to identify the intent
    if any(keyword in user_query for keyword in product_keywords):
        return 'product'
    elif any(keyword in user_query for keyword in inventory_keywords):
        return 'inventory'
    elif any(keyword in user_query for keyword in price_keywords):
        return 'price'
    else:
        # If no specific intent is identified, return a default intent (e.g., "unknown")
        return 'unknown'

