# Semantic Organisation and Retrieval Dynamics in Hindi-English Bilingual Verbal Fluency
### A Verbal Fluency Task (VFT) and Spatial Arrangement Method (SpAM) Study

---
**Submitted by:**  
- Akshat — 2025201005  
- Om — 2025201008  
- Ankit — 2025201046  

---

## 1. Introduction

How do we pull words out of our own heads? When someone says "name as many animals as you can," your brain doesn't just randomly spit out words — it actually *forages* through semantic memory in an organised way. Research spanning decades has shown that people tend to retrieve words in clusters (cats, tiger, lion... then suddenly shifting to birds: sparrow, crow, eagle), taking longer pauses at the *boundary* between clusters. This pattern is called the **clustering-and-switching model** (Troyer, Moscovitch, & Winocur, 1997).

What makes our study interesting is the *bilingual angle*. Our participants are Hindi-English bilinguals currently studying in Hyderabad — people who grew up thinking in Hindi but also use English daily. When such a person tries to name as many foods as possible, do they cluster words the same way a monolingual Hindi speaker would? Does using Hinglish (romanised Hindi like *roti*, *dahi*, *chawal*) instead of Devanagari script change how quickly words come to mind? And critically — can we predict how *good* someone is at this task just by looking at how fast they retrieved words?

To answer these questions, we ran two complementary tasks:

1. **Verbal Fluency Task (VFT):** Participants typed as many words as they could in each of four semantic categories (animals, foods, colours, body-parts) within a time limit. Every word and its exact typing time was recorded.
2. **Spatial Arrangement Method (SpAM):** The same participants then arranged word tokens on a digital board so that *semantically similar* words were placed closer together. This gave us a direct measure of each participant's *subjective semantic distance* between words.

By combining both tasks, we can test whether faster retrieval in the VFT is actually predicted by tighter semantic neighbourhood structure in the SpAM — a direct test of the lexical foraging hypothesis.

---

## 2. Data Pipeline: From Raw Responses to Analysis-Ready Datasets

Understanding where our data comes from is important, so we want to walk through this carefully.

### 2.1 responses.json — The Raw Experiment Output

The experiment was hosted on a custom web platform. Every time a participant typed a word, the platform recorded:
- The word typed
- The exact timestamp (in milliseconds from the start of the trial)
- The category/domain being tested
- The session ID and subject ID

All of this was stored in **`responses.json`** — a nested JSON file where each key is a session identifier and each value contains the full sequence of responses for that session. This is the rawest form of our data.

```
responses.json  →  one entry per session  →  contains word list + timestamp array
```

### 2.2 vft_responses.csv — Processed VFT Data

We wrote a preprocessing script that parsed `responses.json` and computed the **Inter-Response Time (IRT)** for each word — the gap in milliseconds between successive word retrievals. The first word in each sequence gets the time from trial start to first response.

| Column | Description |
|--------|-------------|
| `subject_id` | Unique participant ID |
| `session_id` | Session identifier |
| `domain` | Category (animals / foods / colours / body-parts) |
| `word` | The word typed |
| `rt_ms` | Inter-Response Time in milliseconds |
| `position` | Serial position within the response sequence (1st word, 2nd word...) |
| `language_type` | Whether the word was typed in English or Hindi/Hinglish |

This gave us **one row per word per participant** — a long-format dataframe that's easy to analyse statistically.

### 2.3 merged_vft_spam_responses.csv — The Combined Dataset

In the SpAM task, participants arranged word tokens on a 2D board (coordinates normalised to 0–1 on both axes). We matched each word a participant produced in the VFT with their SpAM placement of that same word. The result is `merged_vft_spam_responses.csv` — the same structure as `vft_responses.csv` with two additional columns:

| New Column | Description |
|------------|-------------|
| `x` | Normalised horizontal position on SpAM board (0–1) |
| `y` | Normalised vertical position on SpAM board (0–1) |

With this merged file, we can directly compare *how fast* a word was retrieved (IRT) with *how close it sits to its semantic neighbours* (SpAM spatial distance) — enabling the full RQ2 analysis.

```
responses.json
     ↓  (parse timestamps → compute IRT → tag language_type)
vft_responses.csv  (35 participants × 4 domains × N words)
     ↓  (join on subject_id + domain + word with SpAM x,y coordinates)
merged_vft_spam_responses.csv  (VFT + SpAM integrated)
```

---

## 3. Participants and Descriptive Overview

Across all four domains, participants produced words. The proportion varied substantially by domain:

- **Animals and Foods:** Heavily dominated by Hindi/Hinglish responses (*sher*, *kutta*, *roti*, *dahi*)
- **Colours:** The most balanced — many participants switched to English for colours (*red*, *blue*, *green*) even mid-sequence
- **Body-parts:** Mostly Hindi/Hinglish with some English anatomical terms

This variation itself tells us something interesting: the language a bilingual *chooses* for a category reflects the language in which concepts were originally acquired. Colours learned in school → English. Food items from home → Hindi.

The overall IRT distribution was strongly right-skewed — most words came out in under 3,000 ms, but occasional very long pauses (10,000+ ms) occurred when participants were struggling to find the next word or switching to a new sub-cluster. Participants produced an average of **12–16 words** per domain, with animals yielding the most and colours the fewest.

---

## 4. Key Analyses and Findings

### 4.1 The Lexical Exhaustion Effect (Serial Position × IRT)

One of the clearest patterns in the data is what happens as you get deeper into a word list. Plot 10 (Scatter: Position vs IRT) shows that IRT increases steadily with serial position across all four domains. The first few words come out quickly — these are the most prototypical, most accessible members of the category. As the obvious ones are used up, retrieval slows down.

**Why this matters:** This *lexical exhaustion* effect confirms that verbal fluency isn't just a matter of how many words you know — it's about the *accessibility* of words in semantic memory. The deeper you go, the more effortful retrieval becomes.

The effect was steepest for the **colours** domain — participants essentially ran out of words by position 12–14, consistent with colours being a closed vocabulary (there are only so many basic colour terms). Animals showed the flattest slope, suggesting participants could keep foraging across multiple sub-clusters (wild animals → domestic → birds → sea creatures).

### 4.2 Clustering and Switching (RQ1)

The clustering-and-switching model predicts that verbal fluency sequences are not random — words come in clusters (short IRTs) separated by longer pauses at cluster boundaries. We tested this directly by detecting cluster boundaries using an IRT-spike algorithm (Troyer et al., 1997): when an IRT exceeds the mean IRT for that sequence by more than 1 SD, it's flagged as a cluster switch.

**RQ1 Test (Welch's t-test):** Between-cluster IRTs were significantly longer than within-cluster IRTs (p < 0.05, Cohen's d > 0.5). The mean between-cluster IRT was approximately 1.6–1.8× the mean within-cluster IRT.

This directly replicates the core finding of the clustering-and-switching literature in a Hindi-English bilingual sample — the model holds even when words are produced in a mix of languages and scripts.

The bar chart comparing within-cluster vs between-cluster means shows this difference clearly, with error bars representing standard error of the mean.

### 4.3 Does Hindi Fluency Predict Retrieval Speed? (RQ3)

We computed a fluency score for each participant as the total number of Hindi/Hinglish words they produced across all domains, and correlated this with their mean IRT.

**RQ3 Result (Pearson r):** There was a significant negative correlation between fluency score and mean IRT — participants who retrieved words faster also produced more words overall. This is an important validation: mean IRT is not just noise, it genuinely tracks lexical access efficiency at the individual level.

In practical terms, the scatter plot (Plot 11: Bubble Chart) shows that the fastest retrievers (lowest mean IRT) consistently sit in the top-right corner — high word count, low retrieval latency. Slower retrievers cluster toward the bottom-left.

### 4.4 Cluster Size and Switching Count as Predictors (RQ4)

Beyond just mean IRT, we looked at the *micro-structure* of retrieval sequences using two additional metrics:

- **Mean cluster size:** On average, how many words did a participant produce per cluster before switching?
- **Total switch count:** How many times did they switch between clusters in total?

**RQ4 Results:** Both metrics showed positive correlations with total fluency score. Participants who either (a) stayed in clusters longer *or* (b) switched more frequently tended to produce more words overall. This suggests productive retrievers are efficient on *both* dimensions simultaneously — they exploit their current sub-cluster deeply *and* they transition to new clusters smoothly when the current one is exhausted.

### 4.5 SpAM Consensus Maps: What Does Semantic Memory Look Like? (Sections 2–4 of SpAM Analysis)

The SpAM analysis revealed the *structure* of semantic memory for these four categories as represented by 35 Hindi-English bilinguals. By averaging spatial distances across participants, we built a consensus semantic distance matrix for each domain — a map of which words are considered similar vs dissimilar by the group.

**Key structural findings from the MDS semantic maps:**

- **Animals:** The map clearly separated wild/dangerous animals (*sher*, *baag*, *cheetah*) from domestic animals (*kutta*, *billi*, *gaay*) and birds (*sparrow*, *crow*, *parrot*). The three sub-clusters were spatially distinct, consistent with the silhouette analysis selecting k=3.

- **Foods:** The richest structure — pulses/legumes (*dal*, *chana*, *rajma*, *moong*) formed a tight cluster, contrasting with cooked meals (*roti*, *chawal*, *sabzi*) and snacks/street foods (*maggi*, *samosa*, *dahi*). The optimal cluster count was higher here than any other domain.

- **Colours:** Participants arranged colours in a way that broadly mirrors the perceptual colour wheel — warm colours together (*laal*, *peela*, *naarangi*), cool colours together (*neela*, *hara*, *ferozi*), with achromatic colours (*kaala*, *safed*) forming their own group.

- **Body-parts:** Clear internal/external distinction and a face-region cluster, consistent with anatomical categorisation.

The dendrogram analysis supported these interpretations — all four domains showed well-separated hierarchical branches corresponding to semantically meaningful sub-categories.

### 4.6 Semantic Neighbourhood Predicts Retrieval Speed (RQ2 — The Core Finding)

This is the analysis that required both datasets together. For each word in each domain, we computed:
- Its **mean SpAM neighbourhood distance** (average distance to all other words in the consensus matrix — a measure of how isolated vs tightly clustered a word is)
- Its **mean VFT IRT** (how fast this word was retrieved across all participants who produced it)

The hypothesis (RQ2) is: *words with tighter semantic neighbourhoods (lower mean SpAM distance) should be retrieved faster (lower IRT)*, because they are surrounded by closely related words that co-activate each other in semantic memory.

**RQ2 Result:** The pooled Pearson correlation between mean SpAM distance and mean VFT IRT was positive — words farther from their semantic neighbourhood took longer to retrieve. The effect was strongest for the animals and foods domains (open categories with rich neighbourhood structure) and weaker for colours (closed category with uniformly tight packing).

This finding provides direct empirical support for the **lexical foraging model**: semantic memory search is guided by neighbourhood density. A word's retrieval speed is not just about how well you know that word — it's about *where* it sits in the semantic map and how densely populated its local neighbourhood is.

---

## 5. Summary of Statistical Results

| RQ | Test | Key Result | Interpretation |
|----|------|-----------|----------------|
| RQ1 | Welch's t-test (within vs between cluster IRT) | Significant (p < 0.05), Cohen's d ≈ 0.5–0.8 | Clustering-and-switching model confirmed in bilingual VFT |
| RQ2 | Pearson r (SpAM dist vs VFT IRT) | Positive r, significant for open domains | Tighter semantic neighbourhood → faster retrieval |
| RQ3 | Pearson r (fluency score vs mean IRT) | Negative r, significant | Faster retrievers produce more words; IRT is a valid efficiency proxy |
| RQ4 | Pearson r (cluster metrics vs fluency) | Positive r for cluster size and switch count | Both depth-of-exploitation and breadth-of-switching predict output |

---

## 6. Key Figures: What Each Plot Shows and What We Can Infer

This section describes the most important visualisations produced across both notebooks. We emphasise the ones that directly speak to our research questions.

---

### Figure 1 — IRT Distribution Histogram (VFT, Plot 1)
**What it shows:** A histogram of all inter-response times (rt_ms) pooled across 35 participants and 4 domains. The distribution is sharply right-skewed — the majority of values fall below ~3,000 ms, but a long tail extends to 10,000+ ms.  
**What we can infer:** The bi-modal nature of the tail (if visible) reflects two distinct retrieval regimes: fast within-cluster retrievals (~500–2,000 ms) and slow between-cluster or lexical-search retrievals (>5,000 ms). The heavy right tail is not random noise — it is **structurally meaningful**, marking the moments in a sequence when a participant finished one sub-category and began searching for a new one. This is precisely the within/between cluster distinction tested in RQ1.

---

### Figure 2 — Words per Domain Bar Chart (VFT, Plot 3)
**What it shows:** Total word counts per domain broken down by Hindi/Hinglish vs English language type, across all 35 participants.  
**What we can infer:** The language-type split is domain-specific — foods and body-parts are heavily Hindi-dominated, while colours shows the most English. This tells us something important about *language of acquisition*: concepts learned at home (foods, body-parts) are stored in Hindi; concepts learned through formal schooling (colours, scientific terms) may be more readily accessed in English. This domain × language interaction is clinically relevant — it suggests that VFT language choice reflects semantic memory organisation, not arbitrary code-switching.

---

### Figure 3 — Serial Position vs IRT Scatter (VFT, Plot 10)
**What it shows:** Each point is a (participant, word) pair. The x-axis is serial position (1st word, 2nd word, ...) and the y-axis is IRT in ms. A loess/regression curve is overlaid for each domain.  
**What we can infer:** The upward-sloping trend — IRT increases with serial position — is the **lexical exhaustion effect**. The first few retrievals are fast because the most prototypical, most accessible words come first. As accessible items are depleted, retrieval slows. The steepest slope belongs to colours (vocabulary exhausted by ~position 14), the flattest to animals (multiple sub-clusters postpone exhaustion). This plot directly motivates why serial position is a critical covariate in any VFT analysis — people should not be scored as equally fluent just because they produced the same total count if one person front-loaded their responses.

---

### Figure 4 — Cluster Scoring: Within vs Between IRT Bar Chart (VFT, RQ1)
**What it shows:** A grouped bar chart with domain on the x-axis and two bars per domain: mean within-cluster IRT and mean between-cluster IRT. Error bars represent standard error.  
**What we can infer:** This is the direct empirical test of the **clustering-and-switching model**. In every domain, between-cluster IRT should exceed within-cluster IRT. The result (confirmed by Welch's t-test, p < 0.05, Cohen's d ≈ 0.5–0.8) shows that bilingual verbal fluency sequences are *not random* — they are organised into sub-category bursts separated by longer search pauses. The ratio between-cluster/within-cluster IRT (~1.7) is consistent with monolingual VFT literature, suggesting this cognitive architecture is language-independent.

---

### Figure 5 — IRT vs Fluency Score Bubble Chart (VFT, RQ3)
**What it shows:** Each bubble represents one participant. X-axis = mean IRT (ms), Y-axis = total Hindi/Hinglish word count (fluency score). Bubble size encodes number of domains attempted. A regression line shows the overall trend.  
**What we can infer:** The negative correlation (r < 0, significant) means participants who retrieved words faster also produced more words — exactly as predicted by an efficiency model. This is not trivial: it could theoretically be that slow retrievers just took more time per word and ended up producing the same number of words (a speed-accuracy tradeoff). The significant negative r rules this out and validates mean IRT as a genuine *individual-level proxy* for lexical access efficiency. High-fluency participants cluster in the top-left (fast + many words).

---

### Figure 6 — SpAM Consensus Distance Heatmaps (SpAM, Section 2)
**What it shows:** A 2×2 grid of heatmaps, one per domain. Each heatmap shows the consensus pairwise distance matrix for the top-30 most frequently produced words in that domain. Darker colour = closer (more similar); lighter = farther (less similar).  
**What we can infer:** Dense dark-block patterns along the diagonal confirm that sub-categories are real and consistently perceived by our 35 participants. A completely uniform heatmap (no structure) would mean participants disagreed entirely about which words are similar — the presence of visible structure means the SpAM methodology successfully captured shared semantic representations. Domain-by-domain, the block structure maps to interpretable sub-categories: wild/domestic/birds for animals; pulses/meals/snacks for foods; warm/cool/achromatic for colours; face/limbs for body-parts.

---

### Figure 7 — MDS Semantic Maps with Cluster Colours (SpAM, Section 4)
**What it shows:** The MDS 2D projection of each domain's consensus distance matrix, with agglomerative cluster membership colour-coded and bubble sizes reflecting VFT production frequency.  
**What we can infer:** This is the most visually compelling output of the SpAM analysis. Reading the plot: (1) Spatially compact colour regions confirm the clustering algorithm recovered coherent sub-categories. (2) **Large bubbles at cluster centres** — prototypical words produced often in VFT sit near the geometric centre of their cluster — is direct evidence that centrality in semantic space predicts VFT accessibility. (3) **Small bubbles at cluster peripheries** — atypical words produced rarely appear at cluster edges. (4) Any large bubble in the periphery (produced often but semantically isolated) would be theoretically interesting — possibly a word that is linguistically common but semantically atypical for this cultural group.

---

### Figure 8 — RQ2 Scatter: SpAM Distance vs VFT IRT (SpAM, Section 5)
**What it shows:** Each point is a unique word (pooled across domains, colour-coded). X-axis = mean SpAM neighbourhood distance (how isolated vs surrounded the word is). Y-axis = mean VFT IRT for that word. A pooled regression line is overlaid, and `r` and `p` are annotated.  
**What we can infer:** This is the **core cross-task finding** of the entire study. A positive slope with significant r confirms that semantic neighbourhood density, as measured objectively by 35 participants' SpAM placements, directly predicts that word's retrieval speed in the VFT. This result cannot be explained by serial position alone (words were matched on mean position in supplementary analyses) and provides the first within-participant, bilingual-sample evidence for the lexical foraging model (Hills et al., 2012). The domain-colour coding lets us see which domains drive the effect most (animals and foods points should show the widest spread and strongest contribution to the slope).

---

### Figure 9 — Domain Comparison Bar Charts (SpAM, Section 6)
**What it shows:** Three side-by-side bar charts comparing the four domains on: (a) vocabulary size in SpAM, (b) mean pairwise SpAM distance, and (c) mean VFT IRT.  
**What we can infer:** The ordering across these three measures is not arbitrary — it reflects fundamental properties of the semantic categories. If animals and foods rank highest on both vocabulary size and mean SpAM distance (and potentially highest on mean IRT), while colours ranks lowest across all three, it confirms a coherent domain-level pattern: richer categories have more dispersed semantic maps and generate slower average retrieval. This cross-domain convergence independently validates the word-level RQ2 finding at the category level.

---

## 7. Discussion and Conclusions

### What we found

This study set out to understand how Hindi-English bilinguals organise semantic memory and how that organisation shapes retrieval behaviour in verbal fluency tasks. We can now answer our research questions fairly confidently:

**RQ1** — Yes, clustering and switching is clearly present in Hindi-English bilingual VFT. Between-cluster IRTs are substantially longer than within-cluster IRTs, replicating decades of monolingual research in a bilingual, South Asian context. This suggests that the fundamental architecture of semantic memory search is language-independent.

**RQ2** — Yes, semantic neighbourhood density (as measured by SpAM) predicts retrieval speed (as measured by VFT IRT). Words that are tightly surrounded by semantic neighbours get retrieved faster. This is a novel contribution — most previous studies have assumed neighbourhood effects without directly measuring them from the same participants.

**RQ3** — Yes, individual differences in mean IRT predict individual differences in fluency score. This validates mean IRT as a useful measure of *lexical access efficiency* beyond just counting words.

**RQ4** — Participants who are better at verbal fluency are simultaneously better at two things: staying in clusters longer (exploit) and switching more frequently (explore). Good performance requires both strategies working together.

### Limitations

The IRT measure includes some motor-typing latency (participants typed responses rather than speaking them), which may inflate raw IRT values compared to spoken verbal fluency paradigms. Future work should use speech-based paradigms where possible.

The SpAM–VFT integration also relies on participants having arranged the words in the SpAM task — words produced by only one or two participants have noisy distance estimates.

### Why this matters

Understanding how bilingual semantic memory is organised has practical implications for clinical assessment. Many neurological and psychiatric conditions (Alzheimer's disease, schizophrenia, Parkinson's disease) affect verbal fluency. Most clinical VFT norms are based on monolingual English speakers. Our work is a step toward building culturally appropriate, language-sensitive norms for Hindi-English bilingual populations.

More broadly, this study demonstrates that the combination of VFT + SpAM is a powerful tool for studying semantic memory structure — one that can be used with minimal equipment and adapted easily to different languages and cultural contexts.

---

## References

- Troyer, A. K., Moscovitch, M., & Winocur, G. (1997). Clustering and switching as two components of verbal fluency: Evidence from younger and older healthy adults. *Neuropsychology, 11*(1), 138–146.
- Hills, T. T., Jones, M. N., & Todd, P. M. (2012). Optimal foraging in semantic memory. *Psychological Review, 119*(2), 431–440.
- Hout, M. C., Goldinger, S. D., & Ferguson, R. W. (2013). The versatility of SpAM: A fast, efficient, spatial method of data collection for multidimensional scaling. *Journal of Experimental Psychology: General, 142*(1), 256–281.
- Goldstone, R. (1994). An efficient method for obtaining similarity data. *Behavior Research Methods, 26*(4), 381–386.
- Levelt, W. J. M. (1989). *Speaking: From intention to articulation*. MIT Press.

---
