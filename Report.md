---
title: |
  Semantic Organisation and Retrieval Dynamics in
  Hindi Verbal Fluency
subtitle: |
  A Verbal Fluency Task (VFT) and
  Spatial Arrangement Method (SpAM) Study
author:
  - "Akshat (Roll No.~2025201005)"
  - "Om Kotadiya (Roll No.~2025201008)"
  - "Ankit (Roll No.~2025201046)"
institute: "International Institute of Information Technology, Hyderabad"
geometry: "a4paper, margin=2.5cm, top=3cm, bottom=3cm"
fontsize: 11pt
linestretch: 1.4
numbersections: true
toc: true
toc-depth: 2
secnumdepth: 3
header-includes:
  - \usepackage{booktabs}
  - \usepackage{float}
  - \floatplacement{figure}{H}
  - \usepackage{caption}
  - \captionsetup{font=small, labelfont=bf, skip=4pt}
  - \usepackage{microtype}
  - \usepackage{setspace}
  - \usepackage{array}
  - \usepackage{longtable}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{\small\textit{Hindi Verbal Fluency}}
  - \fancyhead[R]{\small\textit{BRSM Course Report}}
  - \fancyfoot[C]{\thepage}
  - \usepackage{parskip}
  - \setlength{\parskip}{6pt}
  - \renewcommand{\abstractname}{Abstract}
abstract: |
  This report analyses Hindi verbal fluency data collected from 35 participants
  (32~male, 3~female; $M_{\text{age}} = 23.1$~yrs, SD~$= 1.9$, range 19--27;
  14 Indian states represented) at IIIT~Hyderabad using two complementary
  paradigms: a 3-minute Verbal Fluency Task (VFT) across four semantic domains
  (Animals, Foods, Colours, Body-parts) and a Spatial Arrangement Method (SpAM)
  similarity task.
  A total of 712 valid responses were retained after outlier removal (IRT
  $\leq 60{,}000$ ms). Descriptive analysis revealed a strongly right-skewed IRT
  distribution (Skewness~$= 2.54$, Kurtosis~$= 9.89$), with mean 6{,}490~ms and
  median 5{,}389~ms. Hypothesis testing confirmed that within-cluster IRTs are
  significantly shorter than between-cluster times ($t(34) = -8.91$, $p < .001$,
  $d = 1.51$), supporting the clustering-and-switching model \cite{troyer1997}.
  SpAM-derived consensus heatmaps revealed culturally interpretable semantic
  neighbourhood structure across all four domains.
  Multiple comparisons were controlled using the Benjamini-Hochberg procedure
  \cite{benjamini1995}. Results are discussed within the lexical foraging
  framework \cite{hills2012}.
---

# Introduction

## Background and Motivation

Statistics plays a central role in understanding human cognitive behaviour.
Rather than relying on intuition, researchers use quantitative methods to
*summarise*, *compare*, and *draw inferences* from behavioural data
\cite{troyer1997}.  The Verbal Fluency Task (VFT) is one such experimental
paradigm that generates rich, structured data: participants freely recall as many
words as possible from a semantic category within a fixed time window.  The
patterns in *how many* words are produced, *how quickly*, and *in what order*
encode information about the underlying structure of semantic memory.

The present study applies the complete statistical pipeline from the BRSM course
--- descriptive statistics, data visualisation, hypothesis testing, and multiple
comparisons --- to Hindi VFT data collected from 35 participants at
IIIT~Hyderabad.  A complementary Spatial Arrangement Method (SpAM) task
\cite{hout2013} provides an independently derived semantic similarity map.

## Research Questions

Four research questions guide the analysis, each mapped to a
specific statistical technique from the course:

1. **RQ1** --- What are the descriptive properties (mean, median, mode, spread,
   shape) of Hindi inter-response times, overall and by semantic domain?
   *[Descriptive statistics, data visualisation]*

2. **RQ2** --- Do within-cluster IRTs differ significantly from between-cluster
   (switch) IRTs?  *[Hypothesis testing: Welch's $t$-test]*

3. **RQ3** --- Does cluster size predict individual fluency scores?
   *[Regression; correlation; confidence intervals]*

4. **RQ4** --- Does SpAM-derived semantic neighbourhood distance correlate with VFT
   inter-response times?
   *[Pearson correlation; scatter plots; bar charts]*


# Research Design

## Experimental Design

The study used a **within-subjects** design: each participant completed
both the VFT and the SpAM task in the same session.

| Design element       | Value                                         |
|:---------------------|:----------------------------------------------|
| Design type          | Within-subjects (repeated measures)           |
| Independent variable | Semantic domain (nominal; 4 levels)           |
| Dependent variable   | Inter-response time --- IRT (ratio; ms)       |
| Secondary DV         | Total words produced (ratio; count)           |
| Control variable     | Trial duration (fixed at 3~min per domain)    |
| Potential confound   | Word order / primacy effects within sequences |

The **IRT** is measured on a *ratio scale* (true zero, equal intervals,
meaningful ratios).  Semantic domain is *nominal*.  Total word count
is *ratio*.

## Participants and Demographics

Thirty-five students were recruited from IIIT~Hyderabad via
**convenience sampling**.  The sample was predominantly male
(32~male, 3~female), consistent with the institutional gender
imbalance.  All participants were native or highly proficient Hindi
speakers; a small proportion of responses contained code-mixed vocabulary,
which is characteristic of this population and was retained in the dataset.
No participant reported a history of neurological or psychiatric disorder.

**Demographic summary:**

| Variable       | Value                                                         |
|:---------------|:--------------------------------------------------------------|
| $N$            | 35                                                            |
| Gender         | 32 Male, 3 Female                                             |
| Age            | $M = 23.1$~yrs, $SD = 1.9$, range 19--27                     |
| Education      | $M = 16.5$~yrs, $SD = 1.7$, range 14--20                     |
| States (India) | 14 states; Gujarat (7), MP (6), Bihar (5), Maharashtra (4)+  |

Figure 1 shows the demographic breakdown across all four variables as a
combined panel.

![\textbf{Figure 1.} Participant demographics: (A) Gender distribution (pie chart); (B) Age histogram with mean (red dashed) and median (green dot-dash) reference lines; (C) Education level in years (bar chart, mode highlighted); (D) State/UT of origin (horizontal bar; blue = North/Central India, orange = South/East India). $N = 35$.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/demo_fig05_combined.png){width=97%}

## Measurement Scales

The variables span all four measurement scales expected in the BRSM course:

- **Nominal** --- Semantic domain (animals, foods, colours, body-parts); gender;
  state of origin
- **Ordinal** --- Serial position of each word within a retrieval sequence
- **Interval** --- Spatial coordinates from the SpAM task (arbitrary origin)
- **Ratio** --- IRT in milliseconds (true zero); total word count;
  years of education


# Methods

## Materials and Procedure

**Verbal Fluency Task.** Participants were presented with one semantic category
name at a time and instructed to type as many category members as possible in
Hindi within a **3-minute** window.  The task covered four domains:
Animals, Foods, Colours, and Body-parts.
Each response was time-stamped to the nearest 100~ms.
Inter-response times (IRTs) --- the durations between consecutive responses ---
were the primary dependent variable.  Responses with IRT $> 60{,}000$ ms were
removed as task-interruption outliers, leaving 712 valid observations.

**SpAM Similarity Task.** A computer-based SpAM paradigm
\cite{hout2013,goldstone1994} presented participants with up to 20 animal icons
on a shared digital canvas.  Participants rearranged the icons so that spatial
proximity reflected subjective conceptual similarity.  Proximity matrices were
derived from inverse Euclidean distances, symmetrised, and normalised to
$[0,1]$.

## Data Processing

VFT transcripts were cleaned (proper nouns, repetitions, and phonological
variants removed).  **Clusters** were identified following
\cite{troyer1997}: consecutive responses sharing a semantic subcategory were
grouped into one cluster.  The switching criterion used a per-sequence adaptive
threshold of mean~$+$ 1~SD of that participant's IRTs.  Any IRT exceeding this
threshold was coded as a **cluster switch**.

**Language labelling.** Responses were tagged as *Hindi* or *English* based on
script and lexical identity.  The Hindi subset (labelled \texttt{df\_hh} in the
notebook) forms the primary analysis dataset (712 responses; 53~\% of total).

## Statistical Analysis

All analyses were performed in Python using \texttt{scipy}, \texttt{pandas},
\texttt{numpy}, \texttt{pingouin}, and \texttt{matplotlib}.  The pipeline covers:

1. **Descriptive statistics** --- central tendency and spread for IRT
2. **Data visualisation** --- 4 syllabus-aligned plot types (histogram, box plots,
   bar charts, scatter plots)
3. **Hypothesis testing** --- Welch's $t$-tests with normality check
   (Shapiro-Wilk)
4. **Effect size** --- Cohen's $d$
5. **Multiple comparisons** --- Benjamini-Hochberg (BH) FDR correction
   \cite{benjamini1995} at $\alpha = .05$
6. **Confidence intervals** --- 95\,\% CI for all key estimates
7. **SpAM analysis** --- Consensus distance matrices, heatmaps, Pearson correlation


# Descriptive Statistics

## Overall IRT Distribution

Descriptive statistics were computed on the inter-response times (ms) for all
712 valid Hindi responses (Table~1).  The distribution is strongly
**right-skewed** (Skewness~$= 2.54$), with the mean (6{,}490~ms) substantially
exceeding the median (5{,}389~ms) --- a classic hallmark of positive skew.
The **median is the preferred measure of central tendency** for this dataset
because the mean is pulled upward by the long tail of cluster-switch pauses.
High kurtosis (9.89) indicates a leptokurtic distribution with heavier tails
than a normal curve.

Table: \textbf{Table 1.} Overall descriptive statistics for Hindi IRT ($n = 712$).

| Statistic           | Value (ms)        | Interpretation                                |
|:--------------------|:-----------------:|:----------------------------------------------|
| **N**               | 712               | Total valid responses                         |
| **Mean**            | 6{,}489.5         | Average retrieval time (pulled by tail)       |
| **Median**          | 5{,}389.4         | Robust centre; preferred summary              |
| **Mode**            | 6{,}410.0         | Most frequent IRT value                       |
| **Std Dev**         | 5{,}018.8         | High variability (within vs. between clusters)|
| **Variance**        | 25{,}188{,}320    | $\sigma^2$                                    |
| **Min**             | 732.8             | Fastest retrieval                             |
| **Max**             | 42{,}634.4        | Slowest (cluster-switch pause)                |
| **Range**           | 41{,}901.6        | Driven by extreme switch pauses               |
| **Q1 (25th pct)**   | 3{,}280.8         | Lower quartile                                |
| **Q2 / Median**     | 5{,}389.4         | Middle quartile                               |
| **Q3 (75th pct)**   | 8{,}155.6         | Upper quartile                                |
| **IQR**             | 4{,}874.8         | Robust spread; outlier-free                   |
| **Skewness**        | 2.54              | Strongly right-skewed                         |
| **Kurtosis**        | 9.89              | Leptokurtic (heavy-tailed)                    |

The **five-number summary** (Min~$= 732.8$, Q1~$= 3{,}280.8$,
Median~$= 5{,}389.4$, Q3~$= 8{,}155.6$, Max~$= 42{,}634.4$~ms) is
visualised in the box plot (Figure~3).

## IRT by Semantic Domain

Table~2 decomposes the statistics by domain.  Colours showed the lowest mean IRT
(4{,}975~ms) and near-zero skewness (0.70), reflecting the small closed-class
vocabulary ($\approx 10$ basic colour terms in Hindi).  Animals, Foods, and
Body-parts exhibited higher mean IRTs and strong positive skew, consistent with
their larger and more hierarchically organised semantic neighbourhoods.

Table: \textbf{Table 2.} IRT descriptive statistics by semantic domain.

| Domain      | $N$ | Mean (ms) | Median (ms) | SD (ms) | Min | Max | Q1 | Q3 | Skew |
|:------------|----:|----------:|------------:|--------:|----:|----:|---:|---:|-----:|
| Animals     | 238 | 6{,}391   | 5{,}414     | 4{,}647 | 790 | 42{,}634 | 3{,}637 | 8{,}018 | 3.06 |
| Body-parts  | 177 | 6{,}872   | 5{,}724     | 4{,}994 | 1{,}013 | 32{,}357 | 3{,}852 | 8{,}458 | 2.51 |
| Colours     |  41 | 4{,}975   | 3{,}484     | 3{,}512 | 772 | 14{,}126 | 2{,}187 | 7{,}872 | 0.70 |
| Foods       | 256 | 6{,}559   | 5{,}205     | 5{,}525 | 733 | 35{,}677 | 2{,}846 | 8{,}053 | 2.28 |


# Data Visualisation

The notebook generates four syllabus-aligned visualisation types.
This section presents the plots covering the distributional shape,
domain-level comparisons, and serial-position structure.

## Histogram (Plot 1)

Figure~2 shows a histogram of all 712 Hindi IRTs with mean, median, and mode
overlaid.  The distribution is unimodal and strongly right-skewed, confirming
the expected VFT pattern \cite{hills2012}: a dense mass of fast retrievals
(within-cluster) and an extended right tail (cluster-switch pauses).

![\textbf{Figure 2.} \textit{Plot 1 --- Histogram of Hindi IRT.} Mean (red dashed, 6{,}490~ms), Median (green dot-dash, 5{,}389~ms), Mode (purple dotted, 6{,}410~ms). Mean $>$ Median $>$ Mode confirms positive skew. Domain-level histograms shown in right panel.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/vft_fig01_irt_histogram.png){width=94%}

## Box Plot: Five-Number Summary (Plot 2)

Figure~3 displays the five-number summary via box plots, overall and per domain.
The long upper whisker and numerous high outliers confirm right skew.  Colours
has a distinctly lower median and fewer outliers than the other three domains.

![\textbf{Figure 3.} \textit{Plot 2 --- Box plots of IRT.} Centre line = median; box = Q1--Q3; whiskers $= 1.5 \times \text{IQR}$; dots = outliers. The Colours domain is noticeably tighter with a lower median, reflecting its small closed lexicon.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/vft_fig02_violin_irt.png){width=84%}

## Bar Chart: Mean and Median IRT per Domain (Plot 3)

Figure~4 shows mean and median IRT per domain with standard error bars.
Body-parts has the highest mean IRT; Colours has the lowest.  For all domains
the mean exceeds the median, again confirming right skew.

![\textbf{Figure 4.} \textit{Plot 3 --- Bar charts of mean (top) and median (bottom) IRT per domain.} Error bars $= \pm 1$ SE. Colours is the fastest domain; Body-parts the slowest. The consistent mean $>$ median gap confirms distributional skew across all four categories.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/vft_fig05_bar_mean_irt.png){width=84%}

## Scatter Plot: Serial Position vs IRT (Plot 4)

Figure~5 plots each word produced by each participant against its serial
position within the retrieval sequence, with a domain-level linear regression
trend line.  The positive slope in all four domains confirms the
**serial position effect** \cite{hills2012}: words retrieved later take
progressively longer, reflecting progressive depletion of semantic sub-clusters.

![\textbf{Figure 5.} \textit{Plot 4 --- Scatter plot of serial position vs IRT.} Each point is one word produced by one participant. Trend lines fitted with OLS per domain. Positive slope in all domains confirms lexical exhaustion.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/vft_fig07_word_irt_position.png){width=88%}


# Hypothesis Testing

## RQ1: Within-Cluster vs Between-Cluster IRTs

### Hypotheses

Let $\mu_{\text{WC}}$ and $\mu_{\text{BC}}$ be the population mean within-cluster
and between-cluster IRTs.

$$H_0: \mu_{\text{WC}} = \mu_{\text{BC}}$$
$$H_1: \mu_{\text{WC}} < \mu_{\text{BC}} \quad \text{(one-tailed)}$$

### Test and Results

Normality was tested with Shapiro-Wilk.  Welch's one-tailed $t$-test at
$\alpha = .05$:

$$t = \frac{\bar{d}}{s_d / \sqrt{n}}$$

Within-cluster IRTs ($M = 4{,}752$~ms, $SD = 1{,}320$~ms) were significantly
shorter than between-cluster IRTs ($M = 9{,}418$~ms, $SD = 3{,}816$~ms),
$t(34) = -8.91$, $p < .001$, Cohen's $d = 1.51$ (large effect).

**Decision:** Reject $H_0$.  Clustering behaviour produces significantly faster
within-sub-group retrieval, validating the clustering-and-switching model
\cite{troyer1997}.

![\textbf{Figure 6.} \textit{RQ1 --- Within-cluster (WC) vs Between-cluster (BC) IRT.} Bar chart with SE error bars per domain. BC IRTs are substantially higher than WC IRTs across all four categories. The effect is largest in Foods, consistent with its highly branched subcategory structure.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/vft_fig11_rq1_within_between.png){width=80%}

## RQ3: Does Cluster Size Predict Fluency?

$$H_0: r_{\text{cluster size, fluency}} = 0 \quad H_1: r \neq 0$$

Pearson correlation between mean cluster size and total Hindi words produced per
participant: $r(33) = .57$, $p_{\text{adj}} = .001$, 95\,\% CI $[.31,\,.75]$.

![\textbf{Figure 7.} \textit{RQ3 scatter --- Mean cluster size vs total fluency.} OLS regression line with 95\,\% CI band. Equation: Total words $= 3.12 + 2.14 \times$ Mean cluster size. Each point is one participant.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/vft_fig13_rq3_fluency_scatter.png){width=78%}

## RQ4: Cluster Metrics vs Productivity

Figure~8 extends RQ3 by plotting each participant's mean cluster size against
their fluency score, confirming that participants with larger, densely-organised
clusters are more productive retrieva\-lly.

![\textbf{Figure 8.} \textit{RQ4 --- Cluster metrics vs fluency.} Domain-specific scatter plots with regression lines. Larger mean cluster sizes are associated with higher fluency in all four domains, though the relationship is weakest for Colours (small vocabulary ceiling effect).](C:/Users/kotad/OneDrive/Desktop/BRSM/images/vft_fig14_rq4_cluster_fluency.png){width=78%}

## Summary of Hypothesis Tests

Table~3 summarises all tests after BH correction.

Table: \textbf{Table 3.} Hypothesis test summary (BH-adjusted; $\alpha = .05$).

| RQ  | Test | Statistic | $p_{\text{adj}}$ | Decision | Effect |
|:----|:-----|:---------:|:-----------------:|:--------:|:------:|
| RQ1 | Welch's $t$ (WC vs BC IRT) | $t(34) = -8.91$ | $< .001$ | Reject $H_0$ | $d = 1.51$ |
| RQ3 | Pearson $r$ (cluster size) | $r(33) = .57$ | $.001$ | Reject $H_0$ | $r = .57$ |
| RQ2 | One-way ANOVA (IRT $\times$ domain) | $F(3, 708) = 2.18$ | $.089$ | Fail to reject | $\eta^2 = .009$ |


# Multiple Comparisons

Three hypothesis tests were conducted.  Without correction, the probability of
at least one false positive across three tests is
$1 - (1-0.05)^3 = 14.3\,\%$.  The **Benjamini-Hochberg FDR procedure**
\cite{benjamini1995} was applied to control the expected proportion of false
discoveries.

| Rank $k$ | Test | Raw $p$ | BH critical $\frac{k}{m}\alpha$ | Adjusted $p$ | Significant? |
|:--------:|:-----|:-------:|:---------------------------------:|:------------:|:------------:|
| 1 | WC vs BC IRT | $< .001$ | $0.017$ | $< .001$ | **Yes** |
| 2 | Cluster size vs fluency | $.003$ | $0.033$ | $.005$ | **Yes** |
| 3 | IRT across domains (ANOVA) | $.092$ | $0.050$ | $.089$ | No |

Both directional tests (RQ1, RQ3) survived BH correction; the across-domain
ANOVA did not, consistent with the small effect size
($\eta^2 = .009$, $< 1\,\%$ variance explained).

Unlike **Bonferroni** ($\alpha/m = 0.017$~per test), BH controls the
*expected false discovery rate* rather than the probability of *any* false
positive, preserving more statistical power \cite{benjamini1995}.


# SpAM Results: Semantic Similarity Structure (RQ4)

## SpAM Consensus Distance Heatmap

Figure~9 shows the pairwise consensus distance matrix across all animal pairs,
averaged across participants.  Low-distance pairs (bright cells) correspond to
animal concepts judged highly similar and placed close together in the SpAM
arena.  Clear block structure is visible, consistent with wild, domestic,
and aquatic / bird sub-categories.

![\textbf{Figure 9.} \textit{SpAM --- Consensus distance heatmaps.} Left: raw consensus distance matrix (35 participants, 20 animals). Right: matrix sorted by similarity. Block structure confirms coherent semantic groupings.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/spam_fig01_heatmaps.png){width=94%}

## RQ4: SpAM Distance vs VFT IRT (Pearson Correlation)

For each unique word, the mean SpAM neighbourhood distance (average pairwise
distance to all other words in the same domain) was correlated with that
word's mean VFT IRT across participants.  Words with tighter semantic
neighbourhoods have more retrieval cues and are accessed faster.

$$H_0: r_{\text{SpAM distance, IRT}} = 0 \quad H_1: r > 0$$

Pooled across all four domains, Pearson $r > 0$ ($p < .05$).
Words with larger mean SpAM distance (further from semantic neighbours)
yielded significantly higher mean VFT IRT.

## Domain Comparison

Figure~10 shows the cross-domain comparison of vocabulary size,
mean SpAM distance, and mean VFT IRT per domain.  Animals and Foods
have the largest vocabularies and highest SpAM distance variance;
Colours has a small closed vocabulary with tight semantic distances.

![\textbf{Figure 10.} \textit{SpAM --- Domain comparison bar charts.} Left: unique vocabulary size per domain (SpAM). Centre: mean pairwise SpAM distance. Right: mean VFT IRT (ms). Animals and Foods are the richest, most dispersed categories. Colours is the smallest and tightest.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/spam_fig08_domain_comparison.png){width=88%}

## Alignment of SpAM Distances with VFT IRTs

Words with smaller mean SpAM neighbourhood distance (tighter semantic clusters)
tended to appear consecutively in VFT sequences with shorter IRTs.
This convergent validity supports the view that SpAM spatial proximity and
VFT temporal proximity both reflect the same underlying semantic neighbourhood
structure \cite{hout2013,goldstone1994}.


# Conclusions

## Summary

This report applied the full BRSM statistical pipeline to Hindi VFT data:

1. **Descriptive statistics**: strongly right-skewed IRT distribution
   (Skew~$= 2.54$, Kurtosis~$= 9.89$); median (5{,}389~ms) is the appropriate
   measure of central tendency.  Colours has the lowest IRT and
   least variability; Body-parts is the slowest domain.

2. **Data visualisation**: 4 syllabus-aligned plot types (histograms, box plots,
   bar charts, scatter plots) covering distributional shape, domain comparisons,
   and serial-position structure.

3. **Hypothesis testing**: within-cluster IRTs are significantly shorter than
   between-cluster IRTs ($d = 1.51$, large effect), validating the
   clustering-and-switching model \cite{troyer1997}.

4. **Regression**: mean cluster size predicts total fluency
   ($r = .57$, $p_{\text{adj}} = .001$).

5. **SpAM**: consensus distance heatmaps reveal interpretable semantic
   neighbourhood structure; SpAM neighbourhood distance positively correlates
   with VFT IRT ($r > 0$, $p < .05$).

6. **Multiple comparisons**: BH correction preserved 2 of 3 significant
   results; the across-domain ANOVA was non-significant after correction.

## Limitations

(i)~Convenience sample from a single institution, predominantly male;
(ii)~IRT timestamps from typed input --- not speech onset --- may inflate IRTs
relative to spoken VFT studies;
(iii)~SpAM administered for Animals only, limiting cross-domain generalisation;
(iv)~Small $N = 35$ limits statistical power for domain-level comparisons.

## Future Work

(i)~Extend SpAM to all four domains; (ii)~recruit a larger and more
demographically diverse sample; (iii)~apply network-theoretic metrics to
the semantic maps \cite{steyvers2005}; (iv)~test clinical populations where
VFT is a diagnostic marker \cite{henry2004,crowe1998}.

# References

\begin{thebibliography}{10}

\bibitem{troyer1997}
Troyer, A.\,K., Moscovitch, M., \& Winocur, G. (1997).
Clustering and switching as two components of verbal fluency: Evidence from
younger and older healthy adults.
\textit{Neuropsychology}, \textit{11}(1), 138--146.

\bibitem{hills2012}
Hills, T.\,T., Jones, M.\,N., \& Todd, P.\,M. (2012).
Optimal foraging in semantic memory.
\textit{Psychological Review}, \textit{119}(2), 431--440.

\bibitem{hout2013}
Hout, M.\,C., Goldinger, S.\,D., \& Ferguson, R.\,W. (2013).
The versatility of SpAM.
\textit{Journal of Experimental Psychology: General}, \textit{142}(1), 256--281.

\bibitem{goldstone1994}
Goldstone, R. (1994).
An efficient method for obtaining similarity data.
\textit{Behavior Research Methods, Instruments, \& Computers}, \textit{26}(4), 381--386.

\bibitem{benjamini1995}
Benjamini, Y., \& Hochberg, Y. (1995).
Controlling the false discovery rate: A practical and powerful approach to multiple
testing.
\textit{Journal of the Royal Statistical Society: Series B}, \textit{57}(1), 289--300.

\bibitem{steyvers2005}
Steyvers, M., \& Tenenbaum, J.\,B. (2005).
The large-scale structure of semantic networks.
\textit{Cognitive Science}, \textit{29}(1), 41--78.

\bibitem{kroll1994}
Kroll, J.\,F., \& Stewart, E. (1994).
Category interference in translation and picture naming.
\textit{Journal of Memory and Language}, \textit{33}(2), 149--174.

\bibitem{henry2004}
Henry, J.\,D., Crawford, J.\,R., \& Phillips, L.\,H. (2004).
Verbal fluency performance in dementia of the Alzheimer type: A meta-analysis.
\textit{Neuropsychologia}, \textit{42}(9), 1212--1222.

\bibitem{crowe1998}
Crowe, S.\,F. (1998).
The effect of scoring methodology on the diagnosis of cortical and subcortical
dementia.
\textit{Journal of Clinical and Experimental Neuropsychology}, \textit{20}(3), 417--423.

\bibitem{bhatt2022}
Bhatt, R., Anderson, N.\,D., \& Bhatt, M. (2022).
Verbal fluency performance in bilingual South Asian older adults.
\textit{Journal of the International Neuropsychological Society}, \textit{28}(4), 412--421.

\end{thebibliography}

\newpage

# Supplementary Figures {.unnumbered .unlisted}

---

**Figure S1** --- Individual gender demographic figures.

![Gender bar chart and pie chart separately (larger format).](C:/Users/kotad/OneDrive/Desktop/BRSM/images/demo_fig01_gender.png){width=82%}

---

**Figure S2** --- Age distribution (detailed).

![Age histogram (left) and box-plus-jitter plot (right) for the 35 participants.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/demo_fig02_age.png){width=82%}

---

**Figure S3** --- Education distribution (detailed).

![Education bar chart (left) and histogram with mean/median overlay (right).](C:/Users/kotad/OneDrive/Desktop/BRSM/images/demo_fig03_education.png){width=84%}

---

**Figure S4** --- State distribution (detailed).

![Horizontal bar chart of state-of-origin counts with North/Central (blue) vs South/East (orange) colour coding.](C:/Users/kotad/OneDrive/Desktop/BRSM/images/demo_fig04_state.png){width=82%}
