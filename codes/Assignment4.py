#Given
pr_X0 = 50/100
pr_X1 = 30/100
pr_X2 = 20/100
pr_Y1_X0 = 1/100
pr_Y1_X1 = 5/100
pr_Y1_X2 = 7/100

# finding the probability that the defective item is produced by A.

pr_X0_Y1 = (pr_X0)*(pr_Y1_X0)/((pr_X0)*(pr_Y1_X0)+(pr_X1)*(pr_Y1_X1)+(pr_X2)*(pr_Y1_X2)) #formula

print(pr_X0_Y1)