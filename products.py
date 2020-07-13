import os # operating system

# 讀取檔案內容
def read_file(file_name):
	products = []
	with open(file_name, 'r', encoding = 'utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue # 跳過此次迴圈
				name, price = line.strip().split(',')
				products.append([name, price])
	print(products)
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱(或輸入q離開): ')
		if name == 'q':
			break
		price = input('請輸入該商品價格(元): ')
		price = int(price)
		products.append([name, price])
	return(products)

# 印出所有購買紀錄
def print_products(products):
	print(products)


# 寫入新內容到檔案
def write_file(file_name, products):
	with open(file_name, 'w', encoding = 'utf-8') as f: # 打開檔案 # 限定編碼模式
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') # 寫入檔案 # 字串的合併

def main():
	file_name = 'products.csv'
	# 確認檔案是否存在
	if os.path.isfile(file_name):
		print('已找到檔案, 以下為目前記錄 ,請繼續寫入內容:')
	else:
			print('檔案不存在, 已建立')
	products = read_file(file_name)
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()