
def build_pair_counts(orders):

    pair_counts = {}

    for products in orders.values():

        for i in range(len(products)):

            for j in range(i + 1, len(products)):

                pair = tuple(sorted((products[i], products[j])))

                pair_counts[pair] = pair_counts.get(pair, 0) + 1

    return pair_counts


def recommend_products(product, pair_counts):

    recommendations = {}

    product = product.strip().lower()

    for pair, count in pair_counts.items():

        if product == pair[0].lower():
            other_product = pair[1]

        elif product == pair[1].lower():
            other_product = pair[0]

        else:
            continue

        recommendations[other_product] = count

    return sorted(
        recommendations.items(),
        key=lambda x: (-x[1], x[0])
    )[:3]


def recommend_best_sellers(orders, exclude_products=None):

    if exclude_products is None:
        exclude_products = []

    excluded = {product.lower() for product in exclude_products}

    sales = {}

    for products in orders.values():

        for product in products:

            sales[product] = sales.get(product, 0) + 1

    recommendations = [
        (product, count)
        for product, count in sales.items()
        if product.lower() not in excluded
    ]

    return sorted(
        recommendations,
        key=lambda x: (-x[1], x[0])
    )[:3]


def recommend_for_customer(customer, orders, pair_counts):

    customer = customer.strip().lower()

    customer_name = None

    for name in orders:

        if name.lower() == customer:
            customer_name = name
            break

    if customer_name is None:
        return recommend_best_sellers(orders), True

    purchased = orders[customer_name]

    if not purchased:
        return recommend_best_sellers(orders), True

    recommendations = {}

    for product in purchased:

        for pair, count in pair_counts.items():

            if product == pair[0]:
                other_product = pair[1]

            elif product == pair[1]:
                other_product = pair[0]

            else:
                continue

            if other_product in purchased:
                continue

            if other_product not in recommendations:

                recommendations[other_product] = {
                    "score": 0,
                    "reason_product": product,
                    "reason_count": count
                }

            recommendations[other_product]["score"] += count

            if count > recommendations[other_product]["reason_count"]:

                recommendations[other_product]["reason_product"] = product
                recommendations[other_product]["reason_count"] = count

    ranked = sorted(
        recommendations.items(),
        key=lambda x: (-x[1]["score"], x[0])
    )

    return ranked[:3], False


def calculate_best_sellers(orders):

    return recommend_best_sellers(orders)
