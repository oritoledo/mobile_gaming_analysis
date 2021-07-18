# Import libraries
import pandas as pd
import numpy as np

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

# Inspect the dataframe
print(abdata.head())

# Create a contingency table with pd.crosstab
xtab = pd.crosstab(abdata.group, abdata.is_purchase)

# Print the contingency table
print(xtab)

# Import chi2_contingency module
from scipy.stats import chi2_contingency

# Calculate the p-value
chi2, pval, dof, expected = chi2_contingency(xtab)

# define function that checks significancy of p value

def p_significancy(p):
    significance_threshold = 0.05
    if p <= significance_threshold:
        print("The difference is significant.")
    else:
        print("The difference is insignificant.")

# Print the p-value
print(pval)
p_significancy(pval)



# Calculate and print the number of visits
num_visits = len(abdata)

# Print the number of visits
print("The totoal number of visits by users: ")
print(num_visits)

# Calculate the purchase rate needed at 0.99
num_sales_needed_099 = 1000/0.99
p_sales_needed_099 = num_sales_needed_099/num_visits

# Print the purchase rate needed at 0.99
print("The purchase rate needed at $0.99")
print(p_sales_needed_099)

# Calculate the purchase rate needed at 1.99
num_sales_needed_199 = 1000/1.99
p_sales_needed_199 = num_sales_needed_199/num_visits

# Print the purchase rate needed at 1.99
print("The purchase rate needed at $1.99")
print(p_sales_needed_199)

# Calculate the purchase rate needed at 4.99
num_sales_needed_499 = 1000/4.99
p_sales_needed_499 = num_sales_needed_499/num_visits

# Print the purchase rate needed at 4.99
print("The purchase rate needed at $4.99")
print(p_sales_needed_499)

# Calculate samp size & sales for 0.99 price point
samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))

# Print samp size & sales for 0.99 price point
print("Sample size $0.99 price point:  ")
print(samp_size_099)
print("Sales: ")
print(sales_099)

# Calculate samp size & sales for 1.99 price point
samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

# Print samp size & sales for 1.99 price point
print("Sample size $1.99 price point:  ")
print(samp_size_199)
print("Sales: ")
print(sales_199)

# Calculate samp size & sales for 4.99 price point
samp_size_499 = np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))

# Print samp size & sales for 4.99 price point
print("Sample size $4.99 price point:  ")
print(samp_size_499)
print("Sales: ")
print(sales_499)

# Import the binom_test module
from scipy.stats import binom_test


# Calculate the p-value for Group A
pvalueA = binom_test(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')

# Print the p-value for Group A
print("P value group A: ")
print(pvalueA)
p_significancy(pvalueA)

# Calculate the p-value for Group B
pvalueB = binom_test(sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')

# Print the p-value for Group B
print("P value group B: ")
print(pvalueB)
p_significancy(pvalueB)

# Calculate the p-value for Group C
pvalueC = binom_test(sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')

# Print the p-value for Group C
print("P value group C: ")
print(pvalueC)
p_significancy(pvalueC)




# Print the chosen price group
if(pvalueA < pvalueB and pvalueA < pvalueC):
    print("The justified package price is $4.99.");
elif (pvalueB < pvalueA and pvalueB < pvalueC):
    print("The justified price is $1.99.")
else:
    print("The justified price is $4.99.")

