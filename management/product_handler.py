from menu import products

def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    
    for product in products:
        if id == product["_id"]:
            return product
        
    return {}


def get_products_by_type(product_type):
    if type(product_type) != str:
        raise TypeError("product type must be a str")
    
    product_list = []
    for product in products:
        if product_type == product["type"]:
            product_list.append(product)
    
    return product_list


def add_product(menu, **args):
    ids = []

    for product in menu:
        ids.append(product["_id"])
    ids.sort()

    if(menu == []):
        ids = 1
    args["_id"] = ids = 1 if menu == [] else ids[-1] + 1

    menu.append(args)

    return args


def menu_report():
    product_count = len(products)
    average_price = 0
    most_common_type = None

    itens = []
    sum = 0

    for product in products:
        itens.append(product["type"])
        sum += product["price"]
        average_price = sum / product_count
    
    count_type = []

    for _type in set(itens):
        count = itens.count(_type)
        count_type.append({_type: count})
    
    number = 0

    for _type in count_type:
        for key, value in _type.items():
            if value > number:
                number = value
            if number == value:
                most_common_type = key

    return f"Products Count: {product_count} - Average Price: ${round(average_price, 2)} - Most Common Type: {most_common_type}"

