# Unit 4 — Random Variables & Probability Distributions
from course_data import U, T, Def, Text, ListS, Formulas, Ex, Try, Derive

u4 = U("u4", "Unit 4 — Random Variables & Probability Distributions",
   "Official course blueprint: Lecture 3.3 Random Variables, 3.4 Binomial, 3.5 Poisson, 3.6 Continuous/Normal distribution.")

# ---- 4.1 Random Variables ----
t41s = []
t41s.append(Def("Formal Definition — Random Variable",
  "A random variable is a real-valued function whose domain is the set of possible outcomes of a random experiment and whose range is a subset of the set of real numbers, with the properties: (I) each particular value of the random variable can be assigned some probability, and (II) the sum of all probabilities associated with all values equals 1 (unity).",
  "Sample space ke outcomes ko real numbers map karte hain — e.g., die twice thrown, X = 'number of odd results' takes 0, 1, 2 with probabilities summing to 1. Notation: capital letters X, Y, Z; 'r.v.' shorthand (source remark).",
  ["real-valued function","domain = outcomes","ΣP = 1"]))
t41s.append(Def("Formal Definition — Discrete Random Variable",
  "A random variable is said to be discrete if it has either a finite or a countable number of values (one-to-one correspondence with the natural numbers).",
  "Countable values = sequence mein arrange — students present per day, defective counts. Fractional values nahi le sakta.",
  ["countable","one-to-one with N","finite or sequence"]))
t41s.append(Def("Formal Definition — Continuous Random Variable",
  "A random variable is said to be continuous if it can take all possible real (integer as well as fractional) values between two certain limits; values cannot be arranged in a sequence.",
  "Temperature over a day, race finish time — uncountable values. Point probability = 0 for continuous r.v.; only interval probabilities calculable (integrals).",
  ["uncountable","real interval","P(X = a) = 0"]))
t41s.append(Def("Formal Definition — Probability Mass Function (p.m.f.)",
  "Let X be a random variable taking values x₁, x₂, … and let P[X = xᵢ] = p(xᵢ). This function p(xᵢ) defined for the values assumed by X is called the probability mass function, satisfying p(xᵢ) ≥ 0 and Σ p(xᵢ) = 1.",
  "p.m.f. discrete variable ke har value ki probability assign karta hai. Distribution set {(xᵢ, p(xᵢ))} se specify hota hai.",
  ["p(xᵢ) ≥ 0","Σp(xᵢ)=1","discrete"]))
t41s.append(Def("Formal Definition — Probability Density Function (p.d.f.)",
  "f(x) is called a probability density function if the probability that X lies in (x, x+dx) equals f(x)dx, with f(x) ≥ 0 and ∫ f(x)dx = 1 over the entire range of X.",
  "Interval probability = integral area. P[a < X < b] = ∫ from a to b of f(x) dx. (Source: P[X takes exact value] = 0 for continuous.)",
  ["f(x) ≥ 0","∫f(x)dx = 1","P[a<X<b]=∫f dx"]))
t41s.append(Def("Formal Definition — Distribution Function (c.d.f.)",
  "A function F defined for all values of a random variable X by F(x) = P[X ≤ x] is called the distribution function; it is the cumulative probability up to and including x. Domain = real numbers; range = [0, 1].",
  "X cumulative probability track karta hai. Discrete c.d.f. = running sum; continuous mein F(x) = integral of p.d.f., and f(x) = F′(x) (source).",
  ["F(x) = P(X ≤ x)","cumulative","range [0,1]"]))
t41s.append(ListS("pmf vs pdf vs cdf (from source text)", [
  "Discrete: p.m.f. p(xᵢ) per value; sum = 1.",
  "Continuous: p.d.f. f(x); point probability = 0; interval probability = integral.",
  "c.d.f. F(x) = P(X ≤ x); F′(x) = f(x) for continuous r.v."]))
t41s.append(Ex("Example 1 (Standard) — Valid probability distribution? <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Check whether these are probability distributions: (i) X: 0, 1 with P(X): 1/2, 3/4; (ii) X: 0,1,2 with P(X): 1/3, −1/4, 3/4; (iii) X: 0..3 with P: 1/8, 3/8, 1/4, 1/8.",
  "Σp = 1 & each p ≥ 0 check karo.",
  None, None, None,
  ["(i) Σp = 1/2 + 3/4 = 5/4 > 1 → not a probability distribution.",
   "(ii) one probability negative → not a distribution.",
   "(iii) Σp = 1/8 + 3/8 + 1/4 + 1/8 = 7/8 < 1 → not a distribution."],
  "None of the given tables is a valid probability distribution",
  "Dono conditions check karo — sign & sum."))
t41s.append(Ex("Example 2 (Exam) — p.d.f. parameter & interval probabilities <span class='src'>[SOURCE QUESTION + GENERATED SOLUTION]</span>",
  "A continuous r.v. X has p.d.f. f(x) = A x³ for 0 ≤ x ≤ 1. Determine (i) A, (ii) P[0.2 < X < 0.5], (iii) P[X > 3/4 | X > 1/2].",
  "(i) total integral 1; (ii) integrate; (iii) conditional rule.",
  "f(x) = A x³ on [0,1].",
  "∫f dx = 1; conditional P(E|F) = P(E∩F)/P(F).",
  r"\[ \int_0^1 A x^3 dx = 1,\quad P[a<X<b] = \int_a^b f dx \]",
  ["A × [x⁴/4]₀¹ = 1 → A = 4.",
   "P[0.2<X<0.5] = 4 × [x⁴/4]₀.₂⁰.⁵ = (0.5)⁴ − (0.2)⁴ = 0.0625 − 0.0016 = 0.0609.",
   "P[X>3/4 & X>1/2] = P[X>3/4] = 1 − (3/4)⁴ = 175/256.",
   "P[X>1/2] = 1 − (1/2)⁴ = 15/16.",
   "Required = (175/256)/(15/16) = 35/48."],
  "A = 4; P(0.2<X<0.5) = 0.0609; conditional probability = 35/48",
  "Conditional probability = intersection rule with p.d.f."))
t41s.append(Ex("Example 3 (Standard) — Distribution function of discrete r.v. <span class='src'>[SOURCE SOLVED]</span>",
  "X takes 0,1,2 with p(x) = 1/4, 1/2, 1/4. Write its distribution function F(x).",
  "Running cumulative sums.",
  None, None, None,
  ["F(0) = 1/4.", "F(1) = 1/4 + 1/2 = 3/4.", "F(2) = 1/4 + 1/2 + 1/4 = 1."],
  "F = {1/4, 3/4, 1}",
  "Last value must be 1."))
t41s.append(Text("Expected Value of a Random Variable (concept from source)",
  "Expected value is the fundamental idea in probability distributions: for a discrete r.v., multiply each value by its probability and sum all products — E(X) = Σ xᵢ p(xᵢ). This is the discrete weighted mean. Applications follow in later parts (source note: daily visa cleared example in unit context)."))
t41 = T("t41","Lecture 3.3","Random Variables, p.m.f., p.d.f. & Distribution Function", t41s)
u4["topics"].append(t41)

# ---- 4.2 Binomial ----
t42s = []
t42s.append(Text("Introduction",
  "Binomial distribution swiss mathematician James Bernoulli (1654-1705) se hua — dichotomous outcomes (success/failure) wale repeated trials. Quality control mein defective probability nikaalne ka standard tool."))
t42s.append(ListS("Binomial law applies only when (source)", [
  "Each trial results in either success or failure",
  "The probability of success p remains constant in each trial",
  "Trials are mutually independent",
  "The number of trials is known (1, 2, 3, …, n)"]))
t42s.append(Formulas("Binomial formula & measures", [
  {"latex": r"\[ P(r) = \binom{n}{r} p^r q^{n-r},\quad q = 1 - p \]", "vars": "P(r) = probability of r successes in n trials."},
  {"latex": r"\[ \binom{n}{r} = \frac{n!}{r!(n-r)!} \]", "vars": "0! = 1."},
  {"latex": r"\[ \mu = n p \]", "vars": "Mean."},
  {"latex": r"\[ \sigma = \sqrt{n p q} \]", "vars": "Standard deviation."}]))
t42s.append(ListS("Characteristics (source)", [
  "Distribution form depends on parameters p and n.",
  "If p < 0.5 → positively skewed; p > 0.5 → negatively skewed; p = q → symmetrical.",
  "Mainly for infinite populations; finite OK if sampling with replacement."]))
t42s.append(Ex("Example 1 (Exam) — Six coin tosses <span class='src'>[SOURCE QUESTION + GENERATED SOLUTION]</span>",
  "A fair coin is tossed six times. What is the probability of obtaining four or more heads?",
  "r = 4, 5, 6 terms sum karo.",
  "n = 6, p = q = 1/2.",
  "P(4)+P(5)+P(6).",
  r"\[ P(r) = \binom{6}{r}(1/2)^6 \]",
  ["P(4) = C(6,4)/64 = 15/64; P(5) = 6/64; P(6) = 1/64.",
   "Sum = (15+6+1)/64 = 22/64 = 11/32 ≈ 0.3438."],
  "P(4 or more heads) = 11/32 ≈ 0.3438",
  "Cumulative range problems → enumerate required r values."))
t42s.append(Ex("Example 2 (Exam) — Mean & S.D. of defective bolts <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "If the probability of defective bolts is 0.1, find the mean and standard deviation for the distribution of defective bolts in a total of 500.",
  "μ = np, σ = √(npq).",
  "n = 500, p = 0.1, q = 0.9.",
  None, None,
  ["μ = 500 × 0.1 = 50.",
   "σ = √(500 × 0.1 × 0.9) = √45 = 6.71."],
  "μ = 50 bolts; σ ≈ 6.71 bolts",
  "npq root — don't square p·q first."))
t42s.append(Text("Fitting a Binomial Distribution (source procedure)",
  "Steps: (i) determine p and q (p = 1−q); (ii) expand (p+q)ⁿ — number of terms = n+1; (iii) multiply each term by N (total frequency) to get expected frequencies. p = q → symmetric; p < 0.5 → positively skewed."))
t42s.append(Ex("Example 3 (Exam) — Fitting binomial & comparing observations <span class='src'>[SOURCE SOLVED]</span>",
  "Eight coins tossed 256 times. Fit binomial with p = q = 1/2 and find theoretical mean and S.D.; observed mean/S.D. computed for comparison.",
  "(p+q)⁸ expansion × N; μ = np, σ = √(npq).",
  "n = 8, N = 256.",
  "Binomial expansion coefficients × 256.",
  None,
  ["Expected counts = 256 × C(8, r) / 256 → C(8,r) integers: 1, 8, 28, 56, 70, 56, 28, 8, 1.",
   "μ = np = 8 × 1/2 = 4; σ = √(8×0.5×0.5) = √2 = 1.414.",
   "Observed: mean 4.062, S.D. 1.462 — close ⇒ fit is good."],
  "μ = 4, σ = 1.414; expected frequencies close to observed",
  "Fit quality → compare expected vs observed. <span class='src'>[SOURCE]</span>"))
t42s.append(Try("a) n=4, p=0.12, find P(0). b) n=10, p=0.40, find P(9). c) n=6, p=0.83, find P(5). <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  "Soch: pick correct r and plug into binomial formula.",
  "a) ≈0.599; b) ≈0.2424; c) ≈0.7944? (verify) <span class='src'>[ANSWER GENERATED]</span>",
  ["a) P(0) = (0.88)⁴ ≈ 0.5997.",
   "b) P(9) = C(10,9)(0.4)⁹(0.6) = 10 × 0.000262144 × 0.6 ≈ 0.00157.",
   "c) P(5) = C(6,5)(0.83)⁵(0.17) = 6 × 0.3939 × 0.17 ≈ 0.4016."]))
t42s.append(Try("Data: 5 coins tossed 3100 times; heads 0..5 with frequencies 32,225,710,1085,820,228. Find expected (fit) and theoretical mean, S.D. <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  "Estimate p from data mean (np), n = 5.",
  "Fit with data mean ≈ Σfx/Σf; expand (p+q)⁵ × 3100. <span class='src'>[ANSWER GENERATED method]</span>",
  None))
t42s.append(ListS("Common Mistakes", [
  "q = 1 − p bhoolna.",
  "Constant-p check ignore karna.",
  "Mean np aur SD √(npq) formulas interchange karna."]))
t42 = T("t42","Lecture 3.4","Binomial Distribution", t42s)
u4["topics"].append(t42)

# ---- 4.3 Poisson ----
t43s = []
t43s.append(Text("Introduction",
  "Poisson (developed by French mathematician Simeon Poisson) counts rare events in a time/space region — deaths/accidents in a specific time, production defects,.absentees per day. Binomial with p very small (< 0.01 even) and n large (> 50) — np constant → Poisson limit."))
t43s.append(Formulas("Poisson formula & measures", [
  {"latex": r"\[ P(r) = \frac{m^r e^{-m}}{r!},\quad m = np \]", "vars": "r = 0,1,2,…; e = 2.7183."},
  {"latex": r"\[ \mu = m = np,\quad \sigma = \sqrt{m} \]", "vars": "Mean = variance = np = m."}]))
t43s.append(ListS("Characteristics (source)", [
  "Discrete — limiting form of binomial.",
  "Range of random variable: 0 ≤ r < ∞.",
  "Single parameter m; entire distribution known from m.",
  "Positively skewed; skewness decreases as m increases."]))
t43s.append(Ex("Example 1 (Exam) — Defective toys <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "2% of electronic toys in a manufacturing process turn out defective. What is the probability that a shipment of 200 toys will contain exactly 5 defectives? Also find mean and S.D.",
  "Small p, large n → Poisson with m = np.",
  "n = 200, p = 0.02, m = 4.",
  "P(5) = m⁵e⁻ᵐ/5!.",
  r"\[ P(r) = \frac{m^r e^{-m}}{r!} \]",
  ["P(5) = (4⁵ × e⁻⁴)/120 = (1024 × 0.0183)/120 = 0.156.",
   "Mean = 4; σ = √4 = 2."],
  "P(5 defectives) ≈ 0.156; μ = 4; σ = 2",
  "n large + p small → Poisson approximation saves factorial work. <span class='src'>[SOURCE]</span>"))
t43s.append(Ex("Example 2 (Challenging) — Binomial vs Poisson comparison <span class='src'>[SOURCE SOLVED]</span>",
  "Probability of defects in each tool is 0.02. Find probability of exactly 4 defective tools in a sample of 30 using (i) Binomial, (ii) Poisson.",
  "Compare exact vs approximation.",
  "n = 30, p = 0.02.",
  "Both formulas side by side.",
  None,
  ["(i) Binomial P(4) = C(30,4)(0.02)⁴(0.98)²⁶ = 27405 × 1.6e-7 × 0.59 = 0.00259.",
   "(ii) Poisson: m = np = 0.6; P(4) = (0.6⁴ e⁻⁰.⁶)/24 ≈ 0.00296."],
  "Binomial = 0.00259; Poisson ≈ 0.00296 — close approximation",
  "Poisson approximation accuracy n small p par hi realistic. <span class='src'>[SOURCE]</span>"))
t43s.append(Text("Fitting a Poisson Distribution (source procedure)",
  "Procedure: (1) get mean m = np from data; (2) compute P(r) = m^r e⁻ᵐ/r!; (3) multiply each probability by total frequency N → expected frequencies."))
t43s.append(Try("On average 2% of bulbs are defective. If 100 produced per day, probability that 4 bulbs are defective? <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  "m = np = 2.",
  "P(4) = (2⁴ e⁻²)/24 ≈ 0.0902 <span class='src'>[ANSWER GENERATED]</span>",
  ["P(4) = (16/24) × e⁻² = (2/3) × 0.1353 ≈ 0.0902."]))
t43s.append(Try("400 car ACs inspected; defects per set: 0,1,2,3,4,5 with frequencies 142,156,69,27,5,1. Find expected frequencies (Poisson fit). <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  "Compute data mean m ≈ Σfx/400, then P(r)×400.",
  "Method: mean ≈ (156+2*69+3*27+4*5+5*1)/400 = (156+138+81+20+5)/400 = 400/400 = 1 → expected ≈ 400 × e⁻¹/r!. <span class='src'>[ANSWER GENERATED method]</span>",
  None))
t43s.append(ListS("Common Mistakes", [
  "m = np nikaalte time p se multiply na karna.",
  "Poisson applicable check na karna (p small, n large).",
  "σ = √m instead of √(npq)."]))
t43 = T("t43","Lecture 3.5","Poisson Distribution", t43s)
u4["topics"].append(t43)

# ---- 4.4 Normal ----
t44s = []
t44s.append(Text("Introduction",
  "Continuous random variable = infinite possible values in a range (reservoir level example in source). Normal distribution = most versatile continuous distribution — defined by two parameters μ (mean) and σ (S.D.)."))
t44s.append(ListS("Characteristics of Normal Distribution (source)", [
  "Unimodal — single peak, bell-shaped.",
  "Symmetric (skewness = 0) — mean, median, mode all same.",
  "Two tails extend indefinitely but never touch the horizontal axis."]))
t44s.append(Formulas("Standard normal conversion", [
  {"latex": r"\[ Z = \frac{X - \mu}{\sigma} \]", "vars": "Z = number of standard deviations from X to the mean."}]))
t44s.append(Formulas("Areas under the normal curve (source)", [
  {"latex": r"\[ \mu \pm 1\sigma : 68\%\ (34.13\% \text{ each side}) \]", "vars": ""},
  {"latex": r"\[ \mu \pm 2\sigma : 95.5\%\ (47.75\% \text{ each side}) \]", "vars": ""},
  {"latex": r"\[ \mu \pm 3\sigma : 99.7\%\ (49.85\% \text{ each side}) \]", "vars": ""},
  {"latex": r"\[ \text{Total area under curve} = 1 \]", "vars": ""}]))
t44s.append(Text("Using the Standard Normal Table (source steps)",
  "Step 1: convert X to Z = (X − μ)/σ. Step 2: look up table value (area between 0 and Z). Right of positive Z area = 0.5 − table; left of positive Z = 0.5 + table; symmetric for negative values."))
t44s.append(Ex("Example 1 (Standard) — Reading the table <span class='src'>[SOURCE SOLVED]</span>",
  "(a) Find the area under the normal curve for Z = 1.54. (b) Z = −1.46. (c) Area to the right of Z = 0.25. (d) Area to the left of Z = 1.83.",
  "Table value = area between mean and Z.",
  None, None, None,
  ["(a) area 0.4382.",
   "(b) symmetry → 0.4279.",
   "(c) 0.5 − 0.0987 = 0.4013.",
   "(d) 0.5 + 0.4664 = 0.9664."],
  "(a) 0.4382 (b) 0.4279 (c) 0.4013 (d) 0.9664",
  "Right side subtract 0.5; left side add 0.5."))
t44s.append(Ex("Example 2 (Exam) — Soldiers above six feet <span class='src'>[SOURCE SOLVED]</span>",
  "Mean height of soldiers = 68.22 inches, variance = 10.8. How many in a regiment of 1000 would be over six feet (72 in) tall?",
  "Z = (72 − 68.22)/√10.8.",
  "σ = √10.8 = 3.286.",
  "Right-tail area = 0.5 − table(Z).",
  None,
  ["Z = 3.78/3.286 ≈ 1.15 → table = 0.3749.",
   "Right area = 0.5 − 0.3749 = 0.1251.",
   "Expected = 1000 × 0.1251 = 125.1 ≈ 125."],
  "About 125 soldiers over six feet",
  "Variance diya hai → σ = √variance pehle. <span class='src'>[SOURCE]</span>"))
t44s.append(Ex("Example 3 (Exam) — Training programme durations <span class='src'>[SOURCE SOLVED]</span>",
  "Mean time of a normally distributed programme = 500 hours, S.D. = 100 hours. Find probability that a participant will take: (i) fewer than 570 hours; (ii) between 430 and 580 hours.",
  "Convert to Z, use 0.5 ± table logic.",
  "μ = 500, σ = 100.",
  "(i) left area; (ii) combined symmetric side areas.",
  None,
  ["(i) Z = 70/100 = 0.7 → table 0.2580 → total = 0.5 + 0.2580 = 0.7580.",
   "(ii) Z₁ = −70/100 = −0.7 → 0.2580; Z₂ = 80/100 = 0.8 → 0.2881; total = 0.5461."],
  "(i) ≈ 75.8%; (ii) ≈ 54.6%",
  "Two-sided intervals → add both table values. <span class='src'>[SOURCE]</span>"))
t44s.append(ListS("Purpose & applications (source)", [
  "Fit distribution of measurement, approximate binomial & Poisson, sampling distributions (mean, variance).",
  "Initial discovery: studying random errors in astronomical orbit computations.",
  "Industrial quality control, testing of significance, sampling distribution, graduation of non-normal curve."]))
t44s.append(Try("Standard normal: find probability (a) Z < 1.08, (b) Z > −0.21, (c) between mean and +1.08, (d) between mean & 1.06 minus? (source list partially garbled). <span class='src'>[SOURCE]</span>",
  "0.5 ± table logic.",
  "Answers depend on table values — use Z-table. <span class='src'>[QUESTION PARIALLY INCOMPLETE IN SOURCE]</span>",
  None))
t44s.append(Try("Normal with μ = 100, σ = 10: find (a) P(X>75) (b) P(X<70) (c) P(X>112) (d) P(75<X<85)? (e) P(X<80 or X>110). <span class='src'>[SOURCE PRACTICE QUESTION]</span>",
  "Compute each Z then table.",
  "Z values: −2.5, −3, 1.2 → typical answers derive from table. <span class='src'>[ANSWER GENERATED method]</span>",
  None))
t44s.append(ListS("Common Mistakes", [
  "Area right of positive Z → 0.5 − table (not table).",
  "Variance se σ nikaalna bhoolna.",
  "Symmetry misuse for negative Z."]))
t44 = T("t44","Lecture 3.6","Continuous Probability Distributions — Normal", t44s)
u4["topics"].append(t44)
