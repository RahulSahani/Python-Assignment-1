import random

mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 103.25
}

# Exchange Price Function
def ExchangePrice(exchange_rate , usdPrice):
    return  usdPrice * exchange_rate



# Paragraph Function
def Paragraph(mobile_name , price , manufacturing_country , Final):
    
    para1 = [
    
    f'{mobile_name} is a {manufacturing_country} product.',
    f'Made in {manufacturing_country} is the {mobile_name}. ',
    f'The {mobile_name} was produced in {manufacturing_country}. ',
    f'{manufacturing_country} is the country of manufacture for the {mobile_name}. ',
    f'{mobile_name} is made in {manufacturing_country}'

    ]

    para2 = [
    f'The cost is  ${price}, which is about equivalent to {Final} BDT.',
    f'The cost is  ${price} USD, or around {Final} BDT. ',
    f'The cost is ${price} USD, or roughly {Final} BDT. ',
    f'The rate is ${price} USD which is nearly same to {Final} BDT',
    f'The price is ${price} USD which is almost equal to {Final} BDT'

    ]

    s1 = random.choice(para1)
    s2 = random.choice(para2)
    
    return s1 + s2

Exchange_rate = mobile_data.get('exchange_rate')

#  Your Code Starts from here

for data in mobile_data["data"]:
     name = data["name"]
     price = float(data["price"].replace('USD' , ''))
     manufacturer = data["made"]
     final = ExchangePrice( Exchange_rate , price)
     para = Paragraph(name , price , manufacturer , final)
     print(para)