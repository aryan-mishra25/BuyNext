
import streamlit as st

from src.data_manager import load_orders
from src.recommender import (
    build_pair_counts,
    recommend_products,
    recommend_for_customer,
    calculate_best_sellers
)

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="BuyNext | Smart Recommendations",
    page_icon="🛍️",
    layout="wide"
)


# -----------------------------------
# LOAD PROJECT DATA
# -----------------------------------

@st.cache_data
def get_project_data():

    orders = load_orders()

    pair_counts = build_pair_counts(orders)

    return orders, pair_counts


orders, pair_counts = get_project_data()


# -----------------------------------
# HEADER
# -----------------------------------

st.title("🛍️ BuyNext")

st.subheader("Smart Co-Purchase Product Recommendation Engine")

st.write(
    "Discover products frequently purchased together "
    "and receive personalized recommendations."
)

st.divider()


# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("BuyNext Navigation")

page = st.sidebar.radio(
    "Choose a feature",
    [
        "Dashboard",
        "Product Recommendations",
        "Customer Recommendations",
        "Best Sellers"
    ]
)


# -----------------------------------
# DASHBOARD
# -----------------------------------

if page == "Dashboard":

    st.header("Project Dashboard")

    all_products = sorted({
        product
        for products in orders.values()
        for product in products
    })

    total_orders = sum(
        len(products) > 0
        for products in orders.values()
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Customers", len(orders))

    col2.metric("Products", len(all_products))

    col3.metric("Orders", total_orders)

    col4.metric("Product Pairs", len(pair_counts))

    st.divider()

    st.subheader("Customer Purchase Records")

    for customer, products in orders.items():

        with st.expander(customer):

            if products:
                st.write(", ".join(products))
            else:
                st.info("No purchase history available.")

    st.subheader("How BuyNext Works")

    st.markdown("""
    1. Collect customer purchase records.
    2. Calculate product co-purchase frequencies.
    3. Identify frequently associated products.
    4. Generate personalized recommendations.
    5. Use best sellers for customers without purchase history.
    """)


# -----------------------------------
# PRODUCT RECOMMENDATIONS
# -----------------------------------

elif page == "Product Recommendations":

    st.header("🔍 Product Recommendations")

    all_products = sorted({
        product
        for products in orders.values()
        for product in products
    })

    selected_product = st.selectbox(
        "Select a product",
        all_products
    )

    if st.button("Find Recommendations", type="primary"):

        results = recommend_products(
            selected_product,
            pair_counts
        )

        st.subheader(
            f"Products frequently bought with {selected_product}"
        )

        if results:

            for index, (product, count) in enumerate(results, 1):

                with st.container(border=True):

                    st.write(f"### {index}. {product}")

                    st.write(
                        f"Purchased together in **{count} orders**"
                    )

        else:

            st.warning("No recommendations found.")


# -----------------------------------
# CUSTOMER RECOMMENDATIONS
# -----------------------------------

elif page == "Customer Recommendations":

    st.header("👤 Personalized Recommendations")

    customers = list(orders.keys())

    selected_customer = st.selectbox(
        "Select a customer",
        customers
    )

    if st.button("Generate Recommendations", type="primary"):

        results, cold_start = recommend_for_customer(
            selected_customer,
            orders,
            pair_counts
        )

        st.subheader("Recommendation Results")

        if cold_start:

            st.info(
                "Cold-start detected: Using overall best-selling products."
            )

            for index, (product, count) in enumerate(results, 1):

                with st.container(border=True):

                    st.write(f"### {index}. {product}")

                    st.write(
                        f"Purchased {count} times overall"
                    )

        elif results:

            for index, (product, details) in enumerate(results, 1):

                with st.container(border=True):

                    st.write(f"### {index}. {product}")

                    st.metric(
                        "Recommendation Score",
                        details["score"]
                    )

                    st.caption(
                        f"This product was bought with "
                        f"{details['reason_product']} in "
                        f"{details['reason_count']} orders."
                    )

        else:

            st.warning("No new recommendations available.")


# -----------------------------------
# BEST SELLERS
# -----------------------------------

elif page == "Best Sellers":

    st.header("🏆 Top Best-Selling Products")

    results = calculate_best_sellers(orders)

    for index, (product, count) in enumerate(results, 1):

        with st.container(border=True):

            st.write(f"### {index}. {product}")

            st.write(f"Total purchases: **{count}**")


# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "BuyNext | CP-013 | Python-based Co-Purchase Recommendation Engine"
)
