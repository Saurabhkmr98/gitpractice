from bs4 import BeautifulSoup
import re
"""
Function to remove all tags of img type with given src value in html
"""
def removeImgTags(htmlText, srcValue = "file"):
    soup = BeautifulSoup(htmlText, 'html.parser')
    allImg = soup.findAll("img", src=re.compile(f"^{srcValue}")) # if want to remove img tag that starts with srcValue
    # allImg = soup.findAll("img", src=re.compile(srcValue)   # if want to remove img tag that contains srcValue anywhere in src
    [img.extract() for img in allImg]

    return str(soup) # converted to string else type will be soup


# test run 
htmlText = """<!DOCTYPE html>
<html>
<head>
<title>Humanity</title>
</head>
<body>
<img src="a.jpg">
<img src="tmpfile">
<img src="file:///C:/Users/Subodh%20Verma/Downloads/List.pdf" /">
<img src="a.jpg">
<p>The beginning</p>
</body>
</html>"""
print(removeImgTags(htmlText))
