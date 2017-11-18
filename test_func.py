def get_vat(price, vat_rate):
	vat = price / 100 *vat_rate
	price_no_vate = price - vat
	print(price_no_vate)

#price1 = 100
#vat_rate1 = 18
#get_vat(price1, vat_rate1)

def get_sum(one, two, delimeter=' '):
	return (str(one) + str(delimeter) + str(two)).upper()


