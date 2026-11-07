
import sys
import unittest
from pathlib import Path

# Allow tests to import files from src
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from data_manager import load_orders
from recommender import (
    build_pair_counts,
    recommend_products,
    recommend_for_customer,
    recommend_best_sellers
)


class TestBuyNext(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.orders = load_orders()
        cls.pair_counts = build_pair_counts(cls.orders)

    # Test 1: Check customer data
    def test_customer_data(self):
        self.assertEqual(len(self.orders), 13)

    # Test 2: Check product pair counting
    def test_pair_counting(self):
        self.assertEqual(
            self.pair_counts[("Laptop", "Mouse")], 4
        )

    # Test 3: Check product recommendations
    def test_product_recommendations(self):
        results = recommend_products("Laptop", self.pair_counts)

        self.assertEqual(len(results), 3)
        self.assertEqual(results[0][0], "Mouse")

    # Test 4: Check case-insensitive search
    def test_case_insensitive_search(self):
        results = recommend_products("laptop", self.pair_counts)

        self.assertTrue(len(results) > 0)

    # Test 5: Check customer recommendations
    def test_customer_recommendations(self):
        results, cold_start = recommend_for_customer(
            "Customer_A", self.orders, self.pair_counts
        )

        self.assertFalse(cold_start)
        self.assertTrue(len(results) > 0)

        recommended_products = [item[0] for item in results]

        self.assertNotIn("Laptop", recommended_products)
        self.assertNotIn("Mouse", recommended_products)
        self.assertNotIn("Keyboard", recommended_products)

    # Test 6: Check cold-start recommendations
    def test_cold_start(self):
        results, cold_start = recommend_for_customer(
            "Customer_M", self.orders, self.pair_counts
        )

        self.assertTrue(cold_start)
        self.assertEqual(len(results), 3)

    # Test 7: Check unknown customer
    def test_unknown_customer(self):
        results, cold_start = recommend_for_customer(
            "New_Customer", self.orders, self.pair_counts
        )

        self.assertTrue(cold_start)
        self.assertEqual(len(results), 3)

    # Test 8: Check best sellers
    def test_best_sellers(self):
        results = recommend_best_sellers(self.orders)

        self.assertEqual(len(results), 3)
        self.assertEqual(results[0][1], 7)


if __name__ == "__main__":
    unittest.main()
