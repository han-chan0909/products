products = []
while True:
	name = input('請輸入產品名稱')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	p = [] #清單中的小清單,也可以寫成 p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p) #這個(p)可以直接改成([name, price])
print (products)

print(products[0][0])#大清單的第0格,小清單的第0格子

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.txt', 'w', encoding='utf-8') as f: #txt可以改成csv,可以用 excel打開
	f.write('商品,價格\n')
	for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


