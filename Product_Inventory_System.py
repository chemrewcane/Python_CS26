store_information = ("01011001 store", "Nabunturan")
products = []

print(f"{'='*5} PRODUCT INVENTORY SYSTEM {'='*5}\n")
print(f"Store: {store_information[0]}")
print(f"Location: {store_information[1]}\n")

while True:
    print("\n1. Add Product \n"
          "2. View Products \n"
          "3. Update Product \n"
          "4. Delete Product \n"
          "5. Exit")

    choice = int(input("Choose option: "))

    if choice == 1:
        print("\nAdd Product")

        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))

        product = {"name" : name,
                   "category" : category,
                   "price" : price,
                   "quantity" : quantity}

        products.append(product)

        print(f"Product '{name}' added successfully!")

    elif choice == 2:
        print("\nView Products")

        if not products:
            print("No Products added")
        else:
            for product in products:
                print(f"\nProduct Name: {product['name']}")
                print(f"Category: {product['category']}")
                print(f"Price: {product['price']:,.2f}")
                print(f"Quantity: {product['quantity']}")

            search = input("\nSearch for a product (Press enter to skip): ")

            if search:
                found = False
                for product in products:
                    if product['name'] == search:
                        print("\nProduct Found!")
                        print(f"\nProduct Name: {product['name']}")
                        print(f"Category: {product['category']}")
                        print(f"Price: {product['price']:,.2f}")
                        print(f"Quantity: {product['quantity']}")
                        found = True
                        break

                if not found:
                    print("Product not found.")

    elif choice == 3:
        print("\nUpdate Product")

        if not products:
            print("No Products to update")
        else:
            name = input("Enter Product Name to update: ")
            found = False

            for product in products:
                if product['name'] == name:
                    print("\nProduct Found!")
                    print("1. Update Price")
                    print("2. Update Quantity")

                    update_choice = int(input("Choose option: "))

                    if update_choice == 1:
                        new_price = float(input("Enter New Price: "))
                        product['price'] = new_price
                        print("Product price updated successfully!")

                    elif update_choice == 2:
                        new_quantity = int(input("Enter New Quantity: "))
                        product['quantity'] = new_quantity
                        print("Product quantity updated successfully!")

                    else:
                        print("Please choose between 1 and 2")
                    found = True
                    break

            if not found:
                print("Product not found.")

    elif choice == 4:
        print("\nDelete Product")

        if not products:
            print("No products to delete.")
        else:
            name = input("Enter product name to delete: ")
            found = False

            for product in products:
                if product["name"] == name:
                    products.remove(product)
                    print(f"Product '{name}' deleted successfully!")
                    found = True
                    break

            if not found:
                print("Product not found.")

    elif choice == 5:
        print("Thank you. Please use me again!")
        break

    else:
        print("\nPlease choose only 1 to 5")
