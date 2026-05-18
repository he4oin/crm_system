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


    