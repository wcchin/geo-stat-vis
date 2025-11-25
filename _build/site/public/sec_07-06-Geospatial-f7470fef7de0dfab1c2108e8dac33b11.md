# Geospatial Ethics
------
.square[Ethics .dot[] Code and Rules of Conduct .dot[] Geospatial Privacy]

.headnote.square.bold.x-large[Geovisualisation II]

---
class: left, middle
### What is Ethics

> “Ethics, also known as moral philosophy, involves systematic intellectual reflection on morality in general ... or specific moral concerns in particular. The former can be called .red[theoretical ethics], and the latter .red[applied ethics], though the two are closely related. One realm of applied ethics that ahs garnered considerable attention outside philosophy focuses on professional conduct; thus, .red[the moral questions asked by scientists], as well as those in, for instance, the fields of law, medicine, and business, are legitimate components of ethical inquiry.”

In [Proctor, James D (1998). Ethics in geography: giving moral form tot he geographical imagination. Area 30.1, p. 9.](https://www.jstor.org/stable/20003845)

.red.bold[Ethics is not what you do, but .underline[why] you do it.]

---
class: left, middle

.split-30[.column[
### Ethics in geospatial data analysis
#### Definition
].column[
Ethics in geospatial data analysis refers to the application of moral principles and guidelines to ensure that the collection, analysis, and use of geospatial data are .red[conducted responsibly and with respect for individuals, communities, and the environment].

- [A GIS Code-of-Ethics](https://www.gisci.org/Ethics/Code-of-Ethics)
- [Rules of Conduct for Certified GIS Professionals](https://www.gisci.org/Ethics/Rules-of-Conduct)

]]

---
class: center, middle

.split-30[.column[
### Code of Ethics

The link: [Code-of-Ethics](https://www.gisci.org/Ethics/Code-of-Ethics)
].column[

<img src="resources/w12-img/code_of_ethics.png" width="95%" align="center">
]]

---
class: center, middle

.split-30[.column[
### Rules of Conduct
The link: [Rules of Conduct](https://www.gisci.org/Ethics/Rules-of-Conduct)
].column[

<img src="resources/w12-img/rules_of_conduct.png" width="95%" align="center">
]]

---
class: center, middle

### Ethics is not legality

<img src="resources/w12-img/ethical_legal.png" width="65%" align="center">

Ethics is not a front-line of defense against wrong-doing.

Ethics is more like a touchstone for professionals to identify and resolve ethical dilemmas that they encounter in their research.

---
class: left, middle

.split-30[.column[
### Geospatial Privacy
].column[

In geospatial research, particularly in people-related topics like health, crime, and disease-related studies, we often encounter privacy concerns.

Sometimes, these concerns are the reason we cannot access certain data, such as the COVID-19 distribution data in the early days of the pandemic.
- In the early days of a situation involving small case numbers, the data can be traced back to individual households or persons, potentially creating unnecessary problems for the people involved. As a result, government agencies may be unable to disclose such data.
- bias and inequality, privacy

In other cases, privacy becomes a crucial aspect to consider while writing the results, ensuring that we do not reveal any private information in our reports or manuscripts.
- Making sure the anonyminity or de-identification could not be re-identified.
]]

---
class: left, middle

.split-30[.column[
### Geospatial Privacy
Protecting geospatial information privacy involves employing various strategies to ensure that individuals' personal information remains .red[secure] and .red[anonymous].
].column[

.bold[Data anonymization]:
Remove or alter personally .red[identifiable information] from geospatial datasets. This can be achieved through techniques such as generalization, perturbation, or differential privacy.

.bold[Geo-masking]:
Geo-masking involves altering or obscuring the .red[precise location information] in geospatial data to protect individual privacy. This can be achieved by shifting, rotating, or perturbing the coordinates, or by introducing random noise to the location data. Geo-masking allows for the analysis of geospatial patterns and trends while maintaining a degree of anonymity for individuals or sensitive locations.

.bold[Data aggregation]:
.red[Combine data from multiple individuals or locations] to make it more difficult to trace information back to a specific person or place.

.bold[Privacy-preserving data mining]:
Utilize .red[data mining techniques] that protect privacy, such as k-anonymity, l-diversity, or t-closeness, to analyze geospatial data without revealing sensitive information.

]]
