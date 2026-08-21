# Unit 3 — Probability: Basics, Laws, Conditional, Bayes
from course_data import U, T, Def, Text, ListS, Formulas, Ex, Try, Derive

u3 = U("u3", "Unit 3 — Probability: Basics, Laws & Bayes Theorem",
   "Official course blueprint: Lecture 3.1 definitions & laws, 3.2 conditional probability & Bayes, 3.3 random variables (placed in Unit 4 for narrative flow).")

# ---- 3.1 Basics ----
t31s = []
t31s.append(Text("Introduction",
  "Probability uncertainty ko quantify karta hai — kitna likely hai event. Applications: weather forecasting, insurance & risk analysis, medical diagnosis, ML/AI, games & gambling, engineering reliability analysis."))
t31s.append(Def("Formal Definition — Random Experiment",
  "A random experiment is an experiment whose outcome cannot be predicted with certainty in advance.",
  "Tossing a coin, rolling a die, drawing a card, randomly selecting a student — in advance outcome nahi pata. Uske outcomes collect karne par sample space milta hai.",
  ["uncertainty","experiment","outcome"]))
t31s.append(Def("Formal Definition — Sample Space & Event",
  "The set of all possible outcomes of a random experiment is called the sample space, denoted by S. An event is a subset of the sample space.",
  "Sample space = sab possible results ka set. Event = us subset jiska hum probability assign karte hain (e.g., die pe 'even number' event {2,4,6}).",
  ["sample space","subset","event"]))
t31s.append(ListS("Types of events (source)", [
  "Simple event — one outcome (e.g., A = {2})",
  "Compound event — more than one outcome (e.g., A = {2,4,6})",
  "Impossible event — cannot occur (P = 0), e.g., get 7 on a die",
  "Sure event — always occurs (P = 1)",
  "Complementary event A′ = S − A"]))
t31s.append(Def("Formal Definition — Classical Probability",
  "If an experiment has n equally likely outcomes and m of them are favorable to event A, then P(A) = m/n, where 0 ≤ P(A) ≤ 1.",
  "Classical approach: total equally-likely outcomes denominator; favorable numerator. Coin toss H → favorable 1 of 2 → 1/2.",
  ["m/n","equally likely","favorable outcomes"]))
t31s.append(Formulas("Laws of Probability", [
  {"latex": r"\[ P(A\cup B) = P(A) + P(B) - P(A\cap B) \quad \text{(addition)} \]", "vars": "At least one event; mutually exclusive → P(A∩B)=0."},
  {"latex": r"\[ P(A') = 1 - P(A) \quad \text{(complement)} \]", "vars": "non-occurrence."},
  {"latex": r"\[ P(A\cap B) = P(A)\,P(B\mid A) \quad \text{(multiplication)} \]", "vars": "independent: P(A∩B)=P(A)P(B)."}]))
t31s.append(Ex("Example (Basic) — Coin & Die <span class='src'>[SOURCE SOLVED]</span>",
  "(a) Tossing a coin: find probability of Head. (b) Rolling a die: find probability of an even number.",
  "Sample space + favorable count.",
  "(a) S={H,T}; (b) S={1..6}.",
  "Classical P = m/n.",
  None,
  ["(a) P(H) = 1/2.",
   "(b) A = {2,4,6} → P(A) = 3/6 = 1/2."],
  "P(H) = 1/2; P(even) = 1/2",
  "Sample space clearly likho."))
t31s.append(Ex("Example (Standard) — Addition Law <span class='src'>[SOURCE SOLVED]</span>",
  "A die is rolled. A = even number, B = number greater than 4. Find P(A∪B).",
  "Overlap subtract karna.",
  "A = {2,4,6}, B = {5,6}.",
  "A∩B = {6}.",
  r"\[ P(A\cup B) = P(A)+P(B)-P(A\cap B) \]",
  ["P(A) = 3/6, P(B) = 2/6, P(A∩B) = 1/6.",
   "P(A∪B) = 3/6 + 2/6 − 1/6 = 4/6 = 2/3."],
  "P(A∪B) = 2/3",
  "Overlap na ghatao → overcount."))
t31s.append(Ex("Example (Basic) — Complement Law <span class='src'>[SOURCE SOLVED]</span>",
  "Probability of passing an exam is 0.8. Find probability of failing.",
  "Complement = 1 − P.",
  "P(pass) = 0.8.",
  "P(A′) = 1 − P(A).",
  None,
  ["P(fail) = 1 − 0.8 = 0.2."],
  "P(fail) = 0.2",
  "Complement law quick tool."))
t31s.append(Ex("Example (Standard) — Multiplication Law <span class='src'>[SOURCE SOLVED]</span>",
  "Two coins are tossed. Find probability of getting two heads.",
  "Independent events multiply.",
  "P(H) = 1/2 each toss.",
  "P(HH) = P(H)×P(H).",
  None,
  ["P(HH) = 1/2 × 1/2 = 1/4."],
  "P(HH) = 1/4",
  "Independence check zaruri."))
t31 = T("t31","Lecture 3.1","Basics of Probability — Definitions & Laws", t31s)
u3["topics"].append(t31)

# ---- 3.2 Conditional & Bayes ----
t32s = []
t32s.append(Def("Formal Definition — Conditional Probability",
  "Conditional probability is the probability of occurrence of event A given that event B has already occurred: P(A|B) = P(A∩B)/P(B), where P(B) ≠ 0.",
  "B already hua — sample space ab B tak limited. Face card diya hai toh king aane ka probability sirf 4/12.",
  ["given that","P(A∩B)/P(B)","reduced sample space"]))
t32s.append(Ex("Example (Basic) — Conditional Probability <span class='src'>[SOURCE SOLVED]</span>",
  "One card is drawn from a deck. Find probability it is a king given that it is a face card.",
  "Reduced sample space.",
  "Face cards = 12, kings = 4.",
  "P(K|F) = favorable/total = 4/12.",
  None,
  ["P(K|F) = 4/12 = 1/3."],
  "P(K|F) = 1/3",
  "Given event ka sample space use karo."))
t32s.append(ListS("Independent vs Dependent Events (source)", [
  "<b>Independent:</b> occurrence of one event does not affect the other — P(A∩B) = P(A)P(B). Example: tossing two coins.",
  "<b>Dependent:</b> occurrence of one event affects the other. Example: drawing cards without replacement."]))
t32s.append(Formulas("Bayes Theorem", [
  {"latex": r"\[ P(A\mid B) = \frac{P(B\mid A)\,P(A)}{P(B)} \]", "vars": "Used to revise probabilities based on new information."}]))
t32s.append(ListS("Bayes applications (source)", [
  "Medical testing","Spam filtering","Machine learning","Decision-making"]))
t32s.append(Formulas("Important Probability Identities (source)", [
  {"latex": r"\[ P(S) = 1 \]", "vars": ""},
  {"latex": r"\[ P(\varnothing) = 0 \]", "vars": ""},
  {"latex": r"\[ 0 \le P(A) \le 1 \]", "vars": ""},
  {"latex": r"\[ P(A') = 1 - P(A) \]", "vars": ""},
  {"latex": r"\[ P(A - B) = P(A) - P(A\cap B) \]", "vars": ""}]))
t32s.append(Ex("Example (Standard) — Cards & Dice <span class='src'>[SOURCE SOLVED]</span>",
  "(i) A card is drawn from a deck of 52 cards. Find probability of (a) an ace, (b) a red card. (ii) Two dice are rolled. Find probability that the sum is 7.",
  "Classical counting with careful sample space.",
  "(i) 52 cards; (ii) 36 outcomes.",
  "Favorable/total.",
  None,
  ["(i) P(ace) = 4/52 = 1/13; P(red) = 26/52 = 1/2.",
   "(ii) Favorable pairs: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) → 6 outcomes. P(sum=7) = 6/36 = 1/6."],
  "P(ace) = 1/13; P(red) = 1/2; P(sum 7) = 1/6",
  "Enumerate pairs — don't guess."))
t32s.append(ListS("Common Mistakes", [
  "Multiplication formula ignore karna in dependent cases.",
  "Bayes formula mein P(B) = ΣP(B|Ai)P(Ai) na banana (enrichment).",
  "Without-replacement independent maan lena."]))
t32 = T("t32","Lecture 3.2","Conditional Probability & Bayes Theorem", t32s)
u3["topics"].append(t32)
