"""
Lab Evaluation 3: Functional Principles in Contemporary Languages
Total Marks: 15 (3 Questions x 5 Marks each)
Reference: Unit III.pdf
"""

# Question 1: Immutability and Comprehensions (5 Marks)
# -------------------------------------------------------------------------
# Scenario: You have a list of dictionaries representing product inventory:
products = [{'name': 'Laptop', 'price': 1200}, {'name': 'Mouse', 'price': 25}, {'name': 'Monitor', 'price': 300}]
#
# Task:
# 1. Write a script using a list comprehension to create a new list containing 
#    only the names of products that cost more than 100[cite: 1].
# 2. Constraint: Do not use explicit 'for' loops with 'list.append()'[cite: 1].
# 3. Comment: Explain how this approach adheres to the principle of 
#    avoiding state updating compared to an iterative approach[cite: 1].
exp_products = [product for product in products if(product['price'] > 100)]
# print(exp_products)

# Question 2: Closures and Higher-Order Functions (5 Marks)
# -------------------------------------------------------------------------
# Task:
# 1. Implement a closure named 'make_shirter' that takes a string 'prefix' 
#    as its argument[cite: 1].
# 2. The inner function should take a string 'name' and return the prefix 
#    and name combined (e.g., "Dr. Smith")[cite: 1].
# 3. Demonstrate the use of this closure by creating two specialized 
#    functions (e.g., sir_formatter and madam_formatter) and calling them[cite: 1].
# 4. Comment: Identify the specific higher-order function characteristics 
#    present in your implementation[cite: 1].
def make_shirter(prefix: str):
    def make_prefixed_shirter(name: str):
        return prefix + name
    return make_prefixed_shirter

male_shirter = make_shirter('Mr. ')

print(male_shirter('Praanesh'))


# Question 3: Lazy Evaluation with Generators (5 Marks)
# -------------------------------------------------------------------------
# Task:
# 1. Create a generator function named 'infinite_powers' that yields the 
#    powers of a given base 'n' indefinitely (n^1, n^2, n^3, ...)[cite: 1].
# 2. Use the 'next()' function to retrieve and print the first three 
#    values of 2^x[cite: 1].
# 3. Use a 'for' loop with a 'break' condition to print the powers of 3^x 
#    until the value exceeds 1000[cite: 1].
# 4. Comment: Briefly explain one memory efficiency advantage of using 
#    this generator over a standard list for a large sequence[cite: 1].

def generator(n: int):
    current_exponent:int = 0
    while(True):
        yield (n ** current_exponent)
        # when next hits
        current_exponent += 1

gentoo = generator(2)

for i in range(5):
    print(f"Generator ran {i} times, value: {next(gentoo)}")
