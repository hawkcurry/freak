import string
import timeit
import freq
import freak


def generate_benchmark_input():
    """Generates string which contains all the pairings of printable characters"""
    ret = []
    for c1 in string.printable:
        for c2 in string.printable:
            ret.append(c1 + c2)
    return ''.join(ret)


benchmark_text = generate_benchmark_input()

test_text = 'ab'

f = freq.FreqCounter()
f.ignorecase = True


def test_freq_tally():
    f.tally_str(benchmark_text)


def test_freq():
    f.probability(benchmark_text)


_f = freak.Freak()
_f.ignorecase = True


def test_freak_tally():
    _f.tally_str(benchmark_text)


def test_freak():
    _f.probability(benchmark_text)


original_tally = timeit.timeit(test_freq_tally, number=10**2)
revised_tally = timeit.timeit(test_freak_tally, number=10**2)

print 'f.tally_str() comparison'
print 'Freq: ', '{:.2f}s'.format(original_tally)
print 'Freak:', '{:.2f}s'.format(revised_tally)
print 'Ratio:', '{:.2f}x'.format(original_tally/revised_tally)
print ''

original_prob = timeit.timeit(test_freq, number=10**2)
revised_prob = timeit.timeit(test_freak, number=10**2)


print 'f.probability() comparison'
print 'Freq: ', '{:.2f}s'.format(original_prob)
print 'Freak:', '{:.2f}s'.format(revised_prob)
print 'Ratio:', '{:.2f}x'.format(original_prob/revised_prob)
print ''
