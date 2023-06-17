import calc

def test_add():
	if calc.add(6,2)==8:
		print("Test add(a,b) is OK")
	else:
		print("Test add(a,b) is Fail")

def test_sub():
	if calc.sub(13,7)==6:
		print("Test sub(a,b) is OK")
	else:
		print("Test sub(a,b) is Fail")

def test_mul():
	if calc.mul(7,8)==56:
		print("Test mul(a,b) is OK")
	else:
		print("Test mul(a,b) is Fail")

def test_div():
	if calc.div(6,2)==3:
		print("Test div(a,b) is OK")
	else:
		print("Test div(a,b) is Fail")

test_add()
test_sub()
test_mul()
test_div()