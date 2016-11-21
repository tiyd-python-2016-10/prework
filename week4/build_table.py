def write_table(*lists):
    print("<table>")
    for columns in zip(*lists):
        print("<tr>")
        for col in columns:
            print("<td>{}</td>".format(col))


        print(("<td>{}</td>"*len(columns)).format(*columns))
        print(("<td>{}</td>\n"*len(columns)).format(*columns))
        print("</tr>")
    print("</table>")
    
#<table>
#  <tr>
#     <td></td>
#     <td></td>
#  </tr>
#  <tr>
#     <td></td>
#     <td></td>
#  </tr>
#</table>



from math import factorial
if __name__ == "__main__":
    write_table([1, 2, 3], ["a", "b", "c"])
    
    l = range(32)
    write_table(["number"] + list(l), 
                ["upper"] + [chr(x+65) for x in l], 
                ["lower"] + [chr(x+97) for x in l], 
                ["square"] + [x*x for x in l], 
                ["power"] + [2**x for x in l], 
                ["factorial"] + [factorial(x) for x in l])












