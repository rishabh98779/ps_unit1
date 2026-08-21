# Remaining Unit 1 topics: Range, Q.D., Mean Deviation, SD/Variance/CV
from course_data import U, T, Def, Text, ListS, Formulas, Ex, Try, Derive

u1_rest = []

# ---- Range ----
t13 = T("t13", "Lecture 1.4", "Measures of Dispersion — Range", [
  Text("Concept of Dispersion",
    "Averages akela sufficient nahi — do distributions ka mean same ho sakta hai phir bhi variability alag ho (source example: two paddy varieties, both mean yield 42 kg, ek consistent, ek variable — first variety preferable). Dispersion = scatterness of observations from their average."),
  ListS("Characteristics of a good measure of dispersion (source)", [
    "Rigidly defined",
    "Based on all items",
    "Not unduly affected by extreme items",
    "Lends itself to algebraic manipulation",
    "Simple to understand and easy to calculate"]),
  Def("Formal Definition — Range",
    "Range is defined as the difference between the largest and the smallest values of the variable: Range = L − S, where L = largest value and S = smallest value.",
    "Range sabse simple dispersion measure hai — max minus min. Continuous series mein do methods: (M1) extreme classes ki boundaries; (M2) extreme classes ke mid-values.",
    ["L − S","largest","smallest","extreme values"]),
  ListS("Merits and Demerits of Range (source)", [
    "<b>Merits:</b> simple; easy to calculate; widely used in quality control, weather forecasts, share price analysis.",
    "<b>Demerits:</b> affected by extreme items; based on only two observations; open-end classes par fail; not suitable for mathematical treatment; rarely used."]),
  Ex("Example 1 (Exam) — Percentage change in Range <span class='src'>[SOURCE QUESTION]</span>",
    "Weights of 11 forty-year-old men: 148, 154, 158, 160, 161, 162, 166, 170, 180, 195, 236 pounds. If the heaviest man is omitted, find the percentage change in the range.",
    "Extreme value drop karne par impact.", "11 values.",
    "Range before & after.",
    r"\[ R = L - S \]",
    ["Original range = 236 − 148 = 88.",
     "New range (after omitting 236) = 195 − 148 = 47.",
     "% change = (88 − 47)/88 × 100 = 46.6% decrease."],
    "Range decreases by ≈ 46.6%",
    "Range extreme-dependent — iski demerit."),
  Try("Find the range of component lifespans: 100, 120, 130, 140, 150, 160, 180, 200. <span class='src'>[ENRICHMENT FROM COURSE SLIDES]</span>",
    "Max − min.", "Range = 100 hours", ["R = 200 − 100 = 100 hours."]),
])
u1_rest.append(t13)

# ---- Quartile Deviation ----
t14s = []
t14s.append(Def("Formal Definition — Quartile Deviation",
  "Quartile Deviation (Q.D.) is an absolute measure of dispersion based on quartiles; it equals half the difference between the upper (third) and lower (first) quartile — also called the semi-interquartile range: Q.D. = (Q₃ − Q₁)/2.",
  "Q.D. middle 50% of data par based hai — extreme values se almost unaffected.",
  ["(Q₃ − Q₁)/2","semi-interquartile","quartiles"]))
t14s.append(Formulas("Quartiles — Formulas", [
  {"latex": r"\[ Q_1 = \text{value of } \left(\frac{n+1}{4}\right)^{\text{th}} \text{ item} \]", "vars": "individual series."},
  {"latex": r"\[ Q_3 = \text{value of } \left(\frac{3(n+1)}{4}\right)^{\text{th}} \text{ item} \]", "vars": "individual series."},
  {"latex": r"\[ Q_1 = L + \left(\frac{\frac{N}{4} - m}{f}\right) C \]", "vars": "continuous distribution; L, m (preceding c.f.), f, C = class width."},
  {"latex": r"\[ Q_3 = L_3 + \left(\frac{\frac{3N}{4} - m_1}{f_1}\right) C \]", "vars": "continuous distribution."},
  {"latex": r"\[ \text{Inter-quartile range} = Q_3 - Q_1;\quad Q.D. = \frac{Q_3 - Q_1}{2} \]", "vars": ""},
  {"latex": r"\[ \text{Coefficient of Q.D.} = \frac{Q_3 - Q_1}{Q_3 + Q_1} \]", "vars": "Relative comparison measure."}]))
t14s.append(ListS("Advantages / Limitations / Applications (source)", [
  "<b>Advantages:</b> simple; unaffected by extremes; good for skewed/open-end distributions.",
  "<b>Limitations:</b> ignores 50% of observations; less accurate than SD; not algebraically treatable.",
  "<b>Applications:</b> income distribution, business statistics, educational analysis, economic studies."]))
t14s.append(Ex("Example 1 (Standard) — Q₁, Q₃, Q.D. <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Find upper and lower quartiles and the quartile deviation of: 36, 43, 47, 28, 18, 9, 32.",
  "Quartiles locate karke Q.D.", "7 values.",
  "Sorted order mein (n+1)/4 and 3(n+1)/4 positions.", None,
  ["Sorted: 9, 18, 28, 32, 36, 43, 47.",
   "Q₁ = 2nd = 18; Q₃ = 6th = 43.",
   "Q.D. = (43 − 18)/2 = 12.5."],
  "Q₁ = 18, Q₃ = 43, Q.D. = 12.5",
  "Pehle sort, phir formula positions."))
t14s.append(Ex("Example 2 (Standard) — Q.D. with fractional positions <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Find the quartile deviation of: 5, 7, 8, 12, 15, 18, 21, 24, 30.",
  "Fractional position par interpolation.", "n = 9.", None, None,
  ["Q₁ position = 2.5 → Q₁ = (7+8)/2 = 7.5.",
   "Q₃ position = 7.5 → Q₃ = (21+24)/2 = 22.5.",
   "Q.D. = (22.5 − 7.5)/2 = 7.5."],
  "Q.D. = 7.5",
  "Fractional position → interpolation."))
t14s.append(Try("Find quartile deviation for: 2, 4, 6, 8, 10, 12, 14, 16, 18. <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  None, "Q.D. = 5", ["Q₁ = (4+6)/2 = 5; Q₃ = (14+16)/2 = 15; Q.D. = 5."]))
t14s.append(Try("Calculate coefficient of quartile deviation: Q₁ = 20, Q₃ = 50. <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  None, "0.4286", ["(Q₃−Q₁)/(Q₃+Q₁) = 30/70 = 0.4286."]))
t14s.append(Try("Find quartile deviation of: 5, 9, 12, 15, 18, 22, 25, 28. <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  None, "Q.D. = 7.25 (interpolation) <span class='src'>[ANSWER GENERATED]</span>",
  ["Positions 2.25 and 6.75: Q₁ = 9.75, Q₃ = 24.25, Q.D. = 7.25."]))
t14s.append(ListS("Common Mistakes", [
  "Data sort karna bhoolna.",
  "Q.D. ka full (Q₃ − Q₁) lena — half lena hai.",
  "Coefficient formula ka denominator (Q₃+Q₁) bhoolna."]))
t14s.append(ListS("Exam Focus", [
  "Q₁ = (n+1)/4, Q₃ = 3(n+1)/4 — raw data.",
  "Grouped formula with L, m, f, C revise karo.",
  "Coefficient = (Q₃−Q₁)/(Q₃+Q₁) — unit-free."]))
t14 = T("t14", "Lecture 1.4", "Quartile Deviation & Quartiles", t14s)
u1_rest.append(t14)

# ---- Mean Deviation ----
t15s = []
t15s.append(Def("Formal Definition — Mean Deviation",
  "Mean Deviation of a set of observations is the arithmetic mean of the absolute deviations from the mean (or any other specified value A).",
  "Signed deviations ka sum zero hota hai, isliye absolute deviations |x − A| lete hain. Default base = mean.",
  ["arithmetic mean of absolute deviations","|x − x̄|","about mean/median/A"]))
t15s.append(Formulas("Mean Deviation — Formulas", [
  {"latex": r"\[ M.D. \text{ about } A = \frac{1}{n}\sum |x_i - A| \]", "vars": "raw series."},
  {"latex": r"\[ M.D. = \frac{1}{N}\sum f_i |x_i - \bar{x}| \]", "vars": "frequency distribution, N = Σf."}]))
t15s.append(Text("How to Recognize the Question",
  "'About median' → median pehle, phir |x − median| column. Frequency table → fx se x̄, phir f|x − x̄| column."))
t15s.append(Ex("Example 1 (Exam) — M.D. about the Median <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Calculate mean deviation about the median: 8, 15, 53, 49, 19, 62, 7, 15, 95, 77.",
  "Deviations median se; n even.", "10 values.",
  "n = 10 even → median = average of two middle values.",
  r"\[ M.D. = \frac{1}{n}\sum |x_i - \text{median}| \]",
  ["Sorted: 7,8,15,15,(19,49),53,62,77,95 → median = 34.",
   "Absolute deviations: 26,19,19,15,15,28,27,19,61,43 → sum 272.",
   "M.D. = 272/10 = 27.2."],
  "M.D. = 27.2",
  "Even n → two-middle average."))
t15s.append(Ex("Example 2 (Exam) — M.D. for Frequency Distribution <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Find mean deviation: X = 10, 11, 12, 13, 14; frequencies 3, 12, 18, 12, 3.",
  "Weighted mean pehle, phir f|x − x̄|.", "N = 48.",
  "Weighted formula.", None,
  ["Σfx = 576 → x̄ = 12.",
   "|x − x̄| = 2,1,0,1,2; weighted sum = 36.",
   "M.D. = 36/48 = 0.75."],
  "M.D. = 0.75",
  "Symmetric data → mean middle value."))
t15s.append(ListS("Common Mistakes", [
  "Absolute values lena bhoolna.",
  "'About median' ignore karke mean use karna."]))
t15s.append(ListS("Exam Focus", [
  "M.D. = (1/N) Σ f|x − A|; base A question-specified.",
  "Median-based M.D. mein median pehle nikalo."]))
t15 = T("t15", "Lecture 1.5", "Mean Deviation", t15s)
u1_rest.append(t15)

# ---- SD / Variance / CV ----
t16s = []
t16s.append(Def("Formal Definition — Standard Deviation",
  "Standard Deviation is the positive square-root of the arithmetic mean of the squares of the deviations from the arithmetic mean. Denoted by s (sample) and σ (population).",
  "Deviations square karke unka mean (variance) aur phir positive root — squaring signed cancellation avoid karta hai; root se original units wapas.",
  ["positive square root","mean of squared deviations","σ or s"]))
t16s.append(Formulas("Standard Deviation & Variance — Formulas", [
  {"latex": r"\[ s = \sqrt{\frac{1}{n}\sum (x_i - \bar{x})^2} \]", "vars": "raw data."},
  {"latex": r"\[ s = \sqrt{\frac{1}{N}\sum f_i (x_i - \bar{x})^2} \]", "vars": "frequency distribution."},
  {"latex": r"\[ \sigma^2 = \frac{\sum x^2}{n} - \left(\frac{\sum x}{n}\right)^2 \]", "vars": "computational form — reverse problems."},
  {"latex": r"\[ s = C\sqrt{\frac{\sum f d^2}{N} - \left(\frac{\sum f d}{N}\right)^2},\ d=\frac{x-A}{C} \]", "vars": "step-deviation."},
  {"latex": r"\[ \text{Variance} = \sigma^2 \]", "vars": "variance = (S.D.)²"}]))
t16s.append(Text("Population vs Sample (course slides — enrichment)",
  "Population variance: denominator N; sample variance: denominator n−1 (unbiased estimator). Squaring prevents cancellation, weights outliers, minimized at mean (least-squares optimality)."))
t16s.append(ListS("Merits and Demerits of Standard Deviation (source)", [
  "<b>Merits:</b> rigidly defined; based on all observations; most important/widely used; algebraically treatable; stable under sampling; basis for correlation & sampling.",
  "<b>Demerits:</b> hard to understand/calculate; weights outliers (squaring); absolute → non-comparable directly (hence C.V.)."]))
t16s.append(Ex("Example 1 (Challenging) — Recovering Σx² <span class='src'>[SOURCE QUESTION]</span>",
  "S.D. from a set of 32 observations is 5; sum of observations is 80. Find sum of squares.",
  "Computational form reverse use.", "n=32, σ=5, Σx=80.",
  "σ² = Σx²/n − (Σx/n)² rearrange.", None,
  ["25 = Σx²/32 − 6.25.",
   "Σx² = 31.25 × 32 = 1000."],
  "Σx² = 1000",
  "Expanded form 'find Σx²' traps."))
t16s.append(Ex("Example 2 (Exam) — S.D. by Step-Deviation <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Seed yield (grams) of 50 sesamum plants: classes 2.5–3.5, 3.5–4.5, 4.5–5.5, 5.5–6.5, 6.5–7.5; frequencies 4, 6, 15, 15, 10. Find S.D.",
  "Equal-width classed data → step-deviation.", "N=50, A=5, C=1.",
  "d = (x−A)/C; s = C√(Σfd²/N − (Σfd/N)²).", None,
  ["Midpoints 3,4,5,6,7; d: −2,−1,0,1,2.",
   "Σfd = 21, Σfd² = 77.",
   "s = √(77/50 − (21/50)²) = √1.3636 = 1.1677."],
  "s = 1.1677 grams",
  "Step-deviation table = exam backbone."))
t16s.append(Ex("Example 3 (Basic) — Variance from deviations (slides)",
  "Tensile strength of 5 steel samples (N/mm²): 400, 410, 405, 395, 415. Find variance and S.D.",
  "Mean, deviations, squares.", "n = 5.", None, None,
  ["Mean = 405.",
   "Squared deviations sum = 250.",
   "σ² = 250/5 = 50; σ = 7.07."],
  "σ² = 50, σ = 7.07 N/mm²",
  "Mean galat → variance galat. <span class='src'>[SOURCE SLIDE]</span>"))
t16s.append(Ex("Example 4 (Standard) — Sample variance (slides)",
  "Sample of five values: 10, 12, 14, 16, 18. Sample variance and S.D?",
  "Sample denominator n−1.", "n = 5.",
  "s² = Σ(x−x̄)²/(n−1).", None,
  ["Mean 14; squared deviations sum 40.",
   "s² = 40/4 = 10; s = 3.16."],
  "s² = 10, s = 3.16",
  "Sample vs population denominator trap. <span class='src'>[ENRICHMENT FROM COURSE SLIDES]</span>"))
t16s.append(Def("Formal Definition — Coefficient of Variation",
  "The Coefficient of Variation is a relative measure of dispersion obtained by dividing the standard deviation by the mean, expressed as a percentage: C.V. = (σ/x̄) × 100.",
  "S.D. absolute hai — do series different units compare ke lie C.V. Higher C.V. → more variable/less consistent; lower C.V. → more stable.",
  ["(σ/x̄)×100","relative measure","comparison"]))
t16s.append(Ex("Example 5 (Exam) — Coefficient of Variation <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Paddy variety: yield mean 50 kg, SD 10; plant height mean 55 cm, SD 5. Compare variabilities.",
  "Different units → only C.V. comparable.", "Yield (50,10); Height (55,5).",
  "C.V. = (σ/x̄) × 100.", None,
  ["Yield C.V. = 10/50 = 20%.",
   "Height C.V. = 5/55 = 9.1%.",
   "Yield more variable."],
  "Yield (20%) more variable than height (9.1%)",
  "Raw σ se compare mat karo — C.V. only."))
t16s.append(ListS("Common Mistakes (SD/Variance/CV)", [
  "Deviations square karna bhoolna.",
  "Sample data par denominator n instead of n−1.",
  "Variance vs S.D. interchange.",
  "Early rounding of squares.",
  "Different-unit series raw σ se compare karna."]))
t16s.append(ListS("Exam Focus", [
  "σ² = Σx²/n − x̄² — reverse problems.",
  "Step-deviation for grouped data.",
  "Sample: n−1 denominator (slides).",
  "C.V. = (σ/x̄)×100 — higher = more variable."]))
t16 = T("t16", "Lecture 1.5 + Slides", "Standard Deviation, Variance & Coefficient of Variation", t16s)
u1_rest.append(t16)
