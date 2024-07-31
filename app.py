import streamlit as st
from pymongo import MongoClient

st.title("AI-Powered Customer Support System")
st.write("Enter your query below:")

# MongoDB connection
client = MongoClient("mongodb+srv://abhi:<password>@cluster0.8raszzi.mongodb.net/")
db = client["customer_support"]
collection = db["queries"]

query = st.text_input("Query")
if st.button("Submit"):
    if query:
        # Store query in MongoDB
        collection.insert_one({"query": query, "response": ""})
        st.write("Your query has been submitted.")
    else:
        st.write("Please enter a query.")
