products = []
while True:
	name = input('請輸入商品名稱(或輸入q離開): ')
	if name == 'q':
		break
	products.append(name)
print(products)