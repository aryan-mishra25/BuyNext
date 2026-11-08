
# BuyNext – Co-Purchase Product Recommendation Engine

**Problem ID:** CP-013  
**Domain:** E-Commerce and Retail  
**Difficulty:** Advanced Python

## 1. Project Overview

BuyNext is a Python-based product recommendation engine
that recommends products to customers based on the
purchasing patterns of other customers.

It uses product co-occurrence analysis to identify
products frequently purchased together.

## 2. Problem Statement

Customers often find it difficult to discover relevant
products while shopping online.

BuyNext addresses this problem by analysing customer
purchase histories and recommending products that are
frequently purchased together.

## 3. Objectives

- Store customer purchase records.
- Calculate product co-purchase frequencies.
- Recommend the top three related products.
- Generate personalized customer recommendations.
- Handle customers with no purchase history.
- Display recommendation explanations.

## 4. Technologies Used

- Programming Language: Python 3.11.3
- Editor: Visual Studio Code
- Data Storage: JSON
- Testing Framework: unittest

## 5. Project Structure

BuyNext/
│
├── data/
│   └── orders.json
│
├── src/
│   ├── main.py
│   ├── data_manager.py
│   ├── recommender.py
│   └── day1.py
│
├── tests/
│   └── test_recommender.py
│
└── README.md

## 6. Main Features

### 6.1 Customer Order Storage
Stores customer information and their purchased products
using JSON.

### 6.2 Product Co-Purchase Counting
Counts how frequently two products appear together
in customer orders.

### 6.3 Product Recommendations
Displays the top three products frequently purchased
with a selected product.

### 6.4 Personalized Recommendations
Recommends products based on a customer's previous
purchases while excluding products already purchased.

### 6.5 Cold-Start Handling
Recommends overall best-selling products when a customer
has no purchase history.

### 6.6 Recommendation Explanations
Explains why a product is recommended using its
co-purchase frequency.

## 7. Recommendation Algorithm

1. Load customer purchase data.
2. Generate all unique product pairs.
3. Count the frequency of each pair.
4. Identify products associated with a selected product
   or customer's purchase history.
5. Exclude products already purchased.
6. Rank recommendations by frequency.
7. Display the top three recommendations.

## 8. How to Run the Project

Make sure Python 3.11.3 is installed.

Open the terminal in the project directory.

Run:

python src/main.py

## 9. How to Run Tests

Execute:

python -m unittest discover -s tests -v


## 10. Future Enhancements

- Machine learning-based recommendations.
- User login and registration.
- Product database integration.
- Web-based user interface.
- Advanced collaborative filtering.

## 11. Conclusion

BuyNext demonstrates how purchase history and product
co-occurrence analysis can be used to develop a
basic personalized product recommendation system.

The project implements all five compulsory features
using Python and structured JSON data.
