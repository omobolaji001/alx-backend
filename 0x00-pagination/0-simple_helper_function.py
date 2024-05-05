#!/usr/bin/env python3
""" A python script that define an helper funtion
for pagination.
"""


def index_range(page, page_size):
    """Returns a tuple of size two
    containing the start and end index

    Args:
            page(INT) - The page number
            page_size(INT) - The number of elements
                             contained in a page
    Returns:
            Tuple - The start and end index
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
