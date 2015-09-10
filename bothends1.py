def both_ends(s):
	if len(s) >= 2:
		return s[0] + s[1] + s[-2] + s[-1]
	else:
		return ""
		
print both_ends('spring')
print both_ends('Hello')
print both_ends('a')
print both_ends('xyz')