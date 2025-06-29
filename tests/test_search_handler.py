from django.test.client import RequestFactory
from django.test.testcases import TestCase
from oscar.apps.catalogue import views

from oscar_pg_search.mixins import SearchViewMixin
from oscar_pg_search.postgres_search_handler import PostgresSearchHandler


class CatalogueView(views.CatalogueView, SearchViewMixin):
    pass


class TestSearchHandler(TestCase):
    def test_instance(self):
        result = PostgresSearchHandler.normalize_query("query_string")
        self.assertIsInstance(result, list)
