
<h2 align="center">Inventory Management System</h2>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#installation">Formatter Used</a></li>
    <li><a href="#assumptions">Assumptions Made</a></li>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This system will allow users to manage products, track inventory levels, and generate reports

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

1. Clone the repo
   ```sh
   git clone https://github.com/Ravneet-Kaur-2000/Inventory_Management_System.git
   ```
2. If tabulate package is missing
   ```sh
   pip install tabulate
   ```
2. Run inventory.py file
   ```sh
   python inventory.py
   ```

## Formatter Used
Autopep8: automatically formats Python code to conform to the PEP 8 style guide

1. Install
   ```sh
   pip install --upgrade autopep8
   ```
2. Usage
   ```sh
   autopep8 --in-place --aggressive --aggressive <filename>
   ```
Documentation - https://pypi.org/project/autopep8/
   
## Assumptions Made
1. Extra functions, such as converting the product list to a dictionary, asking the user for positive values for price (float), and asking the user for positive values for ID/quantity/threshold (int), have been added in the Product class.
2. Some functions in the Product and Inventory classes have been made static because they don't require access to specific instances of data.
3. The products.json file is automatically created when the program is run. This happens because at the start of main, an object of the Inventory class is initialized, which calls a function that stores dummy data in the products.json file.
4. To print tables in a good tabular format, the tabulate library has been used.
5. Only when the user exits the program, the changed data is saved back into the products.json file.
6. If we run the program for the first time, products.json is created. If we change the data and exit the program and then run it again, the changed data is loaded, ensuring data persistence after the JSON file is created.
7. The ids are automatically assigned to the products. If the list of products is empty, the ids start from 101; otherwise, when a new product is added, its id is max(existing ids) + 1.
8. Try and except blocks have been incorporated for proper error handling. All edge cases, for example, negative values for price and quantity, and many more have been handled, and proper error messages are displayed for smoother operation.

