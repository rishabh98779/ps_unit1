# Probability & Statistics — Raw Extracted Source Text

_Extracted from the original 208-page PDF (`ilovepdf_merged__7_.pdf`) using `pdftotext -layout`. 209 pages. Note: some mathematical symbols (subscripts, Greek letters, special notation) may not extract cleanly due to the PDF's font encoding — refer to the original PDF for exact formula rendering._

---


## Page 1

```
                                        Lecture 1.5
CO1: To understand fundamental concepts of probability theory and statistics.

                                     Measures of Dispersion

Mean Deviation

Mean Deviation of a set of observations is the arithmetic mean of absolute deviations from

mean or any other specified value.

Given the observations 𝑥! , 𝑥" , 𝑥# , … , 𝑥$ , in order to find ‘Mean Deviation about A’, we first

obtain the deviations (𝑥! − 𝐴), (𝑥" − 𝐴), (𝑥# − 𝐴), … , (𝑥$ − 𝐴). Some of these deviations

may be positive and some negative.

If we write |𝑥% − 𝐴| to denote the positive value of (𝑥% − 𝐴), whatever be the actual sign, the

sum of these ‘absolute deviations’ is

                 |𝑥! − 𝐴| + |𝑥" − 𝐴| + |𝑥# − 𝐴| + … + |𝑥$ − 𝐴| = ∑|𝑥% − 𝐴|


And A.M. of the absolute deviations is

                             !
Mean Deviation about A = $ = ∑|𝑥% − 𝐴|


Mean Deviation is usually calculated arithmetic mean (𝑥̅ ) and hence ‘Mean Deviation’ only

refers to M. D. about mean.

                            !
For simple series, 𝑀. 𝐷. = $ ∑|𝑥% − 𝑥̅ |

                                      !
For frequency distribution, 𝑀. 𝐷. = $ ∑𝑓% |𝑥% − 𝑥̅ |


Solved Examples
```

## Page 2

```
Example 1


•    Calculate the mean deviation of the following values about the median: 8, 15, 53, 49, 19,

     62, 7, 15, 95, 77.

         Solution: Since there are an even number of observations, i.e. 10, the median is the

         average of the two middlemost observations, when arranged in order of magnitude: 7,

         8, 15, 15, (19, 49), 53, 62, 77, 95.

         Median = (19+49)/2 = 34

                               x                                     |𝑥 − 𝑚𝑒𝑑𝑖𝑎𝑛|
                               8                                               26
                              15                                               19
                              53                                               19
                              49                                               15
                              19                                               15
                              62                                               28
                               7                                               27
                              15                                               19
                              95                                               61
                              77                                               43
                             Total                                            272


                                          !                    !
         Mean Deviation about mean = $ ∑|𝑥% − 𝑚𝑒𝑑𝑖𝑎𝑛| = !& ∗ 272 = 𝟐𝟕. 𝟐


Example 2

•    Find the mean deviation of the following series:

       X             10              11         12           13                14        Total
    frequency        3               12         18           12                 3         48
Solution:

           𝑥                 𝑓                  𝑓𝑥                |𝑥 − 𝑥̅ |         𝑓|𝑥 − 𝑥̅ |
           10                 3                  30                  2                  6
           11                12                 132                  1                 12
           12                18                 216                  0                  0
           13                12                 156                  1                 12
```

## Page 3

```
        14                  3                  42                 2                   6
       Total               48                 576                 --                 36



                                           ∑𝑓𝑥 576
                                    𝑥̅ =      =    = 12
                                            𝑁   48
Mean Deviation = 36/48 = 0.75



Standard Deviation

It is defined as the positive square-root of the arithmetic mean of the Square of the deviations

of the given observation from their arithmetic mean.

The standard deviation is denoted by s in case of sample and Greek letter σ (sigma) in case of

population.

The formula for calculating standard deviation is as follows


      !
𝑠 = D$ ∑(𝑥% − 𝑥̅ )"     for raw data


And for grouped data the formulas are


      !
𝑠 = D$ ∑𝑓% (𝑥% − 𝑥̅ )" for frequency distribution


Example 3


•   The standard deviation calculated from a set of 32 observations is 5. If the sum of the

    observations is 80, what is the sum of the squares of these observations?

Solution: We are given n = 32, 𝜎 = 5, ∑𝑥 = 80. It is required to find the value of ∑𝑥 " .

                                               ∑( !    ∑( "
                                   Now 𝜎 " =    $
                                                  −G$H
```

## Page 4

```
                                         ∑𝑥 "   80 "
                                    25 =      −J K
                                         32     32

                                       ∑𝑥 " = 1000.

Example 4


•   The frequency distributions of seed yield of 50 seasamum plants are given below. Find the

    standard deviation.




Example 5
```

## Page 5

```
•     The Frequency distributions of seed yield of 50 seasamum plants are given below. Find the

      standard deviation.

    Seed yield in gms (x)     2.5-35     3.5-4.5      4.5-5.5         5.5-6.5        6.5-7.5
      No. of plants (f)          4          6            5              15             10



    Seed yield in gms (x) No. of plants (f)      Mid x               𝑥−𝐴        df      d2 f
                                                                𝑑=
                                                                      𝐶
    2.5-3.5                 4                    3        -2                    -8      16
    3.5-4.5                 6                    4        -1                    -6      6
    4.5-5.5                 15                   5        0                     0       0
    5.5-6.5                 15                   6        1                     15      15
    6.5-7.5                 10                   7        2                     20      40
    Total                   50                   25       0                     21      77


A=assumed mean=5
N=50, C=1

                                                 ∑𝑓𝑑 "    ∑𝑓𝑑 "
                                    𝑠 =𝐶×N             −J    K
                                                  𝑁        𝑁

                                                   77   21 "
                                       𝑠 =1×N         −J K
                                                   50   50

                                        𝑠 = √1.54 − 0.1764

                                       𝑠 = √1.3636 = 1.1677

Merits and Demerits of Standard Deviation

Merits

1. It is rigidly defined and its value is always definite and based on all the observations and

      the actual signs of deviations are used.

2. As it is based on arithmetic mean, it has all the merits of arithmetic mean.

3. It is the most important and widely used measure of dispersion.
```

## Page 6

```
4. It is possible for further algebraic treatment.

5. It is less affected by the fluctuations of sampling and hence stable.

6. It is the basis for measuring the coefficient of correlation and sampling.

Demerits

1. It is not easy to understand and it is difficult to calculate.

2. It gives more weight to extreme values because the values are squared up.

3. As it is an absolute measure of variability, it cannot be used for the purpose of comparison.




Variance

The square of the standard deviation is called variance

(i.e.) variance = (SD)2.

Coefficient of Variation

The Standard deviation is an absolute measure of dispersion. It is expressed in terms of units

in which the original figures are collected and stated. The standard deviation of heights of plants

cannot be compared with the standard deviation of weights of the grains, as both are expressed

in different units, i.e heights in centimetre and weights in kilograms. Therefore the standard

deviation must be converted into a relative measure of dispersion for the purpose of

comparison. The relative measure is known as the coefficient of variation.

The coefficient of variation is obtained by dividing the standard deviation by the mean and

expressed in percentage. Symbolically,
```

## Page 7

```
                                   ).+.
Coefficient of variation (C.V) = ,-.$ × 100


If we want to compare the variability of two or more series, we can use C.V. The series or

groups of data for which the C.V. is greater indicate that the group is more variable, less stable,

less uniform, less consistent or less homogeneous. If the C.V. is less, it indicates that the group

is less variable or more stable or more uniform or more consistent or more homogeneous.

Example 6


•   Consider the measurement on yield and plant height of a paddy variety. The mean and

    standard deviation for yield are 50 kg and 10 kg respectively. The mean and standard

    deviation for plant height are 55 am and 5 cm respectively.

Here the measurements for yield and plant height are in different units. Hence the variabilities

can be compared only by using coefficient of variation.

                !&
For yield, CV=/& × 100= 20%

                        /
For plant height, CV= // × 100== 9.1%


The yield is subject to more variation than the plant height.




        TEXT BOOKS

    •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

        edition.2014.

    •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

        ed.2013, New Delhi.
```

## Page 8

```
   •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

       Publications, Reprint 2008.




       REFERENCE BOOKS

   •   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

       Narosa Publishing House ,2004,New Delhi.

   •   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New

       Delhi.

   •   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281In

       siders’Guide



       Video Lecture :

h#ps://www.youtube.com/watch?v=wuQSeGYQ0ms&list=PL86hgHi3F9FoYVwLPFjVd0fvhPMLIcp0m
```

## Page 9

```
                                  Lecture 1.4
CO1: To understand fundamental concepts of probability theory and statistics.

  Measures of Dispersion – Range, Quartile Deviation and their
                           numerical



Measures of Dispersion: The averages are representatives of a frequency

distribution. But they fail to give a complete picture of the distribution. They do

not tell anything about the scatterness of observations within the distribution.

Suppose that we have the distribution of the yields (kg per plot) of two paddy

varieties from 5 plots each. The distribution may be as follows




It can be seen that the mean yield for both varieties is 42 kg but cannot say that

the performances of the two varieties are same. There is greater uniformity of

yields in the first variety whereas there is more variability in the yields of the

second variety. The first variety may be preferred since it is more consistent in

yield performance.

  Form the above example it is obvious that a measure of central tendency alone

is not sufficient to describe a frequency distribution. In addition to it we should

have a measure of scatterness of observations. The scatterness or variation of
```

## Page 10

```
observations from their average are called the dispersion. There are different

measures of dispersion like the range, the quartile deviation, the mean deviation

and the standard deviation.

Characteristics of a good measure of dispersion

An ideal measure of dispersion is expected to possess the following properties

   1. It should be rigidly defined

   2. It should be based on all the items.

   3. It should not be unduly affected by extreme items.

   4. It should lend itself for algebraic manipulation.

   5. It should be simple to understand and easy to calculate



Range

This is the simplest possible measure of dispersion and is defined as the

difference between the largest and smallest values of the variable.

   • In symbols, Range = L – S.

   • Where L = Largest value.

   • S = Smallest value.

In individual observations and discrete series, L and S are easily identified.

In continuous series, the following two methods are followed.
```

## Page 11

```
Method 1

L = Upper boundary of the highest class

S = Lower boundary of the lowest class.

Method 2

L = Mid value of the highest class.

S = Mid value of the lowest class




Merits and Demerits of Range
```

## Page 12

```
Merits

   1. It is simple to understand.

   2. It is easy to calculate.

   3. In certain types of problems like quality control, weather forecasts, share

      price analysis, etc.,

      range is most widely used.

Demerits

   1. It is very much affected by the extreme items.

   2. It is based on only two extreme observations.

   3. It cannot be calculated from open-end class intervals.

   4. It is not suitable for mathematical treatment.

   5. It is a very rarely used measure.



Practice Questions

   1. The weight of 11 forty-year-old med were 148, 154, 158, 160, 161, 162,

      166, 170, 180, 195 and 236 pounds. If the heaviest man is omitted, what is

      the percentage change in the range?



      Quartile Deviation: An absolute measure of dispersion based on quartiles is called

      quartile deviation. It is also known as semi-inter quartile range.
```

## Page 13

```
Inter quartile range is the difference between the upper and lower quartile.

Inter quartile range = Q3 – Q1

Semi inter quartile range = (Q3 – Q1)/2



For an individual series,

                   !"# %&
Q1 = value of ! $ "         item

                      !"#    %&
Q3 = value of #3 ! $ "%           item

Where n is the number of items.



For a discrete frequency distribution,

                   '"# %&
Q1 = value of ! $ "         item

For a continuous frequency distribution,
            !
              ()
Q1 = 𝐿 + ( * ) 𝐶 item
            "




Where L = lower limit of the Q1 – class

m =.Cumulative frequency preceding the Q1 – class

f = frequency of the Q1 – class.

And
             #!
                  ()$
Q3 = 𝐿# + ( " *         ) 𝐶 item
                  $



Where 𝐿# = lower limit of the Q3 – class

m1 =.Cumulative frequency preceding the Q3 – class

f1 = frequency of the Q3 – class.
```

## Page 14

```
       C = length of the class interval.

Quest. Find the upper and lower quartiles of the following data. Also find the quartile

deviation. 36, 43, 47, 28, 18, 9, 32.




Q3 = 43

       Q.D. = (Q3 – Q1)/2 = (43-18)/2 = 12.5




Ques. Find the quartile deviation of the data: 5, 7, 8, 12, 15, 18, 21, 24, 30

Solution
```

## Page 15

```
Step 1: Arrange Data

Data is already arranged.

Number of observations: n = 9




Answer: Quartile Deviation = 7.5
```

## Page 16

```
Advantages of Quartile Deviation

   •   Simple to calculate
   •   Not affected by extreme values
   •   Useful for skewed distributions
   •   Suitable for open-end distributions

Limitations

   •   Ignores 50% of observations
   •   Less accurate than standard deviation
   •   Not suitable for algebraic treatment

Applications

   •   Income distribution analysis
   •   Business statistics
   •   Educational performance analysis
   •   Economic studies

Practice Questions

   1. Find quartile deviation for: 2, 4, 6, 8, 10, 12, 14, 16, 18
   2. Calculate coefficient of quartile deviation for: Q1= 20, Q3 = 50.
   3. Find quartile deviation of: 5, 9, 12, 15, 18, 22, 25, 28.




       TEXT BOOKS

   •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

       edition.2014.
```

## Page 17

```
  •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

      ed.2013, New Delhi.

  •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

      Publications, Reprint 2008.

      REFERENCE BOOKS

  •   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

      Narosa Publishing House ,2004,New Delhi.

  •   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006,

      New Delhi.

  •   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281I

      nsiders’Guide




      Video Lecture :

https://www.youtube.com/watch?v=wuQSeGYQ0ms&list=PL86hgHi3F9FoYVwLPFjVd0fv
hPMLIcp0m
```

## Page 18

```
                                     Lecture 1.3

       CO1: To understand fundamental concepts of probability theory and statistics.

  Combined Mean and Weighted Mean and its Numerical Problems



Combined Mean: When two or more groups have different means and different numbers

of observations, the mean of the combined group is called the Combined Mean. It is also

known as Composite Mean.


Formula for Combined Mean:

For two groups:

                                                """! + 𝑛" 𝑋
                                             𝑛! 𝑋         """"
                                      𝑋" =
                                                𝑛! + 𝑛"

Where:

   •     𝑋" = Combined mean
   •     𝒏𝟏 , 𝒏𝟐 = Number of observations in groups 1 and 2
   •     """
         𝑋! , """
              𝑋" = Means of groups 1 and 2



Steps to find Combined Mean:

  •    Multiply each mean by its group size
  •    Add all products
  •    Add total observations
  •    Divide total product by total observations
```

## Page 19

```
Numerical Problems:

   1. The average marks of 40 students in Section A is 65 and the average marks of 35
      students in Section B is 70. Find the combined mean.




      Combined Mean: 67.33

   2. The average salary of 25 male employees is ₹40,000 and the average salary of 15
      female employees is ₹35,000. Find the combined average salary.




        Combined Mean: 38125Rs.
Practice Questions:
```

## Page 20

```
1. An average daily wages of 10 workers in a factory ‘A’ is Rs. 30 and an average daily
   wages of 20 workers in a factory ‘B’ is Rs. 15. Find the average daily wages of all
   workers of both the factories.
2. An average daily wages of all the 90 workers in a factory is Rs. 60. An average daily
   wages of females workers is Rs. 45. Calculate an average daily wages of male workers if
   one-third workers are male.
```

## Page 21

```
Weighted Mean: When different observations are assigned different levels of
importance (weights), the average obtained is called the Weighted Mean.




    Steps to Find Weighted Mean
   1.   Multiply each value by its weight
   2.   Add all weighted values
   3.   Add all weights
   4.   Divide total weighted value by total weight

Ques. A consumer buys a commodity @ Rs. 4.80, Rs 6, Rs 8, Rs 12 and Rs 24 per unit in
each of five successive years. Calculate the average cost per unit if he buys (a) 1000 units
each year (b) 1000 units, 800 units, 600 units, 400 units and 200 units in each of five
successive years.
Solution
```

## Page 22

```
Suppose a student has secured the following marks in three tests:
```

## Page 24

```
                                      Lecture 1.2
       CO1: To understand fundamental concepts of probability theory and statistics.


                              Measures of central tendency

Questions such as: “how many calories do I eat per day?” or “how much time do I spend talking

per day?” can be hard to answer because the answer will vary from day to day. It’s sometimes

more sensible to ask “how many calories do I consume on a typical day?” or “on average, how

much time do I spend talking per day?”.

 In this section we will study three ways of measuring central tendency in data, the mean,

the median and the mode. Each measure gives us a single value? that might be considered

typical. Each measure has its own strengths and weaknesses.

Usually when two or more different data sets are to be compared it is necessary to condense

the data, but for comparison the condensation of data set into a frequency distribution and visual

presentation are not enough. It is then necessary to summarize the data set in a single value.

Such a value usually somewhere in the center and represent the entire data set and hence it is

called measure of central tendency or averages. Since a measure of central tendency (i.e. an

average) indicates the location or the general position of the distribution on the X-axis therefore

it is also known as a measure of location or position.

   A population of books, cars, people, polar bears, all games played by Babe Ruth throughout

his career etc.... is the entire collection of those objects. For any given variable under

consideration, each member of the population has a particular value of the variable associated

to them, for example the number of home runs scored by Babe Ruth for each game played by

him during his career. These values are called data and we can apply our measures of central
```

## Page 25

```
tendency to the entire population, to get a single value (maybe more than one for the mode)

measuring central tendency for the entire population; or we can apply our measures to a subset

or sample of the population, to get an estimate of the central tendency for the population.

   A sample is a subset of the population, for example, we might collect data on the number

of home runs hit by Miguel Cabrera in a random sample of 20 games. If we calculate the mean,

median and mode using the data from a sample, the results are called the sample mean, sample

median and sample mode.

   Sometimes we can look at the entire population, not just a subset. For example, since Babe

Ruth has now retired, so we might collect data on the number of home runs he hit in his career.

If we calculate the mean, median and mode using the data collected from the entire population,

the results are called the population mean, population median and population mode.

Types of Measure of Central Tendency
   •   Arithmetic Mean
   •   Geometric Mean
   •   Harmonic Mean
   •   Mode
   •   Median


Arithmetic Mean or Simply Mean: “A value obtained by dividing the sum of all the
observations by the number of observations is called arithmetic Mean”
                                          !"# %& '(( %)*+,-./0%1
                                 Mean = 2"#)+, %& %)*+,-./0%1
```

## Page 26

```
    Numerical Example:

v Calculate the arithmetic mean for the following the marks obtained

   by 9 students are given below:


    Using formula of arithmetic mean for ungrouped data:                      xi
                                                                                  45
                                                ∑1034 𝑥0                          32
                                         𝑥̅ =                                     37
                                                    𝑛                             46
                                                                                  39
                               n=9                                                36
                                                                                  41
                                 567                                              48
                             𝑥̅ = 8 = 40 𝑚𝑎𝑟𝑘𝑠
                                                                                  36
                                                                          n

    Ø Numerical Example:                                               å x = 360
                                                                       i=1
                                                                              i




    ² Calculate the arithmetic mean for the following data given below:


    u Using formula of direct method of arithmetic mean for grouped data:

                                        ∑"   &:
                                    𝑥̅ = ∑!#$ ! !
                                           " & ,        𝑛 = ∑1034 𝑓0
                                          !#$ !


    The weight recorded to the nearest grams of 60 apples picked out at
```

## Page 27

```
random from a consignment are given below:

106      107       76    82 109          107    115        93 187        95 123        125

111      92        86    70 126          68     130       129   139     119    115     128

100      186       84    99 113          204    111       141   136     123     90     115

98       110       78   185    162       178    140       152   173     146    158     194

148      90       107   181    131       75     184       104   110      80 118        82


                              Weight (grams)     Frequency
                                 65----84             09
                                 85----104                10
                                105----124                17
                                125----144                10
                                145----164                05
                                165----184                04
                                185----204                05
Solution:

 Weight grams)          Midpoints (xi)         Frequency (fi)                  fi xi

       65----84          (65+84)/2 = 74.5                 09          9 * 74.5=670.5
      85----104                 94.5                      10          945.0

      105----124               114.5                      17          1946.5

      125----144               134.5                      10          1345.0

      145----164               154.5                      05          772.5

      165----184               174.5                      04          698.0

      185----204               194.5                      05          972.5
                                                      1                 1

                                                   / 𝑓0 = 60           / 𝑓0 𝑥0 = 7350.0
                                                   034                 034
```

## Page 28

```
                                      ∑1034 𝑓0 𝑥0         7350.0
                               𝑥̅ =                   =          = 122.5 𝑔𝑟𝑎𝑚𝑠
                                       ∑1034 𝑓0             60


    u Using formula of short cut method of arithmetic mean for grouped data:

                    ∑"   &;
          𝑥̅ = 𝐴 + ∑!#$
                     " &
                        ! !
                            ,         𝑛 = ∑1034 𝑓0
                      !#$ !


  Where 𝐷0 = 𝑋0 - 𝐴 and A is the provisional or assumed mean.


 Weight (grams)       Midpoint (𝑥0 )         Frequency (𝑓0 )      𝐷0 = 𝑋0 − 𝐴, A=114.5         𝑓0 𝐷0

      65-84           (65+84)/2=74.5                  09                   -40                 -360

     85-104                   95.5                    10                   -20                 -200

    105-124                   114.5                   17                    0                   0

    125-144                   134.5                   10                   20                  200

    145-164                   154.5                   5                    40                  200

    165-184                   174.5                   4                    60                  240

    185-204                   194.5                   5                    80                  400

                                                / 𝑓0 = 60                                / 𝑓0 𝐷0 = 480
                                                034                                      034




           ∑1034 𝑓0 𝐷0           480
𝑥̅ = 𝐴 +      1        = 114.5 +     = 122.5 𝑔𝑟𝑎𝑚𝑠
            ∑034 𝑓0               60



v Using formula of step deviation method of arithmetic mean for grouped data:

                                                              ∑1034 𝑓0 𝑢0
                                                𝑥̅         =𝐴+ 1          ×ℎ
                                                               ∑034 𝑓0

    : <'
𝑢0 = !=       Where h is the width of the class interval:
```

## Page 29

```
 Weight        Midpoints (xi) Frequency                : <'                  fiui
                                               𝑢0 = != , A = 114.5,
 (grams)                            (fi)
                                                         h=20
 65----84       (65+84)/ 2 =         09                       -2             -18
                    74.5
85----104            94.5            10                       -1             -10
105----124          114.5            17                       0               0
125----144          134.5            10                       1              10
145----164          154.5            05                       2              10
165----184          174.5            04                       3              12
185----204          194.5            05                       4              20
                                     1                                  1

                                    / 𝑓0                               / 𝑓0 𝑢0 = 24
                                    034                                034

                                    = 60


                        ∑1034 𝑓0 𝑢0               24
             𝑥̅ = 𝐴 +      1        × ℎ = 114.5 +    × 20 = 114.5 + 08 = 122.5 𝑔𝑟𝑎𝑚𝑠
                         ∑034 𝑓0                  60


  Properties of Arithmetic Mean:

  The following are the properties of arithmetic mean:


     •      The mean of a constant is that constant.

     •      The sum of deviations from mean is equal to zero. i.e. ∑(𝑥0 − 𝑥̅ ) = 0.

     •      The sum of squared deviations from the mean is smaller than the sum of squared

            deviations from any arbitrary value or provisional mean. i.e. ∑(𝑥0 − 𝑥̅ ) < ∑(𝑥0 − 𝐴)>

     •      The arithmetic mean is affected by the change of origin and scale i.e. when a constant

            is added to or subtracted from each value pf a variable or if each value of a variable is

            multiplied or divided by a constant, then arithmetic mean is affected by these changes.
```

## Page 30

```
Advantages & Disadvantages of Arithmetic Mean

 Advantages

 1. A.M. is readily understood, and hence needs no explanation, when used.

 2. The computation of A.M. is easy and does not involve any laborious numerical

      calculations. Even if all observations are not known individually, A.M. can be found,

      provided their sum and the number of observations is known.

 3. It can be calculated without arranging the data in order of magnitude (as required for

      median), or in the form of a frequency distribution (as required for mode).

 4.   A.M. can be treated algebraically. Given the A.M. and the number of observations in each

      of several groups, A.M. of the composite group can be easily determined by using an

      algebraic formula.

 5. It is a very stable and reliable average as regards sampling fluctuations. If many samples

      are drawn from the same population and each time several measures of central tendency

      calculated, it will be found that A.M. fluctuates less from sample to sample than any other

      measures.

 Disadvantages

 1. A.M. cannot be obtained by inspection, as in the case of median or mode.

 2. It cannot be calculated unless the exact magnitude of all observations and their number is

      known accurately. If some of the extreme values are missing, the accuracy of A.M. is

      greatly affected. A.M. cannot therefore be calculated from a grouped frequency distribution

      with open-end classes, unless some assumptions are made regarding the sizes of these

      classes.

 3. The greatest disadvantage of A.M. is that it is highly affected by the presence of even a few
```

## Page 31

```
   extremely large or small observations.

4. A.M. may not be an actual value of the variable. (For example, A.M. of the number of

   children per family may come to 2.54. However, although there may be 2 children or 3

   children in a family, 2.54 children is meaningless.)




                                           Median

“When the observation are arranged in ascending or descending order, then a value, that divides

a distribution into equal parts, is called median”




    •    Numerical example of median for both grouped and ungrouped data:
```

## Page 32

```
•   In an office there are 5 employees: a supervisor and 4 workers. The workers draw a

    salary of 5000Rs, 6500Rs, 7500Rs and 8000Rs per month while the supervisor gets

    20000Rs per month.

In this case mean (salary) =
?777@ 6?77 @ A?77 @ B777 @ >7777
                 ?
                                   Rs = 47000Rs = 9400Rs

Note that 4 out of 5 employees have their salaries much less than 9400Rs. The mean salary

     9400Rs does not given even an approximate estimate of any one of their salaries.

This is a weakness of the mean. It is affected by the extreme values of the observations in

     the data.

This weakness of mean drives us to look for another average which is unaffected by a few

     extreme values. Median is one such a measure of central tendency.

Median is a measure of central tendency which gives the value of the middlemost

     observation in the data when the data is arranged in ascending (or descending)

     order.



Median of Raw Data

Median of raw data is calculated as follows:

(i) Arrange the (numerical) data in an ascending (or descending) order

                                                                                   1@4
(ii) When the number of observations (n) is odd, the median is the value of E > F 𝑡ℎ

     observation.

(iii) When the number of observations (n) is even, the median is the mean of the

      1              1@4
     E > F 𝑡ℎ 𝑎𝑛𝑑 E > F 𝑡ℎ observations.

Let us illustrate this with the help of some examples.
```

## Page 33

```
   Example 1:




   Example 2:




Median of Ungrouped Data:
```

## Page 34

```
We illustrate calculation of the median of ungrouped data through examples. Example 3: Find

the median of the following data, which gives the marks, out of 15, obtained by 35 students in

a mathematics test.




From the table above, we see that 18th observation is 7
So, Median = 7


Example 4: Find the median of the following data:
```

## Page 35

```
Practice Questions
1. Following are the goals scored by a team in a series of 11 matches
          1, 0, 3, 2, 4, 5, 2, 4, 4, 2, 5
Determine the median score.
```

## Page 36

```
    2. In a diagnostic test in mathematics given to 12 students, the following marks (out of 100)
        are recorded 46, 52, 48, 39, 41, 62, 55, 53, 96, 39, 45, 99
    Calculate the median for this data.




Advantages & Disadvantages of Arithmetic Meadian

    Advantages

    1. Median is not difficult to understand, although it is not so popular as the arithmetic mean.

    2. It is easy to calculate. Even when all the observations are not known, median can be

        calculated, provided the general location of all observations and values near the middle are

        available. Median can also be calculated without difficulty from grouped frequency

        distributions with classes of unequal width or with open-end classes.

    3. Median is applicable to qualitative data in psychological and social studies, where

        numerical measurements may not be available, but it is possible to rank the objects in some

        order.

    Disadvantages
```

## Page 37

```
1. For the calculation of median, the data must be arranged.

2. Unlike A.M. Or G.M. it cannot be treated algebraically. Given the medians of several

   groups of observations, median of the composite group cannot be determined.

3. If is desired to give greater importance to large or small values, median is unsuitable.

4. The calculation oof median from a grouped frequency distribution is based on simple

   interpolation, which assumes that the observations in the median class are uniformly

   distributed. But in reality, this may not be true.

5. Median is affected more by sampling fluctuations than the arithmetic mean, and is

   therefore, less reliable.




                                            Mode

Look at the following example: A company produces readymade shirts of different sizes. The

company kept record of its sale for one week which is given below:




From the table, we see that the sales of shirts of size 105 cm is maximum. So, the company

will go ahead producing this size in the largest number. Here, 105 is nothing but the mode of

the data. Mode is also one of the measures of central tendency.

The observation that occurs most frequently in the data is called mode of the data.
```

## Page 38

```
In other words, the observation with maximum frequency is called mode of the data. The

readymade garments and shoe industries etc, make use of this measure of central tendency.

Based on mode of the demand data, these industries decide which size of the product should

be produced in large numbers to meet the market demand.

Mode of Raw Data

In case of raw data, it is easy to pick up mode by just looking at the data. Let us consider the

following example:

Example 1: The number of goals scored by a football team in 12 matches are:

1, 2 Example 1:, 2, 3, 1, 2, 2, 4, 5, 3, 3, 4. What is the modal score?

Solution: Just by looking at the data, we find the frequency of 2 is 4 and is more than the

frequency of all other scores. So, mode of the data is 2, or modal score is 2.

Example 2: Find the mode of the data: 9, 6, 8, 9, 10, 7, 12, 15, 22, 15

Solution: Arranging the data in increasing order, we have

                                 6, 7, 8, 9, 9, 10, 12, 15, 15, 22

We find that the both the observations 9 and 15 have the same maximum frequency 2. So, both

are the modes of the data.

Remarks:

1. In this lesson, we will take up the data having a single mode only.

2. In the data, if each observation has the same frequency, then we say that the data does not

have a mode.
```

## Page 39

```
Mode of Ungrouped Data

Let us illustrate finding of the mode of ungrouped data through an example

Example 1: Find the mode of the following data:




Solution: From the table, we see that the weight 45 kg has maximum frequency 22 which means

that maximum number of students have their weight 45 kg. So, the mode is 45 kg or the modal

weight is 45 kg.

Practice Questions:

   1. Find the mode of the data: 5, 10, 3, 7, 2, 9, 6, 2, 11, 2

   2. The number of TV sets in each of 15 households are found as given below: 2, 2, 4, 2,

       1, 1, 1, 2, 1, 1, 3, 3, 1, 3, 0 What is the mode of this data?
```

## Page 40

```
Advantages & Disadvantages of Mode

Advantages

1. From a simple frequency distribution, mode can be obtained only by inspection. Also, for

   a simple series with a small number of observations, mode can often be determined without

   any calculation.

2. It is unaffected by the presence of extreme values.

3. Unlike A. M., it can be calculated from frequency distributions, with open-end classes. In

   fact, if the modal class and its two adjoining classes together with their class frequencies

   are available, mode can be determined, provided it is known that all classes are of equal

   width.

Disadvantages
```

## Page 41

```
1. Mode has no significance unless a large number of observations is available.

2. It is a peculiar measure of central tendency. For any given set of observations, is always

   possible to find the values of A.M., G.M. H.M. or median. But it mode may not exist. When

   all values occur with equal frequency, there is no mode. On the other hand if two or more

   values have the same maximum frequency, there is more than one mode (A distribution is

   called unimodal, bimodal or multimodal, when it has one, two or more than two modes).

3. From a grouped frequency distribution, it is difficult to locate the mode accurately. An

   approximate value of mode is obtained by the formula only when all classes are of equal

   width, and the class with the largest frequency is preceded and followed by two other

   classes. Even then, if class frequencies do not show any gradual tendency to maximum

   concentration in a class, or the largest frequency occurs in two or more classes, the formula

   is inapplicable.

4. For the calculation of mode, the data must be arranged in the form of a frequency

   distribution.

5. Mode cannot be treated algebraically.




    Video Lecture :

    1. https://www.youtube.com/watch?v=zC6e47l0tV4


    2. https://www.youtube.com/watch?v=7cwftEm0DeI&list=PL86hgHi3F9FpPKUuhzw7

        0fKCx1GjWjfxg

    3. https://www.youtube.com/watch?v=2N7na6aBvpk
```

## Page 42

```
Introduction to Statistics and Engineering Applications




                PROBABILITY & STATISTICS | Basic Statistics and Probability



       Course: PROBABILITY & STATISTICS | Chapter: Basic Statistics and Probability | Program: Bachelor of Engineering




                                                                                                              DISCOVER · LEARN · EMPOWER
```

## Page 43

```
                                                                    Course Outcomes                                                                            SLIDE 2 / 14




Course Outcome
CO          BT LEVEL                     DESCRIPTION




     CO1               BT3               To understand fundamental concepts of probability theory and statistics




     CO2               BT4               Identify and formulation of engineering problems in different situations involving probabilistic and statistical measures




     CO3               BT5               Classify various types of statistical methods and perform statistical inference




     CO4               BT4               Apply appropriate statistical tools, distributions including correlation and regression analysis techniques




     CO5               BT5               Implement the standard concepts and tools at an intermediate to advanced level that will help in tackling various problems in
                                         hypothesis testing




                 Chandigarh University                                                                                                                               2 / 14
```

## Page 44

```
                                                           Learning Objectives     SLIDE 3 / 14




Learning Outcomes

 1   Describe the role of statistics in engineering data analysis.




 2   Classify different measures of central tendency and dispersion.




 3   Summarize the significance of skewness and kurtosis in distribution shapes.




                       Chandigarh University                                            3 / 14
```

## Page 45

```
                                                                 Lecture                                                                    SLIDE 4 / 14




Definition of Statistics in Engineering

 1   Statistics is the science of collecting, analyzing, and interpreting
     numerical data.


 2   It transforms raw engineering measurements into actionable
     insights for decision-making.


 3   Descriptive statistics summarize data sets like material strength or
     temperature readings.


 4   Inferential statistics allow prediction of future performance based
     on sample data.


 5   Engineering applications include quality control, reliability analysis,
                                                                               Funnel Process PowerPoint Template and Google Slides- SlideKit
     and process optimization.


                       Chandigarh University                                                                                                     4 / 14
```

## Page 46

```
                                                              Lecture                                                                        SLIDE 5 / 14




Measures of Central Tendency

 1   Mean is the arithmetic average representing the center of a data
     set.


 2   Median is the middle value separating the higher half from the
     lower half.


 3   Mode is the most frequently occurring value in a given data
     distribution.


 4   Mean is sensitive to outliers, while median is robust against
     extreme values.


 5   Engineers choose the mean for symmetric data and median for
                                                                        Statistics For Data Science - GeeksforGeeks (source: media.geeksforgeeks.org)
     skewed data.


                       Chandigarh University                                                                                                      5 / 14
```

## Page 47

```
                                                              Lecture                                                                            SLIDE 6 / 14




Measures of Dispersion

 1   Range is the difference between the maximum and minimum
     observed values.


 2   Variance measures the average squared deviation from the mean of
     the data.


 3   Standard deviation is the square root of variance indicating data
     spread.


 4   Coefficient of variation expresses dispersion as a percentage of the
     mean value.


 5   Low dispersion indicates high precision in manufacturing processes
                                                                            Introduction to Statistics - GeeksforGeeks (source: media.geeksforgeeks.org)
     and measurements.


                        Chandigarh University                                                                                                         6 / 14
```

## Page 48

```
                                                                            Worked Example                                                                       SLIDE 7 / 14




Mean and Variance
                                      GOVERNING EQUATION


  Mean (μ) = (400 + 410 + 405 + 395 + 415) / 5 = 405
                       N/mm²

 DATA SET                                            DEVIATIONS FROM MEAN

 Tensile strength of 5 steel samples                 -5, +5, 0, -10, +10.
 (N/mm²): 400, 410, 405, 395, 415.




 • Sum of squared deviations = 25 +
 25 + 0 + 100 + 100 = 250.
 • Variance (σ²) = 250 / 5 = 50
 (N/mm²)²; Std Dev (σ) = √50 ≈ 7.07.
                                                                                             Probability and Statistics - GeeksforGeeks (source: media.geeksforgeeks.org)




                             Chandigarh University                                                                                                                     7 / 14
```

## Page 49

```
                                                                   Lecture                                                                        SLIDE 8 / 14




Common Pitfalls in Central Tendency

 1   Using mean for highly skewed data leads to misleading average
     values.


 2   Ignoring outliers can hide critical failures in safety-critical
     engineering systems.


 3   Confusing sample mean with population mean causes incorrect
     statistical inferences.


 4   Calculating mean of categorical data like 'High', 'Medium', 'Low' is
     invalid.


 5   Always check data distribution shape before selecting the
                                                                             Statistics For Data Science - GeeksforGeeks (source: media.geeksforgeeks.org)
     appropriate measure.


                        Chandigarh University                                                                                                          8 / 14
```

## Page 50

```
                                                                   Lecture   SLIDE 9 / 14




Significance of Skewness

 1   Skewness measures the asymmetry of a probability distribution
     around its mean.


 2   Positive skew indicates a long tail on the right side of the
     distribution.


 3   Negative skew indicates a long tail on the left side of the
     distribution.


 4   Zero skewness implies a perfectly symmetric distribution like the
     normal curve.


 5   In engineering, skewness reveals bias in manufacturing processes
     or measurement errors.


                        Chandigarh University                                     9 / 14
```

## Page 51

```
                                                                 Lecture                                     SLIDE 10 / 14




Significance of Kurtosis

 1   Kurtosis measures the 'tailedness' or peakedness of a probability
     distribution.


 2   High kurtosis indicates heavy tails and a sharp peak in the data.



 3   Low kurtosis indicates light tails and a flatter peak in the data.



 4   Leptokurtic distributions have more outliers than a normal
     distribution.


 5   Platykurtic distributions have fewer outliers and are flatter than
                                                                           Source: media.geeksforgeeks.org
     normal.


                       Chandigarh University                                                                      10 / 14
```

## Page 52

```
                                                       Engineering Application                        SLIDE 11 / 14




Quality Control

 1   Statistical Process Control uses mean and range to monitor
     production stability.


 2   Control charts detect shifts in process mean or increases in
     dispersion.


 3   Six σ methodology relies on standard deviation to reduce defect
     rates.


 4   Skewness analysis identifies tool wear or material inconsistencies in
     production.


 5   Kurtosis analysis helps predict the frequency of extreme quality
                                                                                 Source: numiqo.com
     failures.


                       Chandigarh University                                                               11 / 14
```

## Page 53

```
                                                                           Worked Example                             SLIDE 12 / 14




Skewness Interpretation
                                      GOVERNING EQUATION


  Mean = 1000 hours, Median = 950 hours, Mode = 900
                        hours

 SCENARIO
                                                    • Since Mean > Median > Mode, the
 Time to failure for 100 electronic                 distribution is positively skewed.
 components (in hours).                             • This indicates most components fail
                                                    early, but a few last much longer.
                                                    • Engineers must design for the early
                                                    failures to ensure system reliability.




                                                                                             Source: datavizkit.com




                            Chandigarh University                                                                          12 / 14
```

## Page 54

```
                                                                Lecture                     SLIDE 13 / 14




Key Takeaways

 1   Statistics transforms raw data into actionable engineering insights and decisions.



 2   Central tendency and dispersion measures define the center and spread of data.



 3   Skewness reveals asymmetry, while kurtosis reveals the tailedness of distributions.



 4   Choosing the right measure depends on the data distribution shape and outliers.



 5   These concepts are vital for quality control, reliability, and process optimization.



                       Chandigarh University                                                     13 / 14
```

## Page 55

```
                                                              Lecture     SLIDE 14 / 14




References
 1   Higher Engineering Mathematics — H. K Dass.



 2   Higher Engineering Mathematics — B. S. Grewal



 3   Advanced Engineering Mathematics — R.K. Jain, and S.R.K. Iyengar



 4   Advanced Engineering Mathematics — B.V. Ramana



 5   Statistical methods — S. P. Gupta



 6   A textbook of Engineering Mathematics — N.P. Bali and Manish Goyal



                       Chandigarh University                                   14 / 14
```

## Page 56

```
                                      Lecture 1.1
       CO1: To understand fundamental concepts of probability theory and statistics.


                             Introduction of Basic Statistics

                                     What is Probability?
u Definition:
Probability theory is the study of the mathematical rules that govern random events.
u But what is randomness?
Informally, a random event is an event in which we do not know the outcome without observing
it. Probability tells us what we can say about such events, given our assumptions about the
possible outcomes.
                                      What are Statistics?
u Definition
Statistics is the application of probability to the collection, analysis, and description of random
data.
u Statistics is used to:
  v Design experiments
  v Summarize data
  v Make conclusions about the world
  v Explore complex data

u Applications of Probability and Statistics
  v Computer Science:
  v Machine Learning
  v Data Mining
  v Artificial Intelligence
  v Simulation
  v Image Processing
  v Computer Graphics
  v Visualization
  v Software Testing
  v Algorithms

u Electrical Engineering
  v Signal Processing
  v Telecommunications
  v Information Theory
  v Control Theory
  v Instrumentation, Sensors
  v Hardware/Electronics Testing
```

## Page 57

```
u General
 v Gambling (not recommended)
 v Stock Market Analysis
 v Politics
 v Sports
 v Demographics
 v Medicine
 v Economics
 v All Sciences!!


  u Alan Turing: Connecting CS and Probability
  v “Father of Computer Science”
  v Most famous for:
       • Computability, Turing machine
       • Stored-program computer
       • Turing test
       • WWII cryptanalysis
  v Wrote a dissertation on probability theory!
  v Turing used probability and statistics to crack Enigma




      TEXT BOOKS

  •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

      edition.2014.

  •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

      ed.2013, New Delhi.

  •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

      Publications, Reprint 2008.
```

## Page 58

```
       REFERENCE BOOKS

   •   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

       Narosa Publishing House ,2004,New Delhi.

   •   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New

       Delhi.

   •   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281In

       siders’Guide




Video lecture: https://www.youtube.com/watch?v=MXaJ7sa7q-8
```

## Page 59

```
Topic 1.1.1 - Combined Mean & Weighted Mean and their numerical Problems

Completion requirements

Chandigarh University Theory

Combined Mean & Weighted Mean and their numerical Problems

PROBABILITY & STATISTICS — Basic Statistics Measures of Central Tendency and
Dispersion, Moments, skewness, and Kurtosis

Lecture 1.1.1 to 1.1.3

Duration: 2 hrs

   Learning Outcomes

 LO#     Outcomes



 LO1     Calculate the range and quartile deviation for given data sets.


 LO2     Compute the standard deviation and variance from frequency distributions.


 LO3     Interpret the significance of dispersion measures in statistical analysis.

   Course Outcome Mapping

 CO         Statement                                                                 BT
                                                                                      Level


 CO1        To understand fundamental concepts of probability theory and statistics   BT3

   Lecture Content

● Topic 1: Combined Mean & Weighted Mean and their numerical Problems

1. Introduction to Combined Mean and Weighted Mean Concepts


    Source: www.wikihow.com


    Source: indiafreenotes.com


    Source: www.statisticalaid.com
```

## Page 60

```
       Source: unacademy.com


       Source: media.licdn.com

In the context of Basic Statistics and Probability, understanding how to aggregate data
from different sources is fundamental for engineering analysis. The Combined Mean
allows us to find the average of a dataset that is formed by merging two or more smaller
datasets. Similarly, the Weighted Mean is a specific type of average where each value in
the dataset contributes to the final average in proportion to its assigned weight. These
concepts are crucial when dealing with engineering datasets that are often collected in
stages or from different sub-populations. For instance, calculating the overall average
height of students in a university requires combining the averages of individual
departments, weighted by the number of students in each department. This lecture
focuses on the mathematical formulation and practical application of these means
within probability distributions.

   •     The Combined Mean is calculated by summing the total sum of observations
         from all groups and dividing by the total number of observations across all
         groups.

   •     The formula for Combined Mean is barx_combined = fracsum f_i barx_isum f_i,
         where is the frequency (weight) and is the mean of the -th group.

   •     The Weighted Mean assigns specific importance (weights) to data points,
         reflecting their relative significance in the overall distribution.

   •     In probability, weights often correspond to probabilities , making the weighted
         mean equivalent to the expected value .

   •     Understanding these concepts is essential for LO1, as it helps in analyzing the
         central tendency of skewed engineering data by accurately representing the
         dataset's core.

Summary: This section establishes the theoretical foundation for calculating averages
in composite datasets. We have defined the Combined Mean as the ratio of the total
sum of all observations to the total frequency. We also introduced the Weighted Mean,
highlighting its role in probability theory where weights represent probabilities. These
tools are vital for accurately summarizing data that comes from heterogeneous
sources, a common scenario in engineering statistics.

2. Mathematical Formulation and Numerical Derivation


       Source: s3.ap-southeast-2.amazonaws.com
```

## Page 61

```
To solve numerical problems involving Combined Mean and Weighted Mean, one must
rigorously apply the algebraic formulas derived from the definition of the arithmetic
mean. Consider a dataset divided into groups. Let be the number of observations in
the -th group, and be the mean of that group. The combined mean is given by the
equation barx = fracsum_i=1^k n_i barx_isum_i=1^k n_i. This formula essentially treats
the frequency as the weight . In the context of probability distributions, if is a discrete
random variable taking values with probabilities , the expected value is the weighted
mean where . The relationship is expressed as . This distinction is critical for interpreting
skewness and kurtosis later in the course.

   •     The derivation shows that the combined mean is a linear combination of
         individual means, scaled by their respective frequencies.

   •     If the weights sum to 1, the weighted mean simplifies to the standard expected
         value in probability theory.

   •     Numerical examples often involve finding a missing mean or frequency when the
         combined mean is known, requiring rearrangement of the formula.

   •     The formula barx_new = fracn_1barx_1 + n_2barx_2n_1 + n_2 is a specific case
         used frequently in exam problems.

   •     These calculations directly support LO2 by providing the numerical basis for
         understanding distribution shapes and moments.

Summary: This section provides the step-by-step mathematical framework for solving
problems related to combined and weighted means. We emphasized the importance of
balancing the numerator (sum of weighted means) and the denominator (sum of
weights). By mastering these derivations, students can confidently tackle numerical
problems where data is aggregated from multiple sources, a skill directly applicable to
analyzing complex engineering systems.


       Source: d138zd1ktt9iqe.cloudfront.net

3. Solving Numerical Problems with Engineering Context

Engineering problems often require calculating the average performance of a system
based on data from different operational phases. For example, if a machine operates in
two modes with different failure rates, the combined mean failure rate is a weighted
average based on the time spent in each mode. Let us consider a problem where the
mean of 10 observations is 20 and the mean of 15 observations is 25. To find the
combined mean of 25 observations, we use the formula: . This result indicates that the
overall average lies between the two individual means, closer to the mean of the larger
group. Such calculations are essential for quality control and reliability engineering,
```

## Page 62

```
where LO3 is addressed by classifying the resulting distribution based on the
aggregated data characteristics.

   •     Always verify that the sum of weights equals the total count before finalizing the
         combined mean.

   •     In probability problems, ensure that the sum of probabilities before calculating
         the expected value.

   •     When solving for a missing variable, isolate the term algebraically to avoid
         calculation errors.

   •     Real-world examples include calculating the average cost of production across
         different factories with varying output volumes.

   •     These exercises reinforce the understanding of how data aggregation affects the
         central tendency, linking back to skewness analysis.

Summary: This section bridges theory and practice by solving concrete numerical
problems. We demonstrated how to handle scenarios with missing data or unknown
frequencies. The examples provided illustrate the physical significance of the combined
mean in engineering contexts, such as reliability analysis and cost estimation. By
working through these problems, students gain the proficiency needed to interpret
statistical summaries of complex datasets, which is a prerequisite for analyzing
skewness and kurtosis.


       Source: www.modernanalyst.com


       Source: res.cloudinary.com

4. Connecting Means to Skewness and Kurtosis Analysis

The calculation of combined and weighted means is not an isolated exercise but a
foundational step towards understanding the shape of probability distributions. Once
the mean is established, we can compare it with the median and mode to determine
skewness. If the combined mean is significantly different from the median, it suggests
asymmetry in the data. Furthermore, the weighted mean is the first moment about the
origin, which is the starting point for calculating higher moments like variance and
kurtosis. In the context of Basic Statistics, accurately computing the mean ensures that
subsequent measures of dispersion and shape are valid. For instance, a heavy-tailed
distribution might have a mean that is heavily influenced by extreme values, which the
weighted mean helps to quantify if weights are assigned appropriately.

   •     The mean serves as the pivot point for calculating the second moment (variance)
         and fourth moment (kurtosis).
```

## Page 63

```
   •     A positive skewness in a combined dataset often implies that the weighted mean
         is pulled towards the tail of high values.

   •     Understanding the mean is critical for LO3, as it allows engineers to classify
         distributions as leptokurtic or platykurtic based on moment calculations.

   •     Errors in calculating the combined mean can lead to incorrect interpretations of
         the distribution's symmetry.

   •     This section integrates the concept of the mean with the broader unit of
         Moments, skewness, and Kurtosis.

Summary: In this final section, we connected the calculation of means to the analysis
of distribution shapes. We explained how the mean acts as a reference for determining
skewness and how it contributes to the calculation of kurtosis. By mastering the
combined and weighted means, students are better equipped to analyze the full profile
of a probability distribution. This holistic approach ensures that the statistical measures
used in engineering design and analysis are both accurate and meaningful.


       Source: www.acte.in


       Source: blog.analytics-toolkit.com

▶ Concept Video

Lecture 04: Numerical Measures and Metrics of Forecasting
IIT KANPUR-NPTEL 28:44

● Topic 2: Measures of Dispersion – Range, Quartile Deviation and their numerical
Problems

5. Introduction to Measures of Dispersion

In the study of Basic Statistics and Probability, understanding how data points are
spread out is just as important as knowing the central tendency. Measures of dispersion
quantify this spread, providing insight into the variability within a dataset. While
measures like the mean tell us the average value, dispersion measures tell us how
much the individual observations deviate from that average. For engineering students,
this is crucial for quality control and reliability analysis. In this section, we focus on two
fundamental measures: the Range and the Quartile Deviation. These are often the first
steps in analyzing data before moving to more complex metrics like standard deviation.
The range offers a quick snapshot of the total spread, while the quartile deviation
provides a more robust measure that is less affected by extreme values.

   •     Dispersion measures describe the variability or scatter of data points around the
         central value.
```

## Page 64

```
   •   The Range is the simplest measure, calculated as the difference between the
       maximum and minimum values.

   •   Quartile Deviation (QD) is based on the interquartile range and is resistant to
       outliers.

   •   Both measures are essential for assessing the consistency of engineering
       processes.

   •   Understanding these concepts is a prerequisite for calculating variance and
       standard deviation later in the course.

Summary: This section introduced the concept of dispersion as a vital component of
statistical analysis alongside central tendency. We defined the range as the simplest
measure of spread and the quartile deviation as a more stable measure based on
quartiles. Recognizing the limitations of the range, such as its sensitivity to outliers,
highlights the need for quartile deviation. These foundational concepts prepare
students for advanced calculations involving frequency distributions and variance,
ensuring a comprehensive understanding of data variability in engineering contexts.

6. Calculation of Range and Quartile Deviation

To effectively analyze data in Basic Statistics and Probability, one must master the
calculation of dispersion measures. The Range is defined mathematically as the
difference between the largest and smallest observations in a dataset. It provides an
immediate sense of the data's span. However, because it relies solely on two data
points, it can be misleading if the dataset contains extreme outliers. In contrast, the
Quartile Deviation is derived from the first quartile () and the third quartile (). It is
calculated as half the difference between these two quartiles. This measure focuses on
the middle 50% of the data, making it a preferred choice when data distribution is
skewed or contains anomalies. Calculating these requires organizing data in ascending
order and identifying specific positions.

   •   The formula for Range is .

   •   Quartile Deviation is calculated using the formula .

   •   To find and , data must be sorted and the position determined using and .

   •   Range is easy to compute but lacks precision regarding the distribution of
       intermediate values.

   •   Quartile Deviation is less sensitive to extreme values, offering a more stable
       measure of spread.

Summary: This section detailed the mathematical procedures for calculating range and
quartile deviation. We established that the range is the difference between the
```

## Page 65

```
maximum and minimum values, while quartile deviation is half the interquartile range.
The formulas and were presented. Emphasis was placed on the necessity of sorting
data to accurately locate quartiles. Students learned that while range is simple, quartile
deviation offers robustness against outliers, a critical distinction for statistical analysis
in engineering.

7. Numerical Problems and Interpretation

Applying theoretical concepts to numerical problems is essential for mastering Basic
Statistics and Probability. Consider a dataset of component lifespans: 100, 120, 130,
140, 150, 160, 180, 200 hours. The range is calculated as hours. To find the quartile
deviation, we first determine and . For , is at position and is at . Interpolating between
values, we find and . The quartile deviation is then hours. Interpreting these results, the
range suggests a wide spread, but the quartile deviation indicates that the central 50%
of components have a much tighter lifespan distribution. This interpretation is vital for
reliability engineering.

   •   Numerical examples demonstrate the step-by-step calculation of range and
       quartile deviation.

   •   Interpolation is often required to find quartiles in datasets where is not a
       multiple of 4.

   •   Comparing range and quartile deviation reveals the impact of outliers on data
       spread.

   •   A small quartile deviation with a large range suggests the presence of extreme
       values.

   •   Students must practice converting raw data into ordered lists to solve these
       problems efficiently.

Summary: This section focused on solving numerical problems involving range and
quartile deviation. Through a concrete example of component lifespans, we
demonstrated how to calculate the range and interpolate quartiles to find the quartile
deviation. The interpretation highlighted that a large range combined with a small
quartile deviation indicates outliers. This analysis reinforces the importance of
choosing the appropriate dispersion measure based on data characteristics. Mastery of
these numerical techniques is a key learning outcome for the course, enabling students
to handle real-world statistical data confidently.

8. Significance in Statistical Analysis

Understanding the significance of dispersion measures is a critical learning outcome for
this course. In Basic Statistics and Probability, dispersion provides context to central
tendency. A mean of 100 hours is meaningless without knowing the spread. If the range
```

## Page 66

```
is 10 hours, the process is highly consistent. If the range is 1000 hours, the process is
highly variable. Range and quartile deviation serve as initial diagnostic tools. They help
engineers decide whether to use the mean or median as the best measure of central
tendency. If the range is disproportionately large compared to the quartile deviation, the
data is likely skewed, suggesting the median is a better representative. These measures
also form the basis for calculating the coefficient of variation, allowing comparison of
variability across different datasets with different units or scales.

   •   Dispersion measures provide context to central tendency, preventing
       misinterpretation of averages.

   •   A large range relative to quartile deviation indicates skewness or outliers.

   •   These measures guide the selection of the appropriate central tendency metric
       (mean vs. median).

   •   They are foundational for calculating advanced metrics like variance and
       standard deviation.

   •   In quality control, these measures help identify process instability early in the
       analysis.

Summary: This section explored the broader significance of range and quartile
deviation in statistical analysis. We discussed how dispersion contextualizes central
tendency, ensuring that averages are interpreted correctly. The relationship between
range and quartile deviation was used to detect skewness and outliers. These measures
are not just preliminary steps but are essential for selecting the right statistical
descriptors and for calculating advanced metrics like variance. For engineering
students, this understanding is vital for quality control and process improvement,
ensuring that statistical tools are applied with the correct insight into data behavior.

▶ Concept Video

Lecture # 1.7 Measures of Dispersion( Range, Quartile Deviation, Mean deviation,
variance ,SD, CV )
Knowledge Philosophy 19:09

   Real-Life Applications

   1. Quality Control: Calculating the average defect rate in a manufacturing plant by
      combining data from different production lines, weighted by the number of units
      produced on each line.

   2. Financial Engineering: Determining the weighted average cost of capital (WACC)
      for a company, where the weights are the market values of different debt and
      equity instruments.
```

## Page 67

```
   3. Civil Engineering: Estimating the average load-bearing capacity of concrete
      samples from different batches, weighted by the volume of concrete poured in
      each batch.

   4. Data Science: Computing the expected value of a random variable in a Monte
      Carlo simulation, where the weights represent the probability of specific
      outcomes.

   5. Quality Control: In manufacturing, calculating the range of part dimensions
      helps engineers quickly identify if a machine is drifting out of tolerance limits.

   6. Financial Risk Assessment: Quartile deviation is used in finance to measure the
      volatility of stock prices, focusing on the middle 50% of returns to ignore extreme
      market crashes.

   7. Environmental Monitoring: Analyzing the range of daily temperature readings
      helps climatologists understand the severity of weather anomalies in a specific
      region.

   8. Healthcare Data Analysis: Hospitals use quartile deviation to analyze patient
      recovery ×, ensuring that the central group of patients is treated consistently
      without being skewed by extreme cases.

   References & Suggestive Readings

Textbooks

   •   Higher Engineering Mathematics by H. K Dass. (3rd revised edition ed. S. Chand
       Publishers 2014)

   •   Higher Engineering Mathematics by B. S. Grewal (42th ed. ed. Khanna Publishers
       2013)

   •   Advanced Engineering Mathematics by R.K. Jain, and S.R.K. Iyengar (3rd Edition
       ed. Narosa Publishing House 2004)

Reference Books

   •   Advanced Engineering Mathematics by B.V. Ramana — ed. McGraw Hill 2006

   •   Statistical methods by S. P. Gupta — ed. S Chand & Sons 2017

   •   A textbook of Engineering Mathematics by N.P. Bali and Manish Goyal — Ninth
       edition ed. Laxmi Publications 2010

   Summary — Key Takeaways

   •   The Combined Mean aggregates data from multiple groups by summing total
       observations and dividing by total frequency.
```

## Page 68

```
•   The Weighted Mean assigns specific importance to data points, which is
    mathematically equivalent to the Expected Value in probability.

•   Accurate calculation of the mean is a prerequisite for analyzing skewness and
    kurtosis in engineering datasets.

•   These concepts are essential for interpreting the shape and central tendency of
    probability distributions in Basic Statistics.

•   Range and Quartile Deviation are fundamental measures of dispersion in Basic
    Statistics and Probability.

•   Range is simple but sensitive to outliers, while Quartile Deviation is robust and
    focuses on the central data.

•   Numerical problems require careful sorting of data and interpolation to find
    accurate quartile values.

•   Interpreting these measures helps in selecting the appropriate central tendency
    and identifying data skewness.

Check Your Understanding

1. Define Combined Mean and explain its significance in aggregating data from
   different engineering batches. LO1

2. Explain how the weighted mean relates to the expected value of a discrete
   random variable in probability theory. LO2

3. Identify the main components required to calculate the combined mean when
   given individual group means and frequencies. LO3

4. Analyze the relationship between the combined mean and the individual group
   means in a skewed distribution. LO4

5. Define Range and explain its significance in identifying outliers. LO1

6. Explain the working principle of Quartile Deviation and why it is preferred in
   skewed distributions. LO1

7. Identify the main components required to calculate Quartile Deviation from a
   frequency distribution. LO2

8. Analyze the relationship between Range and Quartile Deviation in a dataset with
   extreme values. LO3
```

## Page 69

```
                                      Lecture 2.1
CO1: To understand fundamental concepts of probability theory and statistics.


                                     MOMENTS

6.1 INTRODUCTION

Moments are popularly used to describe the characteristic of a distribution. They

represent a convenient and unifying method for summarizing many of the most

commonly used statistical measures such as measures of tendency, variation,

skewness and kurtosis. Moments are statistical measures that give certain

characteristics of the distribution. Moments can be raw moments, central

moments and moments about any arbitrary point.

For example, the first raw moment gives mean and the second central moment

gives variance. Although direct formulae exist for central moments even then they

can be easily calculated with the help of raw moments. The rth central moment of

the variable x is hr times the rth central moment of u where u = (x – A)/h is a new

variable obtained by subjecting x to a change of origin and scale. Since A does

not come into the scene so there is no effect of change of origin on moments.




6.2 INTRODUCTION TO MOMENTS
```

## Page 70

```
Moment word is very popular in mechanical sciences. In science moment is a

measure of energy which generates the frequency. In Statistics, moments are the

arithmetic means of first, second, third and so on, i.e. rth power of the deviation

taken from either mean or an arbitrary point of a distribution. In other words,

moments are statistical measures that give certain characteristics of the

distribution. In statistics, some moments are very important. Generally, in any

frequency distribution, four moments are obtained which are known as first,

second, third and fourth moments. These four moments describe the information

about mean, variance, skewness and kurtosis of a frequency distribution.

Calculation of moments gives some features of a distribution which are of

statistical importance. Moments can be classified in raw and central moment.

Raw moments are measured about any arbitrary point A (say). If A is taken to be

zero then raw moments are called moments about origin. When A is taken to be

Arithmetic mean we get central moments. The first raw moment about origin is

mean whereas the first central moment is zero. The second raw and central

moments are mean square deviation and variance, respectively. The third and

fourth moments are useful in measuring skewness and kurtosis.




6.3 METHODS OF CALCULATION OF MOMENTS
```

## Page 71

```
Three types of moments are:

1. Moments about arbitrary point,

2. Moments about mean, and

3. Moments about origin

6.3.1 Moments about Arbitrary Point

When actual mean is in fraction, moments are first calculated about an arbitrary

point and then converted to moments about the actual mean. When deviations are

taken from arbitrary point, the formulas are:

For Ungrouped Data

If 𝑥! , 𝑥" , . . . , 𝑥# are the n observations of a variable X, then their moments about

an arbitrary point A are

                                             ∑#
                                              !$%('! ())
                                                        "
Zero order moment A,                  𝜇$ =         #
                                                             =1

                                             ∑#
                                              !$%('! ())
                                                         %
First order moment A,                 𝜇! =
                                                  #


                                              ∑#
                                               !$%('! ())
                                                         &
Second order moment A,                𝜇" =
                                                   #


                                              ∑#
                                               !$%('! ())
                                                         '
Third order moment A,                  𝜇+ =         #


                                                ∑#
                                                 !$%('! ())
                                                           (
Fourth order moment A,                  𝜇, =
                                                       #
```

## Page 72

```
In general, the rth order moment about arbitrary point A is given by,

                   ∑#
                    !$%('! ())
                               )
            𝜇- =                   ; 𝑓𝑜𝑟 𝑟 = 1,2, − − −
                        #


For Grouped Data

If 𝑥! , 𝑥" , . . . , 𝑥# are the n observations of a variable X, with their corresponding

frequencies 𝑓! , 𝑓" , . . . , 𝑓# then their moments about an arbitrary point A are

                                                   ∑*
                                                    !$% .('! ())
                                                                "
Zero order moment A,                       𝜇′$ =                     = 1; 𝑤ℎ𝑒𝑟𝑒 𝑁 = ∑/01! 𝑓
                                                          #


                                                   ∑*
                                                    !$% .('! ())
                                                                 %
First order moment A,                     𝜇′! =          #


                                                   ∑*
                                                    !$% .('! ())
                                                                &
Second order moment A,                     𝜇′" =          #


                                                    ∑*
                                                     !$% .('! ())
                                                                  '
Third order moment A,                      𝜇′+ =           #


                                                     ∑*
                                                      !$% .('! ())
                                                                   (
Fourth order moment A,                      𝜇′, =
                                                              #


In general, the rth order moment about arbitrary point A is given by

                       ∑*
                        !$% .('! ())
                                    )
,              𝜇′- =                    ; 𝑓𝑜𝑟 𝑟 = 1,2, − − −
                             #




In a frequency distribution, to simplify calculation we can use short-cut method.
```

## Page 73

```
        '! ()
𝑑0 =      2
                    𝑜𝑟 (𝑥0 − 𝐴) = ℎ𝑑0 , then we get the moments about an arbitrary point

A are

                                                   ∑*
                                                    !$% .('! ())
                                                                "
Zero order moment A,                       𝜇′$ =             #
                                                                        = 1; 𝑤ℎ𝑒𝑟𝑒 𝑁 = ∑/01! 𝑓


                                                   ∑*       %
                                                    !$% .! 3!
First order moment A,                      𝜇′! =                 ×ℎ
                                                         #


                                                    ∑*       &
                                                     !$% .! 3!
Second order moment A,                     𝜇′" =         #
                                                                 × ℎ"


                                                     ∑*       '
                                                      !$% .! 3!
Third order moment A,                       𝜇′+ =          #
                                                                  × ℎ+


                                                      ∑*       (
                                                       !$% .! 3!
Fourth order moment A,                       𝜇′, =                 × ℎ,
                                                             #


In general, the rth order moment about arbitrary point A is given by,

         ∑*       )
          !$% .! 3!
𝜇′- =           #
                      × ℎ- ; 𝑓𝑜𝑟 𝑟 = 1,2, − − −


6.3.2 Moments about Origin

In case, when we take an arbitrary point A=0 then, we get the moments about

origin.

For Ungrouped Data

                                                ∑#
                                                 !$%('! ($)
                                                            %
First order moment,                     𝜇′! =                    = 𝑥̅
                                                     #


                                                 ∑#
                                                  !$%('! ($)
                                                            &       !
Second order moment,                     𝜇′" =                    = # ∑#01! 𝑥0"
                                                       #
```

## Page 74

```
                                                   ∑#
                                                    !$%('! ($)
                                                              '          !
Third order moment,                        𝜇′+ =                       = ∑#01! 𝑥0+
                                                          #              #


                                                    ∑#
                                                     !$%('! ($)
                                                               (             !
Fourth order moment,                       𝜇′, =           #
                                                                        = # ∑#01! 𝑥0,


In general, the rth order moment about arbitrary point A is given by

                      ∑#
                       !$%('! ($)
                                 )     !
,             𝜇- =         #
                                     = # ∑#01! 𝑥0- ; 𝑓𝑜𝑟 𝑟 = 1,2, − − −


For Grouped Data

                                                    ∑*
                                                     !$% .('! ($)
                                                                  %              ! /
First order moment A,                       𝜇′! =                        =        ∑ 𝑓 𝑥!
                                                              #                  4 01! 0 0


                                                       ∑*
                                                        !$% .('! ($)
                                                                    &             !
Second order moment A,                      𝜇′" =              #
                                                                          = 4 ∑/01! 𝑓0 𝑥0"


                                                       ∑*
                                                        !$% .('! ($)
                                                                     '            !
Third order moment A,                          𝜇′+ =                         =        ∑/01! 𝑓0 𝑥0+
                                                               #                  4


                                                         ∑*
                                                          !$% .('! ($)
                                                                       (              !
Fourth order moment A,                         𝜇′, =               #
                                                                                 = 4 ∑/01! 𝑓0 𝑥0,


In general, the rth order moment about arbitrary point A is given by

                      ∑*
                       !$% .('! ($)
                                   )       !
,             𝜇′- =                    = 4 ∑/01! 𝑓0 𝑥0- ; 𝑓𝑜𝑟 𝑟 = 1,2, − − −
                               #




6.3.3 Moments about Mean
```

## Page 75

```
When we take the deviation from the actual mean and calculate the moments,

these are known as moments about mean or central moments. The formulae are:




For Ungrouped Data

                                                ∑#
                                                 !$%('! ('̅ )
                                                             "
Zero order moment,                      𝜇$ =             #
                                                                    =1

                                                   ∑#
                                                    !$%('! ('̅ )
                                                                %
First order moment,                      𝜇! =            #
                                                                     =0


Thus, first order moment about mean is zero, because the algebraic sum of the

deviation from the mean is zero ∑#01!(𝑥0 − 𝑥̅ ) = 0

                                                   ∑#
                                                    !$%('! ('̅ )
                                                                &
Second order moment,                     𝜇" =            #
                                                                     = 𝜎 " (𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒 )


Therefore, second order moment about mean is variance.

These results, viz, µ$ = 1, µ! = 0 𝑎𝑛𝑑 µ" = 𝜎" are found very important in

statistical theory and practical.

                                                   ∑#
                                                    !$%('! ('̅ )
                                                                 '
Third order moment,                         𝜇+ =
                                                          #


                                                     ∑#
                                                      !$%('! ('̅ )
                                                                   (
Fourth order moment,                        𝜇, =
                                                             #


In general, the rth order moment about arbitrary point mean is given by

                     ∑#
                      !$%('! ('̅ )
                                  )     !
,             𝜇- =         4
                                      = # ∑#01! 𝑥0- ; 𝑓𝑜𝑟 𝑟 = 1,2, − − −
```

## Page 76

```
For Grouped Data

In case of frequency distribution, the rth order moment about mean is given by:

                            ∑#01! 𝑓0 (𝑥0 − 𝑥̅ )-
                       𝜇- =                      ; 𝑓𝑜𝑟 𝑟 = 1,2, − − −
                                     𝑁

By substituting the different value of are we can gate different orders moment

about mean as follows:

                                              ∑#
                                               !$% .! ('! ('̅ )
                                                               "
Zero order moment,                    𝜇$ =            4
                                                                    = 1 𝑤ℎ𝑒𝑟𝑒 𝑁 = ∑/01! 𝑓

                                              ∑#
                                               !$% .! ('! ('̅ )
                                                                %
First order moment,                    𝜇! =                         =0
                                                      4


Because ∑#01! 𝑓0 (𝑥0 − 𝑥̅ ) = 0

                                              ∑#
                                               !$% .! ('! ('̅ )
                                                                &
Second order moment,                  𝜇" =                          = 𝜎 " (𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒)
                                                      4


                                               ∑#
                                                !$% .! ('! ('̅ )
                                                                '
Third order moment,                    𝜇+ =            4


                                                ∑#
                                                 !$% .! ('! ('̅ )
                                                                  (
Fourth order moment,                    𝜇, =
                                                          4




       TEXT BOOKS

   •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

       edition.2014.
```

## Page 77

```
   •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

       ed.2013, New Delhi.

   •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

       Publications, Reprint 2008.




       REFERENCE BOOKS

   •   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

       Narosa Publishing House ,2004,New Delhi.

   •   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New

       Delhi.

   •   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281In

       siders’Guide



       Video Lecture :

h#ps://www.youtube.com/watch?v=ISaVvSO_3Sg
```

## Page 78

```
                                      Lecture 3.2
CO1: To understand fundamental concepts of probability theory and statistics.

CO2: Identify and formulate engineering problems in different situations involving
probabilistic and statistical measures.

                Conditional Probability and Bayes Theorem


Conditional Probability

Probability of occurrence of event A given that event B has already occurred.

Formula P(A∣B) = P(A∩B)/ P(B)

Where: P(B) ≠ 0.

Example: One card is drawn from a deck. Find probability that it is a king given that it is a
face card.
Solution: Face cards = 12, Kings = 4

P(K∣F) = 4/12 = 1/3


Independent and Dependent Events

Independent Events: Occurrence of one event does not affect another.

Example: Tossing two coins

Condition: P(A∩B) = P(A) P(B)

Dependent Events: Occurrence of one event affects another.

Example: Drawing cards without replacement




Bayes’ Theorem
Used to revise probabilities based on new information.
```

## Page 79

```
Formula: P(A∣B) = (P(B∣A) P(A) )/P(B)

Applications

   •   Medical testing
   •   Spam filtering
   •   Machine learning
   •   Decision-making

Important Probability Identities

Identity 1: P(S) = 1
Identity 2: P(ϕ) = 0
Identity 3: 0 ≤ P(A) ≤ 1
Identity 4: P(A′) = 1 − P(A)
Identity 5: P(A − B) = P(A) − P(A∩B)




Numerical Problems
Example 1: A card is drawn from a deck of 52 cards. Find probability of getting:

   1. An ace
   2. A red card

Solution: Total cards = 52

Aces = 4

P(Ace) = 4/52 =1/13

Red cards = 26

P(Red) = 26/52 = ½



Example 2: Two dice are rolled. Find probability that sum is 7.

Solution: Total outcomes: 6 × 6 = 36

Favorable outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
```

## Page 80

```
Total favorable outcomes = 6

       P(sum = 7) = 6/36 = 1/6



Real-Life Applications of Probability

In Engineering
   • Reliability of machines
   • Failure analysis

In Business
   • Market prediction
   • Risk management

In Medical Science
   • Disease prediction
   • Drug testing

In Artificial Intelligence
   • Prediction algorithms
   • Data analysis




       TEXT BOOKS
   •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised
       edition.2014.
   •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th ed.2013,
       New Delhi.
   •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi
       Publications, Reprint 2008.
```

## Page 81

```
    REFERENCE BOOKS
•   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition
    Narosa Publishing House ,2004,New Delhi.
•   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New
    Delhi.
•   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281In
    siders’Guide


    Video Lecture : https://youtu.be/71oNiqPoKD8?si=Q3oUQjHG2SN6cVkJ
```

## Page 82

```
                                      Lecture 3.1
CO1: To understand fundamental concepts of probability theory and statistics.




             Basics of Probability-Definitions and Laws

Introduction: Probability is a branch of mathematics that deals with uncertainty and the
likelihood of occurrence of events. It helps in predicting how likely an event is to happen.
Applications of Probability
   •    Weather forecasting
   •    Insurance and risk analysis
   •    Medical diagnosis
   •    Machine learning and AI
   •    Games and gambling
   •    Engineering reliability analysis


Random Experiment: A random experiment is an experiment whose outcome cannot
be predicted with certainty in advance.
Examples
   1. Tossing a coin
   2. Rolling a die
   3. Drawing a card from a deck
   4. Selecting a student randomly


Outcome and Sample Space
(a) Outcome: A possible result of a random experiment is called an outcome.
Example: Tossing a coin → Outcomes: H (Head), T (Tail)
(b) Sample Space: The set of all possible outcomes is called the sample space. It is denoted
by S.
```

## Page 83

```
Examples
Example 1: Tossing one coin, S = {H, T}
Example 2: Rolling one die, S = {1, 2, 3, 4, 5, 6}
Example 3: Tossing two coins, S = {HH, HT, TH, TT}


Event: An event is a subset of the sample space. It is usually denoted by capital letters A, B,
C.
Example: If a die is rolled, S = {1, 2, 3, 4, 5, 6}
Event A: getting an even number, A = {2, 4, 6}


Types of Events
(a) Simple Event: An event containing only one outcome.
Example: A = {2}
(b) Compound Event: An event containing more than one outcome.
Example: A = {2, 4, 6}
(c) Impossible Event: An event that cannot occur.
Example: Getting 7 on a die. P(A) = 0
(d) Sure Event: An event that always occurs. P(S) = 1.
(e) Complementary Event: If A is an event, then the complement of A is denoted by A′.
A′ = S−A.
Example: If A = getting even number, A = {2, 4, 6}
Then, A′ = {1, 3, 5}.


Probability of an Event: Probability measures the chance of occurrence of an event.


Classical Definition of Probability: If an experiment has n equally likely outcomes and m
favorable outcomes for event A, then
P(A) = m/n
Where 0 ≤ P(A) ≤ 1.
```

## Page 84

```
Examples on Probability
Example 1: Tossing a Coin: Find probability of getting Head.

Solution: S = {H, T}

Favorable outcomes = 1

Total outcomes = 2

P(H) = ½


Example 2: Rolling a Die: Find probability of getting an even number.

Solution: S = {1, 2, 3, 4, 5, 6}

Even numbers: A = {2, 4, 6}

P(A) = 3/6 = ½



Laws of Probability
(A) Addition Law of Probability: Used when finding probability of occurrence of at least
one event.
Formula: P(A∪B) = P(A) + P(B) − P(A∩B)
Where:
   •     A ∪ B: occurrence of A or B or both
   •     A∩ B: occurrence of both A and B


Special Case: Mutually Exclusive Events: If events cannot occur together:
P(A∩B) = 0, Then
P(A∪B) = P(A) + P(B)


Example: A die is rolled. Find P(A∪B).
Solution: Let A: getting even number and B: getting number greater than 4.

A = {2, 4, 6}, B = {5, 6}, A ∩ B = {6}, P(A) = 3/6, P(B) = 2/6, P(A∩B) = 1/6
```

## Page 85

```
P(A∪B) = P(A) + P(B) − P(A∩B)
        = 3/6 + 2/6 − 1/6 = 4/6 = 2/3


(B) Complement Law: The probability that an event does not occur.
Formula: P(A′) = 1 − P(A).
Example: Probability of passing an exam is 0.8. Find probability of failing.

Solution: P(F) = 1 − 0.8 = 0.2.



(C) Multiplication Law of Probability: Used for finding probability of simultaneous
occurrence of events.

Formula: P(A∩B) = P(A) × P(B∣A)

Where: P(B∣A) = conditional probability

For independent events: P(A∩B) = P(A) × P(B).

Example: Two coins are tossed. Find probability of getting two heads.

Solution: P(H) = ½

Since events are independent.

P(HH) = ½ × ½ = ¼ .




       TEXT BOOKS
   •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised
       edition.2014.
   •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th ed.2013,
       New Delhi.
   •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi
       Publications, Reprint 2008.
```

## Page 86

```
    REFERENCE BOOKS
•   R1 = R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition
    Narosa Publishing House ,2004,New Delhi.
•   R2 = B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New
    Delhi.
•   R3 = S. P. Gupta, Statistical Methods, S. Chand & Sons, 2017, New Delhi,
    ISBN9789351610281, Insiders’ Guide


    Video Lecture : https://youtu.be/YTWM4aOqVwM?si=-fBHOUT0Q57JE70j
```

## Page 87

```
                                      Lecture 2.4
CO1: To understand fundamental concepts of probability theory and statistics.




               Kurtosis and Nature of Distribution


CONCEPT OF KURTOSIS

If we have the knowledge of the measures of central tendency, dispersion and

skewness, even then we cannot get a complete idea of a distribution. In addition

to these measures, we need to know another measure to get the complete idea

about the shape of the distribution which can be studied with the help of Kurtosis.

Prof. Karl Pearson has called it the “Convexity of a Curve”. Kurtosis gives a

measure of flatness of distribution.

The degree of kurtosis of a distribution is measured relative to that of a normal

curve. The curves with greater peakedness than the normal curve is called

“Leptokurtic”. The curves which are flatter than the normal curve are called

“Platykurtic”. The normal curve is called “Mesokurtic.” The Fig.4 describes the

three different curves mentioned above:
```

## Page 88

```
               Fig.: Platykurtic Curve, Mesokurtic Curve and Leptokurtic Curve




Measures of Kurtosis
1. Karl Pearson’s Measures of Kurtosis
For calculating the kurtosis, the second and fourth central moments of variable
are used. For this, following formula given by Karl Pearson is used:


                                                  𝜇"
                                           𝛽! =
                                                  𝜇!!

                                      𝑜𝑟 g! = 𝛽! − 3

where, 𝜇! = Second order central moment of distribution
𝜇" = Fourth order central moment of distribution


Description:1. If 𝛽! = 3 𝑜𝑟 𝛾! = 0, then curve is said to be mesokurtic;
2. If 𝛽! < 3 𝑜𝑟 𝛾! < 0,, then curve is said to be platykurtic;
3. If 𝛽! > 3 𝑜𝑟 𝛾! > 0,, then curve is said to be leptokurtic.
```

## Page 89

```
Example 2: First four moments about mean of a distribution are 0, 2.5, 0.7 and
18.75. Find coefficient of skewness and kurtosis.
Solution: We have 𝜇# = 0, 𝜇! = 2.5, 𝜇$ = 0.7 𝑎𝑛𝑑 𝜇" = 18.75
                               %"     ('.))"
Therefore, Skewness 𝛽# = %!! = (!.+)! = 0.031
                                "




                                    𝜇" 18.75 18.75
                             𝛽! =      =       =      =3
                                    𝜇!! (2.5)!   6.25


As 𝛽! is equal to 3, so the curve is mesokurtic


Practice Question:


1. The first four raw moments of a distribution are 2, 136, 320, and

   40,000. Find out coefficients of skewness and kurtosis.




   TEXT BOOKS

   •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

       edition.2014.

   •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

       ed.2013, New Delhi.
```

## Page 90

```
   •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

       Publications, Reprint 2008.




   REFERENCE BOOKS

   •   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

       Narosa Publishing House ,2004,New Delhi.

   •   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006,

       New Delhi.

   •   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281I

       nsiders’Guide



 Video Lecture :

h#ps://www.youtube.com/watch?v=TM033GCU-SY&t=65s
```

## Page 91

```
                                        Lecture 2.3
CO1: To understand fundamental concepts of probability theory and statistics.


         Skewness – Karl Pearson & Bowley Methods
7.1 CONCEPT OF SKEWNESS

Skewness means lack of symmetry. In mathematics, a figure is called symmetric if

there exists a point in it through which if a perpendicular is drawn on the X-axis, it

divides the figure into two congruent parts i.e., identical in all respect or one part

can be superimposed on the other i.e. mirror images of each other. In Statistics, a

distribution is called symmetric if mean, median and mode coincides. Otherwise,

the distribution becomes asymmetric. If the right tail is longer, we get a positively

skewed distribution for which mean >median > mode while if the left tail is longer,

we get a negatively skewed distribution for which mean < median < mode.

The example of the Symmetrical curve, Positive skewed curve and Negative skewed

curve are given as follows:




                                           Frequency
                    14

                    12

                    10
                                                                            Frequency
                     8
```

## Page 92

```
                                  Fig. 7.1: Symmetrical Curve




16

14

12

10
                                                                                       Frequency
8

6

4

      0       1       2       3       4       5       6       7       8       9   10   11

                              Fig. 7.2: Negative Skewed Curve




     14

     12

     10

      8
                                                                                            Frequency
      6

      4

      2

      0
          0       1       2       3       4       5       6       7       8   9   10   11
```

## Page 93

```
                               Fig. 7.3: Positive Skewed Curve



Difference between Variance and Skewness

The following two points of difference between variance and skewness should be

carefully noted.

1. Variance tells us about the amount of variability while skewness gives the

   direction of variability.

2. In business and economic series, measures of variation have greater practical

   application than measures of skewness. However, in medical and life science

   field measures of skewness have greater practical applications than the variance.




7.2 VARIOUS MEASURES OF SKEWNESS

Measures of skewness help us to know to what degree and in which direction

(positive or negative) the frequency distribution has a departure from symmetry.

Although positive or negative skewness can be detected graphically depending on

whether the right tail or the left tail is longer but, we don’t get idea of the magnitude.

Besides, borderline cases between symmetry and asymmetry may be difficult to
```

## Page 94

```
detect graphically. Hence some statistical measures are required to find the

magnitude of lack of symmetry. A good measure of skewness should possess three

criteria:

1. It should be a unit free number so that the shapes of different distributions, so far

   as symmetry is concerned, can be compared even if the unit of the underlying

   variables are different;

2. If the distribution is symmetric, the value of the measure should be zero.

   Similarly, the measure should give positive or negative values according as the

   distribution has positive or negative skewness respectively; and

3. As we move from extreme negative skewness to extreme positive skewness, the

   value of the measure should vary accordingly.

Measures of skewness can be both absolute as well as relative. Since in a

symmetrical distribution mean, median and mode are identical more the mean

moves away from the mode, the larger the asymmetry or skewness. An absolute

measure of skewness can not be used for purposes of comparison because of the

same amount of skewness has different meanings in distribution with small

variation and in distribution with large variation

Absolute Measures of Skewness
```

## Page 95

```
Following are the absolute measures of skewness:

Skewness (Sk) = Mean – Median

Skewness (Sk) = Mean – Mode

Skewness (Sk) = (Q3 - Q2) - (Q2 - Q1)

For comparing to series, we do not calculate these absolute mearues we calculate

the relative measures which are called coefficient of skewness. Coefficient of

skewness are pure numbers independent of units of measurements.

Relative Measures of Skewness

In order to make valid comparison between the skewness of two or more

distributions we have to eliminate the distributing influence of variation. Such

elimination can be done by dividing the absolute skewness by standard deviation.

The following are the important methods of measuring relative skewness:

1. β and γ Coefficient of Skewness

Karl Pearson defined the following β and γ coefficients of skewness, based upon the

second and third central moments:
```

## Page 96

```
It is used as measure of skewness. For a symmetrical distribution, shall be zero. as

a measure of skewness does not tell about the direction of skewness, i.e. positive or

negative. Because being the sum of cubes of the deviations from mean may be

positive or negative but is always positive. Also, being the variance always

positive. Hence, would be always positive. This drawback is removed if we

calculate Karl Pearson’s Gamma coefficient g1which is the square root of i. e.
```

## Page 97

```
Then the sign of skewness would depend upon the value of m3 whether it is positive or

negative. It is advisable to use g1 as measure of skewness.

Karl Pearson’s Coefficient of Skewness

This method is most frequently used for measuring skewness. The formula for measuring

coefficient of skewness is given by




The value of this coefficient would be zero in a symmetrical distribution. If mean is

greater than mode, coefficient of skewness would be positive otherwise negative. The

value of the Karl Pearson’s coefficient of skewness usually lies between ± 1 for moderately

skewed distribution. If mode is not well defined, we use the formula




By using the relationship

Mode = (3 Median-2 Mean)

Here, -3 < Sk < 3. In practice it is rarely obtained.




Bowleys’s Coefficient of Skewness
```

## Page 98

```
This method is based on quartiles. The formula for calculating coefficient of skewness is

given by




The value of Sk would be zero if it is a symmetrical distribution. If the value is greater than

zero, it is positively skewed and if the value is less than zero it is negatively skewed

distribution. It will take value between +1 and -1.

Example1:

For a distribution Karl Pearson’s coefficient of skewness is 0.64, standard deviation is 13

and mean is 59.2 Find mode and median.

Solution:

We have given Sk = 0.64, σ = 13 and Mean = 59.2.

Therefore, by using formulae
```

## Page 99

```
Practice Questions

1. Karl Pearson’s coefficient of skewness is 1.28, its mean is 164 and mode 100, find the

   standard deviation.

2. For a frequency distribution the Bowley’s coefficient of skewness is 1.2. If the sum of

   the 1st and 3rd quarterlies is 200 and median is 76, find the value of third quartile.

3. The following are the marks of 150 students in an examination. Calculate Karl Pearson’s

   coefficient of skewness.




   TEXT BOOKS

      T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised edition.2014.

      T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th ed.2013, New

       Delhi.
```

## Page 100

```
      T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi Publications,

       Reprint 2008.




   REFERENCE BOOKS

      R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition Narosa

       Publishing House ,2004,New Delhi.

      R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New Delhi.

      S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281Insiders’Gui

       de



 Video Lecture :

https://www.youtube.com/watch?v=EWuR4EGc9EY
```

## Page 101

```
        Standard Deviation & Variance


     PROBABILITY & STATISTICS | Measures of Central Tendency and Dispersion



Course: PROBABILITY & STATISTICS | Chapter: Measures of Central Tendency and Dispersion | Program: Bachelor of Engineering




                                                                                                           DISCOVER · LEARN · EMPOWER
```

## Page 102

```
                                                                    Course Outcomes                                                                            SLIDE 2 / 14




Course Outcome
CO          BT LEVEL                     DESCRIPTION




     CO1               BT3               To understand fundamental concepts of probability theory and statistics




     CO2               BT4               Identify and formulation of engineering problems in different situations involving probabilistic and statistical measures




     CO3               BT5               Classify various types of statistical methods and perform statistical inference




     CO4               BT4               Apply appropriate statistical tools, distributions including correlation and regression analysis techniques




     CO5               BT5               Implement the standard concepts and tools at an intermediate to advanced level that will help in tackling various problems in
                                         hypothesis testing




                 Chandigarh University                                                                                                                               2 / 14
```

## Page 103

```
                                                      Learning Objectives         SLIDE 3 / 14




Learning Outcomes

 1   Explain the concept of combined mean using weighted data sets.




 2   Describe the procedure for calculating weighted mean in mixed groups.




 3   Summarize the relationship between individual means and the combined mean.




                     Chandigarh University                                             3 / 14
```

## Page 104

```
                                                                    Lecture                                                         SLIDE 4 / 14




Defining Variance and Standard Deviation
 1   Variance measures the average squared deviation from the mean.



 2   Standard deviation is the square root of the variance.



 3   Both metrics quantify the spread or dispersion of a dataset.



 4   High variance indicates data points are far from the mean.



 5   Low variance indicates data points are clustered near the mean.



 6   Standard deviation shares the same units as the original data.           Real Predictions Have Curves! - Confidence Interval




                        Chandigarh University                                                                                            4 / 14
```

## Page 105

```
                                                                    Lecture                                                                   SLIDE 5 / 14




Why Squared Deviations Matter
 1   Squaring deviations prevents positive and negative differences from
     canceling out.

 2   It gives more weight to larger deviations or outliers in the data.



 3   The sum of squared deviations is minimized at the arithmetic mean.



 4   This property makes variance the optimal measure for least squares
     methods.

 5   Without squaring, the sum of deviations from the mean is always zero.



 6   Squaring ensures the measure of spread is always a non-negative value.   Standard Deviation: Simple Definition, Step by Step Video (source:
                                                                                                 www.statisticshowto.com)



                        Chandigarh University                                                                                                      5 / 14
```

## Page 106

```
                                                                  Lecture                                                                     SLIDE 6 / 14




Formulas for Population vs Sample
 1   Population variance uses N in the denominator for the entire group.



 2   Sample variance uses N minus 1 to correct for bias in estimation.



 3   The formula for population variance is σ squared equals sum of squared
     deviations divided by N.

 4   The formula for sample variance is s squared equals sum of squared
     deviations divided by N minus 1.

 5   Using N minus 1 provides an unbiased estimator for the population
     variance.

 6   Always identify if your data represents a full population or a sample.   Standard Deviation - MathBitsNotebook(A1) (source: mathbitsnotebook.com)




                        Chandigarh University                                                                                                       6 / 14
```

## Page 107

```
                                                                         Worked Example   SLIDE 7 / 14




Calculating Variance
  CONSIDER A SAMPLE OF FIVE VALUES                   SQUARE THESE DEVIATIONS

  10, 12, 14, 16, 18.                                16, 4, 0, 4, 16.




  • First, calculate the mean: sum is 70,
  so mean is 14.
  • Next, find deviations from the
  mean: -4, -2, 0, 2, 4.
  • Sum of squared deviations is 40.
  • Sample variance is 40 divided by (5
  minus 1), which equals 10.



                             Chandigarh University                                             7 / 14
```

## Page 108

```
                                                               Worked Example                                                                   SLIDE 8 / 14




Standard Deviation
 1   Standard deviation is the square root of the calculated variance.



 2   From the previous example, variance was 10.



 3   The standard deviation is the square root of 10.



 4   This value is approximately 3.16 units.



 5   It tells us the average distance of data points from the mean.



 6   In this case, data points typically vary by about 3.16 from 14.            Standard Deviation: Simple Definition, Step by Step Video (source:
                                                                                                   www.statisticshowto.com)



                        Chandigarh University                                                                                                        8 / 14
```

## Page 109

```
                                                                 Lecture                                 SLIDE 9 / 14




Common Pitfalls in Calculation
 1   Forgetting to square the deviations before summing them up.



 2   Using N instead of N minus 1 for sample variance calculations.



 3   Calculating the mean incorrectly before finding the deviations.



 4   Confusing the standard deviation with the variance value.



 5   Rounding intermediate squared values too early in the process.



 6   Applying population formulas to sample data without adjustment.       Source: static.vecteezy.com




                        Chandigarh University                                                                 9 / 14
```

## Page 110

```
                                                                   Lecture    SLIDE 10 / 14




Combined Mean and Variance Concept
 1   Combined mean is the weighted average of individual group means.



 2   It accounts for the size of each group in the mixture.



 3   The combined variance includes within-group and between-group
     variations.

 4   Larger groups contribute more to the combined mean calculation.



 5   This concept is vital for analyzing mixed engineering datasets.



 6   It allows us to summarize multiple distinct groups into one statistic.



                        Chandigarh University                                      10 / 14
```

## Page 111

```
                                                               Lecture     SLIDE 11 / 14




Calculating Combined Variance
                                GOVERNING EQUATION


     The formula is: Combined Variance = (Sum of (n_i ×
                  (sigma_i^2 + d_i^2))) / N

 1    Combined variance formula includes the sum of individual
      variances.

 2    It also adds the sum of squared deviations of group means from the
      combined mean.

 3    Here, d_i is the difference between the group mean and combined
      mean.

 4    This accounts for the spread within groups and the spread between
      groups.

 5    It provides a complete picture of dispersion for the entire mixed
      population.
                       Chandigarh University                                    11 / 14
```

## Page 112

```
                                                                Relationship                              SLIDE 12 / 14




Individual vs Combined Mean
 1   The combined mean always lies between the smallest and largest group
     means.

 2   It is a weighted average, not a simple arithmetic average of means.



 3   If all groups have equal size, the combined mean is the simple average.



 4   The combined mean shifts towards the mean of the largest group.



 5   This relationship ensures the combined mean represents the total
     dataset accurately.

 6   It reflects the true central tendency of the mixed population.            Source: mathisvisual.com




                           Chandigarh University                                                               12 / 14
```

## Page 113

```
                                                               Lecture                                    SLIDE 13 / 14




Key Takeaways

 1   Variance measures squared spread; standard deviation is its square
     root.


 2   Use N minus 1 for sample variance to avoid bias.



 3   Combined mean is a weighted average of individual group means.



 4   Combined variance includes both within-group and between-group
     variations.


 5   Always check for calculation pitfalls like squaring errors or wrong
                                                                           Source: content.twinkl.co.uk
     denominators.


                       Chandigarh University                                                                   13 / 14
```

## Page 114

```
                                                              Lecture     SLIDE 14 / 14




References
 1   Higher Engineering Mathematics — H. K Dass.



 2   Higher Engineering Mathematics — B. S. Grewal



 3   Advanced Engineering Mathematics — R.K. Jain, and S.R.K. Iyengar



 4   Advanced Engineering Mathematics — B.V. Ramana



 5   Statistical methods — S. P. Gupta



 6   A textbook of Engineering Mathematics — N.P. Bali and Manish Goyal



                       Chandigarh University                                   14 / 14
```

## Page 115

```
                                       Lecture 2.2
CO1: To understand fundamental concepts of probability theory and statistics.


   Relation between Moments about Mean and Moments

                                about Arbitrary Point

The rth moment about mean is given by

                         ∑#"$% 𝑓" (𝑥" − 𝑥̅ )!
                    𝜇! =                      ; 𝑓𝑜𝑟 𝑟 = 0, 1,2, − − −
                                  𝑁

                    ∑#"$% 𝑓" (𝑥" − 𝐴 + 𝐴 − 𝑥̅ )!
               𝜇! =                              ; 𝑓𝑜𝑟 𝑟 = 0, 1,2, − − −
                                  𝑁

                ∑#
                 !$% '! {(*! +,)+(*̅ +,)}
                                         "
         𝜇! =               0
                                             ; 𝑓𝑜𝑟 𝑟 = 0, 1,2, − − −            (1)


If 𝑑" = 𝑥" − 𝐴 𝑡ℎ𝑒𝑛,

                                             𝑥" = 𝐴 + 𝑑"

                                      1          1
                                        ∑𝑥" = 𝐴 + ∑𝑑"
                                      𝑛          𝑛

                                       𝑥" = (𝐴 + 𝑢′% )

                                                  1
                                         𝑢′% =      ∑𝑑
                                                  𝑛 "

                                         𝑢′% = 𝑥̅ − 𝐴
```

## Page 116

```
Therefor, we get from equation (1)

     ∑)'*( 𝑓' (𝑑' − 𝑢′( )&
𝜇& =                       ; 𝑓𝑜𝑟 𝑟 = 0, 1,2, − − −
               𝑁

          )
    1
𝜇& = 4 𝑓' {𝑑'& − 𝐶(& 𝑑&&+( 𝜇(, + 𝐶-& 𝑑&&+- (𝜇(, )- − 𝐶.& 𝑑&&+. (𝜇(, ). + ⋯ + (−1)& (𝜇(, )& }
    𝑁
         '*(


       1          1                      1                       1
𝜇& =     ∑𝑓' 𝑑'& − ∑𝑓' 𝑑' 𝐶(& 𝑑&&+( 𝜇(, + ∑𝑓' 𝐶-& 𝑑&&+- (𝜇(, )- − ∑𝑓' 𝐶.& 𝑑&&+. (𝜇(, ). + ⋯
       𝑁          𝑁                      𝑁                       𝑁
                              1            𝑟
                    + (−1)&     ∑𝑓' :𝜇′1 ;
                              𝑁

                                           !            "                    #
𝜇$ = 𝜇$% − 𝐶&$ 𝜇$'&
                %
                    𝜇&% + 𝐶($ 𝜇$'(
                               %
                                   𝜇&% − 𝐶)$ 𝜇$')
                                              %
                                                  𝜇&% + ⋯ + (−1)$ 𝜇&%                          (2)

In particular on putting r=2,3 and 4 in equation (2), we get

𝜇( = 𝜇′( − 𝜇&%(


𝜇) = 𝜇′) − 3𝜇% ( 𝜇&% + 2𝜇&%)

                                    !
𝜇* = 𝜇′* − 4𝜇% ) 𝜇&% + 6𝜇% ( 𝜇&% − 3𝜇&%*


Effect of Change of Origin and Scale on Moments

               *! +,
Let 𝑢" =         1
                     so that 𝑥" = 𝐴 + ℎ𝑢"            𝑎𝑛𝑑 (𝑥" − 𝑥̅ ) = ℎ(𝑢" − 𝑢=)


Thus, rth moment of x about arbitrary point x=A is given by

               #                               #
     1                1
𝜇′! = > 𝑓" (𝑥" − 𝐴)! = > 𝑓" (ℎ𝑢" )!
     𝑁                𝑁
              "$%                              "$%
```

## Page 117

```
                 #
              1
𝜇 2 ! (𝑥) = ℎ! > 𝑓" (𝑢" )! = ℎ! 𝑢!2 (𝑢)
              𝑁
                 "$%


And, rth moment of x about mean is given by

            #
        1
𝜇! (𝑥) = > 𝑓" (𝑥" − 𝑥̅ )!
        𝑁
           "$%


            #
        1
𝜇! (𝑥) = > 𝑓" {ℎ(𝑢" − 𝑢= )}!
        𝑁
           "$%


                 #
           1
𝜇! (𝑥) = ℎ! > 𝑓" (𝑢" − 𝑢= )! = ℎ! 𝜇! (𝑢)
           𝑁
                "$%


Thus, the rth moment of the variable x about mean is hr times the rth moment of

the new variable u about mean after changing the origin and scale.

Sheppard’s Corrections for Moments

The fundamental assumption that we make in farming class intervals is that the

frequencies are uniformly distributed about the mid points of the class intervals.

All the moment calculations in case of grouped frequency distributions rely on

this assumption. The aggregate of the observations or their powers in a class is

approximated by multiplying the class midpoint or its power by the corresponding

class frequency. For distributions that are either symmetrical or close to being
```

## Page 118

```
symmetrical, this assumption is acceptable. But it is not acceptable for highly

skewed distributions or when the class intervals exceed about 1/20th of the range.

In such situations, W. F. Sheppard suggested some corrections to be made to get

rid of the so called “grouping errors” that enter into the calculation of moments.

   Sheppard suggested the following corrections known as Sheppard’s

corrections in the calculation of central moments assuming continuous frequency

distributions if the frequency tapers off to zero in both directions

                       ℎ3
𝜇3 (𝑐𝑜𝑟𝑟𝑒𝑐𝑡𝑒𝑑 ) = 𝜇3 −
                       12

𝜇4 (𝑐𝑜𝑟𝑟𝑒𝑐𝑡𝑒𝑑 ) = 𝜇4

                       ℎ3       7 5
𝜇5 (𝑐𝑜𝑟𝑟𝑒𝑐𝑡𝑒𝑑 ) = 𝜇5 −    𝜇3 +     ℎ
                       12      240

Where, h is the width of class interval.

PEARSON’S BETA AND GAMMA COEFFICIENTS

Karl Pearson defined the following four coefficients, based upon the first four

central moments:

1. 𝛽% is defined as

                                            𝜇43
                                        𝛽% = 4
                                            𝜇3
```

## Page 119

```
It is used as measure of skewness. For a symmetrical distribution, 𝛽% shall be

zero.

𝛽% as a measure of skewness does not tell about the direction of skewness, i.e.

positive or negative. Because µ4 being the sum of cubes of the deviations from

mean may be positive or negative but 𝜇43 is always positive. Also µ3 being the

variance always positive. Hence 𝛽% would be always positive. This drawback is

removed if we calculate Karl Pearson’s coefficient of skewness g% which is the

square root of 𝛽% ,i. e.

                                                 𝜇4       𝜇4
                             𝛾% = ±G𝛽% =                =
                                               (𝜇3 )4/3   𝜎3

    Then the sign of skewness would depend upon the value of 𝜇4 whether it is

    positive or negative. It is advisable to use g% as measure of skewness.

2. b3 measures kurtosis and it is defined by

                                                𝜇5
                                         𝛽3 =
                                                𝜇33

    And similarly, coefficient of kurtosis g3 is defined as

                                      g3 = 𝛽3 − 3

    Example 1: For the following distribution calculate first four moments about

    mean and also find b% , b3 , g% 𝑎𝑛𝑑 g3 :
```

## Page 120

```
 Marks          5        10      15             20          25         30       35

 Frequency 4             10      20             36          16         12       2




Solution: First we construct the following frequency distribution for calculation

of moments:

 Marks      f       d=(x-20)/5        fd             fd2         fd3        fd4

 5          4       -3                -12            36          -108       324

 10         10      -2                -20            40          -80        160

 5          20      -1                -20            20          -20        20

 20         36      0                 0              0           0          0

 25         16      1                 16             16          16         16

 30         12      2                 24             48          96         192

 35         2       3                 6              18          54         162

                                          ∑𝑓𝑑            ∑𝑓𝑑 3    ∑𝑓𝑑 4         ∑𝑓𝑑 5

                                          = −6           = 178    = −42         = 874




Then,
```

## Page 121

```
                                  ∑𝑓𝑑        6
                         𝜇%2 =        ×ℎ =−     × 5 = −0.3
                                   𝑁        100

                                  ∑𝑓𝑑 3        178
                        𝜇32 =           × ℎ3 =     × 25 = 44.5
                                   𝑁           100

                              ∑𝑓𝑑 4          42
                     𝜇42 =          × ℎ4 = −     × 125 = −52.5
                               𝑁             100

                              ∑𝑓𝑑 5        874
                      𝜇52 =         × ℎ5 =     × 625 = 5462.5
                               𝑁           100

Moments about mean

𝜇( = 𝜇′( − 𝜇&%( = 44.41 = 𝜎 (


𝜇) = 𝜇′) − 3𝜇% ( 𝜇&% + 2𝜇&%) = −12.504

                              !
𝜇* = 𝜇′* − 4𝜇% ) 𝜇&% + 6𝜇% ( 𝜇&% − 3𝜇&%* = 5423.5057


                               𝜇43 (−12.504)3
                           𝛽% = 4 =           = 0.001785
                               𝜇3   (44.41)4

                                    𝜇4      12.504
                             𝛾% =      = −           = −0.0422
                                    𝜎3     (6.6641)4

                                     𝜇5 5423.5057
                              𝛽3 =       =          = 02.7499
                                     𝜇33   (44.41)3

                         g3 = 𝛽3 − 3 = 2.7499 − 3 = −0.2501
```

## Page 122

```
   Practice Questions:

1. The first four moments of a distribution about the value 5 of a variable are 1,

   10, 20 and 25. Find the central moments, b1 and b2.

2. For the following distribution, find central moments, b1 and b2:

      Class        1.5-2.5         2.5-3.5       3.5-4.5        4.5-5.5       5.5-6.5



      Frequency 1                  3             7              3         1



3. Wages of workers are given in the following table:

      Weekly       10-12     12-14     14-16     16-18     18-20      20-22     22-24

      Wages

      Frequency 1            3         7         12        12         4         3



   Find the first four central moment and b1 and b2.



       TEXT BOOKS

  •    T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

       edition.2014.
```

## Page 123

```
   •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

       ed.2013, New Delhi.

   •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

       Publications, Reprint 2008.




       REFERENCE BOOKS

   •   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

       Narosa Publishing House ,2004,New Delhi.

   •   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New

       Delhi.

   •   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281In

       siders’Guide



       Video Lecture :

h#ps://www.youtube.com/watch?v=YlYXSVMr830
```

## Page 124

```
Topic 1.3.2 - Skewness

Completion requirements

Chandigarh University Theory

Skewness

PROBABILITY & STATISTICS — Basic Statistics Measures of Central Tendency and
Dispersion, Moments, skewness, and Kurtosis

Lecture 1.3.2 to 1.3.3

Duration: 2 hrs

   Learning Outcomes

 LO#     Outcomes



 LO1     Explain the definition and significance of kurtosis in a data distribution.


 LO2     Describe the relationship between kurtosis and the shape of a probability curve.


 LO3     Classify distributions as leptokurtic, mesokurtic, or platykurtic based on their kurtosis
         values.

   Course Outcome Mapping

 CO         Statement                                                                           BT
                                                                                                Level


 CO1        To understand fundamental concepts of probability theory and statistics             BT3

   Lecture Content

● Topic 1: Skewness

1. Conceptualizing Skewness and Asymmetry

In the study of moments, skewness, and kurtosis, skewness serves as a fundamental
measure of the asymmetry of a probability distribution around its mean. Unlike
measures of central tendency or dispersion which describe the center or spread of
data, skewness reveals the direction and degree of the 'tail' of the distribution. A
perfectly symmetric distribution, such as the normal distribution, has a skewness of
```

## Page 125

```
zero. However, real-world data often deviates from this ideal symmetry. Understanding
skewness is crucial for interpreting data correctly, as the mean, median, and mode may
not coincide in skewed distributions. This concept directly addresses Learning
Outcome 1 and 2 by defining positive and negative skewness and explaining how they
indicate the direction of asymmetry.

   •     Skewness quantifies the lack of symmetry in a distribution around the mean.

   •     A positive skewness indicates that the distribution has a longer or fatter right tail.

   •     A negative skewness indicates that the distribution has a longer or fatter left tail.

   •     In a positively skewed distribution, the mean is typically greater than the median.

   •     In a negatively skewed distribution, the mean is typically less than the median.

Summary: This section establishes the foundational understanding of skewness as a
measure of asymmetry. It clarifies that the sign of the skewness coefficient determines
the direction of the tail: positive for right-skewed and negative for left-skewed
distributions. Recognizing these patterns allows students to quickly assess the shape of
data without needing to calculate complex coefficients immediately. This conceptual
clarity is essential before moving to mathematical formulations.


       Source: media.licdn.com


       Source: analystprep.com

2. Mathematical Measures of Skewness

To quantify skewness rigorously, we utilize specific mathematical formulas derived from
moments. The most common measure is the Pearson's Moment Coefficient of
Skewness, which relates the third central moment to the cube of the standard
deviation. Another widely used measure is the Bowley's Coefficient of Skewness, which
relies on quartiles and is robust against outliers. The formula for Pearson's moment
coefficient is expressed as , where represents the third central moment and is the
standard deviation. The third central moment is calculated as Math input error. These
formulas provide a numerical value that confirms the visual intuition developed in the
previous section.

   •     Pearson's Moment Coefficient of Skewness is defined as .

   •     The third central moment is given by Math input error.

   •     Bowley's Coefficient of Skewness uses quartiles: .

   •     If the calculated value is positive, the distribution is positively skewed.
```

## Page 126

```
   •     If the calculated value is negative, the distribution is negatively skewed.

Summary: This section introduces the precise mathematical tools needed to calculate
skewness. By defining the third central moment and the standard deviation, we
establish the formula for Pearson's coefficient. We also introduce Bowley's method for
quartile-based analysis. These equations allow for the classification of distributions
based on the sign and magnitude of the coefficient, fulfilling Learning Outcome 3.
Students must be comfortable manipulating these formulas to solve exam problems.


       Source: alevelmaths.co.uk


       Source: conceptdraw.com

3. Interpreting Skewness Coefficients

Interpreting the numerical value of the skewness coefficient is vital for statistical
analysis. A value of zero indicates perfect symmetry. Values between -0.5 and 0.5 are
generally considered to indicate a distribution that is approximately symmetric. Values
greater than 0.5 or less than -0.5 suggest a moderate skewness, while values exceeding
1 or less than -1 indicate a highly skewed distribution. It is important to note that the
magnitude of the coefficient tells us how far the distribution deviates from symmetry.
For instance, a coefficient of 1.5 implies a strong right skew, whereas -1.2 implies a
strong left skew. This interpretation helps in identifying outliers and understanding the
underlying data generation process.

   •     A skewness coefficient of 0 implies a perfectly symmetric distribution.

   •     Coefficients between -0.5 and 0.5 suggest approximate symmetry.

   •     Coefficients outside the range [-0.5, 0.5] indicate moderate to high skewness.

   •     Highly skewed distributions often have coefficients with absolute values greater
         than 1.

   •     The magnitude indicates the degree of asymmetry, while the sign indicates
         direction.

Summary: Here we focus on the practical interpretation of the calculated skewness
values. We define thresholds for symmetry, moderate skew, and high skew. This section
reinforces Learning Outcome 3 by teaching students how to classify distributions based
on the sign and magnitude of the coefficient. Understanding these ranges prevents
misinterpretation of data that appears symmetric but has slight deviations.


       Source: alevelmaths.co.uk
```

## Page 127

```
       Source: analystprep.com

4. Real-World Applications and Examples

Skewness is not just a theoretical concept but has significant applications in various
fields. In finance, stock market returns are often positively skewed, meaning extreme
positive returns are less frequent than extreme negative ones, leading to a long right tail.
In income distribution, data is typically positively skewed because a small number of
individuals earn very high incomes, pulling the mean upwards. Conversely, test scores
in a difficult exam might be negatively skewed if most students score low, with a few
high scores. Understanding these patterns helps in risk assessment and resource
allocation. For example, a negatively skewed income distribution would imply most
people earn very little, with a few earning a lot, which is the opposite of the typical
economic reality.

   •     Income distributions are typically positively skewed due to high earners.

   •     Stock market returns often exhibit positive skewness with rare large gains.

   •     Test scores in difficult exams can show negative skewness.

   •     Skewness analysis helps in identifying outliers and data anomalies.

   •     Quality control data often follows a normal distribution with skewness near zero.

Summary: This section connects the abstract concept of skewness to tangible real-
world scenarios. By examining income, finance, and education data, students see how
asymmetry manifests in practice. These examples solidify the understanding of positive
and negative skewness. Recognizing these patterns is essential for accurate data
modeling and decision-making in engineering and business contexts covered in the
course.


       Source: ermongroup.github.io


       Source: miro.medium.com

▶ Concept Video

Lecture 36 : Moments - Skewness and Kurtosis
IIT KANPUR-NPTEL 43:44

● Topic 2: Kurtosis

5. Introduction to Kurtosis and Distribution Shape
```

## Page 128

```
In the study of moments, skewness, and kurtosis, kurtosis serves as a critical measure
that describes the shape of a probability distribution, specifically focusing on the
'tailedness' and the peakedness of the curve. Unlike skewness, which measures
asymmetry, kurtosis quantifies the extent to which the tails of a distribution differ from
those of a normal distribution. This metric is essential for understanding the risk of
extreme values in data, as high kurtosis implies a higher probability of outliers. For the
course PROBABILITY & STATISTICS, mastering this concept allows students to move
beyond simple mean and variance calculations to a deeper analysis of data structure.
The coefficient of kurtosis helps in classifying distributions into distinct categories,
providing a standardized way to compare datasets with different scales and units.

   •   Kurtosis measures the 'tailedness' of the probability distribution of a real-valued
       random variable.

   •   It indicates the presence of outliers or extreme values in the dataset compared
       to a normal distribution.

   •   The standard normal distribution has a kurtosis value of 3, which serves as the
       baseline for comparison.

   •   Excess kurtosis is often used, calculated as , where is the raw kurtosis.

   •   A positive excess kurtosis indicates heavy tails, while negative excess kurtosis
       indicates light tails.

Summary: To summarize, kurtosis is a fundamental statistical parameter that
complements measures of central tendency and dispersion. It provides insight into the
shape of the probability curve by highlighting the concentration of data around the
mean and the weight of the tails. Understanding this concept is vital for interpreting
data in engineering and scientific contexts where extreme events can have significant
impacts. By calculating and interpreting kurtosis, students can better assess the
reliability of statistical models and the likelihood of rare but impactful events.

6. Mathematical Definition and Calculation

Mathematically, kurtosis is defined as the fourth standardized moment of a distribution.
It is derived from the central moments, which are moments calculated about the mean
rather than zero. The formula for the population kurtosis involves the fourth central
moment divided by the square of the variance. This calculation is rigorous and requires
a solid grasp of moments, which are the foundation of this chapter. In practice, we often
use the sample kurtosis, which includes a correction factor to provide an unbiased
estimate. The relationship between the raw moments and central moments is crucial
here, as kurtosis depends entirely on the fourth central moment. This section connects
directly to Course Outcome CO1 by explaining the definition and significance of
kurtosis in a data distribution.
```

## Page 129

```
   •   The formula for population kurtosis is , where is the fourth central moment
       and is the variance.

   •   The fourth central moment is calculated as .

   •   Sample kurtosis is often denoted as and is calculated using the formula
       fracn(n+1)(n-1)(n-2)(n-3) sum frac(x_i - barx)^4s^4 - frac3(n-1)^2(n-2)(n-3).

   •   Excess kurtosis is defined as .

   •   For a normal distribution, , resulting in a kurtosis of 3 and excess kurtosis of 0.

Summary: This section emphasizes the mathematical rigor required to compute
kurtosis accurately. Students must understand that the fourth power in the numerator
makes the measure highly sensitive to extreme deviations from the mean. This
sensitivity is why kurtosis is a powerful tool for detecting outliers. The distinction
between population and sample kurtosis is also important for statistical inference. By
mastering these formulas, students can apply them to real-world data analysis
problems found in engineering mathematics.

7. Classification of Distributions: Leptokurtic, Mesokurtic, and Platykurtic

Based on the value of the kurtosis coefficient, distributions are classified into three
main types: leptokurtic, mesokurtic, and platykurtic. This classification is fundamental
for describing the shape of a probability curve and understanding the nature of the data.
A mesokurtic distribution has a kurtosis of 3, matching the normal distribution,
indicating a standard peak and tail weight. A leptokurtic distribution has a kurtosis
greater than 3, characterized by a sharper peak and heavier tails, suggesting a higher
risk of extreme values. Conversely, a platykurtic distribution has a kurtosis less than 3,
showing a flatter peak and lighter tails. This classification helps in selecting appropriate
statistical tests and models for specific datasets.

   •   Mesokurtic distributions have a kurtosis value of 3, identical to the normal
       distribution.

   •   Leptokurtic distributions have a kurtosis value greater than 3, indicating heavy
       tails and a high peak.

   •   Platykurtic distributions have a kurtosis value less than 3, indicating light tails
       and a low peak.

   •   Excess kurtosis values are 0 for mesokurtic, positive for leptokurtic, and negative
       for platykurtic.

   •   Visual inspection of histograms can help identify these shapes before
       calculating the exact coefficient.
```

## Page 130

```
Summary: Understanding these classifications allows students to interpret data
distributions effectively. For instance, financial data often exhibits leptokurtic
properties, meaning extreme market crashes are more likely than a normal distribution
would predict. In contrast, some uniform distributions are platykurtic. Recognizing
these patterns is essential for risk management and quality control in engineering. This
knowledge directly supports Course Outcome CO3, enabling students to classify
distributions accurately based on their calculated kurtosis values.

8. Real-Life Applications and Engineering Context

Kurtosis is not just a theoretical concept but has profound applications in various
engineering fields. In quality control, monitoring the kurtosis of manufacturing
dimensions can help detect the presence of defective parts that deviate significantly
from the mean. In finance, kurtosis is used to model asset returns, where high kurtosis
indicates a higher probability of extreme market movements, crucial for portfolio risk
assessment. In signal processing, kurtosis helps in detecting impulsive noise or
anomalies in sensor data. For example, a vibration signal from a bearing might show a
sudden spike in kurtosis, indicating the onset of a fault. These applications demonstrate
the practical relevance of kurtosis in analyzing real-world phenomena.

   •   In finance, high kurtosis in stock returns suggests a higher risk of extreme losses
       or gains.

   •   In manufacturing, kurtosis analysis helps identify outliers in production
       processes that could lead to defects.

   •   In signal processing, kurtosis is used to detect non-Gaussian noise in
       communication systems.

   •   In hydrology, kurtosis helps model flood events, where extreme rainfall is more
       frequent than a normal distribution suggests.

   •   In reliability engineering, kurtosis of failure × can indicate the presence of wear-
       out mechanisms or random failures.

Summary: These examples illustrate how kurtosis bridges the gap between abstract
mathematical concepts and tangible engineering problems. By analyzing the shape of
distributions, engineers can make informed decisions about system design, risk
mitigation, and process improvement. The ability to distinguish between different types
of distributions empowers students to choose the right statistical tools for their specific
applications. This practical understanding reinforces the learning outcomes by showing
how theoretical knowledge translates into professional competence.

▶ Concept Video
```

## Page 131

```
Lecture 36 : Moments - Skewness and Kurtosis
IIT KANPUR-NPTEL 43:44

   Real-Life Applications

   1. Income Distribution Analysis: Economists use skewness to analyze national
      income data, which is almost always positively skewed, indicating that a few
      high earners pull the average income up significantly.

   2. Financial Risk Management: Investors analyze the skewness of asset returns;
      positive skewness is often preferred as it suggests the potential for large gains
      outweighs the risk of large losses.

   3. Quality Control in Manufacturing: Engineers check the skewness of product
      dimensions to ensure the production process is centered and not drifting
      towards producing defective items on one side of the specification.

   4. Healthcare Data Analysis: Medical researchers study the skewness of patient
      recovery × or disease prevalence to understand if extreme cases are common or
      rare in a specific population.

   5. Financial Risk Management: Analyzing stock market returns where leptokurtic
      distributions indicate a higher likelihood of extreme market crashes or booms
      compared to a normal distribution.

   6. Quality Control in Manufacturing: Using kurtosis to detect outliers in production
      data, ensuring that the manufacturing process remains stable and does not
      produce defective items with extreme dimensions.

   7. Signal Processing and Noise Detection: Identifying impulsive noise in audio or
      communication signals by observing a sudden increase in the kurtosis of the
      signal's amplitude distribution.

   8. Hydrological Engineering: Modeling extreme rainfall events and flood risks,
      where platykurtic or leptokurtic distributions help predict the frequency of rare
      but severe weather events.

   References & Suggestive Readings

Textbooks

   •   Higher Engineering Mathematics by H. K Dass. (3rd revised edition ed. S. Chand
       Publishers 2014)

   •   Higher Engineering Mathematics by B. S. Grewal (42th ed. ed. Khanna Publishers
       2013)
```

## Page 132

```
   •   Advanced Engineering Mathematics by R.K. Jain, and S.R.K. Iyengar (3rd Edition
       ed. Narosa Publishing House 2004)

Reference Books

   •   Advanced Engineering Mathematics by B.V. Ramana — ed. McGraw Hill 2006

   •   Statistical methods by S. P. Gupta — ed. S Chand & Sons 2017

   •   A textbook of Engineering Mathematics by N.P. Bali and Manish Goyal — Ninth
       edition ed. Laxmi Publications 2010

   Summary — Key Takeaways

   •   Skewness measures the asymmetry of a distribution around its mean.

   •   Positive skewness indicates a longer right tail, while negative skewness indicates
       a longer left tail.

   •   Pearson's moment coefficient and Bowley's quartile coefficient are standard
       measures.

   •   Real-world data like income and stock returns often exhibit significant skewness.

   •   Kurtosis measures the 'tailedness' and peakedness of a distribution, distinct
       from skewness which measures asymmetry.

   •   The standard normal distribution is mesokurtic with a kurtosis of 3, serving as
       the reference point for all other distributions.

   •   Leptokurtic distributions have heavy tails and a sharp peak, while platykurtic
       distributions have light tails and a flat peak.

   •   Excess kurtosis simplifies comparison by setting the normal distribution's value
       to 0, making positive values indicate heavy tails and negative values indicate
       light tails.

   Check Your Understanding

   1. Define skewness and explain its significance in describing the shape of a
      distribution. LO1

   2. Explain how the sign of the skewness coefficient indicates the direction of
      asymmetry in data. LO2

   3. Identify the main components of Pearson's moment coefficient of skewness
      formula. LO3

   4. Analyze the relationship between the mean, median, and mode in a positively
      skewed distribution. LO4
```

## Page 133

```
   5. Define kurtosis and explain its significance in analyzing the shape of a probability
      distribution. LO1

   6. Describe how the value of kurtosis affects the height of the peak and the weight
      of the tails in a probability curve. LO2

   7. Classify a given dataset as leptokurtic, mesokurtic, or platykurtic based on its
      calculated kurtosis value. LO3

   8. Analyze the relationship between excess kurtosis and the standard normal
      distribution, explaining why the value 3 is subtracted. LO3

Generated by AI Lesson Builder — Chandigarh University

Last modified: Tuesday, 7 July 2026, 4:18 PM

Previous activity

Jump to...
```

## Page 134

```
                                      Lecture 3.6
CO1: To understand fundamental concepts of probability theory and statistics.

CO2: Identify and formulate engineering problems in different situations involving
probabilistic and statistical measures.




     CONTINUOUS PROBABILITY DISTRIBUTIONS

Let us now consider a situation, where the variable of interest may take any value

within a given range. Suppose that we are planning to release water for

hydropower generation and irrigation. Depending on how much water we have

in the reservoir, viz., whether it is above or below the ‘normal’ level, we decide

on the quantity of water and time of its release. The variable indicating the

difference between the actual level and the normal level of water in the reservoir,

can take positive or negative values, integer or otherwise. Moreover, this value is

contingent upon the inflow to the reservoir, which in turn is uncertain. This type

of random variable which can take an infinite number of values is called a

continuous random variable, and the probability distribution of such a variable is

called a continuous probability distribution.

Now we present one important probability density function (p.d.f), viz., the

normal distribution.
```

## Page 135

```
Normal Distribution

The normal distribution is the most versatile of all the continuous probability

distributions. It is useful in statistical inferences, in characterising uncertainties

in many real life situations, and in approximating other probability distributions.

As stated earlier, the normal distribution is suitable for dealing with variables

whose magnitudes are continuous. Many statistical data concerning business

problems are displayed in the form of normal distribution. Height, weight and

dimensions of a product are some of the continuous random variables which are

found to be normally distributed. This knowledge helps us in calculating the

probability of different events in varied situations, which in turn is useful for

decision-making. To define a particular normal probability distribution, we need

only two parameters i.e., the mean (µ) and standard deviation (σ).

Now we turn to examine the characteristics of normal distribution with the help

of the figure, and explain the methods of calculating the probability of different

events using the distribution.
```

## Page 136

```
              Figure: Frequency Curve for the Normal Probability Distribution


Characteristics of Normal Distribution

1) The curve has a single peak, thus it is unimodal i.e., it has only one mode and

   has a bellshape.

2) Because of the symmetry of the normal probability distribution (skewness =

   0), the median and the mode of the distribution are also at the centre. Thus,

   for a normal curve, the mean, median and mode are the same value.

3) The two tails of the normal probability distribution extend indefinitely but

   never touch the horizontal axis.




Areas Under the Normal Curve

The area under the normal curve gives us the proportion of the cases falling

between two numbers or the probability of getting a value between two numbers.
```

## Page 137

```
Irrespective of the value of mean (µ) and standard deviation (σ), for a normal

distribution, the total area under the curve is 1.00. The area under the normal

curve is approximately distributed by its standard deviation as follows:

µ ± 1σ    covers 68% area, i.e., 34.13% area will lie on either side of µ.

µ ± 2σ    covers 95.5% area, i.e., 47.75% will lie on either side of µ.

µσ ± 3σ   covers 99.7% area, i.e., 49.85% will lie on either side of µ.




Using the Standard Normal Table

The areas under the normal curve are shown in the Appendix Table-3 at the end

of this block. To use the standard normal table to find normal probability values,

we follow two steps. They are:

Step 1: Convert the normal distribution to a standard normal distribution. The

standard random variable Z, can be computed as follows:

                                         !"#
                                    𝑍=         .
                                          $


Where,

X = Value of the random variable with which we are concerned.

µ = mean of the distribution of this random variable
```

## Page 138

```
σ = standard deviation of this distribution.

Z = Number of standard deviations from X to the mean of this distribution.

Step 2: Look up the probability of z value from the Appendix Table-3, given at

the end of this block, of normal curve areas. This Table is set up to provide the

area under the curve to any specified value of Z. (The area under the normal curve

is equal to 1. The curve is also called the standard probability curve).

Let us consider the following illustration to understand as to how the table should

be consulted in order to find the area under the normal curve.




Illustration 8

(a) Find the area under the normal curve for Z = 1.54.

Solution: Consulting the Appendix Table-3 given at the end of this block, we find

the entry corresponding to Z = 1.54 the area is 0.4382 and this measures the

Shaded area between Z = 0 and Z = 1.54 as shown in the following figure.
```

## Page 139

```
(b) Find the area under normal curve for Z = -1.46

Solution: Since the curve is symmetrical, we can obtain the area between z =

ñ1.46 and Z = 0 by considering the area corresponding to Z = 1.46. Hence, when

we look at Z of 1.46 in Appendix Table-3 given at the end of this block, we see

the probability value of 0.4279. This value is also the probability value of Z =

ñ1.46 which must be shaded on the left of the µ as shown in the following figure.




(c) Find the area to the right of Z = 0.25
```

## Page 140

```
Solution: If we look up Z = 0.25 in Appendix table, we find the probable area of

0.0987. Subtract 0.0987 (for Z = 0.25) from 0.5 getting 0.4013 (.5 - .0987 =

0.4013).




d) Find the area to the left of Z = 1.83.

Solution: If we are interested in finding the area to the left of Z (positive value),

we add 0.5000 to the table value given for Z. Here, the table value for Z (1.83) =

0.4664. Therefore, the total area to the left of Z = 0.9664 (0.5000 + 0.4664) i.e.,

equal to the shaded area as shown below:
```

## Page 141

```
Now let us take up some illustrations to understand the application of normal

probability distribution.

Illustration 9

Assume the mean height of soldiers to be 68.22 inches with a variance of 10.8

inches. How many soldiers in a regiment of 1,000 would you expect to be over

six feet tall?

                   !" &
Solution: 𝑍 =
                    $


X = 72 inches; µ = 68.22 inches; and σ = √10.8 = 3.286

       '(" )*.((
∴𝑍 =               = 1.15
         ,.(*)


for Z = 1.15 the area is .3749 (Appendix Table-3).
```

## Page 142

```
Area to the right of the ordinate at 1.16 from the normal table is (0.5 - 0.3749) =

0.1251. Hence, the probability of getting soldiers above six feet is 0.1251 and out

of 1,000 soliders, the expectation is 1,000 × 0.1251 = 125.1 or 125. Thus, the

expected number of soldiers over six feet tall is 125.

Illustration 10

   (a) 15,000 students appeared for an examination. The mean marks were 49

       and the standard deviation of marks was 6. Assuming the marks to be

       normally distributed, what proportion of students scored more than 55

       marks?
```

## Page 143

```
(b) If in the same examination, Grade ‘A’ is to be given to students scoring

   more than 70 marks, what proportion of students will receive grade ‘A’?




   Illustration 11
```

## Page 144

```
          In a training programme (self-administered) to develop marketing skills of

          marketing personnel of a company, the participants indicate that the mean

          time on the programme is 500 hours and that this normally distributed

          random variable has a standard deviation of 100 hours. Find out the

          probability that a participant selected at random will take:

          i)    fewer than 570 hours to complete the programme, and

          ii)   between 430 and 580 hours to complete the programme.

          Solution:

(i)   To get the Z value for the probability that a candidate selected at random

      will take fewer than 570 hours, we have
                      !" &  -'."-.. '.
                𝑍=     $
                           = /.. = /.. = 0.7


 Consulting the Appendix Table-3 for a Z value of 0.7, we find a probability of

 0.2580 (this probability will lie between the mean, 500 hours and 570 hours. As

 explained in illustration 8(d), we must add 0.5 to this probability (0.2580) that the

 random variable will be between the left-hand tail and the mean.

 Therefore, we obtain the probability that the random variable will lie between the

 left-hand tail and 570 hours is 0.7580 (0.5 + 0.2580). This situation is shown

 below:
```

## Page 145

```
Thus, the probability of a participant taking less than 570 hours to complete the

programme, is marginally higher than 75 per cent.

(ii)   In order to get the probability, of a participant chosen at random, that he

       will take between 430 and 580 hours to complete the programme, we must,

       first, compute the Z value for 430 and 580 hours.

                                           𝑋− µ
                                      𝑍=
                                            𝜎

                                     430 − 500 −70
                       𝑍 𝑓𝑜𝑟 430 =            =     = −0.7
                                        100     100

                                     580 − 500 −80
                       𝑍 𝑓𝑜𝑟 580 =            =     = −0.8
                                        100     100

       The table shows the probability values of Z values of -0.7 and 0.8 are

       0.2580 and 0.2881 respectively. This situation is shown in the following

       figure.
```

## Page 146

```
Thus, the probability that the random variables lie between 430 and 580

hours is 0.5461 (0.2580 + 0.2881).




Importance and Application of Normal Distribution

This distribution was initially discovered for studying the random errors in

measurements, which are encountered during the calculations of orbits of

heavenly bodies. It happens because of the fact that the normal distribution

follows the basic principle of errors. It is mainly for this quality that the

distribution has a wide range of applications in the theory of statistics. To

count a few:

Industrial quality control

   • Testing of significance
```

## Page 147

```
           • Sampling distribution of various statistics

           • Graduation of non-normal curve

           • length of the leaves observed at particular times of the year.

The main purpose for using a normal distribution are:

   (i)     To fill a distribution of measurement for same sample data,

   (ii)    To approximate the distributions like Binomial, Poisson etc.

   (iii)   To fit sampling distribution of various statistics like mean or variance

           etc.
```

## Page 148

```
Practice Questions

1. Given a standardized normal distribution area between the mean and positive

   value of Z as in Appendix Table 2) what is the probability that:

a) Z is less than +1.08?

b) Z is greater than ñ 0.21?

c) Z is between the mean and +1.08?

d) Z is less than ñ 0.27 the mean and greater than +1.06?

e) Z is between ñ 0.21 and the mean?

2. Give a normal distribution with µ = 100 and σ = 10, what is the probability

   that:

a) X > 75?

b) X < 70?

c) X > 112?

d) 75 < X > 85?

e) X < 80 or X > 110?




       TEXT BOOKS

   •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

       edition.2014.
```

## Page 149

```
   •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

       ed.2013, New Delhi.

   •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

       Publications, Reprint 2008.




       REFERENCE BOOKS

   •   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

       Narosa Publishing House ,2004,New Delhi.

   •   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New

       Delhi.

   •   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281In

       siders’Guide



       Video Lecture :

h$ps://www.youtube.com/watch?v=c06FZ2Yq9rk
```

## Page 150

```
                                      Lecture 3.5
CO1: To understand fundamental concepts of probability theory and statistics.

CO2: Identify and formulate engineering problems in different situations involving
probabilistic and statistical measures.




        DISCRETE PROBABILITY DISTRIBUTIONS

Poisson Distribution

Poisson distribution, developed by a French mathematician Simeon Poisson, is

so known by his name. It deals with counting the number of occurrences of a

particular event in a specific time interval or region of space. It is used in

practice where there are infrequently occurring events with respect to time,

volume (similar units), area, etc. For instance, the number of deaths or accidents

occurring in a specific time, the number of defects in production, the number of

workers absent per day etc. The binomial distribution, as discussed above, is

determined by two parameters ‘p’ and ‘n’. In a number of cases ‘p’ (the

probability of success) may happen to be very small (even less than 0.01) and the

‘n’ (the no. of trials) is large enough (like more than 50) so that their product ‘np’

remains a constant, the situation is termed as ‘Poisson Distribution’, and it gives

an approximation for binomial probability distribution formula, i.e.,

                                       P(r) = nCr pr qn-r
```

## Page 151

```
The Poisson distribution process corresponds to a Bernoulli process with a very

large number of trials (n) and a very low probability of success. This would

comparatively be simpler in dealing with and is given by the Poisson distribution

formula as follows:

                                           𝑚! 𝑒 "#
                                  𝑃 (𝑟 ) =
                                             𝑟!

where, p (r) = Probability of successes desired

r = 0, 1, 2, 3, 4, …, ∞ (any positive integer)

e = a constant with value: 2.7183 (the base of natural logarithms)

m = The mean of the Poisson Distribution, i.e., np or the average number of

occurrences of an event.

Characteristics of the Poisson Distribution

   a. It is also a discrete probability distribution and it is the limiting form of the

      binomial distribution.

   b. The range of the random variable is 0 ≤ r < ∞

   c. It consists of a single parameter ‘m’ only. So, the entire distribution can be

      obtained by knowing this value only.

   d. It is a positively skewed distribution. The skewness, therefore, decreases

      when ‘m’ increases.
```

## Page 152

```
Measures of Central Tendency and Dispersion for Poisson Distribution

In poisson distribution, the mean (m) and the variance (s2) represent the same

value, i.e.,

Mean = variance = np = m


S.D. (σ) = Variance = )𝑛𝑝


Let us consider the following illustrations to understand the application of the

poisson distribution.




Illustration 5

2% of the electronic toys produced in a certain manufacturing process turnout

to be defective. What is the probability that a shipment of 200 toys will contain

exactly 5 defectives? Also find the mean and standard deviation.

Solution:

In the given illustration n = 200;

Probabiliity of a defective toy (P) =2/100

Since, n is large and p is small, the poisson distribution is applicable. Apply

the formula:
```

## Page 153

```
                                                𝑚! 𝑒 "#
                                     𝑃 (𝑟 ) =
                                                  𝑟!

The probability of 5 defective pieces in 200 toys is given by:

                                              𝑚$ 𝑒 "#
                                     𝑃 (5 ) =
                                                5!

where

m = np = 200 × 0.02 = 4;

e = 2.7183 (constant)

                                      $
          %! ('.)*+,)"#   (*/'%)0          1
                                 (&.($)*)#
∴ 𝑃 (5) =               =
           $∗%∗,∗'∗*            *'/


                                     (1024)(0.0183)
                          𝑃 ( 5) =                  = 0.156
                                          120

Mean = np = 200 × 0.02 = 4; σ = )𝑛𝑝 = √4 = 2.




Illustration 6

Find the probability of exactly 4 defective tools in a sample of 30 tools chosen at

random by a certain tool producing firm by using

i) Binomial distribution and

ii) Poisson distribution.
```

## Page 154

```
The probability of defects in each tool is given to be 0.02.




Solution:

i)      When binomial distribution is used, the probability of 4 defectives in 30

        tools is given by:

         P (4) = 30C4 (0.02)4 (0.98)26

                = 27405 × 0.00000016 × 0.59 = 0.00259

ii)     When poisson distribution is used, the probability of 4 defectives in 30

        tools is given by:

                                                         𝑚% 𝑒 "#
                                                 𝑃 (4) =
                                                           4!

where

m = np = 30 × 0.02 = 0.6;

e = 2.7183 (constant)

            (/.2)& ('.)*+,)",.-       /.$%+$ ∗ /.*'42
∴ 𝑃 (4) =                         =                     = 0.00296
                 %∗,∗'∗*                    '%
```

## Page 155

```
Fitting of a Poisson Distribution

To fit a poisson distribution to a given observed data (frequency distribution), the

procedure is as follows:

1. We must obtain the value of its mean i.e., m = np

2. The probabilities of various values of the random variables (r) are to be

   computed by using p.m.f. i.e.,

                                            𝑚! 𝑒 "#
                                    𝑃 (𝑟) =
                                              𝑟!

3. Each probability so obtained in step 2 is then multiplied by N (the total

   frequency) to get expected frequencies.

Let us consider an illustration to understand for fitting poisson distribution.

Illustration 7

The number of defects per unit in a sample of 330 units of manufactured product

was found as follows:




Fit a poisson distribution to the above given data.
```

## Page 156

```
Solution: The mean of the given frequency distribution is:

       (0 ∗ 214) + (1 ∗ 92) + (2 ∗ 20) + (3 ∗ 3) + (4 ∗ 1) 145
  𝑚=                                                      =     = 0.439
                    214 + 92 + 20 + 3 + 1                   330

We can write

                                        0.439! 𝑒 "/.%,4
                               𝑃 (𝑟 ) =
                                             𝑟!

Substituting r = 0, 1, 2, 3, and 4, we get the probabilities for various values of r,

as shown below:
```

## Page 157

```
Practice Questions

1. What are the features of binomial and poisson distributions?

2. Suppose on an average 2% of electric bulbs manufactured by a company are

   defective. If they produce 100 bulbs in a day, what is the probability that 4

   bulbs will have defects on that day?

3. Four hundred car air-conditioners are inspected as they come off the

   production line and the number of defects per set is recorded below. Find the

   expected frequencies by assuming the poisson model.

   No. of defects:           0       1      2       3       4     5

   No. of ACs:             142       156    69      27       5     1




       TEXT BOOKS

   •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

       edition.2014.

   •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

       ed.2013, New Delhi.

   •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

       Publications, Reprint 2008.
```

## Page 158

```
       REFERENCE BOOKS

   •   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

       Narosa Publishing House ,2004,New Delhi.

   •   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New

       Delhi.

   •   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281In

       siders’Guide



       Video Lecture :

h#ps://www.youtube.com/watch?v=c06FZ2Yq9rk
```

## Page 159

```
                                      Lecture 3.4
CO1: To understand fundamental concepts of probability theory and statistics.

CO2: Identify and formulate engineering problems in different situations involving
probabilistic and statistical measures.




        DISCRETE PROBABILITY DISTRIBUTIONS

All possible values of a discrete random variable together with their probabilities

of occurrence. It is called a discrete probability distribution. There are two kinds

of distributions in the discrete probability distribution.

i) Binomial Distribution, and

(ii) Poisson Distribution.

Let us discuss these two distributions in detail

Binomial Distribution

It is the basic and the most common probability distribution. It has been used to

describe a wide variety of processes in business. For example, a quality control

manager wants to know the probability of obtaining defective products in a

random sample of 10 products. If 10 per cent of the products are defective, he/

she can quickly obtain the answer, from tables of the binomial probability
```

## Page 160

```
distributions. It is also known as Bernoulli Distribution, as it was originated by

Swiss Mathematician James Bernoulli (1654-1705).

The binomial distribution describes discrete, not continuous, data resulting from

an experiment known as Bernoulli Process. Binomial distribution is a probability

distribution expressing the probability of one set of dichotomous alternatives, i.e.,

success or failure.

As per this distribution, the probability of getting 0, 1, 2, …, n heads (or tails) in

n tosses of an unbiased coin will be given by the successive terms of the

expansion of (q + p)n , where p is the probability of success (heads) and q is the

probability of failure (i.e. = 1- p).

Binomial law of probability distribution is applicable only when:

a) A trial results in either success or failure of an event.

b) The probability of success ëpí remains constant in each trial.

c) The trials are mutually independent i.e., the outcome of any trial is neither

affected by others nor affects others.

Assumptions

i) Each trial has only two possible outcomes either Yes or No, success or failure,

etc.
```

## Page 161

```
ii) Regardless of how many times the experiment is performed, the probability of

the outcome, each time, remains the same.

iii) The trials are statistically independent.

iv) The number of trials is known and is 1, 2, 3, 4, 5, etc.

Binomial Probability Formula:

                                   P(r) = nCr pr qn-r

where, P (r) = Probability of r successes in n trials;

p = Probability of success;

q = Probability of failure = 1 - p;

r = No. of successes desired; and

n = No. of trials undertaken

The determining equation for nCr can easily be written as:

n       !!
Cr = #!(!%#)!


n! can be simplified as follows:

n! = n (n-1)! = n (n-1) (n-2) ! = n (n-1) (n-2) (n-3) ! and so on.
```

## Page 162

```
Hence the following form of the equations, for carrying out computations of the

binomial probability is perhaps more convenient.

                                               𝑛!
                                𝑃(𝑟) =                𝑝# 𝑞 !%#
                                          𝑟! (𝑛 − 𝑟)!

The symbol ! means factorial, which is computed as follows: 5! means 5 × 4 × 3

× 2 × 1 = 120. Mathematicians define 0! as 1.

If n is large in number, say, 50C3, then we can write (with the help of the above

explanation)

              '(!       '(∗+,∗+-∗+.!   '(∗+,∗+-
50
     C3 = )!('(%))! =       )!+.!
                                     =  )∗/∗0


Similarly

               .'!      .'∗.+∗.)∗./∗.0∗.(!   .'∗.+∗.)∗./∗.0∗.(!
75
     C5 =             =                    =                    , 𝑎𝑛𝑑 𝑠𝑜 𝑜𝑛.
            '!(.'%')!         '!∗.(!             '∗+∗)∗/∗0


Characteristics of a Binomial Distribution

i)          The form of the distribution depends upon the parameters ‘p’ and ‘n’.

ii)         The probability that there are ‘r’ successes in ‘n’ no. of trials is given by

                                                       !!
                                 P(r) = nCr pr qn-r= #!(!%#)! 𝑝# 𝑞 !%#

iii)        It is mainly applied when the population being sampled is infinite.
```

## Page 163

```
iv)   It can also be applied to a finite population, if it is not very small or the

      units sampled are replaced before the next trial is attempted. The point

      worth noting is ‘p’ should remain unchanged.

Let us consider the following illustration to understand the application of

binomial distribution.

Illustration 1

A fair coin is tossed six times. What is the probability of obtaining four or more

heads?

Solution: When a fair coin is tossed, the probabilities of head and tail in case of
an unbiased coin are equal, i.e.,
```

## Page 166

```
Measures of Central Tendency and Dispersion for the Binomial Distribution

As discussed in the Introduction, the binomial distribution has expected values

of mean (µ) and a standard deviation (σ). We now see the computation of both

these statistical measures.

We can represent the mean of the binomial distribution as :

Mean (µ) = np.

where, n = Number of trials; p = probability of success

And, we can calculate the standard deviation by :
```

## Page 167

```
σ = 2𝑛𝑝𝑞


where, n = Number of trials; p = probability of success; and q = probability of

failure = 1 - p

Illustration 3

If the probability of defective bolts is 0.1, find the mean and standard deviation

for the distribution of defective bolts in a total of 50.

Solution: P = 0.1, n = 500

∴ Hence (µ) = np = 500 × 0.1 = 50

Thus, we can expect 50 bolts to be defective.


Standard Deviation (σ) = 2𝑛𝑝𝑞


n = 500, p = 0.1, q = 1 - p = 1 - 0.1 = 0.9

∴ σ = 500 × .1× .9 = 6.71

Fitting a Binomial Distribution

When a binomial distribution is to be fitted to observed data, the following

procedure is adopted:

i)     Determine the values of ‘p’ and ‘q’. If one of these values is known, the

       other can be found out by the simple relationship p = 1- q and q = 1- p. If
```

## Page 168

```
       p and q are equal, we can say, the distribution is symmetrical. On the other

       hand if p’ and ‘q’ are not equal, the distribution is skewed. The distribution

       is positively skewed, in case ‘p’ is less than 0.5, otherwise it is negatively

       skewed.

ii)    Expand the binomial (p + q)n . The power ‘n’ is equal to one less than the

       number of terms in the expanded binomial. For example, if 3 coins are

       tossed (n = 3) there will be four terms, when 5 coins are tossed (n = 5) there

       will be 6 terms, and so on.

iii)   Multiply each term of the expanded binomial by N (the total frequency), in

       order to obtain the expected frequency in each category.

Let us consider an illustration for fitting a binomial distribution.

Illustration 4

Eight coins are tossed at a time 256 times. Number of heads observed at each

throw is recorded and the results are given below. Find the expected frequencies.

What are the theoretical values of mean and standard deviation? Also calculate

the mean and standard deviation of the observed frequencies
```

## Page 170

```
If we compare the above expected frequencies with the observed frequencies,

given in the illustration, we find that the two frequencies are in close agreement.

This provides the basis to conclude that the observed distribution will fits the

expected distribution.

The mean of the above distribution is:

µ = np = 8×1/2 =4


                                               0      0
The Standard Deviation is (σ) = 2𝑛𝑝𝑞 =48 ∗ ∗ = √2 = 1.414
                                               /      /



If we compute the mean and standard deviation of the observed frequencies, we

will obtain the following values

𝑋< = 4.062; S.D. = 1.462.

Practice Questions:

• Determine the following by using binomial probability formula.

     a) If n = 4 and P = 0.12, then what is P (0) ?

     b) If n = 10 and P = 0.40, then what is p (9) ?

      c) If n = 6 and P = 0.83, then what is P (5)?

• The following data shows the result of the experiment of throwing 5 coins at

   a time 3,100 times and the number of heads appearing in each throw. Find the
```

## Page 171

```
expected frequencies and comment on the results. Also calculate mean and

standard deviation of the theoretical values.

No. of heads:         0      1      2        3        4      5

frequency:            32    225    710    1,085     820     228



    TEXT BOOKS

•   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

    edition.2014.

•   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

    ed.2013, New Delhi.

•   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

    Publications, Reprint 2008.




    REFERENCE BOOKS

•   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

    Narosa Publishing House ,2004,New Delhi.

•   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New

    Delhi.

•   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281In

    siders’Guide



    Video Lecture :
```

## Page 172

```
h#ps://www.youtube.com/watch?v=c06FZ2Yq9rk
```

## Page 173

```
                                     Lecture 3.3
CO2: Identify and formulate engineering problems in different situations involving
probabilistic and statistical measures.


                               Random Variables


Study related to performing the random experiments and computation of
probabilities for events (subsets of sample space) have been made in detail in the
first four units of this course. In many experiments, we may be interested in a
numerical characteristic associated with outcomes of a random experiment. Like
the outcome, the value of such a numerical characteristic cannot be predicted in
advance.

For example, suppose a die is tossed twice and we are interested in number of
times an odd number appears. Let X be the number of appearances of odd number.
If a die is thrown twice, an odd number may appear ‘0’ times (i.e. we may have
even number both the times) or once (i.e. we may have odd number in one throw
and even number in the other throw) or twice (i.e. we may have odd number both
the times). Here, X can take the values 0, 1, 2 and is a variable quantity behaving
randomly and hence we may call it as ‘random variable’. Also notice that its
values are real and are defined on the sample space

{(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
(5, 1), (5, 2), (5, 3), (5, 4), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)}

i.e
```

## Page 174

```
             0, 𝑖𝑓 𝑡ℎ𝑒 𝑜𝑢𝑡𝑐𝑜𝑚𝑒 𝑖𝑠 (2,2 ), (2,4), (2,6), (4,2), (4,4), (4,6), (6,2), (6,4), (6,6)
    1, 𝑖𝑓 𝑡ℎ𝑒 𝑜𝑢𝑡𝑐𝑜𝑚𝑒 𝑖𝑠 (1,2), (1,4), (1,6), (2,1), (2,3), (2,5), (3,2), (3,4), (3,6) , (4,1), (4,3), (4,5),
 𝑋=#
                                  (5,2), (5,4), (5,6), (6,1), (6,3), (6,5)
            2, 𝑖𝑓 𝑡ℎ𝑒 𝑜𝑢𝑡 𝑜𝑚𝑒 𝑖𝑠 (1,1), (1,3), (1,5), (3,1), (3,3), (3,5), (5,1), (5,3), (5,5)

                       !     $                      $&     $                      !      $
So, 𝑃[𝑋 = 0] = "# = % , 𝑃[𝑋 = 1] = "# = ' , 𝑃[𝑋 = 2] = "# = %

                                                            $     $    $
And 𝑃 [𝑋 = 0] + 𝑃 [𝑋 = 1] + 𝑃[𝑋 = 2] = % + ' + % = 1

Observe that, a probability can be assigned to the event that X assumes a
particular value. It can also be observed that the sum of the probabilities
corresponding to different values of X is one.

So, a random variable can be defined as below:

Definition: A random variable is a real-valued function whose domain is a set of
possible outcomes of a random experiment and range is a sub-set of the set of real
numbers and has the following properties:

 I.      Each particular value of the random variable can be assigned some
         probability
II.      Uniting all the probabilities associated with all the different values of the
         random variable gives the value 1(unity).

      Remark 1: We shall denote random variables by capital letters like X, Y, Z,
      etc. and write r.v. for random variable

      DISCRETE RANDOM VARIABLE

      A random variable is said to be discrete if it has either a finite or a countable
      number of values. Countable number of values means the values which can be
      arranged in a sequence, i.e. the values which have one-to-one correspondence
      with the set of natural numbers, i.e. on the basis of three-four successive
      known terms, we can catch a rule and hence can write the subsequent terms.
```

## Page 175

```
For example suppose X is a random variable taking the values say 2, 5, 8, 11,
… then we can write the fifth, sixth, … values, because the values have one-
to-one correspondence with the set of natural numbers and have the general
term as 3n - 1 i.e. on taking n = 1, 2, 3, 4, 5, … we have 2, 5, 8, 11, 14,…. So,
X in this example is a discrete random variable. The number of students
present each day in a class during an academic session is an example of
discrete random variable as the number cannot take a fractional value.

Probability Function

Let X be a r.v. which takes the values 𝑥$ , 𝑥' , … 𝑎𝑛𝑑 𝑙𝑒𝑡 𝑃 [𝑋 = 𝑥( ] = 𝑝(𝑥𝑖).
This function 𝑝(𝑥( ), 𝑖 = 1,2, … defined for the values 𝑥$ , 𝑥' , … assumed by X
is called probability mass function of X satisfying 𝑝(𝑥( ) ≥ 0 and
∑( 𝑝(𝑥( ) = 1.

The set {(x$ , p(x$ )) , (x' , p(x' )), … } specifies the probability distribution of
a discrete r.v. X. Probability distribution of r.v. X can also be exhibited in the
following manner:

 X        𝑥$                 𝑥'            𝑥"          …
 P(X)     𝑝(𝑥$ )           𝑝(𝑥')         𝑝(𝑥" )        …



Now, let us take up some examples concerning probability mass function:
Example 1: State, giving reasons, which of the following are not probability
distributions:

(i)

                       X           0              1
```

## Page 176

```
                             P(X)     1                       3
                                      2                       4


(2)

                   X           0                    1                2
                   P(X)        "                    *$
                               %                     '
                                                                         ¾



(3)

                   X           0                    1                2
                   P(X)        $                    $
                                                                     ¼
                               %                    '




(4)

            X           0                  1              2                  3
            P(X)        $                  "
                                                          ¼                  1/8
                        &                  &




Solution:

(i) Here 𝑝(𝑥( ) ≥ 0, 𝑖 = 1,2; 𝑏𝑢𝑡
            '
                                                                         1 3 5
        B 𝑝(𝑥( ) = 𝑝(𝑥$ ) + 𝑝(𝑥' ) = 𝑝(0) + 𝑝(1) =                        + = >1
                                                                         2 4 4
        (+$

So,   the       given       distribution       is   not   a       probability      distribution   as
∑'(+$ 𝑝(𝑥( ) is greater than 1.

                                                                             $
(ii) It is not probability distribution as 𝑝(𝑥' ) = 𝑝(1) = − ' i.e. negative.
```

## Page 177

```
   (iii) Here 𝑝(𝑥( ) ≥ 0, 𝑖 = 1,2,3,4; 𝑏𝑢𝑡
    %

   B 𝑝(𝑥( ) = 𝑝(𝑥$ ) + 𝑝(𝑥' ) + 𝑝(𝑥" ) + 𝑝(𝑥% ) = 𝑝(1) + 𝑝(2) + 𝑝(3) + 𝑝(4)
   (+$
                     1 3 1 1 7
                 =    + + + = <1
                     8 8 4 8 8

   \The given distribution is not probability distribution.



CONTINUOUS RANDOM VARIABLE

we have defined the discrete random variable as a random variable having
countable number of values, i.e. whose values can be arranged in a sequence. But,
if a random variable is such that its values cannot be arranged in a sequence, it is
called continuous random variable. Temperature of a city at various points of time
during a day is an example of continuous random variable as the temperature
takes uncountable values, i.e. it can take fractional values also. So, a random
variable is said to be continuous if it can take all possible real (i.e. integer as well
as fractional) values between two certain limits. For example, let us denote the
variable, “Difference between the rainfall (in cm) of a city and that of another city
on every rainy day in a rainy reason”, by X, then X here is a continuous random
variable as it can take any real value between two certain limits. It can be noticed
that for a continuous random variable, the chance of occurrence of a particular
value of the variable is very small, so instead of specifying the probability of
taking a particular value by the variable, we specify the probability of its lying
within an interval. For example, chance that an athlete will finish a race in say
exactly 10 seconds is very-very small, i.e. almost zero as it is very rare to finish
the race in a fixed time. Here, the probability is specified for an interval, i.e. we
```

## Page 178

```
may be interested in finding as to what is the probability of finishing the race by
the athlete in an interval of say 10 to 12 seconds. So, continuous random variable
is represented by different representation known as probability density function
unlike the discrete random variable which is represented by probability mass
function.

Probability Density Function

Let f(x) be a continuous function of x . Suppose the shaded region ABCD shown
in the following figure represents the area bounded by y = f(x ), x -axis and the
ordinates at the points x and x + dx , where dx is the length of the interval ( x ,
x + dx ).

                                  AB           y=f(x)




                                  C D




Now, if dx is very-very small, then the curve AB will act as a line and hence
the shaded region will be a rectangle whose area will be AD X DC i.e. f(x)dx

[AD = the value of y at x i.e. f (x), DC = length dx of the interval ( x, x + dx )]

Also, this area = probability that X lies in the iterval (𝑥, 𝑥 + 𝑑𝑥)

                              = 𝑃 [𝑥 ≤ 𝑋 ≤ 𝑥 + 𝑑𝑥 ]

Hence,
```

## Page 179

```
                         𝑃 [𝑥 ≤ 𝑋 ≤ 𝑥 + 𝑑𝑥 ] = 𝑓(𝑥)𝑑𝑥

,[./0/ .12.]
             = 𝑓 (𝑥 ), where dx is very very small.
     2.

     ,[./0/ .12.]
lim               0 = 𝑓 (𝑥 ),
45→7      2.




f(x), so defined, is called probability density function.

Probability density function has the same properties as that of probability mass
function. So, 𝑓 (𝑥 ) ≥ 0 and sum of the probabilities of all possible values that
the random variable can take, has to be 1. But, here, as X is a continuous
random variable, the summation is made possible through ‘integration’ and
hence∫ 𝑓 (𝑥 )𝑑𝑥 = 1


where integral has been taken over the entire range R of values of X.
Remark 2

i)    Summation and integration have the same meanings but in mathematics
      there is still difference between the two and that is that the former is used
      in case of discrete values, i.e. countable values and the latter is used in
      continuous case.
ii)   An essential property of a continuous random variable is that there is zero
      probability that it takes any specified numerical value, but the probability
      that it takes a value in specified intervals is non-zero and is calculable as
      a definite integral of the probability density function of the random
      variable and hence the probability that a continuous r.v. X will lie between
      two values a and b is given by
```

## Page 180

```
                                                     8
                           𝑃[𝑎 < 𝑋 < 𝑏 ] = O 𝑓 (𝑥 )𝑑𝑥
                                                     9

Example 5: A continuous random variable X has the probability density
function:

f(x) = Ax3, 0 ≤ 𝑥 ≤ 1

Determine

(i) A       (ii) P [0.2 < X < 0.5]         (iii) P[X>3/4 given X>1/2]



Solution:

(i) As f( x ) is probability density function

                                       O 𝑓(𝑥)𝑑𝑥 = 1

                              $                  $
                            O 𝑓(𝑥)𝑑𝑥 = O 𝐴𝑥 " 𝑑𝑥 = 1
                             7               7

                             $                $
                         .!             $
                      𝐴 Q % R = 1 => 𝐴 Q% − 0R = 1 => 𝐴 = 4
                             7                7




(ii) P [0.2 < X < 0.5]=
             7.;                 7.;                     7.;
                                      𝑥%
            O 𝑓 (𝑥 )𝑑𝑥 = O 𝐴𝑥 𝑑𝑥 = 4 S T = [(0.5)% − (0.2)% ]
                                       "
             7.'          7.'         4 7.'

                          =0.0625-0.0016=0.0609



             "                $              "            $
(iii) 𝑃 Q𝑋 > %     𝑔𝑖𝑣𝑒𝑛 𝑋 > 'R = 𝑃 Q𝑋 > % Z𝑋 > 'R
```

## Page 181

```
                                          3       1
                                   𝑃 Q𝑋 > 4 ⋂ 𝑋 > 2R
                               =
                                                1
                                         𝑃 Q𝑋 > 2R



                                                3
                                         𝑃 Q𝑋 > 4R
                                    =
                                                1
                                         𝑃 Q𝑋 > 2R

              "       $              $                    " %          &$        $<;
Now, 𝑃 Q𝑋 > %R = ∫" 𝑓 (𝑥 )𝑑𝑥 = ∫" 4𝑥 " 𝑑𝑥 = (1)% − \%] = 1 − ';# = ';#
                     !              !


              $       $              $                   $ %       $        $;
Now, 𝑃 Q𝑋 > 'R = ∫# 𝑓 (𝑥 )𝑑𝑥 = ∫# 𝑥 " 𝑑𝑥 = (1)% − \%] = 1 − $# = $#
                     $              $




                                       3
                                𝑃 Q𝑋 > R 175 16    35    35
     𝑇ℎ𝑒 𝑟𝑒𝑞𝑢𝑖𝑟𝑒𝑑 𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦 =        4 =   ×  =      =
                                       1
                                𝑃 Q𝑋 > 2R 256 15 16 × 3 48



DISTRIBUTION FUNCTION

A function F defined for all values of a random variable X by 𝐹 (𝑥) = 𝑃[𝑋 £ 𝑥 ]
is called the distribution function. It is also known as the cumulative distribution
function (c.d.f.) of X since it is the cumulative probability of X up to and
including the value x. As X can take any real value, therefore the domain of the
distribution function is set of real numbers and as F(x) is a probability value,
therefore the range of the distribution function is [0, 1].

Remark 3: Here, X denotes the random variable and x represents a particular
value of random variable. F(x) may also be written as FX(x), which means that it
```

## Page 182

```
is a distribution function of random variable X.

Discrete Distribution Function

Distribution function of a discrete random variable is said to be discrete
distribution function or cumulative distribution function (c.d.f.). Let X be a
discrete random variable taking the values 𝑥$ , 𝑥' , 𝑥" , … with respective
probabilities 𝑝$ , 𝑝' , 𝑝" , …

 Then 𝐹 (𝑥𝑖 ) = 𝑃 [𝑋 ≤ 𝑥𝑖] = 𝑃[𝑋 = 𝑥$ ] + 𝑃[𝑋 = 𝑥' ] + … + 𝑃 [𝑋 = 𝑥( ]

                                        = 𝑝$ + 𝑝' + … + 𝑝( .

 The distribution function of X, in this case, is given as in the following table:


                         X                   𝐹 (𝑥 )
                         𝑥$                    𝑝$

                         𝑥'                 𝑝$ + 𝑝'

                         𝑥"              𝑝$ + 𝑝' + 𝑝"

                         𝑥%           𝑝$ + 𝑝' + 𝑝" + 𝑝%

                          .                     .
                          .                     .
                          .                     .




The value of F(x) corresponding to the last value of the random variable X is
always 1, as it is the sum of all the probabilities. F(x) remains 1 beyond this last
value of X also, as it being a probability can never exceed one.
```

## Page 183

```
For example, Let X be a random variable having the following probability
distribution:

                           X      0     1          2

                           p(x) 1       1          1



                                  4     2          4



Notice that p(x) will be zero for other values of X. Then, Distribution function
of X is given by

     X                         F(x) = P[X ≤ x ]

     0                                1/4

     1                          1/4 +1/2 =3/4

     2                         1/4 + ½ + ¼ = 1



Here, for the last value, i.e., for X = 2, we have F(x) = 1. Also, if we take a value
beyond 2 say 4, then we get

                          F(4) = P[X ≤ 4]
                                = P[X = 4] + P[X = 3] + P[X ≤ 2]

                                = 0 + 0 + 1 = 1.
```

## Page 184

```
Example 7: A random variable X has the following probability function:

 X           0     1        2        3         4       5        6        7

 P(x)        0     1/10     1/5      1/5       3/10    1/100    1/50     17/100



Determine the distribution function of X.

Solution: Here,

F(0) = P[X ≤ 0] = P[X = 0] = 0,

F(1) = P[X ≤ 1] = P[X = 0] + P [X = 1] = 0 + 1/10

F(2) = P[X ≤ 2] = P[X = 0] + P [X = 1] + [X = 2] = 0 + 1/10 + 1/5 = 3/10



and so on. Thus, the distribution function F(x) of X is given in the following
table:

         X                               F(x) = P[X<= x]
         0                                         0
         1                                     1/10
         2                                     3/10
         3                                 3/10+1/5=1/2
         4                                 1/2+3/10=4/5
         5                               4/5+1/100=81/100
         6                           81/100+1/50=83/100
         7                               83/100+17/100=1



Continuous Distribution Function
```

## Page 185

```
Distribution function of a continuous random variable is called the continuous
distribution function or cumulative distribution function (c.d.f.).

Let X be a continuous random variable having the probability density function
f(x), as defined in the last section of this unit, then the distribution function
F(x) is given by
                                                  .
                         𝐹 (𝑥) = 𝑃[𝑋 ≤ 𝑥 ] = O 𝑓 (𝑥 )𝑑𝑥
                                                 *=

Also in the last section, we have defined the p.d.f. f(x) as

                                     𝑃[𝑥 ≤ 𝑋 ≤ 𝑥 + 𝑑𝑥]
                       𝑓 (𝑥 ) = lim                    0
                                45→7        𝑑𝑥

                                 𝑃[𝑋 ≤ 𝑥 + 𝑑𝑥 ] − 𝑃[𝑋 ≤ 𝑥]
                   𝑓 (𝑥 ) = lim                            0
                            45→7           𝑑𝑥

                                       𝐹(𝑥 + 𝑑𝑥) − 𝐹(𝑥)
                        𝑓 (𝑥 ) = lim                    0
                                  45→7        𝑑𝑥

F(x)=Derivative of F(x) with respect to x

                                   𝑓 (𝑥 ) = 𝐹′(𝑥)

                                             𝑑
                                  𝑓 (𝑥 ) =      𝐹(𝑥)
                                             𝑑𝑥

                                   𝑑𝐹 (𝑥 ) = 𝑓(𝑥)

Here, 𝑑𝐹 (𝑥) is known as the probability differential.
                   .
So,      𝐹 (𝑥) = ∫*= 𝑓0 (𝑥)𝑑𝑥 and 𝐹 > (𝑥) = 𝑓(𝑥).
```

## Page 186

```
                 PROBABILITY DISTRIBUTIONS

INTRODUCTION

A probability distribution is essentially an extension of the theory of probability

which we have already discussed in the previous unit. This unit introduces the

concept of a probability distribution, and to show how the various basic

probability distributions (binomial, poisson, and normal) are constructed. All

these probability distributions have immensely useful applications and explain a

wide variety of business situations which call for computation of desired

probabilities.

By the theory of probability

P(H1) + P(H2) + …+ P(Hn) = 1

This means that the unity probability of a certain event is distributed over a set of

disjointed events making up a complete group. In general, a tabular recording of

the probabilities of all the possible outcomes that could result if random (chance)

experiment is done is called “Probability Distribution”. It is also termed as

theoretical frequency distribution.

Frequency Distribution and Probability Distribution
```

## Page 187

```
One gets a better idea about a probability distribution by comparing it with a

frequency distribution. It may be recalled that the frequency distributions are

based on observation and experimentation. For instance, we may study the profits

(during a particular period) of the firms in an industry and classify the data into

two columns with class intervals for profits in the first column, and corresponding

classify frequencies (No. of firms) in the second column.

The probability distribution is also a two-column presentation with the values of

the random variable in the first column, and the corresponding probabilities in the

second column. These distributions are obtained by expectations on the basis of

theoretical or past experience considerations. Thus, probability distributions are

related to theoretical or expected frequency distributions.

In the frequency distribution, the class frequencies add up to the total number of

observations (N), where as in the case of probability distribution the possible

outcomes (probabilities) add up to ‘one’. Like the former, a probability

distribution is also described by a curve and has its own mean, dispersion, and

skewness.

Let us consider an example of probability distribution. Suppose we toss a fair

coin twice, the possible outcomes are shown

                Possible Outcomes from Two-toss Experiment of a Fair Coin
```

## Page 188

```
Now we are interested in framing a probability distribution of the possible

outcomes of the number of Heads from the two-toss experiment of a fair coin. We

would begin by recording any result that did not contain a head, i.e., only the

fourth outcome. Next, those outcomes containing only one head, i.e., second and

third outcomes, and finally, we would record that the first outcome contains two

heads. We recorded the same in to highlight the number of heads contained in

each outcome.

  Probability Distribution of the Possible No. of Heads from Two-toss Experiment of a Fair Coin




We must note that the above tables are not the real outcome of tossing a fair coin

twice. But, it is a theoretical outcome, i.e., it represents the way in which we

expect our two-toss experiment of an un-biased coin to behave over time.
```

## Page 189

```
TYPES OF PROBABILITY DISTRIBUTION

Probability distributions are broadly classified under two heads:

(i) Discrete Probability Distribution, and

(ii) Continuous Probability Distribution.

i) Discrete Probability Distribution: The discrete probability is allowed to take

on only a limited number of values. Consider for example that the probability of

having your birthday in a given month is a discrete one, as one can have only 12

possible outcomes representing 12 months of a year.

ii) Continuous Probability Distribution: In a continuous probability

distribution, the variable of interest may take on any values within a given range.

Suppose we are planning to release water for hydropower generation. Depending

on how much water we have in the reservoir viz., whether it is above or below

the normal level, we decide on the amount and time of release. The variable

indicating the difference between the actual reservoir level and the normal level,

can take positive or negative values, integer or otherwise. Moreover, this value is

contingent upon the inflow to the reservoir, which in turn is uncertain. This type

of random variable which can take an infinite number of values is called a

continuous random variable, and the probability distribution of such a variable is

called a continuous probability distribution. Before we attempt discrete and
```

## Page 190

```
continuous probability distributions, the concept of random variable which is

central to the theme, needs to be elaborated.

CONCEPT OF RANDOM VARIABLES

A random variable is a variable (numerical quantity) that can take different values

as a result of the outcomes of a random experiment. When a random experiment

is carried out, the totality of outcomes of the experiment forms a set which is

known as sample space of the experiment. Similar to the probability distribution

function, a random variable may be discrete or continuous.

The example given in the Introduction; we have seen that the outcomes of the

experiment of two-toss of a fair coin were expressed in terms of the number of

heads. We found in the example, that H (head) can assume values of 0, 1 and 2

and corresponding to each value, a probability is associated. This uncertain real

variable H, which assumes different numerical values depending on the outcomes

of an experiment, and to each of whose value a possibility assignment can be

made, is known as a random variable. The resulting representation of all the

values with their probabilities is termed as the probability distribution of H.

It is customary to present the distribution as shown.

                         Probability Distribution of No. of Heads
```

## Page 191

```
In this case, as we find that H takes only discrete values, the variable H is called

a discrete random variable, and the resulting distribution is a discrete

probability distribution. The function that specifies the probability distribution

of a discrete random variable is called the probability mass function (p.m.f.).

In the above situations, we have seen that the random variable takes a limited

number of values. There are certain situations where the variable under

consideration may have infinite values. Consider for example, that we are

interested in ascertaining the probability distribution of the weight of one kg.

coffee packs. We have reasons to believe that the packing process is such that a

certain percentage of the packs slightly below one kg., and some packs are above

one kg. It is easy to see that it is essentially by chance that the pack will weigh

exactly 1 kg., and there are an infinite number of values that the random variable

‘weight’ can take. In such cases, it makes sense to talk of the probability that the

weight will be between two values, rather than the probability of the weight taking

any specific value. These types of random variables which can take an infinitely

large number of values are called continuous random variables, and the

resulting distribution is called a continuous probability distribution. The
```

## Page 192

```
function that specifies the probability distribution of a continuous random

variable is called the probability density function (p.d.f.).

Sometimes, for the sake of convenience, a discrete situation with a large number

of outcomes is approximated by a continuous distribution. For example, if we

find that the demand of a product is a random variable taking values of 1, 2, 3,

…to 1,000, it may be worthwhile to treat it as a continuous variable.

In a nutshell, if the random variable is restricted to take only a limited number of

values, it is termed as discrete random variable and if it is allowed to take any

value within a given range it is termed as continuous random variable.

It should be clear, from the above discussion, that a probability distribution is

defined only in the context of a random variable or a function of random variable.

Thus in any situation, it is important to identify the relevant random variable and

to find the probability distribution to facilitate decision making.

Expected Value of a Random Variable

Expected value is the fundamental idea in the study of probability distributions.

For finding the expected value of a discrete random variable, we multiply each

value that the random variable can assume by its corresponding probability of

occurrence and then sum up all the products. For example to find out the expected

value of the discrete random variable (RV) of ‘Daily Visa Cleared’ given:
```

## Page 193

```
Now, we will examine situations involving discrete random variables and discuss

the methods for assessing them.



       TEXT BOOKS

   •   T1 = H. K Dass, Higher Engineering Mathematics, S. Chand Publishers,3rd revised

       edition.2014.

   •   T2 = B.S. Grewal, Higher Engineering Mathematics, Khanna Publishers,42th

       ed.2013, New Delhi.

   •   T3= N. P. Bali and Manish Goyal, A textbook of engineering Mathematics, Laxmi

       Publications, Reprint 2008.




       REFERENCE BOOKS

   •   R1=R. K. Jain and S. R. K. Lyenger, Advanced Engineering Mathematics ,3rd Edition

       Narosa Publishing House ,2004,New Delhi.

   •   R2 =B. V. Ramana Advanced Engineering Mathematics, McGrawHill, July2006, New

       Delhi.
```

## Page 194

```
   •   S.P.Gupta,StatisticalMethods,S.Chand&Sons,2017,NewDelhi,ISBN9789351610281In

       siders’Guide



       Video Lecture :

h#ps://www.youtube.com/watch?v=3v9w79NhsfI

h#ps://www.youtube.com/watch?v=c06FZ2Yq9rk
```

## Page 195

```
Kurtosis: Understanding Data Distribution Shape




           PROBABILITY & STATISTICS | Moments, Skewness, and Kurtosis



   Course: PROBABILITY & STATISTICS | Chapter: Moments, Skewness, and Kurtosis | Program: Bachelor of Engineering




                                                                                                        DISCOVER · LEARN · EMPOWER
```

## Page 196

```
                                                                    Course Outcomes                                                                            SLIDE 2 / 14




Course Outcome
CO          BT LEVEL                     DESCRIPTION




     CO1               BT3               To understand fundamental concepts of probability theory and statistics




     CO2               BT4               Identify and formulation of engineering problems in different situations involving probabilistic and statistical measures




     CO3               BT5               Classify various types of statistical methods and perform statistical inference




     CO4               BT4               Apply appropriate statistical tools, distributions including correlation and regression analysis techniques




     CO5               BT5               Implement the standard concepts and tools at an intermediate to advanced level that will help in tackling various problems in
                                         hypothesis testing




                 Chandigarh University                                                                                                                               2 / 14
```

## Page 197

```
                                                           Learning Objectives                           SLIDE 3 / 14




Learning Outcomes

 1   Explain the definition and significance of kurtosis in a data distribution.




 2   Describe the relationship between kurtosis and the shape of a probability curve.




 3   Classify distributions as leptokurtic, mesokurtic, or platykurtic based on their kurtosis values.




                       Chandigarh University                                                                  3 / 14
```

## Page 198

```
                                                                    Lecture                                                          SLIDE 4 / 14




Definition of Kurtosis
 1   Kurtosis measures the 'tailedness' or peakedness of a probability
     distribution.

 2   It quantifies how much data falls into the tails versus the center.


 3   Mathematically, it is the standardized fourth central moment of the
     distribution.

 4   High kurtosis indicates heavy tails and a sharp peak in the data.


 5   Low kurtosis indicates light tails and a flatter, more uniform peak.


 6   It is distinct from skewness, which measures asymmetry in the
     distribution.

 7   The symbol used for population kurtosis is typically denoted as β₂.      Bell Shaped Curve: Normal Distribution In Statistics




                        Chandigarh University                                                                                             4 / 14
```

## Page 199

```
                                                                 Lecture                          SLIDE 5 / 14




Mathematical Formula
                                                              GOVERNING EQUATION


                                               The formula for kurtosis is β₂ = μ₄ / σ⁴


 1   Here μ₄ represents the fourth central moment of the distribution.


 2   The symbol σ represents the standard deviation of the data set.


 3   The fourth central moment is the average of the fourth powers of deviations.


 4   We divide by the fourth power of standard deviation to standardize the value.


 5   This normalization allows comparison between distributions with different units or scales.


 6   The formula ensures the value is dimensionless and comparable across datasets.


                       Chandigarh University                                                           5 / 14
```

## Page 200

```
                                                                       Lecture                             SLIDE 6 / 14




Excess Kurtosis Concept
                                  GOVERNING EQUATION


                       Excess kurtosis = β₂ - 3


 1   Excess kurtosis is defined as kurtosis minus 3.


 2   We subtract 3 because the normal distribution has a kurtosis of 3.


 3   A value of zero indicates a normal distribution shape.


 4   Positive excess kurtosis means the distribution is more peaked than
     normal.
 5   Negative excess kurtosis means the distribution is flatter than normal.

                                                                                 Source: analystprep.com
 6   This metric simplifies the classification of distributions in statistical
     analysis.
                         Chandigarh University                                                                  6 / 14
```

## Page 201

```
                                                                              Lecture                                      SLIDE 7 / 14




Leptokurtic Distributions
  EXAMPLE
                                                   • Leptokurtic distributions have a
  A dataset with many values near the              kurtosis value greater than 3.
  mean and few far away.                           • They exhibit a sharp, high peak in
                                                   the center of the data.
                                                   • They also possess heavy tails,
                                                   meaning more extreme outliers exist.
                                                   • The term comes from Greek 'leptos'
                                                   meaning thin or sharp.
                                                   • In engineering, this often indicates
                                                   a process with high precision but risk.
                                                   • These distributions are more prone
                                                   to extreme events than normal
                                                   distributions.



                                                                                             Source: www.scotthyoung.com




                           Chandigarh University                                                                                7 / 14
```

## Page 202

```
                                                                   Lecture                             SLIDE 8 / 14




Mesokurtic Distributions
 1   Mesokurtic distributions have a kurtosis value exactly equal to 3.


 2   They represent the standard normal distribution shape.


 3   The peak and tails are moderate compared to other distributions.


 4   The term comes from Greek 'mesos' meaning middle or average.


 5   This is the baseline against which other distributions are compared.


 6   Most natural phenomena approximate a mesokurtic distribution.


 7   No excess kurtosis is present in a mesokurtic distribution.             Source: analystprep.com




                        Chandigarh University                                                               8 / 14
```

## Page 203

```
                                                                     Lecture                              SLIDE 9 / 14




Platykurtic Distributions
 1   Platykurtic distributions have a kurtosis value less than 3.


 2   They exhibit a flatter peak and lighter tails than normal distributions.


 3   The term comes from Greek 'platys' meaning broad or flat.


 4   Data is more evenly spread out across the range of values.


 5   Extreme outliers are less likely to occur in platykurtic distributions.


 6   This shape is common in uniform distributions or mixed populations.


 7   The peak is lower and the shoulders are higher than a bell curve.          Source: analystprep.com




                         Chandigarh University                                                                 9 / 14
```

## Page 204

```
                                                               Lecture                                     SLIDE 10 / 14




Worked Numerical Example
                                  GOVERNING EQUATION


            We calculate kurtosis as β₂ = 128 / (2⁴)


 1   Consider a dataset with a fourth central moment of 128.


 2   The standard deviation of this dataset is 2.


 3   The fourth power of 2 is 16.


 4   Dividing 128 by 16 gives a kurtosis value of 8.


 5   The excess kurtosis is 8 - 3 = 5.

                                                                         Source: classrankcalculator.com
 6   Since 5 is positive, the distribution is leptokurtic.


                         Chandigarh University                                                                  10 / 14
```

## Page 205

```
                                                                      Lecture       SLIDE 11 / 14




Visual Comparison of Shapes
 1   Leptokurtic curves are taller and narrower than the normal curve.


 2   Platykurtic curves are shorter and wider than the normal curve.


 3   The area under all probability curves must always equal 1.


 4   Visualizing these shapes helps in identifying data anomalies quickly.


 5   Heavy tails in leptokurtic data imply higher risk of outliers.


 6   Light tails in platykurtic data imply more consistent, predictable outcomes.


 7   The normal curve sits in the middle as the reference standard.


                         Chandigarh University                                           11 / 14
```

## Page 206

```
                                                                    Lecture       SLIDE 12 / 14




Common Pitfalls in Kurtosis
 1   Do not confuse kurtosis with skewness or asymmetry.


 2   Kurtosis does not measure the height of the peak alone.


 3   A flat peak can still have high kurtosis if tails are heavy.


 4   Sample kurtosis can be unstable with small sample sizes.


 5   Always check for outliers before calculating kurtosis on raw data.


 6   Misinterpreting excess kurtosis as the raw kurtosis value leads to errors.


 7   Remember that kurtosis is sensitive to extreme values in the dataset.


                         Chandigarh University                                         12 / 14
```

## Page 207

```
                                                                    Lecture                       SLIDE 13 / 14




Key Takeaways
                                                                 GOVERNING EQUATION


                                               Mesokurtic is the standard normal shape (β₂ = 3)


 1   Kurtosis measures the tailedness and peakedness of a distribution.


 2   Leptokurtic means high peak and heavy tails (β₂ > 3).


 3   Platykurtic means low peak and light tails (β₂ < 3).


 4   Excess kurtosis is calculated by subtracting 3 from the raw value.


 5   Understanding kurtosis is essential for risk analysis in engineering.


                       Chandigarh University                                                           13 / 14
```

## Page 208

```
                                                              Lecture     SLIDE 14 / 14




References
 1   Higher Engineering Mathematics — H. K Dass.



 2   Higher Engineering Mathematics — B. S. Grewal



 3   Advanced Engineering Mathematics — R.K. Jain, and S.R.K. Iyengar



 4   Advanced Engineering Mathematics — B.V. Ramana



 5   Statistical methods — S. P. Gupta



 6   A textbook of Engineering Mathematics — N.P. Bali and Manish Goyal



                       Chandigarh University                                   14 / 14
```