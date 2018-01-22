import collections


class Freak:
    def __init__(self):
        self.ignore_chars = set("""\n\t\r~@#%^&*"'/\-+<>{}|$!:()[];?,=""")
        self.ignorecase = True

        self.pair_count = collections.defaultdict(collections.Counter)
        self.total_count = collections.Counter()

    def enumerate_pairs(self, line):
        for idx in range(len(line)-1):
            if line[idx] in self.ignore_chars or line[idx+1] in self.ignore_chars:
                continue
            yield line[idx], line[idx+1]

    def tally_str(self, line, weight=1):
        for c1, c2 in self.enumerate_pairs(line):
            self.pair_count[c1][c2] += weight
            self.total_count[c1] += weight

    def probability(self, line, max_prob=40):
        total_count = 0
        total_sum = 0
        for c1, c2 in self.enumerate_pairs(line):
            total_sum += self._probability(c1, c2, max_prob)
            total_count += 1
            if total_count == 0:
                return 0
        return total_sum / total_count

    def _probability(self, c1, c2, max_prob=40):
        num = self.pair_count[c1][c2]
        den = self.total_count[c1]

        if self.ignorecase:
            _c1 = c1.upper() if c1.islower() else c1.lower()
            _c2 = c2.upper() if c2.islower() else c2.lower()
            den += self.total_count[_c1]
            num += self.pair_count[_c1][c2]
            num += self.pair_count[_c1][_c2]
            num += self.pair_count[c1][_c2]

        if den == 0:
            return 0
        prob = float(num)/float(den)*100
        return min(prob, max_prob)

    def load_freq(self, freq):
        for c1, counter in freq.items():
            for c2, value in counter.items():
                self.pair_count[c1][c2] += value
                self.total_count[c1] += value

    # TODO: resetcounts
    # TODO: save

    # TODO: promote

    # TODO: lookup