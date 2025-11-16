## GE5230 - week 5 - lab session

date: 2025-02-17

lecturer: Benny

**submission: 2025-02-23 23.59**



### Data

Use data files for point locations: hdb_data_2013.csv.xz and hdb_data_2023.csv.xz

for the study area boundary: master-plan-2019-planningarea.shp



### Tasks 

(total 10.5 marks)

1. Generate square grids with each cell length & width=250m for the tasks below (preparation).
2. For both year (2013 & 2023), split the data into 3 data-sets, draw a KDE map for each of them, using Epanechnikov (parabolic) kernel & bandwidth$=750$m; arrange them so that we can compare the maps side-by-side (between the 2 years and between the three types of flats) (0.5 for each sub-map, 3 marks in total):
   1. 3 rooms and below
   2. 4 rooms
   3. 5 rooms and above
3. For each flat types group, draw a dual-KDE plots (magnitude of difference) between the two years and observe the changes within the 10 years. Please use the settings/parameters (kernel function, bandwidth) that you think is appropriate to generate the maps and provide explanation on your observations. (3 marks)
4. Use one year data (2013 or 2023), compare the differences between flat types (3 groups) using dual-KDE (3 pairs) and provide your observations/explanations ($\leq150$ words). (4.5 marks)

