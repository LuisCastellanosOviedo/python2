from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachi", "Charmander"])
table.add_column("Type", ["Electric", "fire"])

print(table.align)
table.align = "l"

print(table)
