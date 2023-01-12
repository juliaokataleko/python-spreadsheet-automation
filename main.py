import openpyxl

inventory_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inventory_file["Sheet1"]

product_per_supplier = {}

# get products number per supplier
for product_row in range(2, product_list.max_row + 1):
    # supplier name
    supplier_position = product_list.cell(product_row, 4)
    supplier_name = supplier_position.value
    
    # check if supplier exists
    if supplier_name in product_per_supplier:
        # current_number_of_products = product_per_supplier[supplier_name]
        current_number_of_products = product_per_supplier.get(supplier_name)
        product_per_supplier[supplier_name] = current_number_of_products + 1
    else:
        # print(f"Adding a new supplier in list {supplier_name}")
        product_per_supplier[supplier_name] = 1
              
print(product_per_supplier)

# 2 - get total inevtory supplier