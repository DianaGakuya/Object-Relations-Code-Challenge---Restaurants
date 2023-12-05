from customer import Customer
from restaurant import Restaurant
from review import Review

# Create sample instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
restaurant1 = Restaurant("Best Eats")
restaurant2 = Restaurant("Tasty Treats")

# Add reviews
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)
customer2.add_review(restaurant2, 3)

# Test cases
print("=== Test Cases ===")

# Test Customer Class
print("Customer Full Name:", customer1.full_name())  # John Doe
print("All Customers:", Customer.all())  # [customer1, customer2]
print("Find Customer by Name:", Customer.find_by_name("Jane Smith"))  # Customer object for Jane Smith
print("Find All Customers by Given Name:", Customer.find_all_by_given_name("John"))  # [customer1]

# Test Restaurant Class
print("\nRestaurant Name:", restaurant1.get_name())  # Best Eats
print("All Restaurants:", Restaurant.all())  # [restaurant1, restaurant2]
print("Restaurant Reviews:", restaurant1.get_reviews())  # [Review object by customer1, Review object by customer2]
print("Restaurant Customers:", restaurant1.customers())  # [customer1, customer2]
print("Restaurant Average Star Rating:", restaurant1.average_star_rating())  # 4.5

# Test Review Class
print("\nReview Rating:", customer1.reviews[0].get_rating())  # 4
print("All Reviews:", Review.all())  # [Review object by customer1, Review object by customer2]

# Additional Test Cases
print("\n=== Additional Test Cases ===")

# Test adding more reviews
customer1.add_review(restaurant2, 2)
customer2.add_review(restaurant2, 4)

print("Customer Num Reviews:", customer1.num_reviews())  # 2
print("All Restaurants for Customer:", customer1.restaurants())  # [restaurant1, restaurant2]
print("All Customers for Restaurant:", restaurant2.customers())  # [customer2, customer1]

# Test average star rating when there are no reviews
restaurant3 = Restaurant("New Place")
print("Restaurant Average Star Rating (No Reviews):", restaurant3.average_star_rating())  # 0

# Test find_by_name and find_all_by_given_name when no match is found
print("Find Customer by Name (No Match):", Customer.find_by_name("Nonexistent Name"))  # None
print("Find All Customers by Given Name (No Match):", Customer.find_all_by_given_name("Nonexistent"))  # []

# Test case with an empty list
customer3 = Customer("Sam", "Jones")
print("All Reviews (Empty):", customer3.reviews)  # []
