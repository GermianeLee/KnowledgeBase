# KnowledgeBase
This Python program creates and evaluates a simple logical knowledge base using propositional logic, then generates
and displays its truth table. It defines a KnowledgeBase class that takes three Boolean propositions P, Q, and R as input.
Within the class, it computes three key components: (1) (P ∧ Q) → R (if both P and Q are true, then R must be true), 
(2) Q → P (if Q is true, then P must be true), and (3) Q as a standalone fact. These are combined into the knowledge
base formula KB = ((P ∧ Q) → R) ∧ (Q → P) ∧ Q. The program then evaluates whether the knowledge base implies R (i.e., KB → R).
Helper functions are provided to format Boolean values as "T" or "F", center strings for neat display, and print the results as
a formatted Markdown-like truth table. The main() function iterates through all eight possible truth value combinations of P, Q, 
and R, evaluates the logical expressions for each, stores the results, and prints the complete truth table. The second block of code
is a simplified, non-class version that performs the same logical computations and prints them in a plain-text tabular format without the Markdown styling.
