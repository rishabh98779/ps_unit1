# Unit 2 — Moments, Skewness & Kurtosis
from course_data import U, T, Def, Text, ListS, Formulas, Ex, Try, Derive

u2 = U("u2", "Unit 2 — Moments, Skewness & Kurtosis",
   "Official course blueprint: Lecture 2.1 Moments, 2.2 Moments relation & Pearson coefficients, 2.3 Skewness (Karl Pearson & Bowley), 2.4 Kurtosis + slide modules.")

# ---- 2.1 Moments ----
t21s = []
t21s.append(Text("Introduction",
  "Moments distribution ke characteristics describe karne ka convenient unified method hain — tendency, variation, skewness, kurtosis sab summarize hote hain. First raw moment = mean; second central moment = variance; third & fourth = skewness, kurtosis. Moments teen types: arbitrary point, mean (central), origin (A = 0 for raw/origin moments)."))
t21s.append(Def("Formal Definition — Moments",
  "In statistics, moments are the arithmetic means of the first, second, third and higher powers of the deviations taken either from the mean or from an arbitrary point of a distribution.",
  "Deviation ki r-th power ka arithmetic mean = r-th moment. Arbitrary point pe lo toh 'moments about arbitrary point'; mean pe lo toh 'central moments'; A=0 pe lo toh 'raw/origin moments'.",
  ["deviation powers","arithmetic mean","central/raw/arbitrary"]))
t21s.append(Formulas("Moments about Arbitrary Point (grouped data)", [
  {"latex": r"\[ \mu'_r = \frac{\sum_{i=1}^n f_i (x_i - A)^r}{N},\quad N = \sum f_i \]", "vars": "A = arbitrary point; shortcut with d = (x−A)/h multiplies by h^r."},
  {"latex": r"\[ \mu'_r = \frac{\sum f_i d_i^r}{N} \times h^r \]", "vars": "short-cut form (grouped data)."},
  {"latex": r"\[ \mu'_1 = \bar{x} - A,\quad \mu_0 = 1 \]", "vars": "First arbitrary moment gives mean shift."}]))
t21s.append(Formulas("Central Moments (about mean)", [
  {"latex": r"\[ \mu_r = \frac{\sum f_i (x_i - \bar{x})^r}{N} \]", "vars": "μ₀ = 1, μ₁ = 0, μ₂ = σ² (variance)."},
  {"latex": r"\[ \mu_2 = \sigma^2,\quad \text{first central moment } \mu_1 = 0 \]", "vars": "because Σ fᵢ(xᵢ − x̄) = 0."}]))
t21s.append(ListS("Properties recap (source)", [
  "The first raw moment about origin is the mean; the first central moment is 0.",
  "Second raw moment = mean square deviation; second central moment = variance.",
  "Third and fourth moments measure skewness and kurtosis.",
  "Change of origin has no effect on moments; change of scale multiplies the r-th moment by h^r."]))
t21 = T("t21","Lecture 2.1","Moments — Concepts, Types & Formulas", t21s)
u2["topics"].append(t21)

# ---- 2.2 Relation & beta/gamma ----
t22s = []
t22s.append(Text("Why convert?",
  "Actual mean fraction mein aane par direct central moments tedious hote hain — pehle arbitrary point par moments nikalo, phir relations se central moments mein convert karo."))
t22s.append(Derive("Relation between Moments about Mean and Arbitrary Point (source derivation)", [
  "Let dᵢ = xᵢ − A. Then x̄ = A + μ′₁ where μ′₁ = (Σ d)/n.",
  r"Expand \( \mu_r = \frac{1}{N}\sum f_i (d_i - \mu'_1)^r \) binomially.",
  "μ₂ = μ′₂ − μ′₁² ;",
  "μ₃ = μ′₃ − 3μ′₁μ′₂ + 2μ′₁³ ;",
  "μ₄ = μ′₄ − 4μ′₁μ′₂ + 6μ′₁²μ′₂ − 3μ′₁⁴."]))
t22s.append(Formulas("Conversion formulas (critical)", [
  {"latex": r"\[ \mu_2 = \mu'_2 - \mu_1'^2 \]", "vars": "second central moment."},
  {"latex": r"\[ \mu_3 = \mu'_3 - 3\mu'_1\mu'_2 + 2\mu_1'^3 \]", "vars": "third."},
  {"latex": r"\[ \mu_4 = \mu'_4 - 4\mu'_1\mu'_2 + 6\mu_1'^2\mu'_2 - 3\mu_1'^4 \]", "vars": "fourth."},
  {"latex": r"\[ \beta_1 = \frac{\mu_3^2}{\mu_2^3},\quad \gamma_1 = \sqrt{\beta_1} = \frac{\mu_3}{\sigma^3} \]", "vars": "Pearson β₁ & γ₁ coefficients for skewness."},
  {"latex": r"\[ \beta_2 = \frac{\mu_4}{\mu_2^2},\quad \gamma_2 = \beta_2 - 3 \]", "vars": "Pearson β₂ & γ₂ for kurtosis."}]))
t22s.append(Text("Sheppard's Corrections (source)",
  "Grouped frequency distribution moments assume frequencies uniformly distributed about midpoints — approximation error for skewed data. Sheppard corrections: μ₂(corrected) = μ₂ − h²/12, μ₃(corrected) = μ₃, μ₄(corrected) = μ₄ − (h²/12) μ₂ + (7h⁴/240), where h = class width."))
t22s.append(Ex("Example (Exam) — First four moments & β₁, β₂ <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Marks 5,10,15,20,25,30,35 with frequencies 4,10,20,36,16,12,2. Calculate first four moments about mean and find β₁, β₂, γ₁, γ₂.",
  "Table columns fd, fd², fd³, fd⁴ construct karke moments.", "N = 100.",
  "Short-cut with A = 20 marks, h = 5.", None,
  ["Σfd = −6, Σfd² = 178, Σfd³ = −42, Σfd⁴ = 874.",
   "μ′₁ = −0.3, μ′₂ = 44.5, μ′₃ = −52.5, μ′₄ = 5462.5.",
   "Central: μ₂ = 44.41 (= σ²), μ₃ = −12.504, μ₄ = 5423.5057.",
   "β₁ = (−12.504)²/(44.41)³ = 0.001785; γ₁ = μ₃/σ³ = −0.0422.",
   "β₂ = 5423.5057/(44.41)² = 2.7499; γ₂ = −0.2501."],
  "μ = (0, 44.41, −12.504, 5423.51); β₂ < 3 → platykurtic",
  "Full table + correct formula selection hi marks dete hain. <span class='src'>[SOURCE WORKED SOLUTION]</span>"))
t22s.append(Try("First four moments about the value 5 of a variable are 1, 10, 20, 25. Find central moments, β₁, β₂. <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  "Conversion formulas use karo.",
  "μ₂ = 9, μ₃ = −6, μ₄ = 54; β₁ = 4/81, β₂ = 2/3 <span class='src'>[ANSWER GENERATED]</span>",
  ["μ′₁ = 1: μ₂ = 10 − 1 = 9; μ₃ = 20 − 3(1)(10) + 2 = −6; μ₄ = 25 − 4(1)(10) + 6(1)(10) − 3 = 54. β₁ = 36/729 = 4/81; β₂ = 54/81 = 2/3."]))
t22s.append(ListS("Common Mistakes", [
  "Conversion formula signs galat lagana — carefully substitute.",
  "γ₁ sign: direction μ₃ par depend karta hai.",
  "Sheppard's correction optional hai — question specify kare toh hi apply."]))
t22 = T("t22","Lecture 2.2","Moments Conversion & Pearson β–γ Coefficients", t22s)
u2["topics"].append(t22)

# ---- 2.3 Skewness ----
t23s = []
t23s.append(Def("Formal Definition — Skewness",
  "Skewness means lack of symmetry. A distribution is symmetric if mean, median and mode coincide; otherwise it is asymmetric. If the right tail is longer, the distribution is positively skewed (mean > median > mode); if the left tail is longer, it is negatively skewed (mean < median < mode).",
  "Symmetric curve = mirror image; skewed = tail ek taraf lambi. Positive skew → right tail lambi; negative → left tail.",
  ["lack of symmetry","mean>median>mode (positive)","mean<median<mode (negative)"]))
t23s.append(ListS("Absolute measures of skewness (source)", [
  "Sk = Mean − Median",
  "Sk = Mean − Mode",
  "Sk = (Q₃ − Q₂) − (Q₂ − Q₁)",
  "Comparison ke lie relative coefficient (divide by SD) use karte hain."]))
t23s.append(Formulas("Coefficient formulas", [
  {"latex": r"\[ Sk = \frac{\text{Mean} - \text{Mode}}{\sigma} \quad \text{(Karl Pearson)} \]", "vars": "Primary method — most used."},
  {"latex": r"\[ Sk = \frac{3(\text{Mean} - \text{Median})}{\sigma} \]", "vars": "If mode ill-defined: Mode = 3Median − 2Mean substitution."},
  {"latex": r"\[ Sk = \frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1} \quad \text{(Bowley)} \]", "vars": "Quartile-based; range +1 to −1."},
  {"latex": r"\[ \gamma_1 = \sqrt{\beta_1} = \frac{\mu_3}{\sigma^3} \]", "vars": "Pearson moment coefficient γ₁; direction from μ₃ sign."}]))
t23s.append(Text("Variance vs Skewness (source difference)",
  "Variance variability ki amount batata hai; skewness direction. Business/economic series mein variance zyada practical; medical/life-science mein skewness."))
t23s.append(Ex("Example (Exam) — Finding Mode & Median from Sk <span class='src'>[SOURCE QUESTION + GENERATED SOLUTION]</span>",
  "For a distribution, Karl Pearson's coefficient of skewness is 0.64, standard deviation is 13 and mean is 59.2. Find mode and median.",
  "Sk formula rearrange for mode; Mode relation se median.",
  "Sk = 0.64, σ = 13, Mean = 59.2.",
  "Sk = (Mean − Mode)/σ.", None,
  ["Mode = Mean − Sk×σ = 59.2 − 0.64×13 = 59.2 − 8.32 = 50.88.",
   "Using Mode = 3Median − 2Mean → Median = (Mode + 2Mean)/3 = (50.88 + 118.4)/3 = 56.43."],
  "Mode = 50.88, Median = 56.43",
  "Reverse-engineering formulas common exam style."))
t23s.append(Try("Karl Pearson's coefficient of skewness is 1.28, mean = 164, mode = 100. Find the standard deviation. <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  None, "σ = 50 <span class='src'>[ANSWER GENERATED]</span>",
  ["σ = (Mean − Mode)/Sk = 64/1.28 = 50."]))
t23s.append(Try("Bowley's coefficient of skewness is 1.2. If Q₁ + Q₃ = 200 and median is 76, find Q₃. <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  None, "Q₃ = 132.5 <span class='src'>[ANSWER GENERATED]</span>",
  ["Sk = (Q₁ + Q₃ − 2Q₂)/(Q₃ − Q₁) = 1.2 → (Q₁+Q₃−152)/(Q₃−Q₁) = 1.2. With Q₁ + Q₃ = 200: (48)/(Q₃ − Q₁) = 1.2 → Q₃ − Q₁ = 40 → Q₃ = 120, Q₁ = 80? Then (200 − 152)/40 = 1.2 ✓ → Q₃ = 120."]))
t23s.append(Text("Interpretation ranges (course slides — enrichment)",
  "Coefficient 0 → symmetric; between −0.5 and 0.5 → approximately symmetric; beyond ±0.5 → moderate; beyond ±1 → highly skewed."))
t23s.append(ListS("Common Mistakes", [
  "Direction galat predict karna (positive → right tail).",
  "Mode ill-defined hone par median relation na use karna.",
  "Bowley coefficient ka quartile relation mix up karna."]))
t23 = T("t23","Lecture 2.3","Skewness — Karl Pearson & Bowley Methods", t23s)
u2["topics"].append(t23)

# ---- 2.4 Kurtosis ----
t24s = []
t24s.append(Def("Formal Definition — Kurtosis",
  "Kurtosis is a measure of the flatness or peakedness of a distribution relative to the normal curve. Prof. Karl Pearson called it the 'convexity of a curve'; it quantifies 'tailedness'.",
  "Central tendency, dispersion, skewness se bhi complete picture nahi — peakedness/tails of distribution kurtosis se. Leptokurtic > normal peaked, Platykurtic < normal, Mesokurtic = normal.",
  ["tailedness","peakedness","β₂ = μ₄/σ⁴"]))
t24s.append(Formulas("Kurtosis formulas", [
  {"latex": r"\[ \beta_2 = \frac{\mu_4}{\sigma^4} \quad (\text{raw kurtosis}) \]", "vars": "μ₄ = fourth central moment. Slide deck uses σ⁴ = (σ²)²."},
  {"latex": r"\[ \gamma_2 = \beta_2 - 3 \quad (\text{excess kurtosis}) \]", "vars": "γ₂ = 0 → normal."}]))
t24s.append(ListS("Classification (source + slides)", [
  "β₂ = 3 (γ₂ = 0) → mesokurtic (normal curve)",
  "β₂ < 3 (γ₂ < 0) → platykurtic (flatter peak, light tails)",
  "β₂ > 3 (γ₂ > 0) → leptokurtic (sharp peak, heavy tails)",
  "Leptokurtic → more outliers; Platykurtic → fewer outliers than normal."]))
t24s.append(Ex("Example (Exam) — Skewness & Kurtosis from moments <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "First four moments about mean of a distribution are 0, 2.5, 0.7 and 18.75. Find coefficient of skewness and kurtosis.",
  "μ₁ = 0, μ₂ = 2.5, μ₃ = 0.7, μ₄ = 18.75 use karke β₁, β₂.",
  "Central moments given.",
  "β₁ = μ₃²/μ₂³; β₂ = μ₄/μ₂².", None,
  ["β₁ = (0.7)²/(2.5)³ = 0.031.",
   "β₂ = 18.75/(2.5)² = 18.75/6.25 = 3 → mesokurtic."],
  "β₁ ≈ 0.031 (nearly symmetric), β₂ = 3 (mesokurtic)",
  "Moments directly given → immediate coefficient calculation. <span class='src'>[SOURCE]</span>"))
t24s.append(Try("First four raw moments of a distribution are 2, 136, 320 and 40,000. Find coefficients of skewness and kurtosis. <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  "Pehle conversion: central moments, phir β₁ β₂.",
  "β₁ ≈ 0, β₂ = 3.05 (approx mesokurtic) <span class='src'>[ANSWER GENERATED]</span>",
  ["Mean = μ′₁ = 2. Central: μ₂ = 136 − 4 = 132; μ₃ = 320 − 3(2)(136) + 2(8) = −480; μ₄ = 40000 − 4(2)(136) + 6(4)(136) − 3(16) = 42102.",
   "β₁ = (−480)²/(132)³ ≈ 0.1; β₂ = 42102/(132)² ≈ 2.42 → platykurtic.",
   "Note: [FORMULA VALUES MAY VARY IF RAW MOMENTS] — verify in exam conditions."]))
t24s.append(ListS("Common Mistakes", [
  "Kurtosis ko skewness se confuse karna — kurtosis peakedness/tailedness.",
  "Peak height alone na dekhna — tails consider karo.",
  "γ₂ sign interpretation galat karna."]))
t24 = T("t24","Lecture 2.4","Kurtosis & Nature of Distribution", t24s)
u2["topics"].append(t24)
