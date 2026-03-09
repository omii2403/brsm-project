# Hindi Verbal Fluency � Mid-Project Speaker Script

> **How to use this:** Read each section out loud as-is. The slide heading tells you when to advance.

---

## SLIDE 1 � Title

Good morning everyone. Our project is titled **"Hindi Verbal Fluency"** and today we are presenting our mid-project report for the BRSM course here at IIIT Hyderabad.

My name is Akshat Kotadia, and I am presenting along with Om Mehra and Ankit Chavda.

Our project has two phases. The **first phase � the Verbal Fluency Task, or VFT � is complete.** The second phase � the SpAM spatial arrangement task � is planned and will be executed next.

Today we will walk you through the experiment design, how we collected and processed the data, the hypotheses we are testing, our exploratory findings, and finally the results of our two hypothesis tests.

---

## SLIDE 2 � Agenda

Let me quickly give you a roadmap of the presentation.

We will cover **six sections:**

First, we explain the experiment itself � the design, the four semantic domains, and who our participants are.

Second, we explain the data � the web platform we built, how the pipeline works, how many responses we got, and the language mix.

Third, we formally state our **two research hypotheses** before showing any results.

Fourth, we go through the **exploratory analysis** � the IRT distribution, domain-wise breakdowns, the serial position effect, and cluster scoring.

Fifth, we briefly outline the **SpAM phase** that is planned next.

And sixth, we show the **statistical results** for both hypotheses with figures.

---

## SLIDE 3 � Experimental Design

So let's start with the experiment.

This is a **within-subjects, repeated-measures design.** Every participant completed all four domain trials � the same person does Animals, Foods, Colours, and Body-parts. This is important because it removes individual variability when we compare across domains.

Our **independent variable** is the semantic domain � four levels. Our **primary dependent variable** is the Inter-Response Time, or IRT, measured in milliseconds. IRT is simply the time between two consecutive ENTER keypresses. So if a participant types "cow" and then 2 seconds later types "horse", the IRT for "horse" is 2,000 milliseconds. Our secondary DV is the total word count � how many words someone produces in one minute.

Each trial lasts exactly **one minute.** The order is fixed: Animals, then Foods, then Colours, then Body-parts. Before the real trials, participants do a one-minute warm-up on the "Furniture" category � just to get comfortable with the task.

Now, why these four domains?

**Animals** is an open-ended category � wild animals, domestic animals, birds � very large vocabulary, very strong clustering tendency.

**Foods** has the richest sub-structure � pulses, meals, snacks, condiments � and is the most culturally Hindi-specific category.

**Colours** is unusual � it is a **closed vocabulary,** roughly ten to fifteen terms. This means it gets exhausted very fast and shows a very different retrieval pattern compared to the others.

**Body-parts** has internal and external sub-clusters, a face sub-cluster, and is heavily mixed between Hindi and English anatomical terms.

In terms of measurement scales � domain, gender, state, and language tag are **nominal.** Serial position within the retrieval sequence is **ordinal.** The SpAM spatial coordinates are **interval.** IRT, word count, and education years are all **ratio** scale � they have a true zero.

---

## SLIDE 4 � Data Collection Platform

Now let me explain how we actually collected the data.

We built a **custom web-based experiment.** Participants opened the experiment in a browser, read Hindi-language instructions, and began the task � consent was implicit via the start button.

All the data is stored in a file called **responses.json.** Let me explain what is inside.

For each participant, we have a numeric subject ID, the trial type, the domain name, the list of responses with their language tags, and most importantly an array called **response_times** � this is the raw timestamp array in milliseconds for every single ENTER keypress.

The IRT for any word is simply: the timestamp of that word minus the timestamp of the previous word. For the very first word, IRT is measured from the moment the trial starts.

We also capture the **SpAM phase data** � after the fluency task, participants drag word tokens around a blank canvas and spatially arrange them by perceived similarity. For each word, we record normalised x and y coordinates, giving us a spatial map of their semantic knowledge.

This file covers **35 participants,** with sub-second precision � down to about 100 milliseconds. Because this is a bilingual population, both Devanagari script and Latin script words were accepted.

---

## SLIDE 5 � Participants & Demographics

Let me now describe who participated.

We have **35 participants** in total � all Hindi-speaking students.

The gender breakdown is **32 male and 3 female.** We acknowledge this is heavily skewed � it reflects IIIT Hyderabad's institutional gender composition, not a deliberate choice. Because of the very small female group, we do not run any gender-based comparisons � the statistical power would simply be too low.

The **mean age is 23.1 years,** standard deviation 1.9, with a range from 19 to 27. This is a tight, homogeneous age band � all young adults in the same academic environment.

**Mean education is 16.5 years,** standard deviation 1.7, ranging from 14 to 20 years. Most participants have completed at least a bachelor's degree.

The participants come from **14 different Indian states.** The most represented are Gujarat with 7, Madhya Pradesh with 6, Bihar with 5, and Maharashtra with 4. States span North, Central, East, and South India. This gives us natural geographic and dialectal diversity � which we treat as natural variance since we are not testing dialect effects.

All participants are **native or highly proficient Hindi speakers.** Sampling was convenience-based within IIIT Hyderabad.

---

## SLIDE 6 � Demographics Figure

This figure summarises those demographics visually in four panels.

Panel A is the **gender pie chart** � you can clearly see the 32 to 3 imbalance.

Panel B is the **age histogram** � centred around 23, with a mean of 23.1 and SD of 1.9 � a roughly normal distribution in a narrow range.

Panel C is the **education bar chart** � showing the spread from 14 to 20 years, centred at 16.5.

Panel D shows the **state-of-origin distribution** � Gujarat, MP, and Bihar are the top three. Blue represents North and Central India, orange represents South and East.

---

## SLIDE 7 � Data Pipeline

Now let me walk you through how we went from the raw JSON file to analysis-ready data.

We start with **responses.json** � 35 participants, nested arrays of VFT timestamps and SpAM spatial coordinates.

**Step one:** We parse the response_times array and compute IRTs. For each word at position i, IRT equals the timestamp at position i minus the timestamp at position i minus one.

**Step two:** We tag the language of each response. Any word in Devanagari script is tagged Hindi. Any word in Latin script is tagged English.

This gives us **vft_responses.csv** � one row per word, with columns for subject ID, domain, word, response time in milliseconds, serial position, and language tag.

**Step three:** We filter to keep only Hindi-tagged words. This gives us our primary analysis dataset � we call it **df_hh** � which contains **712 valid Hindi IRTs.** This is 53% of all responses. The remaining 47% are English responses, kept as supplementary context.

**Step four:** We apply the cluster detection algorithm. Following Troyer and colleagues 1997, we flag a cluster switch whenever the IRT for a word exceeds that participant's own mean IRT plus one standard deviation. This is an **adaptive, per-participant threshold** � it does not impose a universal cutoff, which would be biased by individual typing speed differences.

**Step five:** We merge in the SpAM spatial coordinates to produce **merged_vft_spam_responses.csv** � 1,040 rows, with x and y coordinates ready for Phase 2.

---

## SLIDE 8 � Response Counts & Language Mix

Now let's look at the data itself.

**How many Hindi responses did we get per domain?**

Animals: 238. Foods: 256 � the highest. Colours: only 41 � by far the smallest, because it is a closed-category vocabulary. Body-parts: 177. Total: **712 Hindi responses.**

Now why is Colours so low? This connects directly to the language mix.

When we look at what percentage of responses per domain are in Hindi versus English, we see something very interesting.

For **Foods, 77% of responses are Hindi** � the highest. Food vocabulary is deeply embedded in Indian culture and is retrieved naturally in Hindi.

For **Animals, 64% Hindi.** Also high.

For **Body-parts, around 55% Hindi.**

But for **Colours � only 28% Hindi, and 72% English.** English colour loanwords like *red, blue, green, orange* are simply more lexically accessible for this bilingual cohort. People have heard and used "red" far more than "laal" in everyday life.

Overall, **53% of all responses are Hindi and 47% are English.** Nearly half the data is code-switched � which is entirely natural for bilingual Hindi speakers in an urban academic setting. This is not a data quality problem � it is a key characteristic of the participant pool that we explicitly document.

Our primary analysis is restricted to the 712 Hindi responses.

---

## SLIDE 9 � Research Hypotheses

Now � before we show any results � we formally state our two research hypotheses. Both are **directional and one-tailed,** meaning we committed to a direction before looking at the data. This is important for statistical integrity.

---

**Research Question 1: Does within-cluster IRT differ from between-cluster IRT?**

Null hypothesis: mean within-cluster IRT equals mean between-cluster IRT � no difference.  
Alternative hypothesis: mean within-cluster IRT is **strictly less than** between-cluster IRT. One-tailed.

The rationale: If semantic memory is organised into subcategories � say, wild animals, domestic animals, birds � then words within one subcategory should be retrieved quickly in close succession, giving short IRTs. But when a subcategory exhausts and the person must jump to a new one, that transition pause should be longer. This is the core prediction of the **clustering-and-switching model** by Troyer and colleagues from 1997.

We test this with **Welch's independent-samples t-test** � Welch's rather than Student's, because the two groups have different variances.

---

**Research Question 2: Does mean cluster size predict total verbal fluency?**

Null hypothesis: the correlation between cluster size and fluency is zero.  
Alternative: the correlation is **greater than zero** � one-tailed positive.

The rationale: A participant who stays within a cluster for longer retrieves more words per unit time. Fewer switches means fewer costly between-cluster pauses, so more total words within the one-minute window.

We test this with **Pearson correlation with Benjamini-Hochberg correction.**

---

Both hypotheses are pre-specified from the clustering-and-switching theoretical framework � not generated post-hoc.

---

## SLIDE 10 � VFT Analysis Section Divider

We now move into the actual results.

A quick summary of what we are analysing: **712 valid Hindi IRTs, across 4 semantic domains, from 35 participants, each given exactly 1 minute per domain.**

---

## SLIDE 11 � IRT Distribution: Histogram

Let's look at the overall IRT distribution across all 712 Hindi responses.

Looking at this histogram, the distribution is **strongly right-skewed.** You can see a dense peak on the left � those are the fast within-cluster retrievals � and a long tail extending far to the right � those are slow between-cluster pauses and lexical exhaustion pauses.

The key statistics:

The **mean is 6,490 milliseconds.** The **median is 5,389 milliseconds.** The **mode is around 6,410 milliseconds.** The standard deviation is 5,019 milliseconds � which is almost 77% of the mean itself. That is enormous variability, and it tells you the distribution is not homogeneous.

The minimum IRT is **733 ms** � about three-quarters of a second � the fastest a person can type a word and press Enter. The maximum is **42,634 ms** � over 42 seconds � an extreme between-cluster switching pause.

The **skewness is 2.54** � strongly positive, confirming the visual right skew.

The **kurtosis is 9.89** � this is a leptokurtic distribution. The tails are far heavier than a normal distribution. This tells us the data is a **mixture of two regimes:** fast within-cluster responses piling up on the left, and slow between-cluster pauses forming the heavy right tail. This two-regime shape is the exact fingerprint of the clustering-and-switching model.

Why do we report the **median rather than the mean?** Because with skewness of 2.54, the mean is pulled upward by extreme values. The median of **5,389 ms** is our preferred central tendency � it is robust to outliers.

---

## SLIDE 12 � IRT by Domain: Raincloud Plots

Now let's compare the IRT distributions **across the four domains** using raincloud plots.

A raincloud plot combines three things in one panel: the kernel density curve � the half-violin � showing the full distributional shape; the box plot showing median and IQR; and the raw individual data points jittered below. This gives us the most complete picture of the data without hiding anything.

Looking at the domain medians:

**Colours has the lowest median � 3,484 ms.** It is significantly faster than all other domains. Why? Because it is a closed vocabulary. There are roughly ten to fifteen Hindi colour terms. Once you have said *laal, neela, peela, haara, safed, kaala* � you are essentially done. The distribution is tight and compressed because there is no deep sub-structure to exploit.

**Body-parts has the highest median � 5,724 ms.** This is the slowest domain. Anatomical vocabulary in Hindi is split � everyday terms like *haath* and *pair* are easy, but less-common terms require more search. On top of that, English equivalents like *heart, liver, kidney* compete with Hindi terms, creating bilingual lexical competition that slows retrieval.

**Animals and Foods** are in between � medians of 5,414 and 5,205 ms � and both show large right tails from cluster-switch pauses at subcategory boundaries.

The **right-skewed shape in every single domain** is the canonical signature of the clustering-and-switching model � which is itself strong preliminary validation even before formal hypothesis testing.

---

## SLIDE 13 � Serial Position Effect

This figure shows the relationship between **serial position** � the rank of a word within the trial � and the IRT for that word.

Every dot here is one word produced by one participant at a given rank. The OLS regression lines are fitted independently per domain.

The key finding: **all four trend lines slope upward.** The later a word is produced in the trial, the longer it takes to retrieve. This is the **serial position effect** � also called **lexical exhaustion.**

Think of it like foraging. At the start of the trial, the semantic neighbourhood is fresh and fully populated � words are easy to access, IRTs are short. As you retrieve more words, you deplete the nearby neighbourhood. You must reach further into less-accessible areas, and each step costs more time.

**Colours has the steepest slope.** By around the 10th word, most Hindi colour terms are exhausted. Each additional word from that point requires a genuine effortful search � or a switch to English. So costs rise steeply.

**Foods has the shallowest slope.** Foods has a deeply hierarchical structure � pulses, snacks, meals, condiments, beverages � five or six richly populated sub-clusters. You can keep retrieving at relatively low cost for much longer before exhaustion sets in.

This slope ordering matches exactly what we would predict from the vocabulary depth of each domain � strong convergent evidence that we are measuring a genuine cognitive process.

---

## SLIDE 14 � Cluster Scoring

This figure shows two cluster-level metrics: **mean cluster size** and **mean number of switches per trial.**

First, a critical validation point. The mean cluster size is **above 1 for all four domains.** Why does this matter? If lexical retrieval were random � just pulling words from memory in no particular order � clusters of size 1 would dominate. The fact that cluster sizes are consistently between 4 and 5.6 means participants are reliably producing words in **semantically coherent bursts.** Retrieval is organised, not random.

Looking at the numbers:

**Foods has the largest mean cluster size � 5.58.** The hierarchical structure of food vocabulary lets participants stay within a subcategory for longer before switching.

**Colours has the smallest � 4.06.** The closed vocabulary forces frequent switches. There are simply not enough Hindi colour terms to sustain a long in-cluster run.

Animals is 5.02 and Body-parts is 5.24, both in between.

The **overall mean cluster size is 4.99** � the typical participant produces about 5 words per cluster.

For the switch count � participants switch subcategory approximately **1.9 times per trial** on average. Nearly twice per one-minute session. This is entirely consistent with what the clustering-and-switching model predicts.

---

## SLIDE 15 � Mid-Project Summary & Next Steps

Let me now summarise where we are and where we are going.

On the **completed side:**

We have collected data from 35 participants, processed 712 Hindi IRTs, built the full pipeline, explored the data with four plot types, and run both hypothesis tests. Everything in Phase 1 is done.

On the **planned side � Phase 2, the SpAM analysis:**

Once the spatial arrangement data is processed, we will compute **consensus distance matrices** � averaging pairwise distances between words across 35 participants per domain � and visualise them as heatmaps showing block structure.

We will run **Multidimensional Scaling** to create 2-dimensional semantic geometry maps. Then **hierarchical clustering** with silhouette score optimisation to identify the natural number of clusters per domain.

Finally, the key Phase 2 test � **RQ4:** does SpAM spatial distance predict VFT inter-response time? The conjecture is: words placed closer together on the canvas will show shorter IRTs when produced consecutively � because spatial proximity reflects semantic proximity in memory.

---

## SLIDE 16 � Hypothesis Test RQ1: Within-Cluster vs Between-Cluster IRT

Now the formal results for **Research Question 1.**

This bar chart shows mean IRT for within-cluster responses versus between-cluster responses, broken down by domain. Error bars are standard errors.

The pattern is immediately clear: **BC IRT is approximately twice WC IRT across every single domain.** This is not domain-specific � it is universal.

The numbers:

**Within-cluster mean IRT: 4,752 milliseconds.** Under 5 seconds. **Between-cluster mean IRT: 9,418 milliseconds.** Over 9 seconds.

The ratio is **1.98** � between-cluster switching takes almost exactly twice as long as within-cluster retrieval.

We tested this with **Welch's independent-samples t-test,** one-tailed as pre-specified.

Result: **t(34) = -8.91, p less than .001.** The p-value is far below any conventional alpha threshold.

More importantly: **Cohen's d is 1.51.** By Cohen's 1988 conventions, 0.8 is large. 1.51 is a very large effect. This is not just statistically significant � it is **substantively large** and practically meaningful.

**Decision: We reject the null hypothesis.** Within-cluster IRT is significantly shorter than between-cluster IRT. The clustering-and-switching model is replicated in a Hindi-speaking population � providing cross-linguistic generalisability for the model.

Foods shows the largest absolute gap between BC and WC � consistent with its richly branched subcategory structure giving sharp semantic boundaries.

---

## SLIDE 17 � Hypothesis Test RQ2: Cluster Size & Fluency

Now **Research Question 2.**

We are testing whether participants who form larger semantic clusters also produce more total words.

The result: **Pearson r = 0.57, p = 0.005, one-tailed, N = 35.**

The **r-squared is 0.33** � cluster size explains **33% of the variance** in verbal fluency. For a single predictor in a cognitive science study, this is a moderate-to-large shared variance.

The **95% confidence interval is 0.31 to 0.75** � this interval comfortably excludes zero, giving strong confidence in the positive direction.

**Decision: We reject the null hypothesis.** There is a significant positive correlation between cluster size and fluency.

The regression equation is: **Total words = 3.12 + 2.14 times mean cluster size.** For every one-unit increase in mean cluster size, a participant produces approximately **2 additional words** in the one-minute trial.

What does this mean? Participants with better-organised, more densely connected semantic sub-networks can stay within a subcategory longer before switching. Fewer costly between-cluster transitions means more cognitive resources available for within-cluster retrieval � translating directly into more total words produced.

In plain terms: **clustering efficiency drives verbal fluency.** This result maps onto a clear cognitive mechanism, not just a statistical association.

---

## SLIDE 18 � Thank You

That brings us to the end of our mid-project presentation.

To summarise the two key results:

**RQ1 � Welch's t-test:** Cohen's d = 1.51, p less than .001. Between-cluster IRT is nearly twice within-cluster IRT. The clustering-and-switching model holds in Hindi.

**RQ2 � Pearson r:** r = .57, r-squared = .33, 95% CI from 0.31 to 0.75, p = .005. Cluster size explains 33% of fluency variance. Better-organised semantic memory predicts higher word output.

**Next step:** SpAM Phase 2 � spatial arrangement task analysis, MDS, hierarchical clustering, and RQ4 cross-task correlation.

Thank you. We are happy to take any questions.
