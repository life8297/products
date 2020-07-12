products = []
while True: # 未知範圍常用while True; 已知範圍用for搭配range
	name = input('請輸入商品名稱(或輸入q離開): ')
	if name == 'q':
		break
	price = input('請輸入該商品價格(元): ')
	price = int(price)
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
# products[0][0] # 大清單中的第0資料, 中的小清單第0個資料
# products[1][1] # 大清單中的第1資料, 中的小清單第1個資料

for p in products: # 利用for拆解第一層清單
	print(p[0], '的價格為:', p[1], '元')

with open('products.csv', 'w', encoding = 'utf-8') as f: # 打開檔案 # 限定編碼模式
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '元' + '\n') # 寫入檔案 # 字串的合併