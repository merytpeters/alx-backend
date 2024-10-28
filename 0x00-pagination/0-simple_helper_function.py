#!/usr/bin/env python3
"""Pagination, function to calculate index range"""


def index_range(page, page_size):
    """Function that takes two arguments, page and page_size"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
