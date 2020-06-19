'''
A python Test for indepencence. Separate all inputs with spaces.
'''

import numpy as np
import pandas as pd
import scipy.stats as sst

[r, c] = list(map(int, input("Row by column: \n").split(" ")))
data = np.zeros([r, c])
for j in range(r):
    note = "Enter row " + str(j+1) + ":\n"
    new_row_string = input(note).split(" ")
    while len(new_row_string) != c:
        note = "Length doesn't match. Enter row " + str(j+1) + ":\n"
        new_row_string = input(note).split(" ")
    new_row = list(map(float, new_row_string))
    data[j, :] = np.array(new_row)
data_tabular = pd.DataFrame(data)
C_sum = np.array(data_tabular.sum(axis=1))
R_sum = np.array(data_tabular.sum(axis=0))
T_sum = data.sum()
data_tabular["C_sum"] = C_sum
RT_sum = np.array(data_tabular.sum(axis=0))
data_tabular = data_tabular.append(pd.DataFrame(
    data_tabular.sum(axis=0), columns=["R_sum"]).transpose())
print("\n\n", "Data summed:\n", data_tabular, "\n\n")
expected_data = np.outer(C_sum, R_sum)/T_sum
expected_data_tabular = pd.DataFrame(expected_data)
print("Data expected:\n", expected_data_tabular, "\n\n")
alpha = float(input("Alpha: \n"))
Chisq_statistics = ((data - expected_data) *
                    (data - expected_data) / expected_data).sum()
print("χ²(r-1="+str(r-1)+",c-1="+str(c-1)+") =", Chisq_statistics)
sst.chi2.pdf(alpha, (r-1)*(c-1))
print("χ²-value at significance "+str(alpha) +
      ":", sst.chi2.ppf(1 - alpha, (r-1)*(c-1)))
p = 1 - sst.chi2.cdf(Chisq_statistics, (r-1)*(c-1))
print("P-value is:", p)
options = {0: "reject", 1: "accept"}
print("Therefore we choose to", options[int(
    p > alpha)], "H0 at significance level", str(alpha)+".")
