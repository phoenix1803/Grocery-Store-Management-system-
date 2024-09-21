import pickle
import time
from datetime import datetime

def main_menu():
    print("Welcome to the Grocery Store")
    print("Grocery Store Management System")
    print("1. Admin")
    print("2. Buyer")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        admin_login()
    elif choice == '2':
        buyer_menu()
    elif choice == '3':
        exit()
    else:
        print("Invalid choice! Please try again.")
        main_menu()

def admin_login():
    admin_id = input("Enter Admin ID: ")
    password = input("Enter Password: ")
    if admin_id == 'admin' and password == '1234':
        admin_menu()
    else:
        print("Incorrect credentials! Try again.")
        admin_login()

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. View Stocks")
        print("2. Buy Stocks")
        print("3. Edit Stocks")
        print("4. Add Stock")
        print("5. View Orders")
        print("6. Check Order Status")
        print("7. Check Customers")
        print("8. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_stocks()
        elif choice == '2':
            buy_stocks()
        elif choice == '3':
            edit_stocks()
        elif choice == '4':
            add_stock()
        elif choice == '5':
            view_orders()
        elif choice == '6':
            check_order_status()
        elif choice == '7':
            check_customers()
        elif choice == '8':
            main_menu()
        else:
            print("Invalid choice! Please try again.")

def buyer_menu():
    customer_name = input("Enter your name: ")
    cart = []
    while True:
        print("\nBuyer Menu:")
        print("1. Add Item to Cart")
        print("2. Checkout")
        print("3. View Previous Orders")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item_to_cart(cart)
        elif choice == '2':
            checkout(cart, customer_name)
            break
        elif choice == '3':
            view_previous_orders(customer_name)
        elif choice == '4':
            main_menu()
        else:
            print("Invalid choice! Please try again.")

def view_stocks():
    print("Viewing Stocks...")
    time.sleep(1)
    try:
        with open('stocks.dat', 'rb') as f:
            stocks = pickle.load(f)
            print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Item", "Price", "Quantity"))
            for stock in stocks:
                print("{:<10} {:<20} {:<10} {:<10}".format(stock['id'], stock['item'], stock['price'], stock['quantity']))
    except FileNotFoundError:
        print("No stocks available!")

def buy_stocks():
    print("Buying Stocks...")
    time.sleep(1)

def edit_stocks():
    print("Editing Stocks...")
    try:
        with open('stocks.dat', 'rb') as f:
            stocks = pickle.load(f)
        stock_id = input("Enter the ID of the stock you want to edit: ")
        for stock in stocks:
            if stock['id'] == stock_id:
                print(f"Current Price: {stock['price']}, Current Quantity: {stock['quantity']}")
                new_price = float(input("Enter new price: "))
                new_quantity = int(input("Enter new quantity: "))
                stock['price'] = new_price
                stock['quantity'] = new_quantity
                with open('stocks.dat', 'wb') as f:
                    pickle.dump(stocks, f)
                print("Stock updated successfully.")
                break
        else:
            print("Stock ID not found.")
    except FileNotFoundError:
        print("No stocks available to edit.")

def add_stock():
    print("Adding New Stock...")
    stock_id = input("Enter Stock ID: ")
    item_name = input("Enter Item Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    
    new_stock = {'id': stock_id, 'item': item_name, 'price': price, 'quantity': quantity}
    
    try:
        with open('stocks.dat', 'rb') as f:
            stocks = pickle.load(f)
    except FileNotFoundError:
        stocks = []
    
    stocks.append(new_stock)
    
    with open('stocks.dat', 'wb') as f:
        pickle.dump(stocks, f)
    print("Stock added successfully.")

def view_orders():
    print("Viewing Orders...")
    try:
        with open('orders.dat', 'rb') as f:
            orders = pickle.load(f)
            for order in orders:
                print(f"Customer: {order['customer']} | Total: {order['total']} | Time: {order['time']}")
    except FileNotFoundError:
        print("No orders available!")

def check_order_status():
    print("Checking Order Status...")
    try:
        with open('orders.dat', 'rb') as f:
            orders = pickle.load(f)
            order_id = input("Enter the Order ID to check status: ")
            for idx, order in enumerate(orders):
                if idx == int(order_id):
                    print(f"Order {order_id}: Status - {'Processed' if order['processed'] else 'Pending'}")
                    return
        print("Order not found!")
    except FileNotFoundError:
        print("No orders to check status!")

def check_customers():
    print("Checking Customers...")
    try:
        with open('orders.dat', 'rb') as f:
            orders = pickle.load(f)
            customers = set(order['customer'] for order in orders)
            print("Customers who have made purchases: ", ", ".join(customers))
    except FileNotFoundError:
        print("No customers found!")

def add_item_to_cart(cart):
    item_id = input("Enter Item ID: ")
    quantity = int(input("Enter Quantity: "))
    try:
        with open('stocks.dat', 'rb') as f:
            stocks = pickle.load(f)
            for stock in stocks:
                if stock['id'] == item_id:
                    if stock['quantity'] >= quantity:
                        cart.append({'item': stock['item'], 'price': stock['price'], 'quantity': quantity})
                        print(f"{quantity} of {stock['item']} added to cart.")
                        stock['quantity'] -= quantity
                        with open('stocks.dat', 'wb') as f:
                            pickle.dump(stocks, f)
                    else:
                        print("Insufficient stock!")
    except FileNotFoundError:
        print("No stocks available!")

def checkout(cart, customer_name):
    print("\nChecking out...")
    total = 0
    for item in cart:
        total += item['price'] * item['quantity']
    
    print(f"Total Amount: {total}")
    need_bill = input("Do you want a bill? (y/n): ")
    
    if need_bill.lower() == 'y':
        generate_bill(cart, customer_name, total)
    
    save_order(cart, customer_name, total)
    time.sleep(1)
    print("Thank you for shopping!")

def generate_bill(cart, customer_name, total):
    filename = f"{customer_name}_bill.txt"
    with open(filename, 'w') as f:
        f.write("------ Grocery Store ------\n")
        f.write(f"Customer: {customer_name}\n")
        f.write(f"Date/Time: {datetime.now()}\n")
        f.write("\nItems Purchased:\n")
        for item in cart:
            f.write(f"{item['item']} - {item['quantity']} * {item['price']} = {item['quantity'] * item['price']}\n")
        f.write(f"\nTotal: {total}\n")
        print(f"Bill generated successfully and saved as {filename}.")
    
    with open(filename, 'r') as f:
        print(f.read())

def save_order(cart, customer_name, total):
    try:
        with open('orders.dat', 'rb') as f:
            orders = pickle.load(f)
    except FileNotFoundError:
        orders = []

    orders.append({'customer': customer_name, 'cart': cart, 'total': total, 'time': datetime.now(), 'processed': True})
    
    with open('orders.dat', 'wb') as f:
        pickle.dump(orders, f)
        print("Order saved successfully.")

def view_previous_orders(customer_name):
    print(f"\nViewing orders for {customer_name}...")
    try:
        with open('orders.dat', 'rb') as f:
            orders = pickle.load(f)
            for order in orders:
                if order['customer'] == customer_name:
                    print(f"Order at {order['time']}: Total - {order['total']}")
    except FileNotFoundError:
        print("No orders found!")

if __name__ == "__main__":
    main_menu()
