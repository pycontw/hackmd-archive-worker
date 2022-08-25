# Practicing Statistics in Python: Hypothesis Testing - Mosky Liu

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/6obyax5u" height=450 width=100%></iframe>

> 從這開始


:star2: slide: https://speakerdeck.com/mosky/hypothesis-testing-with-python
:star2: github: https://github.com/moskytw/hypothesis-testing-with-python

* Build our bad reviews in statistics
    * Build a statical model by a hypothesis
    
* Hypothesis contains **equal** = null hypothesis
* Hypothesis contains **not equal** = alternative hypothesis

# Welch's t-test
* test mean
* Student's t-test assumed the populations have the same variance. Welch's t-test relaxed this assumption.

# Chi-squared test
* test proportions

# Power analysis
* 2x2 chi-squared test almost equal to two-proportion z-test
# Mann-Whitney U test
* test medians
# More tests

# Complete steps 
1. Decide **what to test.**
2. Decide **alpha**, **raw effect size**, **beta** to achieve.
3. Calculate **sample size.**
4. Still collect a sample as large as possible.
5. Test.
6. Investigate beta if need.
7. Report fully, **not only significant or not.**
    - Means, confidence intervals, p-value, research design, etc.

# Keep Learning
[Reference]
1. [Seeing Theory](https://seeing-theory.brown.edu/cn.html)
2. [Statistics - SciPi tutorial](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)
3. [StatsModels](https://www.statsmodels.org/stable/index.html)
4. Biological Statistics
5. Research Design

###### tags: `PyConTW2019`
