# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 29 Sep 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com

"""
import spacy

# loading the nlp model

nlp = spacy.load("en_core_web_sm")


def get_intent_by_spacy(user_query):
    user_query = user_query.lower()
    user_query_doc = nlp(user_query)
    intent_keywords = [token.text for token in user_query_doc if token.pos_ == "VERB" or token.pos_ == "NOUN"]
    # print('intent-keywords:', intent_keywords)
    return intent_keywords


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
