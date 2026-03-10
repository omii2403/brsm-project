---
title: |
  Semantic Organisation and Retrieval Dynamics in
  Hindi Verbal Fluency
subtitle: |
  Mid-Project Analysis Report --- Verbal Fluency Task (VFT)
author:
  - "Akshat Kotadia (Roll No. 2025201005)"
  - "Om Mehra (Roll No. 2025201008)"
  - "Ankit Chavda (Roll No. 2025201045)"
institute: "International Institute of Information Technology, Hyderabad"
date: "March 2026"
geometry: "a4paper, margin=2cm, top=2.2cm, bottom=2.2cm"
fontsize: 11pt
linestretch: 1.2
numbersections: true
toc: true
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
  - \fancyhead[L]{\small\textit{Hindi Verbal Fluency --- Mid-Project}}
  - \fancyhead[R]{\small\textit{BRSM Course Report}}
  - \fancyfoot[C]{\thepage}
  - \usepackage{parskip}
  - \setlength{\parskip}{4pt}
  - \renewcommand{\abstractname}{Abstract}
abstract: |
  This mid-project report documents the experimental design, data pipeline,
  and analyses conducted on a Hindi Verbal Fluency Task (VFT) at IIIT
  Hyderabad.  Thirty-five participants generated category members across
  four semantic domains (Animals, Foods, Colours, Body-parts), producing
  712 valid Hindi responses.  Inter-response times (IRTs) are strongly
  right-skewed (Skewness = 2.54, Kurtosis = 9.89; mean 6490 ms, median
  5389 ms).  Confirmatory testing finds that within-cluster IRTs are
  significantly shorter than between-cluster IRTs (t(34) = -8.91,
  p < .001, d = 1.51), replicating the clustering-and-switching model in a
  Hindi-speaking sample.  Mean cluster size significantly predicts total
  fluency (r(33) = .57, p = .003).  Exploratory analyses uncover domain-level
  IRT differences, a serial-position exhaustion effect, and systematic
  bilingual code-switching concentrated in the Colours domain.  The Spatial
  Arrangement Method (SpAM) constitutes the planned Phase 2.
---


# Background and Information

## The Verbal Fluency Task

The **Verbal Fluency Task (VFT)** is a cornerstone paradigm in cognitive
psychology and neuropsychology.  Participants are given a semantic category cue
(e.g., "Animals") and asked to generate as many category members as they can
within a fixed time window, typically 60 seconds.  The resulting sequence of
responses, and the timing between them, encodes rich information about how
semantic memory is organised and accessed.

Retrieval is not random.  People naturally generate words in tight
**clusters** of subcategory-related items (e.g., "lion, tiger, leopard") and
then pause when they exhaust one subcategory and **switch** to another (e.g.,
a longer pause before "elephant").  This **clustering-and-switching model**
(Troyer, Moscovitch & Winocur, 1997) is the most widely cited framework for
interpreting VFT behaviour.  The core empirical prediction is that
inter-response times (IRTs) within a cluster are shorter than the pauses that
precede a switch to a new subcategory.

## Why Hindi?

Virtually all previous clustering-and-switching research has used English or
European-language participants.  Hindi presents three important differences:

1. **Script complexity** -- Devanagari typing is cognitively and motorically
   more demanding than Latin typing for many participants, potentially inflating
   IRTs uniformly.
2. **Bilingual code-switching** -- educated Hindi speakers at IIIT Hyderabad
   regularly interleave English and Hindi lexical items within a single trial.
   A proportion of responses appear in Latin script even when the cue is given
   in Hindi.
3. **Cultural semantic structure** -- category vocabularies (especially Foods
   and Animals) reflect Indian rather than Western cultural content, potentially
   yielding different subcategory boundaries.

This study applies the clustering-and-switching framework to a Hindi-speaking
student cohort, with explicit handling of bilingual code-switching.

## Broader Project Goals and Research Questions

The project has two phases.  Phase 1 (this report) analyses the raw temporal
and cluster structure of the VFT data.  Phase 2 will administer the Spatial
Arrangement Method (SpAM) to the same participants, capturing subjective
semantic neighbourhood geometry, and test whether spatial proximity predicts
temporal proximity in retrieval.

The research questions addressed in this mid-project report are:

| # | Research Question | Type | Method |
|:--|:------------------|:----:|:-------|
| **RQ1** | Do within-cluster IRTs differ significantly from between-cluster IRTs? | Confirmatory | Welch's t-test (one-tailed), Cohen's d |
| **RQ2** | Does mean cluster size predict individual verbal fluency scores? | Confirmatory | Pearson r, linear regression |
| **EH1** | How do IRT distributions differ across the four semantic domains? | Exploratory | Descriptive statistics, raincloud plots |
| **EH2** | Does IRT increase with serial position within a trial? | Exploratory | OLS regression per domain |
| **RQ3** *(Phase 2)* | Does SpAM neighbourhood distance correlate with VFT IRT? | Confirmatory | Pearson r, cross-task scatter |


---


# Experiment Explanation

## Design

The study uses a **within-subjects** repeated-measures design.  Every
participant completed the VFT in all four semantic domains, so each individual
contributes data across all conditions.

| Variable | Role | Scale | Levels / Range |
|:---------|:----:|:-----:|:---------------|
| Semantic domain | Independent | Nominal | Animals, Foods, Colours, Body-parts |
| Inter-response time (IRT) | Primary DV | Ratio (ms) | 733 -- 42634 ms |
| Total words produced (fluency score) | Secondary DV | Count | Varies per participant |

## Participants

Thirty-five students were recruited from IIIT Hyderabad via convenience
sampling.  Inclusion criteria: (1) self-reported native or near-native Hindi
proficiency; (2) no reported neurological or psychiatric history.

| Variable       | Value                                                           |
|:---------------|:----------------------------------------------------------------|
| N              | 35                                                              |
| Gender         | 32 Male, 3 Female                                               |
| Age            | M = 23.1 yrs, SD = 1.9, range 19--27                           |
| Education      | M = 16.5 yrs, SD = 1.7, range 14--20                           |
| States (India) | 14 states; Gujarat (7), MP (6), Bihar (5), Maharashtra (4+)    |

The sample is young, predominantly male, and drawn from across India, which is
characteristic of the IIIT Hyderabad student body.  Fourteen Indian states are
represented, ensuring broad regional linguistic diversity.

![*Combined demographics panel.* Top row: gender distribution (bar) and age histogram. Bottom row: years of education histogram and geographic distribution by Indian state. The sample is young (19--27 yrs), predominantly male, and geographically diverse across India.](images/demo_fig05_combined.png){width=94%}

## Stimuli and Semantic Domains

Four semantic domains were chosen to span a range of vocabulary sizes,
structural organisation, and cultural salience:

| Domain | Type | Vocabulary size | Subcategory structure |
|:-------|:-----|:---------------:|:----------------------|
| **Animals** | Open, hierarchical | Large | Wild / domestic / birds / aquatic |
| **Foods** | Open, culturally rich | Very large | Pulses / meals / snacks / fruits |
| **Colours** | Closed, perceptual | Small (~15) | Warm / cool / achromatic |
| **Body-parts** | Semi-closed, anatomical | Medium | Face / limbs / torso / internal |

Colours is theoretically the most informative domain for testing vocabulary
exhaustion because its small closed inventory is depleted quickly,
after which participants must either stop or switch to English colour names.

## Apparatus and Procedure

The experiment was delivered through a **custom web application**.  Each
session was logged as a JSON object in `responses.json` keyed by `session_id`,
capturing:

- Cumulative timestamps for every word submission (ENTER key-press, to the nearest 100 ms)
- The typed word in its original script (Devanagari or Latin)
- A spatial token placement for the SpAM phase (Phase 2)

Participants saw one category cue per trial (presented in Hindi, e.g.,
*"Jaanwar"* for Animals) and were instructed to type as many category members
as possible within **60 seconds**.  A 1-minute **Furniture warm-up trial**
preceded the four target domains to familiarise participants with the typing
interface.  Domain order was fixed: Animals --> Foods --> Colours --> Body-parts.


---


# Data Explanation

## Processing Pipeline

The raw `responses.json` was transformed into an analysis-ready dataset through
five steps:

1. **IRT computation** -- for each word at position i, IRT_i = t_i - t_(i-1),
   where t_0 = 0 (trial onset).  First-word IRT equals the initial access
   latency from the cue presentation.
2. **Language tagging** -- words in Devanagari script are labelled *Hindi*;
   words in Latin script are labelled *English*.
3. **Hindi filter** -- only Devanagari tokens retained, yielding 712 valid
   Hindi responses (53% of all 1340 raw submissions).
4. **Cluster scoring** -- consecutive words are grouped into a cluster when
   pairwise IRTs fall below an adaptive threshold of
   (mean IRT + 1 SD) computed per participant.  A new `cluster_id` is assigned
   after each detected switch.
5. **CSV export** -- one row per word: `vft_responses.csv`.

```
responses.json
  --> IRT computation  --> language tagging
  --> Hindi filter (712 tokens)
  --> cluster scoring (cluster_id, is_switch)
  --> vft_responses.csv
```

## Dataset Variables

| Column | Type | Description |
|:-------|:----:|:------------|
| `subject_id` | Integer | Anonymised participant identifier |
| `domain` | String | Animals / Foods / Colours / Body-parts |
| `word` | String | Word as typed (original script) |
| `rt_ms` | Float | IRT in milliseconds |
| `position` | Integer | Serial position within the trial (1 = first word) |
| `language_type` | String | "Hindi" (Devanagari) or "English" (Latin) |
| `cluster_id` | Integer | Cluster membership; new ID after each switch |
| `is_switch` | Boolean | True if this word opened a new cluster |

**Derived variables:**

| Variable | Definition | Used in |
|:---------|:-----------|:--------|
| Within-cluster IRT | Mean rt_ms where is_switch = False | RQ1 |
| Between-cluster IRT | Mean rt_ms where is_switch = True | RQ1 |
| Mean cluster size | Mean words per cluster_id, per participant | RQ2 |
| Total fluency score | Count of Hindi tokens per participant | RQ2 |

## Response Counts and Language Distribution

### Domain-Level Counts

| Domain      | Hindi tokens | % of total |
|:------------|:-----------:|:----------:|
| Animals     | 238         | 33.4%      |
| Foods       | 256         | 36.0%      |
| Colours     | 41          |  5.8%      |
| Body-parts  | 177         | 24.9%      |
| **Total**   | **712**     | **100%**   |

Foods and Animals dominate the Hindi token counts, reflecting their
open-ended hierarchical vocabulary structure and the large number of
culturally salient Hindi terms available.  Colours has the fewest Hindi tokens:
once the small Hindi colour lexicon (~15 terms) is exhausted, participants
invariably switch to English colour names.

![*Hindi vs English token counts by domain.* Side-by-side bars for Devanagari (Hindi, dark) and Latin-script (English, light) submissions per domain. Animals and Foods are strongly Hindi-dominant; Colours is the only domain where English submissions rival Hindi, reflecting the faster exhaustion of the Hindi colour lexicon.](images/domain-hin-en.png)

The mosaic plot above encodes both absolute count (cell area) and script
(colour) for each domain, making it easy to see that Colours is the only domain
where English-script tokens outnumber Hindi.

### Participant-Level Language Dominance

Individual participants vary considerably in their reliance on Hindi.
The figure below ranks participants by their Hindi-script proportion across
all four domains.  The majority (>80%) produced more than half of their tokens
in Hindi; a small tail of participants is near-balanced or English-dominant,
consistent with urban STEM-cohort bilingualism.

![*Hindi-script proportion per participant, sorted descending.* Each bar = one participant. The dashed line at 0.5 separates Hindi-dominant (above) from English-dominant (below). Most participants are clearly Hindi-dominant; a small subset produced approximately equal proportions in each script.](images/dominant-lang.png){width=88%}

The domain-specific breakdown of **total words by participant dominant language**
shows that Hindi-dominant participants consistently produce more Hindi tokens
in every domain.  The gap is largest for Animals and Foods (richest Hindi
vocabularies) and collapses for Colours, where even strongly Hindi-dominant
participants run out of Devanagari colour terms and switch to English.

![*Total Hindi words per domain split by participant dominant language.* Blue bars = Hindi-dominant participants; orange = English-dominant. Hindi-dominant participants produce more Hindi tokens in every domain. The gap is smallest in Colours, confirming that Devanagari colour vocabulary is limited even for the most Hindi-fluent participants.](images/total-words-per-domain-per-dominant-lang.png){width=88%}

## IRT Descriptive Statistics

### Overall Distribution

| Statistic | Value (ms) |
|:----------|:----------:|
| N         | 712        |
| Mean      | 6489.5     |
| Median    | 5389.4     |
| SD        | 5018.8     |
| Min       | 732.8      |
| Max       | 42634.4    |
| IQR       | 4874.8     |
| Skewness  | 2.54       |
| Kurtosis  | 9.89       |

The distribution is strongly **right-skewed** (Skewness = 2.54) with heavy
tails (Kurtosis = 9.89).  The median (5389 ms) is a better central tendency
estimate than the mean (6490 ms), which is pulled upward by occasional very long
between-cluster pauses.  This leptokurtic shape -- sharp peak of fast
within-cluster retrievals plus a heavy right tail of switch pauses -- is the
canonical IRT signature of the clustering-and-switching model.

![*IRT histogram -- overall and by domain.* Left panel: overall distribution with mean (red dashed, 6490 ms), median (green dot-dash, 5389 ms), and mode (purple dotted) annotated. The strong right skew is evident. Right panels: per-domain histograms. Colours produces the tightest, lowest-skew distribution; Animals and Foods show the longest tails.](images/vft_fig01_irt_histogram.png){width=96%}

### IRT by Semantic Domain

| Domain     |  N  | Mean (ms) | Median (ms) | SD (ms) | Skew |
|:-----------|----:|----------:|------------:|--------:|-----:|
| Animals    | 238 |      6391 |        5414 |    4647 | 3.06 |
| Body-parts | 177 |      6872 |        5724 |    4994 | 2.51 |
| Colours    |  41 |      4975 |        3484 |    3512 | 0.70 |
| Foods      | 256 |      6559 |        5205 |    5525 | 2.28 |

Colours has the lowest mean IRT (4975 ms) and minimal skew (0.70), consistent
with rapid depletion of a small closed lexicon.  Body-parts has the highest mean
(6872 ms), reflecting greater retrieval difficulty for anatomical vocabulary.
Foods shows the widest spread (SD = 5525 ms), reflecting its rich multi-tier
subcategory structure.

The **raincloud plots** below combine kernel-density shape, boxplot summary, and
individual data points into a single panel, giving a complete picture of each
domain's IRT distribution simultaneously.

![*Raincloud plots of IRT by semantic domain.* Half-violin = kernel density; box = Q1--Q3 with median; individual dots = raw observations (jittered). Body-parts has the highest median IRT; Colours is the tightest and fastest. The right-skewed shape visible in all four domains is the temporal signature of clustering-and-switching retrieval.](images/vft_fig03_raincloud_irt.png){width=88%}

### IRT Separated by Language Script

English-script (Latin) responses appear faster than Hindi-script (Devanagari)
responses within every domain.  This is consistent with the hypothesis that
participants access English category members with lower retrieval effort --
either because those items were acquired earlier (in English-medium schooling)
or because fewer English alternatives are available, reducing search time.

![*IRT by domain and language script.* Grouped box plots comparing Devanagari (Hindi, dark) and Latin-script (English, light) response times within each domain. English IRTs are consistently lower than Hindi IRTs. Within the Hindi subset, the ordering Colours < Animals < Foods < Body-parts matches the overall domain ranking.](images/rt-domain-lang.png){width=90%}

## Cluster Structure

### Adaptive Threshold and Scoring

Cluster boundaries were detected using per-participant adaptive thresholds:
a switch was scored whenever the IRT exceeded (mean IRT + 1 SD) for that
participant.  This approach accounts for individual differences in baseline
typing speed and prevents fast typists from being over-clustered and slow
typists from being under-clustered.

The figure below shows mean cluster size (left) and mean switch count per trial
(right) broken down by domain.  Mean cluster size > 1 in every domain confirms
that participants are genuinely grouping responses into subcategory bursts rather
than retrieving items in an unclustered stream.  Foods produces the
largest clusters (rich multi-tier subcategory structure); Colours the smallest
(small closed vocabulary rapidly depleted, frequent switches to English).

![*Cluster size and switch count by domain.* Left: mean cluster size (words per cluster). Right: mean number of switches per trial. Foods supports the deepest clustering; Colours the shallowest. Mean cluster size > 1 across all domains confirms non-random subcategory-based retrieval.](images/vft_fig06_cluster_scoring.png){width=88%}

### Fluency and IRT

The scatter plot below shows that participants with faster mean IRTs tend to
produce more Hindi words overall (r = -.57, p < .001 at token level).  Mean IRT
is therefore a valid individual-level proxy for lexical access efficiency:
faster retrieval capacity translates directly into higher fluency output.

![*Mean IRT vs total fluency score per participant.* Each point = one participant (n = 35). The negative relationship confirms that faster retrievers produce more words. OLS regression line with 95% CI band. This validates mean IRT as an efficiency proxy at the participant level.](images/vft_fig09_fluency_vs_irt.png){width=78%}


---


# Hypothesis Testing

## RQ1: Within-Cluster vs Between-Cluster IRTs

### Rationale

The clustering-and-switching model makes a specific and falsifiable prediction:
the IRT immediately *before* a switch (entering a new subcategory) should be
substantially longer than IRTs *within* a cluster.  This is because switching
requires releasing the current subcategory context, searching for a new patch,
and initiating access into it -- all processes that consume additional time
beyond simple lexical retrieval.

### Hypotheses

- **H0:** Mean within-cluster IRT = Mean between-cluster IRT
- **H1:** Mean within-cluster IRT < Mean between-cluster IRT  *(one-tailed)*

### Method

Per-participant mean within-cluster IRT (rows where `is_switch = False`) and
mean between-cluster IRT (rows where `is_switch = True`) were computed across
all four domains.  A **Welch's independent-samples t-test** (one-tailed,
alpha = .05) was applied.  Welch's variant was chosen because the two groups
have markedly different variances (within: SD ~ 1320 ms; between: SD ~ 3816 ms).

### Results

| Condition | M (ms) | SD (ms) |
|:----------|:------:|:-------:|
| Within-cluster | 4752 | 1320 |
| Between-cluster | 9418 | 3816 |

    t(34) = -8.91,  p < .001,  d = 1.51

**Decision:** Reject H0.  Between-cluster IRT is 1.98x within-cluster IRT.
The effect size d = 1.51 is large, confirming the clustering-and-switching
model clearly and robustly in this Hindi-speaking sample.

![*RQ1 -- Within- vs between-cluster IRT by domain.* Grouped bars (mean +/- 1 SE) per semantic domain. Between-cluster IRTs (rightmost bar of each pair, lighter shade) exceed within-cluster IRTs (darker) in every domain. The effect is largest for Foods (deepest clustering) and smallest for Colours (shallowest clustering, fewest switch events).](images/vft_fig11_rq1_within_between.png){width=84%}

## RQ2: Cluster Size as Predictor of Fluency

### Rationale

A participant who forms larger clusters (exploits subcategories deeply before
switching) should generate more words in total than a participant who switches
frequently between small clusters.  Deep exploitation is more time-efficient
than constant re-searching across subcategory boundaries.

### Hypotheses

- **H0:** rho (cluster size, fluency score) = 0
- **H1:** rho (cluster size, fluency score) > 0  *(one-tailed)*

### Method

Per-participant mean cluster size (averaged across all four domains) was
correlated with total Hindi words produced using **Pearson r** (one-tailed).
A simple OLS regression was also fit to quantify the linear relationship.

### Results

    r(33) = .57,  p = .003,  95% CI [.31, .75]
    Total words = 3.12 + 2.14 * Mean cluster size
    F(1,33) = 16.2,  p < .001,  R^2 = .33

**Decision:** Reject H0.  Mean cluster size explains 33% of the variance in
total fluency score.  Each one-word increase in average cluster size predicts
approximately two additional Hindi words produced overall.

![*RQ2 -- Mean cluster size vs total Hindi fluency score.* Each point = one participant (n = 35). Positive slope (r = .57): participants who exploit subcategory clusters more deeply produce more words overall. OLS regression line with 95% CI. The relationship holds across the full range of cluster sizes observed.](images/vft_fig13_rq3_fluency_scatter.png){width=80%}

## Summary

| # | Test | Statistic | p | Effect | Decision |
|:--|:-----|:---------:|:-:|:------:|:--------:|
| RQ1 | Within- vs between-cluster IRT (Welch t, one-tailed) | t(34) = -8.91 | < .001 | d = 1.51 | Reject H0 |
| RQ2 | Cluster size predicts fluency (Pearson r, one-tailed) | r(33) = .57 | .003 | R^2 = .33 | Reject H0 |

Both confirmatory hypotheses are strongly supported.  The clustering-and-switching
model is robustly replicated in Hindi, and cluster depth is a meaningful
predictor of fluency output.


---


# Exploratory Hypotheses

The following patterns emerged from EDA and are reported as exploratory findings
without adjustment for multiple comparisons.  They are not counted as
confirmatory evidence but inform the design of Phase 2 analyses.

## EH1: Domain-Level IRT Differences

Semantic domain systematically modulates IRT.  Closed-vocabulary domains
(Colours: M = 4975 ms) are substantially faster than open hierarchical domains
(Body-parts: M = 6872 ms).  The pattern is explained by vocabulary size:
larger domains sustain fast within-cluster retrieval for longer before
participants reach the semantic periphery, paradoxically producing more
between-cluster switches that lengthen the tail.  Colours, however, exhausts
its Hindi inventory quickly and suppresses the right tail entirely.

> **EH1 finding:** Closed-class domains (Colours) produce shorter, less-skewed
> IRT distributions than open hierarchical domains (Animals, Foods), consistent
> with vocabulary-size modulation of retrieval dynamics.

## EH2: Serial Position Effect (Lexical Exhaustion)

As participants progress through a trial, their IRTs increase -- a pattern
known as the **lexical exhaustion effect**.  Earlier serial positions access
the most strongly activated, most central category members; later positions
require search into the semantic periphery, which takes longer.

The scatter plots below show word-level IRT plotted against serial position
for each domain, with OLS trend lines.  All four domains show a positive slope.
The gradient is steepest for Colours (small inventory exhausted by position ~8)
and shallowest for Foods (large multi-tier vocabulary sustains fast access for
much longer).

![*Serial position vs IRT by domain.* Each point = one word from one participant. OLS trend line with 95% CI per domain. All four domains show a positive slope (IRT increases with position), confirming the lexical exhaustion effect. The gradient is steepest for Colours and shallowest for Foods, reflecting the relative sizes of their Hindi lexicons.](images/vft_fig07_word_irt_position.png){width=90%}

> **EH2 finding:** IRT increases with serial position in all four domains,
> confirming lexical exhaustion. The rate of increase is inversely proportional
> to domain vocabulary size.

---


# Future Plan: Phase 2 (SpAM)

## Overview

Phase 2 will administer the **Spatial Arrangement Method (SpAM)** to the same
35 participants.  In the SpAM task (Hout, Goldinger & Ferguson, 2013),
participants drag word tokens onto a blank 2-D canvas and arrange them so that
semantically similar words are placed close together and dissimilar words far
apart.  The Euclidean distance between any two word positions in a participant's
arrangement directly indexes their subjective semantic similarity for those words.

Crucially, the SpAM data is already collected -- participants completed the
spatial arrangement as part of the same web-session as the VFT, with their
token placements recorded in the `droppedwords` field of `responses.json`.
Phase 2 therefore requires parsing and analysis rather than new data collection.

## Planned Analyses

**1. Consensus distance matrices (per domain)**

For each domain, pairwise Euclidean distances will be averaged across all 35
participants to compute a consensus semantic proximity matrix.  This produces
a 2-D representation of the "group-level" semantic space for each category.

**2. MDS visualisation and hierarchical clustering**

Multi-Dimensional Scaling (MDS) will project each domain's consensus matrix
into 2-D space for visual inspection.  Agglomerative hierarchical clustering
on the distance matrix will recover the latent subcategory structure (e.g.,
wild animals vs domestic animals within the Animals domain).

**3. RQ3: Cross-task correlation (SpAM distance vs VFT IRT)**

The primary confirmatory test for Phase 2 is:

- **H0:** rho (SpAM distance, VFT IRT) = 0
- **H1:** rho (SpAM distance, VFT IRT) > 0

Word pairs with low SpAM distance (semantically close) should produce short
VFT IRTs (retrieved within the same cluster); word pairs with high SpAM
distance (semantically distant) should produce long VFT IRTs (retrieved across
a switch boundary).  This prediction follows directly from the
clustering-and-switching model.  p-values will be Benjamini--Hochberg corrected
for the four domains tested.

**4. Domain vocabulary-breadth comparison**

Neighbourhood density from the SpAM matrices will be compared across the four
domains to test whether Foods and Animals (which supported deeper VFT clustering)
genuinely have denser, more tightly structured semantic neighbourhoods than
Colours and Body-parts.


---


# References

\begin{thebibliography}{10}

\bibitem{troyer1997}
Troyer, A.\,K., Moscovitch, M., \& Winocur, G. (1997).
Clustering and switching as two components of verbal fluency:
Evidence from younger and older healthy adults.
\textit{Neuropsychology}, \textit{11}(1), 138--146.

\bibitem{hills2012}
Hills, T.\,T., Jones, M.\,N., \& Todd, P.\,M. (2012).
Optimal foraging in semantic memory.
\textit{Psychological Review}, \textit{119}(2), 431--440.

\bibitem{hout2013}
Hout, M.\,C., Goldinger, S.\,D., \& Ferguson, R.\,W. (2013).
The versatility of SpAM: A fast, efficient, spatial measure of semantic
and perceptual similarity.
\textit{Journal of Experimental Psychology: General}, \textit{142}(1), 256--281.

\bibitem{benjamini1995}
Benjamini, Y., \& Hochberg, Y. (1995).
Controlling the false discovery rate: A practical and powerful approach to
multiple testing.
\textit{Journal of the Royal Statistical Society: Series B}, \textit{57}(1),
289--300.

\bibitem{goldstone1994}
Goldstone, R. (1994).
An efficient method for obtaining similarity data.
\textit{Behavior Research Methods, Instruments, \& Computers}, \textit{26}(4),
381--386.

\bibitem{steyvers2005}
Steyvers, M., \& Tenenbaum, J.\,B. (2005).
The large-scale structure of semantic networks: Statistical analyses and a
model of semantic growth.
\textit{Cognitive Science}, \textit{29}(1), 41--78.

\bibitem{bhatt2022}
Bhatt, R., Anderson, N.\,D., \& Bhatt, M. (2022).
Verbal fluency performance in bilingual South Asian older adults.
\textit{Journal of the International Neuropsychological Society}, \textit{28}(4),
412--421.

\end{thebibliography}
