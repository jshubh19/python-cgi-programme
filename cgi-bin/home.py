import cgi, cgitb
cgitb.enable()

print("Content-type: text/html\r\n\r\n")
print("<html>")
print("<head><title>Hompage</title></head>")
print("<body>")
print("<h2>Welcome to homepage</h2>")
form=cgi.FieldStorage()
if form.getvalue("name"):
    name=form.getvalue("name")
    print("<h1>Hello "+ name+" Konichiwa..Ola...Gracias..Namste</h1>")
if form.getvalue("happy"):
    print("<p>Happines is the key of good life. Keep smiling</p>")
if form.getvalue("sad"):
    print("<p> Why are you sad Dear</p>")

print('<form action="" method="post">')
print('<p>Name: <input type="text" name="name" placeholder="enter name" ></p>')
print('<p>How are you feeling today?</p>')
print('<input type="checkbox" name="happy">happy')
print('<input type="checkbox" name="sad">sad')
print('<input type="submit" value="submit" >')
print("</form>")
print("</body>")
print("</html>")
