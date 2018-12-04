print("Practice")
print("Escapes with \\:")
print(" \n newlines and \t tabs")

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from inutition
and requires and explanation
\n\t where there is none.
"""


print(".............")
print(poem)
print(".............")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000

beans, jars, crates = formula(start_point)

print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
secret = formula(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*secret))
