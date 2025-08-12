class KnowledgeBase:
    def __init__(self, P, Q, R):
        self.P = P
        self.Q = Q
        self.R = R
        self.p1 = self.implication(self.conjunction(P, Q), R)  # (P ^ Q) => R
        self.p2 = self.implication(Q, P)  # Q => P
        self.p3 = Q  # Q
        self.kb = self.evaluate_kb(P, Q, R)  # KB = (((P ^ Q) => R) ^ (Q => P) ^ Q)
        self.result = self.implication(self.kb, R)  # KB => R

    @staticmethod
    def conjunction(a, b):
        return a and b

    @staticmethod
    def implication(a, b):
        return (not a) or b

    @staticmethod
    def evaluate_kb(P, Q, R):
        p1 = KnowledgeBase.implication(KnowledgeBase.conjunction(P, Q), R)
        p2 = KnowledgeBase.implication(Q, P)
        p3 = Q
        return p1 and p2 and p3

    def get_truth_values(self):
        return [self.P, self.Q, self.R, self.p1, self.p2, self.p3, self.kb, self.result]


def bool_to_string(b):
    return "T" if b else "F"


def center(s, width):
    if len(s) >= width:
        return s
    left_padding = (width - len(s)) // 2
    right_padding = width - len(s) - left_padding
    return " " * left_padding + s + " " * right_padding


def print_truth_table(truth_table):
    headers = ["Prop P", "Prop Q", "Prop R", "(P ∧ Q) → R", "Q → P", "Prop Q (p3)", "Knowledge Base", "KB → R"]
    widths = [8, 8, 8, 15, 10, 12, 15, 10]

    # Build Markdown table header row
    header_row = "|"
    for i in range(len(headers)):
        header_row += f" {center(headers[i], widths[i])} |"
    print(header_row)

    # Build Markdown table alignment row
    align_row = "|"
    for width in widths:
        dashes = "-" * width
        align_row += f":{dashes}:|"
    print(align_row)

    # Print each row of the truth table
    for row in truth_table:
        row_str = "|"
        for i in range(len(row)):
            row_str += f" {center(bool_to_string(row[i]), widths[i])} |"
        print(row_str)


def main():
    # Generate all possible truth values for P, Q, R
    permutations = [
        [True, True, True],
        [True, True, False],
        [True, False, True],
        [True, False, False],
        [False, True, True],
        [False, True, False],
        [False, False, True],
        [False, False, False]
    ]

    # Generate truth table
    truth_table = []
    for input_vals in permutations:
        kb = KnowledgeBase(input_vals[0], input_vals[1], input_vals[2])
        truth_table.append(kb.get_truth_values())

    print_truth_table(truth_table)


if __name__ == "__main__":
    main()
