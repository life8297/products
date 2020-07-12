products = []
while True: # 未知範圍常用while True; 已知範圍用for搭配range
	name = input('請輸入商品名稱(或輸入q離開): ')
	if name == 'q':
		break
	price = input('請輸入該商品價格(元): ')
	# 二維清單
	# 原始: 
	# p = [] 
	# p.append(name)
	# p.append(price)

	# 進階: 
	# p = [name, price] 
	# products.append(p)

	# 更進階:
	products.append([name, price])	
print(products)

# 存取二維清單
products[0][0] # 大清單中的第0資料, 中的小清單第0個資料
products[1][1] # 大清單中的第1資料, 中的小清單第1個資料