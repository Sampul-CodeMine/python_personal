print('Let us practise everything.')
print("You\'d need to know \'bout escapes \\ that do \n newlines and \t tabs.")
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print('------------------------------------------')
print(poem)
print('------------------------------------------')

five = 10 - 2 + 3 - 6
print('This should be five (5) %r' % five)


def secret_formula(started):
    jellyBeans = started * 500
    jar = jellyBeans / 1000
    crate = jar / 100
    return jellyBeans, jar, crate


startPoint = 10000
beans, jars, crates = secret_formula(startPoint)

print('With a starting point of: %d' % startPoint)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

startPoint = startPoint / 10
print('We can also do that this way:')
print('With a starting point of: %d' % startPoint)
print("We would have %d beans, %d jars, and %d crates." % (secret_formula(startPoint)))
print()
