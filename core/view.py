def view_func(file_name ,data):
    text = ""
    with open(f'./htdocs/{file_name}.html', 'r') as file:
        text = file.read()
   
    return text.format(**data)
#     return f"""

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     {dict["mainPage"]}
    
# </body>
# </html>
# """

def build_table():
    f"""
        <table>
       <tr>{"".join([f'<td>{s}</td>' for s in range(100)])}</tr>
    """
    a =  f"""<table border="1">
                <tr>
                    <td>Row 1, Column 1</td>
                    <td>Row 1, Column 2</td>
                    <td>Row 1, Column 3</td>
                </tr>
                <tr>
                    <td>Row 2, Column 1</td>
                    <td>Row 2, Column 2</td>
                    <td>Row 2, Column 3</td>
                </tr>
                <tr>
                    <td>Row 3, Column 1</td>
                    <td>Row 3, Column 2</td>
                    <td>Row 3, Column 3</td>
                </tr>
            </table>"""
    table_d = ''.join([f'<tr><td>{s}</td></tr>' for s in range(100)])