from menu import products

def calculate_tab(list_of_dictionaries):
    itens = []

    for item in list_of_dictionaries:
        for product in products:
            if (item["_id"] == product["_id"]):
                itens.append(product["price"] * item["amount"])
        
        subtotal = sum(itens)

    return {"subtotal": f"${round(subtotal, 2)}"}

