# Python_2_challenge
# Restaurant Review System

This project implements a restaurant review system with three main classes: `Customer`, `Restaurant`, and `Review`. These classes are designed to manage customer reviews and relationships between customers, restaurants, and reviews.

## Table of Contents

- [Customer Class](#customer-class)
- [Restaurant Class](#restaurant-class)
- [Review Class](#review-class)
- [Object Relationship Methods](#object-relationship-methods)
- [Aggregate and Association Methods](#aggregate-and-association-methods)

## Customer Class

### Methods

- `Customer __init__(given_name, family_name)`
  - Initializes a new customer with the provided given name and family name.

- `Customer given_name()`
  - Returns the customer's given name.
  - Can be changed after the customer is created.

- `Customer family_name()`
  - Returns the customer's family name.
  - Can be changed after the customer is created.

- `Customer full_name()`
  - Returns the full name of the customer in Western style (concatenated given name and family name).

- `Customer all()`
  - Returns a list of all customer instances.

- `Customer add_review(restaurant, rating)`
  - Creates a new review and associates it with the customer and given restaurant.
  - `restaurant` is a restaurant object.
  - `rating` is an integer star rating.

- `Customer restaurants()`
  - Returns a unique list of all restaurants a customer has reviewed.

- `Customer num_reviews()`
  - Returns the total number of reviews that a customer has authored.

- `Customer find_by_name(name)` (class method)
  - Given a full name as a string, returns the first customer whose full name matches.

- `Customer find_all_by_given_name(name)` (class method)
  - Given a given name as a string, returns a list of customers with that given name.

## Restaurant Class

### Methods

- `Restaurant __init__(name)`
  - Initializes a new restaurant with the provided name.

- `Restaurant name()`
  - Returns the restaurant's name.

- `Restaurant reviews()`
  - Returns a list of all reviews for that restaurant.

- `Restaurant customers()`
  - Returns a unique list of all customers who have reviewed the restaurant.

- `Restaurant average_star_rating()`
  - Returns the average star rating for the restaurant based on its reviews.

## Review Class

### Methods

- `Review __init__(customer, restaurant, rating)`
  - Initializes a new review with the provided customer, restaurant, and rating.

- `Review rating()`
  - Returns the rating for a restaurant.

- `Review customer()`
  - Returns the customer object for that review.

- `Review restaurant()`
  - Returns the restaurant object for that review.

- `Review all()`
  - Returns a list of all reviews.

## Object Relationship Methods

Refer to the class-specific methods above for object relationship functionalities.

## Aggregate and Association Methods

Refer to the class-specific methods above for aggregate and association functionalities.


## MIT License

Copyright (c) Year Hellen Wamaitha

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
