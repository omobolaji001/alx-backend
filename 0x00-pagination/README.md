# Pagination in Python

This project aims to implement pagination functionality in Python, allowing you to paginate through a dataset efficiently. Pagination is a common requirement in web applications when displaying large sets of data.

## Table of Contents
1. [Simple Helper Function](#simple-helper-function)
2. [Simple Pagination](#simple-pagination)
3. [Hypermedia Pagination](#hypermedia-pagination)
4. [Deletion-Resilient Hypermedia Pagination](#deletion-resilient-hypermedia-pagination)

---

## Simple Helper Function

### Function Description

The `index_range` function takes two integer arguments, `page` and `page_size`. It returns a tuple containing a start index and an end index that correspond to the range of indexes to return in a list for those specific pagination parameters.

- Page numbers are 1-indexed, meaning the first page is referred to as page 1.

### Example Usage

```python
# Import the index_range function
index_range = __import__('0-simple_helper_function').index_range

# Example 1
res = index_range(1, 7)
print(type(res))
print(res)
# Output: <class 'tuple'>, (0, 7)

# Example 2
res = index_range(page=3, page_size=15)
print(type(res))
print(res)
# Output: <class 'tuple'>, (30, 45)
```

---

## Simple Pagination

### Class Description

This section implements simple pagination functionality by defining a `Server` class that can paginate through a database of popular baby names. The class allows you to retrieve a specific page of data based on page number and page size.

### Usage

- The `get_page` method of the `Server` class takes two integer arguments, `page` (default 1) and `page_size` (default 10). It returns a list of lists representing the dataset for the requested page.

- Asserts are used to validate that both `page` and `page_size` are integers greater than 0.

- If the input arguments are out of range for the dataset, an empty list is returned.

### Example Usage

```python
# Import the Server class
Server = __import__('1-simple_pagination').Server

# Create a Server instance
server = Server()

# Example 1: Pagination with valid values
print(server.get_page(1, 3))

# Example 2: Pagination with invalid values (out of range)
print(server.get_page(3000, 100))
```

---

## Hypermedia Pagination

### Class Description

This section extends the pagination functionality by implementing hypermedia pagination. It introduces a `get_hyper` method within the `Server` class that returns pagination information in a dictionary.

### Usage

- The `get_hyper` method takes the same arguments as `get_page` and returns a dictionary with the following key-value pairs:
  - `page_size`: The length of the returned dataset page.
  - `page`: The current page number.
  - `data`: The dataset page.
  - `next_page`: The number of the next page (None if no next page).
  - `prev_page`: The number of the previous page (None if no previous page).
  - `total_pages`: The total number of pages in the dataset as an integer.

- The `get_hyper` method internally uses the `get_page` method for data retrieval.

### Example Usage

```python
# Import the Server class
Server = __import__('2-hypermedia_pagination').Server

# Create a Server instance
server = Server()

# Example: Retrieve hypermedia pagination information
print(server.get_hyper(1, 2))
```

---

## Deletion-Resilient Hypermedia Pagination

### Class Description

This section enhances the hypermedia pagination to be deletion-resilient. The goal is to ensure that if certain rows are removed from the dataset between two queries, the user does not miss any items when changing pages.

### Usage

- The `get_hyper_index` method takes two integer arguments, `index` (default None) and `page_size` (default 10). It returns a dictionary containing pagination information.

- The dictionary includes the following key-value pairs:
  - `index`: The current start index of the return page.
  - `next_index`: The next index to query.
  - `page_size`: The current page size.
  - `data`: The actual page of the dataset.

- The `indexed_dataset` method is used to cache the dataset and index it by sorting position, starting at 0.

- Assertions are used to verify that `index` is in a valid range.

### Example Usage

```python
# Import the Server class
Server = __import__('3-hypermedia_del_pagination').Server

# Create a Server instance
server = Server()

# Example: Retrieve deletion-resilient hypermedia pagination information
print(server.get_hyper_index(3, 2))
```


**Copyright © 2024 ALX, All rights reserved.**
