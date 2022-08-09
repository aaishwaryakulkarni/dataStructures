def star_triangle(n):
	for i in range(n):
		print(" "*(n-1-i), end = "")
		print("*"*((i*2)+1))

star_triangle(5)