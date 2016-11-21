
def write_table(*lists):
    """each list is a column, the values in the list will be the row values"""
    print("<table>")
    for columns in zip(*lists):
        print("<tr>")
        for val in columns:
            print("<td>{}</td>".format(val))
        print("</tr>")
    print("</table>")


def print_head():
    print("<!doctype html><html><head><title>tables kata</title>")
    print("<style>table,tr,td{border:1px solid black; border-collapse:collapse}</style>")
    print("</head><body>")
    
def print_foot():
    print("</body></html>")

from math import factorial
if __name__ == "__main__":
    print_head()
    write_table([1, 2, 3], ["a", "b", "c"])
    
    
    l = range(32)
    write_table(["number"] + list(l), 
                ["upper"] + [chr(x+65) for x in l], 
                ["lower"] + [chr(x+97) for x in l], 
                ["square"] + [x*x for x in l], 
                ["power"] + [2**x for x in l], 
                ["factorial"] + [factorial(x) for x in l])

    write_table
    print_foot()











