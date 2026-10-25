import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("bestsellers.csv")

df.drop_duplicates(inplace=True)

df.rename(
    columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"},
    inplace=True,
)

df["Price"] = df["Price"].astype(float)

# Get the first 5 rows of the spreadsheet
# print(df.head())

# # Get the shape of the spreadsheet
# print(df.shape)

# # Get the column names of the spreadsheet
# print(df.columns)

# # Get summary statistics for each column
# print(df.describe())

# author_counts = df["Author"].value_counts()
# # print(author_counts)

# avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
# # print(avg_rating_by_genre)

# # Export top selling authors to a CSV file
# author_counts.head(10).to_csv("top_authors.csv")

# # Export average rating by genre to a CSV file
# avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")


# Not part of the tutorial below
unique_books = df.drop_duplicates(subset=["Title"])

# Cheapest Book
cheapest_books = unique_books.nsmallest(10, "Price")
# print("Number of books:", len(cheapest_books))
# print(cheapest_books[["Title", "Price"]])
# cheapest_books.to_csv("cheapest_books.csv", index=False)


# Most Expensive Books
most_expensive_books = unique_books.nlargest(10, "Price")

# print("Number of books:", len(most_expensive_books))
# print(most_expensive_books[["Title", "Price"]])
# most_expensive_books.to_csv("most_expensive_books.csv", index=False)

# Most Reviewed Books
most_reviewed_books = unique_books.nlargest(10, "Reviews")

# print("Number of books:", len(most_reviewed_books))
# print(most_reviewed_books[["Title", "Reviews"]])
# most_reviewed_books.to_csv("most_reviewed_books.csv", index=False)

# Least Reviewed Books
least_reviewed_books = unique_books.nsmallest(10, "Reviews")

# print("Number of books:", len(least_reviewed_books))
# print(least_reviewed_books[["Title", "Reviews"]])
# least_reviewed_books.to_csv("least_reviewed_books.csv", index=False)

#  Trends

year = 2009

# Global Highest Rating with Fiction and Non Fiction
highest_rating = unique_books.nlargest(10, "Rating")

# print("Number of books:", len(highest_rating))
# print(highest_rating[["Title", "Rating"]])
# highest_rating.to_csv("highest_rating.csv", index=False)

# Year after Year highest rated books separated by genre
# Fiction
while year <= 2019:
    # Get the highest rated Fiction book for each year
    books_by_year = unique_books[
        (unique_books["Publication Year"] == year)
        & (unique_books["Genre"] == "Fiction")
    ]
    highest_rating_by_fiction = books_by_year.sort_values(
        by=["Rating", "Reviews"], ascending=[False, False]
    ).head(1)
    print(f"--- Fiction | {year}---")
    print(highest_rating_by_fiction[["Title", "Rating", "Publication Year"]])
    # highest_rating_by_year.to_csv(f"highest_rating_{year}.csv", index=False)
    year += 1

year = 2009
while year <= 2019:
    # Get the highest rated Non Fiction book for each year
    books_by_year = unique_books[
        (unique_books["Publication Year"] == year)
        & (unique_books["Genre"] == "Non Fiction")
    ]
    highest_rating_by_non_fiction = books_by_year.sort_values(
        by=["Rating", "Reviews"], ascending=[False, False]
    ).head(1)
    print(f"--- Non Fiction | {year}---")
    print(
        highest_rating_by_non_fiction[["Title", "Rating", "Publication Year"]]
    )
    # highest_rating_by_year.to_csv(f"highest_rating_{year}.csv", index=False)
    year += 1


# Global Lowest Rating with Fiction and Non Fiction
lowest_rating = unique_books.nsmallest(10, "Rating")

# print("Number of books:", len(lowest_rating))
# print(lowest_rating[["Title", "Rating"]])
# lowest_rating.to_csv("lowest_rating.csv", index=False)

year = 2009
while year <= 2019:
    # Get the lowest rated Fiction book for each year
    books_by_year = unique_books[
        (unique_books["Publication Year"] == year)
        & (unique_books["Genre"] == "Fiction")
    ]
    lowest_rating_by_year = books_by_year.nsmallest(1, "Rating")
    # print(f"--- Fiction | {year}---")
    # print(f"Year: {year}")
    # print(lowest_rating_by_year[["Title", "Rating", "Publication Year", "Genre"]])
    # lowest_rating_by_year.to_csv(f"lowest_rating_{year}.csv", index=False)

    # Get the lowest rated Non Fiction book for each year
    books_by_year = unique_books[
        (unique_books["Publication Year"] == year)
        & (unique_books["Genre"] == "Non Fiction")
    ]
    lowest_rating_by_year = books_by_year.nsmallest(1, "Rating")
    # print(f"--- Non Fiction | {year}---")
    # print(f"Year: {year}")
    # print(lowest_rating_by_year[["Title", "Rating", "Publication Year", "Genre"]])
    # lowest_rating_by_year.to_csv(f"lowest_rating_{year}.csv", index=False)
    year += 1


results = [
    cheapest_books,
    most_expensive_books,
    highest_rating,
    lowest_rating,
    most_reviewed_books,
    least_reviewed_books,
]
# results.to_csv("results.csv", index=False)
# print(results)
