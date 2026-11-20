name=input("Please enter your name: ")
description=input("Please enter a description of yourself: ")
html_content =f"""<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    <center>
        <h1>{name}</h1>
    </center>
    <hr />
    {description}
    <hr />
</body>
</html>"""

with open("profile.html", "w") as file:
    file.write(html_content)