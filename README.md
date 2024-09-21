# Grocery Store Management System.

This is a Python-based menu-driven **Grocery Store Management System** designed to streamline both administrative and customer interactions. The system provides two modes: **Admin** and **Buyer**. It leverages binary files to store stock and order data, ensuring fast access and persistence of information. The system is robust, allowing for easy stock management, order processing, and real-time checkout for buyers.

## Features

### Admin Mode:
- **View Stocks**: Display available stock with item details (ID, name, price, quantity).
- **Buy Stocks**: Add stock quantities for restocking purposes.
- **Edit Stocks**: Update the price and quantity of existing items.
- **Add Stock**: Manually add new stock items with ID, name, price, and quantity.
- **View Orders**: See a list of customer orders with purchase details.
- **Check Order Status**: Verify if a specific order has been processed.
- **Check Customers**: Display a list of customers who have made purchases.

### Buyer Mode:
- **Add Items to Cart**: Select items to add to the cart from available stocks.
- **Checkout**: Complete the purchase and generate an auto-printed bill with store and customer details, transaction time, and total.
- **View Previous Orders**: Check past orders made by the buyer.

## Technology Stack
- **Python**: Core programming language used to implement the system logic.
- **Pickle**: For binary data storage of stock and order details.
- **Text Files**: Used for bill generation and customer receipts.
- **Time Delays**: For a more realistic user experience.

## How to Run
1. Clone the repository.
2. Run the `main.py` script.
3. Select between **Admin** or **Buyer** mode and follow the menu options.
4. Admin credentials: ID: `admin`, Password: `1234`.
