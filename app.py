from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)

# @app.route('/api', methods=['GET'])
# def get_data():
#     data = {
#         "message": "Welcome to the Flask API!",
#         "status": "success"
#     }
#     return jsonify(data)

# # 1.1 Find Assignment Title Length
# # http://127.0.0.1:5000/title-length?title=Introduction to Python

# @app.route('/title-length', methods=['GET'])
# def get_title_length():
#      title = request.args.get('title', '')
#      length = len(title)
#      return f"Assignment title length: {length}"


# # 1.2 Extract Initials from a Student Name
# @app.route('/extract-initials', methods=['GET'])
# def extract_initials():
#     name = request.args.get('name', '')
#     # initials = ''.join([word[0].upper() for word in name.split()])
#     initials = ''
#     for word in name.split():
#         initials += word[0].upper()
#     return f"Student initials: {initials}"

# # 1.3 Create Assignment Slug
# @app.route('/create-slug', methods=['GET'])
# def create_slug():
#     title = request.args.get('title', '')
#     slug = title.replace(' ', '-').lower()
#     return f"Assignment slug: {slug}"

# # 2. Calculations

# # 2.1 Calculate Total Marks
# @app.route('/calculate-total-marks', methods=['GET'])
# def calculate_total_marks():
#     marks1 = int(request.args.get('marks1', 0))
#     marks2 = int(request.args.get('marks2', 0))
#     marks3 = int(request.args.get('marks3', 0))
#     total_marks = marks1 + marks2 + marks3
#     return f"Total marks: {total_marks}"

# # 2.2 Calculate Average Marks
# @app.route('/calculate-average-marks', methods=['GET'])
# def calculate_average_marks():
#     marks1 = int(request.args.get('marks1', 0))
#     marks2 = int(request.args.get('marks2', 0))
#     marks3 = int(request.args.get('marks3', 0))
#     average_marks = (marks1 + marks2 + marks3) / 3
#     return f"Average marks: {average_marks:.2f}"

# # 2.3 Calculate Grade
# @app.route('/calculate-grade', methods=['GET'])
# def calculate_grade():
#     total_marks = int(request.args.get('totalMarks', 0))
#     if total_marks >= 90:
#         grade = 'A'
#     elif total_marks >= 80:
#         grade = 'B'
#     elif total_marks >= 70:
#         grade = 'C'
#     elif total_marks >= 35:
#         grade = 'D'
#     else:
#         grade = 'F'
#     return f"Grade: {grade}"

# # 3. Conditional Checks

# # 3.1 Check Pass or Fail
# @app.route('/check-pass-fail', methods=['GET'])
# def check_pass_fail():
#     marks = int(request.args.get('marks', 0))
#     result = "Pass" if marks >= 40 else "Fail"
#     return result


# # 3.2 Check Eligibility for Scholarship
# @app.route('/check-scholarship', methods=['GET'])
# def check_scholarship():
#     marks = int(request.args.get('marks', 0))
#     attendance = int(request.args.get('attendance', 0))
#     if marks >= 85 and attendance >= 90:
#         return "Eligible for Scholarship"
#     else:
#         return "Not eligible for Scholarship"


# # 4. Function-Based Utilities

# # 4.1 Calculate Late Submission Penalty
# def calculate_penalty(days_late, penalty_per_day):
#     return days_late * penalty_per_day

# @app.route('/calculate-late-penalty', methods=['GET'])
# def calculate_late_penalty():
#     days_late = int(request.args.get('daysLate', 0))
#     penalty_per_day = int(request.args.get('penaltyPerDay', 0))
#     penalty = calculate_penalty(days_late, penalty_per_day)
#     return f"Total penalty: {penalty}"

# # 4.2 Estimate Study Hours
# def calculate_study_hours(daily_hours, total_days):
#     return daily_hours * total_days

# @app.route('/estimate-study-hours', methods=['GET'])
# def estimate_study_hours():
#     daily_hours = int(request.args.get('dailyHours', 0))
#     total_days = int(request.args.get('totalDays', 0))
#     total_hours = calculate_study_hours(daily_hours, total_days)
#     return f"Total study hours: {total_hours}"

# # 4.3 Recommend Assignment Topics
# topics_data = {
#     'AI': ['Machine Learning', 'Neural Networks', 'Natural Language Processing'],
#     'Web Development': ['HTML', 'CSS', 'JavaScript', 'React'],
#     'Data Science': ['Data Analysis', 'Visualization', 'Pandas', 'NumPy']
# }

# def recommend_topics(interest):
#     return topics_data.get(interest, [])

# @app.route('/recommend-topics', methods=['GET'])
# def recommend_topics_route():
#     interest = request.args.get('interest', '')
#     recommended_topics = recommend_topics(interest)
#     return f"Recommended Topics: {', '.join(recommended_topics)}" if recommended_topics else "No topics found for this interest"

# Book data
# book = {
#     'title': 'The God of Small Things',
#     'author': 'Arundhati Roy',
#     'publicationYear': 1997,
#     'genre': 'Novel',
#     'isAvailable': True,
#     'stock': 5,
# }

# @app.route('/book', methods=['GET'])
# def get_book():
#     return jsonify(book)

# # 2.1.2 Endpoint to return full title and author
# def getFullTitleAndAuthor(book):
#     return f"{book['title']} by {book['author']}"

# @app.route('/book/fulltitle-author', methods=['GET'])
# def get_full_title_and_author():
#     full_title_author = getFullTitleAndAuthor(book)
#     return jsonify({'fullTitleAndAuthor': full_title_author})


# # 2.1.3 Endpoint to return genre and availability
# def getGenreAndAvailability(book):
#     return {'genre': book['genre'], 'isAvailable': book['isAvailable']}

# @app.route('/book/genre-availability', methods=['GET'])
# def get_genre_and_availability():
#     genre_availability = getGenreAndAvailability(book)
#     return jsonify(genre_availability)

# # 2.1.4 Endpoint to calculate the age of the book
# def calculateBookAge(book):
#     current_year = datetime.now().year
#     return current_year - book['publicationYear']

# @app.route('/book/age', methods=['GET'])
# def get_book_age():
#     book_age = calculateBookAge(book)
#     return jsonify({'age': book_age})

# # 2.1.5 Endpoint to return a summary of the book
# def getBookSummary(book):
#     return f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Published: {book['publicationYear']}"

# @app.route('/book/summary', methods=['GET'])
# def get_book_summary():
#     summary = getBookSummary(book)
#     return jsonify({'summary': summary})

# # 2.1.6 Endpoint to check the stock status of the book
# def checkStockAndOrder(book):
#     if book['stock'] > 0:
#         return {'status': 'In Stock', 'stock': book['stock']}
#     else:
#         return {'status': 'Order Required', 'stock': book['stock']}

# @app.route('/book/stock-status', methods=['GET'])
# def get_stock_status():
#     stock_status = checkStockAndOrder(book)
#     return jsonify(stock_status)

# Define the GitHub public data
#

# PY2.2 - HW1
# Given Data for Question 2.2.1 to 2.2.5
# temperatures = [22, 26, 19, 30, 23, 28, 17, 31]
# prices = [80, 120, 95, 150, 60, 110]
# ratings = [4.2, 3.8, 2.5, 4.7, 3.0, 4.9, 3.6]
# indian_names = ['Akshay', 'Priyanka', 'Arjun', 'Anushka', 'Rajesh', 'Kavita']
# products = [10, 25, 50, 75, 100, 150, 200]


# # Question 2.2.1: Filter temperatures above 25 degrees Celsius
# def filterHighTemperatures(temp):
#     return temp > 25

# @app.route('/high-temperatures', methods=['GET'])
# def high_temperatures():
#     filtered_temperatures = list(filter(filterHighTemperatures, temperatures))
#     return jsonify(filtered_temperatures)

# # Question 2.2.2: Filter prices less than or equal to 100 rupees
# def filterLowPrices(price):
#     return price <= 100

# @app.route('/low-prices', methods=['GET'])
# def low_prices():
#     filtered_prices = list(filter(filterLowPrices, prices))
#     return jsonify(filtered_prices)

# # Question 2.2.3: Filter product ratings greater than 3.5
# def filterHighRatings(rating):
#     return rating > 3.5

# @app.route('/high-ratings', methods=['GET'])
# def high_ratings():
#     filtered_ratings = list(filter(filterHighRatings, ratings))
#     return jsonify(filtered_ratings)

# # Question 2.2.4: Filter Indian names longer than 6 characters
# def filterLongIndianNames(name):
#     return len(name) > 6

# @app.route('/long-indian-names', methods=['GET'])
# def long_indian_names():
#     filtered_names = list(filter(filterLongIndianNames, indian_names))
#     return jsonify(filtered_names)

# # Question 2.2.5: Filter products cheaper than a certain price
# @app.route('/cheaper-products', methods=['GET'])
# def cheaper_products():
#     filter_param = request.args.get('filterParam', type=int)  # Extract filterParam from query
#     if filter_param is not None:
#         filtered_products = [price for price in products if price < filter_param]
#         return jsonify(filtered_products)
#     else:
#         return jsonify({"error": "filterParam is required"}), 400


# PY2.2 - HW2

# numbers = [-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# # Exercise 1: Filter Prime Numbers
# def filter_prime_numbers():
#     return [num for num in numbers if is_prime(num)]

# @app.route('/prime-numbers', methods=['GET'])
# def prime_numbers():
#     return jsonify(filter_prime_numbers())


# # Exercise 2: Filter Positive Numbers
# def filter_positive_numbers():
#     return [num for num in numbers if num > 0]

# @app.route('/positive-numbers', methods=['GET'])
# def positive_numbers():
#     return jsonify(filter_positive_numbers())


# # Exercise 3: Filter Negative Numbers
# def filter_negative_numbers():
#     return [num for num in numbers if num < 0]

# @app.route('/negative-numbers', methods=['GET'])
# def negative_numbers():
#     return jsonify(filter_negative_numbers())


# # Exercise 4: Filter Odd Numbers
# def filter_odd_numbers():
#     return[num for num in numbers if num % 2 != 0]

# @app.route('/odd-numbers', methods=['GET'])
# def odd_numbers():
#     return jsonify(filter_odd_numbers())


# # Exercise 5: Filter Numbers Greater Than a Given Value
# @app.route('/numbers-greater-than', methods=['GET'])
# def numbers_greater_than():
#     value = request.args.get('value', type=int)
#     if value is not None:
#         greater_than_value = [num for num in numbers if num > value]
#         return jsonify(greater_than_value)
#     else:
#         return jsonify({"error": "value query parameter is required"}), 400


#     # Exercise 6: Filter Numbers Less Than a Given Value
# @app.route('/numbers-less-than', methods=['GET'])
# def numbers_less_than():
#     value = request.args.get('value', type=int)
#     if value is not None:
#         less_than_value = [num for num in numbers if num < value]
#         return jsonify(less_than_value)
#     else:
#         return jsonify({"error": "value query parameter is required"}), 400

# # PY2.3 - HW1

# # Given Data
# employees = [
#     { 'name': 'Rahul Gupta', 'department': 'HR', 'salary': 50000 },
#     { 'name': 'Sneha Sharma', 'department': 'Finance', 'salary': 60000 },
#     { 'name': 'Priya Singh', 'department': 'Marketing', 'salary': 55000 },
#     { 'name': 'Amit Kumar', 'department': 'IT', 'salary': 65000 }
# ]

# bikes = [
#     { 'make': 'Hero', 'model': 'Splendor', 'mileage': 80 },
#     { 'make': 'Bajaj', 'model': 'Pulsar', 'mileage': 60 },
#     { 'make': 'TVS', 'model': 'Apache', 'mileage': 70 }
# ]

# songs = [
#     { 'title': 'Tum Hi Ho', 'genre': 'Romantic', 'rating': 4 },
#     { 'title': 'Senorita', 'genre': 'Pop', 'rating': 5 },
#     { 'title': 'Dil Chahta Hai', 'genre': 'Bollywood', 'rating': 3 }
# ]

# tasks = [
#     { 'taskId': 1, 'taskName': 'Prepare Presentation', 'status': 'pending' },
#     { 'taskId': 2, 'taskName': 'Attend Meeting', 'status': 'in-progress' },
#     { 'taskId': 3, 'taskName': 'Submit Report', 'status': 'completed' }
# ]

# # http://127.0.0.1:5000/employees/department/HR

# def filterByDepartment(employee, department):
#     return employee['department'] == department

# @app.route("/employees/department/<department>", methods=["GET"])
# def get_employees(department):

#     filtered_employees = [employee for employee in employees if filterByDepartment(employee, department)]

#     return jsonify(filtered_employees)


# def filterByMileage(bike, minMileage):
#     return bike['mileage'] > minMileage

# @app.route('/bikes/mileage/<int:minMileage>', methods=['GET'])
# def get_bikes_by_mileage(minMileage):
#     filtered_bikes = [bike for bike in bikes if filterByMileage(bike, minMileage)]
#     return jsonify(filtered_bikes)


# def filterByMake(bike, make):
#     return bike['make'].lower() == make.lower()

# @app.route('/bikes/make/<make>', methods=['GET'])
# def get_bikes_by_make(make):
#     filtered_bikes = [bike for bike in bikes if filterByMake(bike, make)]
#     return jsonify(filtered_bikes)


# def filterByRating(song, minRating):
#     return song['rating'] > minRating

# @app.route('/songs/rating/<int:minRating>', methods=['GET'])
# def get_songs_by_rating(minRating):
#     filtered_songs = [song for song in songs if filterByRating(song, minRating)]
#     return jsonify(filtered_songs)


# def filterByGenre(song, genre):
#     return song['genre'].lower() == genre.lower()

# @app.route('/songs/genre/<genre>', methods=['GET'])
# def get_songs_by_genre(genre):
#     filtered_songs = [song for song in songs if filterByGenre(song, genre)]
#     return jsonify(filtered_songs)
# def filterByStatus(task, status):
#     return task['status'].lower() == status.lower()

# @app.route('/tasks/status/<status>', methods=['GET'])
# def get_tasks_by_status(status):
#     filtered_tasks = [task for task in tasks if filterByStatus(task, status)]
#     return jsonify(filtered_tasks)

# #PY2.3 - HW2


# # Given Data
# products = [
#     { 'name': 'Product A', 'inStock': True },
#     { 'name': 'Product B', 'inStock': False },
#     { 'name': 'Product C', 'inStock': True },
#     { 'name': 'Product D', 'inStock': False }
# ]

# users = [
#     { 'name': 'Alice', 'age': 25 },
#     { 'name': 'Bob', 'age': 30 },
#     { 'name': 'Charlie', 'age': 17 },
#     { 'name': 'David', 'age': 16 }
# ]

# products = [
#     { 'name': 'Product A', 'price': 50 },
#     { 'name': 'Product B', 'price': 150 },
#     { 'name': 'Product C', 'price': 200 },
#     { 'name': 'Product D', 'price': 80 }
# ]

# articles = [
#     { 'title': 'Article A', 'wordCount': 300 },
#     { 'title': 'Article B', 'wordCount': 600 },
#     { 'title': 'Article C', 'wordCount': 700 },
#     { 'title': 'Article D', 'wordCount': 200 }
# ]

# movies = [
#     { 'title': 'Movie A', 'rating': 8.5 },
#     { 'title': 'Movie B', 'rating': 7.0 },
#     { 'title': 'Movie C', 'rating': 9.0 },
#     { 'title': 'Movie D', 'rating': 6.5 }
# ]

# employees = [
#     { 'name': 'Employee A', 'experience': 3 },
#     { 'name': 'Employee B', 'experience': 6 },
#     { 'name': 'Employee C', 'experience': 10 },
#     { 'name': 'Employee D', 'experience': 2 }
# ]
# # http://127.0.0.1:5000/in-stock-products


# def filterInStockProducts(product):
#     return product['inStock'] == True

# @app.route('/in-stock-products', methods=['GET'])
# def get_in_stock_products():
#     filtered_products = [product for product in products if filterInStockProducts(product)]
#     return jsonify(filtered_products)


# # http://127.0.0.1:5000/adult-users


# def filterAdults(user):
#     return user['age']>= 18

# @app.route('/adult-users', methods=['GET'])
# def get_adult_users():
#     filtered_user= []
#     for user in users:
#         if filterAdults(user):
#             filtered_user.append(user)


#     return jsonify(filtered_user)

# # http://127.0.0.1:5000/expensive-products?price=100
# def filterExpensiveProducts(product, min_price):
#     return product['price'] > min_price

# @app.route('/expensive-products', methods=['GET'])
# def get_expensive_products():
#     min_price = float(request.args.get('price', 0))
#     filtered_products = [product for product in products if filterExpensiveProducts(product, min_price)]
#     return jsonify(filtered_products)

# def filterLongArticles(article, min_words):
#     return article['wordCount'] > min_words

# @app.route('/long-articles', methods=['GET'])
# def get_long_articles():
#     min_words = int(request.args.get('minWords', 0))
#     filtered_articles = [article for article in articles if filterLongArticles(article, min_words)]
#     return jsonify(filtered_articles)


# def filterHighRatedMovies(movie, min_rating):
#     return movie['rating'] > min_rating

# @app.route('/high-rated-movies', methods=['GET'])
# def get_high_rated_movies():
#     min_rating = float(request.args.get('rating', 0))
#     filtered_movies = [movie for movie in movies if filterHighRatedMovies(movie, min_rating)]
#     return jsonify(filtered_movies)

# def filterExperiencedEmployees(employee, min_experience):
#     return employee['experience'] > min_experience

# @app.route('/experienced-employees', methods=['GET'])
# def get_experienced_employees():
#     min_experience = int(request.args.get('years', 0))
#     filtered_employees = [employee for employee in employees if filterExperiencedEmployees(employee, min_experience)]
#     return jsonify(filtered_employees)

# PY2.4 - HW1


# # Given Data
# heights = [160, 175, 180, 165, 170]


# def sortHeightsAscending(heights):
#     return sorted(heights)


# @app.route("/heights/sort-ascending", methods=["GET"])
# def sort_heights_ascending():
#     sorted_heights = sortHeightsAscending(heights)
#     return jsonify(sorted_heights)


# def sortHeightsDescending(heights):
#     return sorted(heights, reverse=True)


# @app.route("/heights/sort-descending", methods=["GET"])
# def sort_heights_descending():
#     sorted_heights = sortHeightsDescending(heights)
#     return jsonify(sorted_heights)


# # Given Data
# employees = [
#     {"name": "Rahul", "employeeId": 101, "salary": 50000},
#     {"name": "Sita", "employeeId": 102, "salary": 60000},
#     {"name": "Amit", "employeeId": 103, "salary": 45000},
# ]


# def sortEmployeesBySalaryDescending(employees):

#     return sorted(employees, key=lambda x: x["salary"], reverse=True)


# @app.route("/employees/sort-by-salary-descending", methods=["GET"])
# def sort_employees_by_salary_descending():
#     sorted_employees = sortEmployeesBySalaryDescending(employees)
#     return jsonify(sorted_employees)


# # Given Data
# books = [
#     {"title": "The God of Small Things", "author": "Arundhati Roy", "pages": 340},
#     {"title": "The White Tiger", "author": "Aravind Adiga", "pages": 321},
#     {"title": "The Palace of Illusions", "author": "Chitra Banerjee", "pages": 360},
# ]


# def sortBooksByPagesAscending(books):

#     return sorted(books, key=lambda x: x["pages"])


# @app.route("/books/sort-by-pages-ascending", methods=["GET"])
# def sort_books_by_pages_ascending():
#     sorted_books = sortBooksByPagesAscending(books)
#     return jsonify(sorted_books)


# # PY2.4 - HW2

# books = [
#     {"title": "Moby Jonas", "author": "Herman Melville", "publication_year": 2023},
#     {"title": "1984", "author": "George Orwell", "publication_year": 1984},
#     {
#         "title": "A Tale of Two Cities",
#         "author": "Charles Jonas",
#         "publication_year": 2000,
#     },
# ]


# def sortBooksByYear(books):
#     return sorted(books, key=lambda x: x["publication_year"])


# @app.route("/books/sort-by-year", methods=["GET"])
# def sort_books_by_year():
#     sorted_books = sortBooksByYear(books)
#     return jsonify(sorted_books)


# # Given Data
# employees = [
#     {"name": "John", "salary": 75000},
#     {"name": "Jane", "salary": 50000},
#     {"name": "Doe", "salary": 30000},
# ]


# def sortEmployeesBySalary(employees):
#     return sorted(employees, key=lambda x: x["salary"], reverse=True)


# @app.route("/employees/sort-by-salary", methods=["GET"])
# def sort_employees_by_salary():
#     sorted_employees = sortEmployeesBySalary(employees)
#     return jsonify(sorted_employees)


# products = [
#     {"name": "Product C", "price": 10},
#     {"name": "Product A", "price": 15},
#     {"name": "Product B", "price": 25},
# ]


# def sortProductsByPrice(products):
#     return sorted(products, key=lambda x: x["price"])


# @app.route("/products/sort-by-price", methods=["GET"])
# def sort_products_by_price():
#     sorted_products = sortProductsByPrice(products)
#     return jsonify(sorted_products)


# events = [
#     {"name": "Event B", "date": "2023-01-01"},
#     {"name": "Event A", "date": "2023-05-01"},
#     {"name": "Event C", "date": "2023-12-01"},
# ]


# def sortEventsByDate(events):
#     return sorted(events, key=lambda x: x["date"])


# @app.route("/events/sort-by-date", methods=["GET"])
# def sort_events_by_date():
#     sorted_events = sortEventsByDate(events)
#     return jsonify(sorted_events)


# movies = [
#     {"title": "Movie A", "rating": 9.0},
#     {"title": "Movie B", "rating": 8.5},
#     {"title": "Movie C", "rating": 7.0},
# ]


# def sortMoviesByRating(movies):
#     return sorted(movies, key=lambda x: x["rating"], reverse=True)


# @app.route("/movies/sort-by-rating", methods=["GET"])
# def sort_movies_by_rating():
#     sorted_movies = sortMoviesByRating(movies)
#     return jsonify(sorted_movies)


# customers = [
#     {"name": "Customer B", "lastPurchase": "2023-11-01"},
#     {"name": "Customer A", "lastPurchase": "2023-06-15"},
#     {"name": "Customer C", "lastPurchase": "2023-03-10"},
# ]


# def sortCustomersByLastPurchase(customers):
#     return sorted(customers, key=lambda x: x["lastPurchase"], reverse=True)


# @app.route("/customers/sort-by-last-purchase", methods=["GET"])
# def sort_customers_by_last_purchase():
#     sorted_customers = sortCustomersByLastPurchase(customers)
#     return jsonify(sorted_customers)


if __name__ == "__main__":
    app.run(debug=True)
