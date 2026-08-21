# -*- coding: utf-8 -*-
# Course content authored from /workspace/probability_statistics_raw_source.md
# Section types: def, text, list, formula, example, try, derive

CO_TABLE = [
 ("CO1","BT3","To understand fundamental concepts of probability theory and statistics"),
 ("CO2","BT4","Identify and formulate engineering problems in different situations involving probabilistic and statistical measures"),
 ("CO3","BT5","Classify various types of statistical methods and perform statistical inference"),
 ("CO4","BT4","Apply appropriate statistical tools, distributions including correlation and regression analysis techniques"),
 ("CO5","BT5","Implement standard concepts and tools at an intermediate to advanced level for tackling problems in hypothesis testing"),
]

DATA = {"units": []}

def U(id, title, sub): return {"id": id, "title": title, "sub": sub, "topics": []}
def T(id, code, title, sections): return {"id": id, "code": code, "title": title, "sections": sections}
def Def(title, formal, hinglish, keywords=None): return {"type": "def", "title": title, "formal": formal, "hinglish": hinglish, "keywords": keywords or []}
def Text(title, body): return {"type": "text", "title": title, "body": body}
def ListS(title, items): return {"type": "list", "title": title, "items": items}
def Formulas(title, items): return {"type": "formula", "title": title, "items": items}  # items: {latex, vars, note}
def Ex(title, problem, asked=None, given=None, method=None, formula=None, steps=None, answer=None, tip=None):
    e = {"type": "example", "title": title, "problem": problem, "asked": asked, "given": given, "method": method, "formula": formula, "steps": steps, "answer": answer, "tip": tip}
    return e
def Try(problem, hint=None, answer=None, solution=None): return {"type": "try", "problem": problem, "hint": hint, "answer": answer, "solution": solution}
def Derive(title, steps): return {"type": "derive", "title": title, "steps": steps}

# ============================= UNIT 1 =============================
u1 = U("u1", "Unit 1 — Basic Statistics: Central Tendency & Dispersion",
   "Official course blueprint: Lectures 1.1–1.5 + slide modules (Introduction, Central Tendency, Combined/Weighted Mean, Dispersion, Mean Deviation, Standard Deviation, Variance, Coefficient of Variation).")

# ---- Topic 1.1 ----
t11 = T("t11", "Lecture 1.1", "Introduction to Statistics & Probability", [
  Text("Introduction", "Course ka yeh opening lecture do foundation concepts set karta hai — probability random events ke mathematical rules ka study hai, aur statistics usi probability ko real data par apply karne ka tool hai. Poori course ka base yahi hai, isliye definitions exam mein seedha poochhi jaati hain."),
  Def("Formal Definition — Probability",
      "Probability theory is the study of the mathematical rules that govern random events.",
      "Probability ka matlab hai random events (jinka outcome bina observe kiye pakka nahi hota) ko mathematical rules se analyze karna. Toss, die, experiment outcomes — in sab ke liye probability batati hai ki given assumptions ke saath hum kya conclude kar sakte hain."),
  Text("What is Randomness?", "Informally, a random event is an event in which we do not know the outcome without observing it. Probability tells us what we can say about such events, given our assumptions about the possible outcomes. <span class='src'>[SOURCE]</span>"),
  Def("Formal Definition — Statistics",
      "Statistics is the application of probability to the collection, analysis, and description of random data.",
      "Statistics raw data ko collect, analyze aur describe karne ke liye probability ki theory use karta hai. Iski help se hum experiments design karte hain, data summarize karte hain aur conclusions nikaalte hain."),
  ListS("Statistics is used to (source list)", [
    "Design experiments",
    "Summarize data",
    "Make conclusions about the world",
    "Explore complex data"]),
  ListS("Applications of Probability & Statistics (source list)", [
    "Computer Science — Machine Learning, Data Mining, AI, Simulation, Image Processing, Computer Graphics, Visualization, Software Testing, Algorithms",
    "Electrical Engineering — Signal Processing, Telecommunications, Information Theory, Control Theory, Instrumentation/Sensors, Hardware Testing",
    "General — Gambling (not recommended), Stock Market, Politics, Sports, Demographics, Medicine, Economics, All Sciences"]),
  Text("Engineering slide notes (enrichment from course slides)", "Statistics is the science of collecting, analyzing, and interpreting numerical data. It transforms raw engineering measurements into actionable insights. Descriptive statistics summarize data sets (e.g., material strength, temperature readings); inferential statistics allow prediction of future performance based on sample data. Engineering applications include quality control, reliability analysis and process optimization. <span class='src'>[ENRICHMENT FROM COURSE SLIDES]</span>"),
  Text("Historical note (source)", "Alan Turing — 'Father of Computer Science' — wrote a dissertation on probability theory and used probability and statistics to crack the Enigma code during WWII."),
])

# ---- Topic 1.2 ----
t12_sections = []
t12_sections.append(Text("Central Tendency — Concept",
  "Jab data compare karna ho ya summarize karna ho, toh poori dataset ko ek single value mein condense karte hain — yahi value 'center' ko represent karti hai, isliye ise <b>measure of central tendency</b> (ya average) kaha jata hai. Yeh distribution ki X-axis par location batata hai, isliye ise <b>measure of location</b> bhi kehte hain. Source mein teen main averages cover hain: <b>Mean, Median, Mode</b>. (Types listed in source: Arithmetic Mean, Geometric Mean, Harmonic Mean, Median, Mode — lectures focus on the arithmetic mean plus median and mode.)"))
t12_sections.append(Def("Formal Definition — Arithmetic Mean",
  "Arithmetic Mean is a value obtained by dividing the sum of all the observations by the number of observations.",
  "Mean basically poore data ka single representative hota hai: sab values ka sum, divided by kitni values hain. Example: marks 45,32,37,46,39,36,41,48,36 (n=9) ka sum 360 hai, toh mean = 360/9 = 40. <span class='src'>[SOURCE EXAMPLE]</span>",
  ["sum of observations","number of observations","x̄ = Σx/n","average"]))
t12_sections.append(Text("Population vs Sample (source terminology)",
  "A <b>population</b> is the entire collection of objects (books, cars, people, all games of a player, etc.). A <b>sample</b> is a subset of the population. Mean/median/mode computed on the entire population are called population mean/median/mode; computed on a sample they are called sample mean/median/mode. Exam mein terminology confusion avoid karo — 'sample mean' aur 'population mean' ka symbol context clear rakho."))
t12_sections.append(Formulas("Arithmetic Mean — Formulas", [
  {"latex": r"\[ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} \quad \text{(ungrouped / raw data)} \]", "vars": r"\(x_i\) = observations, \(n\) = number of observations, \(\bar{x}\) = mean."},
  {"latex": r"\[ \bar{x} = \frac{\sum f_i x_i}{\sum f_i} \quad \text{(direct method, grouped data)} \]", "vars": r"\(f_i\) = frequencies, \(x_i\) = values (or class midpoints for continuous data), \(n = \sum f_i\)."},
  {"latex": r"\[ \bar{x} = A + \frac{\sum f_i d_i}{\sum f_i}, \quad d_i = x_i - A \quad \text{(short-cut method)} \]", "vars": r"\(A\) = assumed mean, \(d_i = x_i - A\)."},
  {"latex": r"\[ \bar{x} = A + \left(\frac{\sum f_i u_i}{\sum f_i}\right) h, \quad u_i = \frac{x_i - A}{h} \quad \text{(step-deviation method)} \]", "vars": r"\(h\) = class width, \(u_i\) = coded deviation."}]))
t12_sections.append(Text("Which Method Should I Use? (method selection in Hinglish)",
  "(1) <b>Direct method</b>: raw/discrete data ya jab numbers chhote hain — straightforward. (2) <b>Short-cut method</b>: jab values bade hain aur unme se ek convenient assumed mean \(A\) pick kar sakte ho — deviations chhote ban jaate hain. (3) <b>Step-deviation method</b>: grouped/continuous data jab class width \(h\) same ho — \(u=(x-A)/h\) deviations ko integers mein convert kar deta hai. Exam mein 'using short-cut method' ya 'step deviation method' explicitly bola jaye toh wohi method follow karna mandatory hai."))
t12_sections.append(ListS("Properties of Arithmetic Mean (source)", [
  "The mean of a constant is that constant.",
  "Sum of deviations from the mean is zero: Σ(xᵢ − x̄) = 0.",
  "Sum of squared deviations from the mean is minimum: Σ(xᵢ − x̄)² < Σ(xᵢ − A)² for any arbitrary A.",
  "Mean is affected by change of origin and scale (adding/multiplying each value by a constant changes the mean accordingly)."]))
t12_sections.append(ListS("Advantages & Disadvantages of Arithmetic Mean (source)", [
  "<b>Advantages:</b> readily understood; easy computation (needs only sum and count); no need to arrange data; can be treated algebraically (combined mean of groups possible); stable under sampling fluctuations.",
  "<b>Disadvantages:</b> cannot be obtained by inspection; needs exact values of all observations (open-end classes problematic); highly affected by extreme values; may not be an actual observed value (e.g., 2.54 children per family)."]))
t12_sections.append(Ex("Example 1 (Basic) — Mean of raw data <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Calculate the arithmetic mean for the marks obtained by 9 students: 45, 32, 37, 46, 39, 36, 41, 48, 36.",
  "Examiner raw data ka mean expect karta hai — direct formula.",
  "9 values; n = 9, Σx = 360.",
  "Raw (ungrouped) data given hai, isliye x̄ = Σx/n.",
  r"\[ \bar{x} = \frac{\sum x_i}{n} \]",
  ["Σx = 45+32+37+46+39+36+41+48+36 = 360.",
   "x̄ = 360/9 = 40."],
  "Mean = 40 marks",
  "Raw data mein direct Σx/n karo. Intermediate Σx table show karna exam-safe hai."))
t12_sections.append(Ex("Example 2 (Standard) — Grouped data, Direct Method <span class='src'>[SOURCE QUESTION + GENERATED SOLUTION]</span>",
  "Weights (grams) of 60 apples: classes 65–84, 85–104, 105–124, 125–144, 145–164, 165–184, 185–204 with frequencies 9, 10, 17, 10, 5, 4, 5. Find the mean.",
  "Grouped frequency distribution diya hai, midpoint nikaal ke direct method.",
  "N = Σf = 60.",
  "Class intervals hain, isliye midpoints xᵢ le lo aur x̄ = Σfx/Σf apply karo.",
  r"\[ \bar{x} = \frac{\sum f_i x_i}{\sum f_i} \]",
  ["Midpoints: 74.5, 94.5, 114.5, 134.5, 154.5, 174.5, 194.5.",
   "fx: 670.5, 945, 1946.5, 1345, 772.5, 698, 972.5 (Σfx = 7350).",
   "x̄ = 7350/60 = 122.5."],
  "x̄ = 122.5 grams",
  "Grouped data mein fx column ka table exam mein zaroor banao."))
t12_sections.append(Ex("Example 3 (Standard) — Short-Cut Method <span class='src'>[SOURCE QUESTION + GENERATED SOLUTION]</span>",
  "Same apple-weight distribution as Example 2. Find mean using the short-cut method with assumed mean A = 114.5.",
  "Deviation-based shortcut.",
  "A = 114.5.",
  "Values large hain, toh assumed mean se deviations chhote karte hain.",
  r"\[ \bar{x} = A + \frac{\sum f_i d_i}{\sum f_i},\ d_i = x_i - A \]",
  ["d: −40, −20, 0, 20, 40, 60, 80.",
   "fd: −360, −200, 0, 200, 200, 240, 400, Σfd = 480.",
   "x̄ = 114.5 + 480/60 = 114.5 + 8 = 122.5."],
  "x̄ = 122.5 grams (same as direct method — verification)",
  "Class midpoints equal difference (20) par hain toh short-cut convenient hai."))
t12_sections.append(Ex("Example 4 (Standard) — Step-Deviation Method <span class='src'>[SOURCE QUESTION + GENERATED SOLUTION]</span>",
  "Same distribution. Find mean by the step-deviation method (h = 20, A = 114.5).",
  "Devations ko h se divide karke integers banate hain.",
  "h = 20, A = 114.5.",
  "Equal class width → step deviation sabse fast.",
  r"\[ \bar{x} = A + \left(\frac{\sum f_i u_i}{\sum f_i}\right)h,\ u_i = \frac{x_i-A}{h} \]",
  ["u: −2, −1, 0, 1, 2, 3, 4.",
   "fu: −18, −10, 0, 10, 10, 12, 20 → Σfu = 24.",
   "x̄ = 114.5 + (24/60)×20 = 114.5 + 8 = 122.5."],
  "x̄ = 122.5 grams",
  "Step-deviation mein answer same aana chahiye — cross-check ka practice karo."))
t12_sections.append(Def("Formal Definition — Median",
  "When the observations are arranged in ascending or descending order, then a value that divides a distribution into two equal parts is called the median.",
  "Median woh middle value hai jo data ko aadhe-aadha parts mein split karta hai jab data ascending order mein ho. Mean extreme values se distort ho jaata hai (e.g., 4 workers earning ₹5000–8000 and supervisor ₹20000 → mean ₹9400, but 4 out of 5 earn much less than ₹9400), isliye median robust alternative hota hai. <span class='src'>[SOURCE EXAMPLE]</span>",
  ["ascending order","middle value","splits into two equal parts","robust to outliers"]))
t12_sections.append(Formulas("Median — Formulas (raw data)", [
  {"latex": r"\[ \text{If } n \text{ odd: } M = \left(\frac{n+1}{2}\right)^{\text{th}} \text{ observation} \]", "vars": "n = number of observations (after arranging in order)."},
  {"latex": r"\[ \text{If } n \text{ even: } M = \frac{\left(\frac{n}{2}\right)^{\text{th}} + \left(\frac{n}{2}+1\right)^{\text{th}}}{2} \]", "vars": "Average of two middle observations."}]))
t12_sections.append(Ex("Example 5 (Standard) — Median of ungrouped data <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Find the median marks (out of 15) obtained by 35 students; the frequency table's cumulative arrangement shows the 18th observation equals 7 (source table).",
  "Frequency table se cumulative position identify karna.",
  "n = 35 (odd).",
  "n odd → (n+1)/2 = 18th observation is the median.",
  r"\[ M = \left(\frac{n+1}{2}\right)^{\text{th}} \text{observation} \]",
  ["(35+1)/2 = 18th observation.",
   "18th observation = 7 (from the cumulative count of the frequency table)."],
  "Median = 7 marks",
  "Frequency table mein median find karna hai toh cumulative frequencies compare karo."))
t12_sections.append(ListS("Advantages & Disadvantages of Median (source)", [
  "<b>Advantages:</b> easy to understand and calculate; works even with open-end or unequal-width classes; applicable to qualitative/ranked data (psychological and social studies).",
  "<b>Disadvantages:</b> data must be arranged; cannot be treated algebraically (composite median of groups not derivable); unsuitable when extreme values need weightage; grouped-data interpolation assumes uniform distribution inside the median class; more affected by sampling fluctuations than the mean."]))
t12_sections.append(Def("Formal Definition — Mode",
  "The observation that occurs most frequently in the data is called the mode.",
  "Mode woh value hai jiski frequency maximum hoti hai — e.g., shirt size 105 cm sold the most this week → company produces more of that size. Garment/shoe industries mode-based decisions use karte hain. <span class='src'>[SOURCE EXAMPLE]</span>",
  ["maximum frequency","most frequent value","modal value"]))
t12_sections.append(Text("Remarks on Mode (source)",
  "(1) If each observation has the same frequency, the data has no mode. (2) If two or more values tie for maximum frequency, the distribution is bimodal/multimodal. (3) Example: 9, 6, 8, 9, 10, 7, 12, 15, 22, 15 — both 9 and 15 have frequency 2 → two modes. <span class='src'>[SOURCE EXAMPLE]</span>"))
t12_sections.append(ListS("Advantages & Disadvantages of Mode (source)", [
  "<b>Advantages:</b> obtainable by inspection; unaffected by extreme values; computable from open-end classes if the modal class and adjoining classes (equal width) are available.",
  "<b>Disadvantages:</b> meaningless for few observations; may not exist or may not be unique; hard to locate exactly from grouped data (formula only approximate for equal-width classes with a clear maximum); not algebraically treatable."]))
t12_sections.append(Ex("Example 6 (Basic) — Mode by inspection <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Goals scored by a football team in 12 matches: 1, 2, 2, 3, 1, 2, 2, 4, 5, 3, 3, 4. Find the modal score.",
  "Highest frequency wali value.",
  "12 observations.",
  "Inspection — count frequencies.",
  None,
  ["Frequency of 2 is 4; all others occur fewer times."],
  "Mode = 2",
  "Raw data ho toh mode inspection se fast ho jaata hai."))
t12_sections.append(Try("Find the mode of: 5, 10, 3, 7, 2, 9, 6, 2, 11, 2. <span class='src'>[SOURCE PRACTICE QUESTION]</span>", None, "Mode = 2 (frequency 3)", None))
t12_sections.append(Def("Formal Definition — Combined Mean",
  "When two or more groups have different means and different numbers of observations, the mean of the combined group is called the Combined Mean (also known as Composite Mean).",
  "Jab alag-alag groups ke individual means aur sizes pata hon, toh overall mean combined mean formula se nikalta hai — simple average of means galat hoga kyun ki group sizes alag hain.",
  ["n₁x̄₁ + n₂x̄₂","weighted by group size","composite mean"]))
t12_sections.append(Formulas("Combined Mean", [
  {"latex": r"\[ \bar{x}_c = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2} \]", "vars": r"\(n_i\)=group size, \(\bar{x}_i\)=group mean."}]))
t12_sections.append(ListS("Steps to find Combined Mean (source)", [
  "Multiply each mean by its group size",
  "Add all products",
  "Add total observations",
  "Divide total product sum by total observations"]))
t12_sections.append(Ex("Example 7 (Exam) — Combined Mean <span class='src'>[SOURCE QUESTION + SOURCE ANSWER]</span>",
  "Average marks of 40 students in Section A is 65 and of 35 students in Section B is 70. Find the combined mean.",
  "Group means + sizes → combined.",
  "n₁=40, x̄₁=65; n₂=35, x̄₂=70.",
  "Combined mean formula.",
  r"\[ \bar{x}_c = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1+n_2} \]",
  ["Numerator = 40×65 + 35×70 = 2600 + 2450 = 5050.",
   "Denominator = 75.",
   "x̄_c = 5050/75 = 67.33."],
  "Combined mean ≈ 67.33",
  "Missing-variable types: combined mean diya ho aur ek group ka mean poochha ho toh algebraically rearrange karo."))
t12_sections.append(Def("Formal Definition — Weighted Mean",
  "When different observations are assigned different levels of importance (weights), the average obtained is called the Weighted Mean.",
  "Har value ka importance alag ho toh simple average misleading hota hai — weights se multiply karke weighted mean nikalte hain. Probability mein weights probabilities ban jaate hain, aur weighted mean = expected value ho jaata hai (source observation).",
  ["Σwx / Σw","weights","importance of values"]))
t12_sections.append(Ex("Example 8 (Exam) — Weighted Mean <span class='src'>[SOURCE QUESTION + GENERATED SOLUTION]</span>",
  "A consumer buys a commodity @ ₹4.80, ₹6, ₹8, ₹12, ₹24 per unit in five successive years. Calculate average cost per unit if he buys (a) 1000 units each year; (b) 1000, 800, 600, 400, 200 units respectively.",
  "Equal vs unequal weights comparison.",
  "Prices: 4.8, 6, 8, 12, 24. Weights (b): 1000, 800, 600, 400, 200.",
  "(a) equal weights → simple mean; (b) weighted mean = Σwx/Σw.",
  r"\[ \bar{x}_w = \frac{\sum w_i x_i}{\sum w_i} \]",
  ["(a) x̄ = (4.8+6+8+12+24)/5 = 54.8/5 = ₹10.96.",
   "(b) Σwx = 4.8(1000)+6(800)+8(600)+12(400)+24(200) = 4800×5 = 19200; Σw = 3000.",
   "x̄_w = 19200/3000 = ₹6.4."],
  "(a) ₹10.96 per unit; (b) ₹6.4 per unit",
  "Weights equal hone par weighted mean = simple mean hota hai."))
t12_sections.append(ListS("Common Mistakes (Mean/Median/Mode)", [
  "Applying Σx/n to grouped data without midpoints — grouped data ho toh pehle midpoints nikalo.",
  "Median n even case mein sirf ek middle value lena — do middle values ka average chahiye.",
  "Mode ke lie data arrange na karna — frequency count zaroori.",
  "Combined mean ke lie group means ka simple average lena — group sizes se weight karna mandatory.",
  "Slide-deck pitfall list (enrichment): using mean for highly skewed data; ignoring outliers; confusing sample mean with population mean; computing mean of categorical data — invalid."]))
t12_sections.append(ListS("Exam Focus", [
  "Direct vs short-cut vs step-deviation — teeno methods same answer dete hain; exam mein specified method strictly use karo.",
  "Combined mean: numerator weighted sum, denominator total count — most-asked formula.",
  "Median odd/even rule + Mode remarks (no-mode / bimodal) rapid theory points.",
  "Source practice set: (i) median of goals 1,0,3,2,4,5,2,4,4,2,5 → 3; (ii) median of marks 46,52,48,39,41,62,55,53,96,39,45,99 → 50. <span class='src'>[SOURCE QUESTIONS, ANSWERS GENERATED]</span>"]))
t12 = T("t12", "Lecture 1.2 & 1.3", "Measures of Central Tendency (Mean · Median · Mode · Combined & Weighted Mean)", t12_sections)
u1["topics"].extend([t11, t12])
DATA["units"].append(u1)
