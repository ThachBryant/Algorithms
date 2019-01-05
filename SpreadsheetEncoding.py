def spreadsheet_encode(col_str):
	num = 0
	count = len(col_str) - 1
	for s in col_str:
		num += 26**count* (ord(s) - ord('A')+1)
	return num

print(spreadsheet_encode('A'))
print(spreadsheet_encode("AA"))
print(spreadsheet_encode('BB'))
