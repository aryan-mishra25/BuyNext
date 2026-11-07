
from data_manager import load_orders
from recommender import (
    build_pair_counts,
    recommend_products,
    recommend_for_customer,
    calculate_best_sellers
)


def display_orders(orders):

    print("\nCUSTOMER PURCHASE RECORDS")
    print("-------------------------")

    for customer, products in orders.items():
        print(customer, ":", products)


def display_pair_counts(pair_counts):

    print("\nPRODUCT CO-PURCHASE COUNTS")
    print("--------------------------")

    for pair, count in sorted(pair_counts.items()):
        print(pair[0], "+", pair[1], ":", count)


def show_product_recommendations(product, pair_counts):

    results = recommend_products(product, pair_counts)

    print("\nTOP 3 PRODUCT RECOMMENDATIONS")
    print("-----------------------------")

    if not results:
        print("No recommendations found.")
        return

    for name, count in results:
        print(f"{name} - Bought together in {count} orders")


def show_customer_recommendations(customer, orders, pair_counts):

    results, is_cold_start = recommend_for_customer(
        customer, orders, pair_counts
    )

    print("\nCUSTOMER RECOMMENDATIONS")
    print("------------------------")

    if is_cold_start:
        print("Cold-start: Using best-selling products.")

        for product, count in results:
            print(f"{product} - Purchased {count} times")

        return

    if not results:
        print("No new recommendations available.")
        return

    for product, details in results:

        print("\nProduct:", product)
        print("Recommendation Score:", details["score"])

        print(
            "Explanation: Bought with",
            details["reason_product"],
            "in",
            details["reason_count"],
            "orders."
        )


def main():

    orders = load_orders()

    if not orders:
        print("Unable to load customer data.")
        return

    pair_counts = build_pair_counts(orders)

    while True:

        print("\n======================================")
        print("          BUYNEXT RECOMMENDER")
        print("======================================")

        print("1. View Customer Orders")
        print("2. View Product Pair Counts")
        print("3. Recommend Products")
        print("4. Recommend Products for Customer")
        print("5. View Best Sellers")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":

            display_orders(orders)

        elif choice == "2":

            display_pair_counts(pair_counts)

        elif choice == "3":

            product = input("\nEnter product name: ")

            show_product_recommendations(product, pair_counts)

        elif choice == "4":

            customer = input("\nEnter customer name: ")

            show_customer_recommendations(
                customer, orders, pair_counts
            )

        elif choice == "5":

            print("\nTOP 3 BEST-SELLING PRODUCTS")

            for product, count in calculate_best_sellers(orders):
                print(f"{product} - Purchased {count} times")

        elif choice == "6":

            print("\nThank you for using BuyNext!")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
