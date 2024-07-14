import json
from tabulate import tabulate


class Product:
    def __init__(
            self,
            id: int,
            name: str,
            price: float,
            quantity: int) -> None:
        """
        :param id: id of the product.
        :param name: name of the product.
        :param price: price of the product.
        :param quantity: quantity of the product
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> dict:
        """
        Function to convert the product list to dictionary containing key value pairs

        :return: dictionary of a particular product
        """
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    @staticmethod
    def get_positive_price(message: str) -> float:
        """
        Function to ask the user to enter a positive value for the price

        :param message: message given to user for input
        :return: positive float value
        """
        while True:
            try:
                value = float(input(message))
                if value <= 0:
                    print("Please enter a positive value")
                    continue
                return value
            except ValueError:
                print("Please enter a numeric value only")

    @staticmethod
    def get_positive(message: str) -> int:
        """
        Function to ask the user to enter a positive value for the quantity/id/threshold

        :param message: message given to user for input
        :return: positive int value
        """
        while True:
            try:
                value = int(input(message))
                if value <= 0:
                    print("Please enter a positive value")
                    continue
                return value
            except ValueError:
                print("Please enter a numeric value only")


class Inventory:
    """
    class to manage the inventory products. Defines functions to perform operations like add/delete/update
    and many more on products

    """

    def __init__(self):
        self.products = []
        self.load_data()

    def add_product(self, product: Product) -> None:
        """
        Function to add product to the inventory

        :param product: details of product to add

        >>> len(inventory.products)
        6
        >>> product = Product(107, 'Comb', 5.89, 10)
        >>> inventory.add_product(product)
        >>> len(inventory.products)
        7
        """
        self.products.append(product)

    def total_inventory_value(self) -> float:
        """
        Function to calculate the total inventory value by multiplying each products price * quantity
        and summing it up

        :return: the float value of total inventory calculated
        >>> inventory.total_inventory_value()
        2261.35
        """
        total_value = 0
        for product in self.products:
            total_value = total_value + product.price * product.quantity
        return total_value

    def list_all_products(self) -> list:
        """
        Function to return all the products in the inventory with their details

        :return: list of all products
        >>> len(inventory.list_all_products())
        7
        >>> inventory.list_all_products()
        [[101,'Facewash', 120.05, 6], [102, 'Toothbrush', 10.79, 20], [103, 'BodyWash', 50.25, 4]
        [104, 'Toner', 60.25, 7], [105, 'Lotion', 70.89, 2], [106, 'Shampoo', 45.62, 11],
        [107, 'Comb', 5.89, 10]]
        """
        rows = [[product.id, product.name, product.price, product.quantity]
                for product in self.products]
        return rows

    def low_stock_alert(self, threshold: int) -> list or None:
        """
        Function to return the list of all products for which the quantity is under a threshold

        :param threshold: the threshold that we compare with the quantity of each product
        :return: list of all products with quantity less than threshold and if there are no products None returned

        >>> inventory.low_stock_alert(5)
        [[103, 'BodyWash', 50.25, 4], [105, 'Lotion', 70.89, 2]]
        >>> inventory.low_stock_alert(1)
        None
        """
        rows = []
        for product in self.products:
            if product.quantity < threshold:
                rows.append([product.id, product.name,
                            product.price, product.quantity])
        if rows:
            return rows
        return None

    def view_product(self, id_to_search: int) -> list or None:
        """
        Function to return a particular product based on the product id given

        :param id_to_search: to id of the product we want to return
        :return: list of product whose id matched the id_to_search


        >>> inventory.view_product(102)
        [102, 'Toothbrush', 10.79, 20]
        """
        for product in self.products:
            if product.id == id_to_search:
                row = [
                    product.id,
                    product.name,
                    product.price,
                    product.quantity]
                return row
        return None

    def update_product(
            self,
            id_to_search: int,
            new_price: float = None,
            new_quantity: int = None
    ) -> None:
        """
        Function to update the product based on the given id, the update can be for price/quantity/both.
        Given id is checked in the product list before the call to this function is made

        :param id_to_search: to id of the product we want to update
        :param new_price: the new price with which we want to update the previous price with, if not given taken as None
        :param new_quantity: the new quantity with which we want to update the previous quantity with, if not given taken as None
        :return: None

        >>> inventory.view_product(105)
        [105, 'Lotion', 70.89, 2]
        >>> inventory.update_product(105, 81.33, 8)
        >>> inventory.view_product(105)
        [105, 'Lotion', 81.33, 8]
        """
        for product in self.products:
            if product.id == id_to_search:
                if new_price is not None:
                    product.price = new_price
                if new_quantity is not None:
                    product.quantity = new_quantity

    def delete_product(self, id_to_search: int) -> bool:
        """
        Function to delete a particular product from the inventory based on a particular id

        :param id_to_search:
        :return: True if the product is found and deleted, False if not found

        >>> inventory = Inventory()
        >>> inventory.delete_product(103)
        True
        """
        for product in self.products:
            if product.id == id_to_search:
                self.products.remove(product)
                return True
        return False

    def dump_data(self) -> None:
        """
        Function to dump the data into the inventoy once the user exist from main.
        All the products in the product list are dumped to products.json file after converting each product list to dictionary

        :return: None
        """
        json_data = json.dumps([product.to_dict()
                               for product in self.products], indent=4)
        with open("products.json", "w") as file:
            file.write(json_data)

    def load_data(self) -> None:
        """
        Function to dump data into the products.json file. If file does not exist a new product.json file is created with dummy data and
        then the data is loaded else data id loaded directly
        :return: None
        """
        json_file_products = [
            {"id": 101, "name": "Facewash", "price": 120.05, "quantity": 6},
            {"id": 102, "name": "Toothbrush", "price": 10.79, "quantity": 20},
            {"id": 103, "name": "BodyWash", "price": 50.25, "quantity": 4},
            {"id": 104, "name": "Toner", "price": 60.25, "quantity": 7},
            {"id": 105, "name": "Lotion", "price": 70.89, "quantity": 2},
            {"id": 106, "name": "Shampoo", "price": 45.62, "quantity": 11}
        ]

        try:
            with open("products.json", 'r') as file:
                data = json.load(file)
                for item in data:
                    product = Product(item["id"], item["name"], float(item["price"]), item["quantity"])
                    self.products.append(product)
        except FileNotFoundError:
            json_data = json.dumps(json_file_products, indent=4)
            with open("products.json", "w") as file:
                file.write(json_data)
            with open("products.json", 'r') as file:
                data = json.load(file)
                for item in data:
                    product = Product(item["id"], item["name"], float(item["price"]), item["quantity"])
                    self.products.append(product)

    @staticmethod
    def print_table(rows: list = None) -> None:
        """
        Function to print the list of products in a particular format using tabulate for good structure

        :param rows: list of products to display
        """
        if not rows:
            print("No products in the inventory right now")
            return
        if not isinstance(rows[0], list):
            rows = [rows]
        headers = ["ID", "Name", "Price", "Quantity"]
        formatted_rows = [[r[0], r[1], f"${r[2]:.2f}", r[3]] for r in rows]
        print("\n-----------Items in the Inventory---------")
        print(tabulate(formatted_rows, headers=headers, tablefmt="grid"))


def main():
    inventory = Inventory()  # inventory object initilaized

    while True:
        print("\n----------- Inventory Management System -------------")
        print("1.Add Product")
        print("2.Update Product")
        print("3.Delete Product")
        print("4.View Product")
        print("5.List All Products")
        print("6.Low-Stock Alert")
        print("7.Total Inventory Value")
        print("8.Exit")

        selection = input("\nEnter your choice(1-8): ").strip()

        # add product
        if selection == '1':
            # if product list is empty, the ids will be automatimatically
            # assigned starting from 101
            if inventory.products:
                id = max(product.id for product in inventory.products) + 1
            else:
                id = 101
            name = input("Enter Product Name: ")
            price = Product.get_positive_price("Enter Product Price: ")
            quantity = Product.get_positive("Enter Product Quantity: ")
            new_product = Product(id, name, price, quantity)
            inventory.add_product(new_product)
            print("Product added successfully!!!!")

        # update product
        elif selection == '2':
            id_to_search = Product.get_positive(
                "Enter the id of the product to update: ")
            all_product_ids = [product.id for product in inventory.products]
            # if id is in product list, product is updated else continue to
            # menu
            if id_to_search in all_product_ids:
                print("Update Options:")
                print("1.Price")
                print("2.Quantity")
                print("3.Both")
                # the user can either update price, quantity or both
                update_choice = input("Enter your choice(1-3): ").strip()
                while update_choice not in {'1', '2', '3'}:
                    update_choice = input(
                        "Please enter a valid choice(1-3): ").strip()
                new_price = new_quantity = None
                if update_choice == '1' or update_choice == '3':
                    new_price = Product.get_positive_price(
                        "Enter the new price: ")
                if update_choice == '2' or update_choice == '3':
                    new_quantity = Product.get_positive(
                        "Enter the new quantity: ")
                result = inventory.update_product(
                    id_to_search, new_price, new_quantity)
                print("Product updated successfully!!")
            else:
                print("Product not found with the particular id")

        # delete product based on id
        elif selection == '3':
            id_to_search = Product.get_positive(
                "Enter the id of the product to delete: ")
            result = inventory.delete_product(id_to_search)
            if result:
                print("Product deleted successfully!!")
            else:
                print("Could not delete product since no id found")

        # view product based on id
        elif selection == '4':
            id_to_search = Product.get_positive(
                "Enter the id of the product to display: ")
            row = inventory.view_product(id_to_search)
            if row:
                inventory.print_table(row)
            else:
                print("Product not found with the particular id")

        # view all products
        elif selection == '5':
            rows = inventory.list_all_products()
            if rows:
                inventory.print_table(rows)
            else:
                print("No products in the inventory right now")

        # check low stock inventory given threshold
        elif selection == '6':
            threshold = Product.get_positive(
                "Enter the threshold for which you want to check: ")
            rows = inventory.low_stock_alert(threshold)
            if rows:
                inventory.print_table(rows)
            else:
                print("No products found less than threshold")

        # view total inventory value
        elif selection == '7':
            total_value = inventory.total_inventory_value()
            print(f"Total Inventory Value in System: ${total_value:.2f}")

        # exit program and save data to json file
        elif selection == '8':
            inventory.dump_data()
            break

        else:
            print("Please enter a valid choice(1-8)")


if __name__ == "__main__":
    main()
