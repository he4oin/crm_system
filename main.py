def register_client(name,phone):
    return {
        "имя": name,
        "телефон": phone,
        "статус": "активен"
    }

print(register_client(name = "Матвей" , phone = "+7904948892"))

def create_order(item, price, loyalty_card=False):
    if loyalty_card:
        final_price = price * 0.9
        print(f"Заказ {item} оформлен со скидкой. К оплате {final_price}")
    else:
        print(f"Заказ {item} оформлен. К оплате {price}")

create_order(item="Ноутбук", price=30000, loyalty_card=True)


TAX_RATE = 0.20
print(f"TAX_RATE до вызова функции: {TAX_RATE}")

def calculate_tax(price):
    global TAX_RATE
    TAX_RATE = 0.15
    final_tax = price * TAX_RATE
    return final_tax

result = calculate_tax(250)
print(f"Ваш расчет: {result}")
print(f"TAX_RATE после вызова функции: {TAX_RATE}")