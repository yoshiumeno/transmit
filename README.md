# transmit
python codes and data to check validity of Kayano-Nishiura's transmission model for COVID-19

## pyton code
1) hersys_curve_gen.py
2) hersys_curve_gen_fdh.py
3) hersys_curve_gen_fsh.py

are python codes to create "dummy" HER-SYS data files to drive the R-code provided by Kayano-Nishiura.

hersys_data.csv, hersys_data_fdh.csv and hersys_data_fsh.csv are the data files created by the above codes.
The first column shows the date number starting on 2021/02/17 until 2022/05/31 (1 -> 2021/02/17, 2 -> 2021/02/18, 3 -> 2021/02/19, ...).
The 2nd-11th colums show infection numbers of respective age brackets.

From these data files, "File2.Hersys_infection.csv" (necessary to run the R-code) can be created as follows:
1. The first line should read: Infection	a0009	a1019	a2029	a3039	a4049	a5059	a6069	a7079	a8089	a90	cases
(i.e. 12 columns)
2. The data must start at least two weeks earlier than 2021/02/17. Thus, the first column of the second line should read, for example, 2021/2/2.
3. For the period between 2021/2/2 and2021/2/16, put '80' in the 2nd-11th columns.
4. For 2021/2/17 to 2021/11/30, paste the data of hersys_data*.csv to the 2nd-11th columns.
5. The last (12th) column is the sum of 2th-11th columns.

See the example "File2.Hersys_infection.csv" created based on "hersys_data.csv".

## Kayano-Nishiura's R-code
https://zenodo.org/records/15244462 (created on April 19, 2025)
Dataset and code for "Evaluating the COVID-19 vaccination program in Japan, 2021 using the counterfactual reproduction number" in Scientific Reports 2023 Oct 18;13(1):17762. doi: 10.1038/s41598-023-44942-6.
<img width="3280" height="126" alt="image" src="https://github.com/user-attachments/assets/0881ab21-84cb-4d38-92f8-eb05f36950c0" />
