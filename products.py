# 讀取檔案內容
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
 	for line in f:
  		if '商品,價格' in line:
  			continue # 繼續、跳過此次迴圈
  		name, price = line.strip().split(',')
  		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱(或輸入q離開): ')
	if name == 'q':
		break
	price = input('請輸入該商品價格(元): ')
	price = int(price)
	products.append([name, price])	

# 印出所有購買紀錄
print(products)

# 寫入新內容到檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: # 打開檔案 # 限定編碼模式
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # 寫入檔案 # 字串的合併