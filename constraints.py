# Example of a tiny novel generator under 256 characters of code

import random;print(' '.join(random.choice(open('data/corpus.txt').read().split()) for _ in range(1000)))
