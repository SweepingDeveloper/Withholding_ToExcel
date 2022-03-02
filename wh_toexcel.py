b_min = [0,181,609,1922,3893,7267,9179,22677]
b_max = [181,609,1922,3893,7267,9179,22677,999999]
acc_tax = [0,0,42.8,200.36,633.98,1443.74,2055.58,6779.88]
b_rate = [0,.1,.12,.22,.24,.32,.35,.37]

formula = "="
b_count = len(b_min)
cell = "H11"
greater_than = ">"
less_than = "<="

for a in range(0,b_count-1,1):
    formula += "IF(AND(" + cell + greater_than + str(b_min[a]) + ";" + cell + less_than + str(b_max[a]) + ")"
    formula += ";" + str(acc_tax[a]) + "+(" + cell + "-" + str(b_min[a]) + ")*"+str(b_rate[a])
    formula += ";"

formula += str(acc_tax[b_count-1]) + "+(" + cell + "-" + str(b_min[b_count-1]) + ")*"+str(b_rate[b_count-1])

for a in range(0,b_count-1,1):
    formula += ")"


print (formula)
