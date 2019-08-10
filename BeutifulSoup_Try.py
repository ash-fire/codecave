html_doc = """
<html>
        <head>
                <title>Home</title>
        </head>
        <body  bgcolor"black">
                <h1 style"color: blue">Home</h1>
                <p>This is a website that will teach you what I learned about the brain</p>
                <img src="https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjmmOfNs5TgAhWnhVQKHYHdBfcQjRx6BAgBEAU&url=https%3A%2F%2Fresearch.vtc.vt.edu%2Fnews%2F2013%2Ffeb%2F13%2Fbrain-awareness-week-designed-highlight-advances-b%2F&psig=AOvVaw2amsC6wFrCVHJ-9dzd8YmC&ust=1548899784637391"/>
                <h1 style"color: red;">In Classroom Learning</h1>
                
        </body>
</html>"""


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
heading = soup.body.h1.string
para = soup.p.string
print(heading)
print("\n")
print(para)









