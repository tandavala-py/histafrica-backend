import unittest
from typing import List, Optional

from histafrica.shared.application.dto import (
    Filter,
    Item,
    PaginationOutput,
    PaginationOutputMapper,
    SearchInput,
)
from histafrica.shared.domain.repository import SearchResult


class TestSearchInput(unittest.TestCase):
    def test_fields(self):
        self.assertEqual(
            SearchInput.__annotations__,
            {
                "page": Optional[int],
                "per_page": Optional[int],
                "sort": Optional[str],
                "sort_dir": Optional[str],
                "filter": Optional[Filter],
            },
        )


class TestPaginationOut(unittest.TestCase):

    def test_fields(self):
        self.assertEqual(
            PaginationOutput.__annotations__,
            {
                "items": List[Item],
                "total": int,
                "per_page": int,
                "current_page": int,
                "last_page": int,
            },
        )


class PaginationOutputChild(PaginationOutput):
    pass


class TestPaginationOutputMapper(unittest.TestCase):

    def test_from_child(self):
        mapper = PaginationOutputMapper.from_child(PaginationOutputChild)

        self.assertIsInstance(mapper, PaginationOutputMapper)
        self.assertTrue(issubclass(mapper.output_child, PaginationOutputChild))

    def test_to_output(self):
        result = SearchResult(
            items=["fake"],
            total=1,
            current_page=1,
            per_page=1,
            sort="name",
            sort_dir="asc",
            filter="filter fake",
        )

        output = PaginationOutputMapper.from_child(PaginationOutputChild).to_output(
            result.items, result=result
        )
        self.assertEqual(
            output,
            PaginationOutputChild(
                items=result.items,
                total=result.total,
                current_page=result.current_page,
                last_page=result.last_page,
                per_page=result.per_page,
            ),
        )
