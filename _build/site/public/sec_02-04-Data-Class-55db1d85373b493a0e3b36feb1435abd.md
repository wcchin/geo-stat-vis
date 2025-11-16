# Data Classification

## Definition of Numerical Data Classification

Numerical Data Classification is a method of **categorizing or grouping** numerical data into different classes or bins based on specific criteria or algorithms. This approach helps simplify data analysis, visualization, and interpretation by transforming __continuous numerical values into discrete categories or intervals__.

The number of breaks:
- for visualization purpose, the common preferred number of breaks is $\leq 7$,
- common numbers of breaks in practice is: 4--5,
- follow the requirement of the analysis method or domain knowledge.

Several common classification methods include:
- Equal Interval
- Quantile Breaks
- Standard Deviation
- Natural Breaks
- Head-tail Breaks
]]


## Data Classification Approaches
### Equal Interval
This classification method involves dividing the range of the data into equal-sized intervals or classes. The class boundaries are determined by dividing the difference between the maximum and minimum values by the number of desired classes. This method is simple and easy to understand but may result in classes with significantly different numbers of observations or misrepresentation of the data distribution.


```{figure} ./resources/w02-img/data_classify-equal_interval.png
:label:
:alt:
:align: center

The breaks and the number of records in each class for Equal Interval.
```


### Quantile Breaks
Quantile classification is based on the statistical distribution of the data, dividing the data into classes with an equal number of observations. Each class represents a quantile, such as quartiles (4 classes), quintiles (5 classes), deciles (10 classes), or other user-specified quantiles. This method ensures that each class has an equal frequency of values.

```{figure} ./resources/w02-img/data_classify-quantiles.png
:label:
:alt:
:align: center

The breaks and the number of records in each class for Quantiles.
```


### Standard Deviation
Standard Deviation classification divides the data into classes based on the number of standard deviations from the mean. This method is helpful for data that __follow a normal or near-normal distribution__, as it takes into account the dispersion and variability of the data.

```{figure} ./resources/w02-img/data_classify-StdMean.png
:label:
:alt:
:align: center

The breaks and the number of records in each class for standard deviation.
```


### Natural Breaks
Natural Breaks classification is a data-driven method that seeks to minimize the within-class variance and maximize the between-class variance. It identifies break points or class boundaries by grouping similar values together while keeping dissimilar values in different classes. This method is widely used in geographic information systems (GIS) and spatial data analysis.

```{figure} ./resources/w02-img/data_classify-NaturalBreaks.png
:label:
:alt:
:align: center

The breaks and the number of records in each class for Natural Breaks.
```



### Head-tail Breaks
Head/Tail Breaks is a data classification method introduced to categorize data with heavy-tailed distributions. This method offers an alternative to traditional classification schemes by focusing on the inherent hierarchy within the data.
The Head/Tail Breaks method uses the mean or average to divide a dataset into small and large values recursively. It starts by calculating the first mean (m1) of the entire dataset and then calculates the second mean (m2) for values greater than m1. This process continues until the notion of "__far more small things than large ones__" no longer holds.

```{figure} ./resources/w02-img/data_classify-HeadTailBreaks.png
:label:
:alt:
:align: center

The breaks and the number of records in each class for Head/Tail Breaks.
```



## Summary

Choosing an optimal data classification scheme is essential for effectively summarizing and analyzing numerical data. The selection depends on **the data's characteristics, the analysis objectives, and the desired level of detail**. See a list here from [mapclassify](https://github.com/pysal/mapclassify) for many other approaches.
Experiment with different methods and assess their effectiveness in achieving your analytical goals. The optimal scheme should provide *meaningful distinctions between classes, maintain simplicity, and facilitate accurate data interpretation*.

*While Natural Breaks is the default option in many GIS software, it is not always the most suitable option for the data. Sometime, manually breaking the data is also recommended.*


1. **Equal Interval**: This simple method divides the data range into __equal-sized intervals__. It is straightforward and easy to understand but may result in classes with significantly different numbers of observations.
2. **Quantile Breaks**: This method divides data into classes with an equal number of observations based on statistical distribution. It is useful when you require a specific number of classes or __a balanced representation__ of the data.
3. **Standard Deviation**: This method classifies data based on the number of standard deviations from the mean. It is helpful when data __follows a normal or near-normal distribution__ and accounts for data dispersion and variability.
4. **Natural Breaks**: This data-driven method minimizes within-class variance and maximizes between-class variance. It is widely used in geographic information systems (GIS) and spatial data analysis. Jenks' natural breaks are suitable for datasets with uneven distributions or __when you need to emphasize the differences between groups__.
5. **Head/Tail Breaks]: Introduced by Jiang (2013), this recursive method focuses on capturing __the inherent hierarchy within heavy-tailed data__. It provides an alternative to traditional schemes and is particularly suitable for data with a heavy-tailed distribution.
