import sys

print("How many rows? ", file=sys.stderr)
rows = int(input())
print("How many cols? ", file=sys.stderr)
cols = int(input())

print("<table>")
for r in range(rows):
    print("<tr>")
    for c in range(cols):
        print("<td>({}, {})</td>".format(r, c))

    #coords = zip([r]*cols, range(cols))
    #t = tuple(item for sublist in coords for item in sublist)
    #row = "<td>({}, {})</td>"*cols

    #print(row.format(*t))
    #print(("<td>(%s, %s)</td>"*cols) % t)

    print("</tr>")
print("</table>")


