#!/usr/bin/env python3
"""Defines class Server that paginates a database of popular baby names.
"""
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset.
        """
        dataset = self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        try:
            indices = index_range(page, page_size)
            return dataset[indices[0]: indices[1]]
        except IndexException as e:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing informations about the dataset.
        """
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size

        hypermedia = {
            "page_size": page_size if page_size <= len(data) else len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if (page + 1) < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hypermedia
