def register_client(name,phone):
    return {
        "имя": name,
        "телефон": phone,
        "статус": "активен"
    }
print(register_client(name = "Матвей" , phone = "+7904948892"))