from flask import Flask, render_template, url_for, redirect

app= Flask(__name__)

#############################################################

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/bookings")
def bookings():
    return render_template("bookings.html")
@app.route("/contactus")
def contactus():
    return render_template("contactus.html")




@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500


#############################################################




#############################################################
if __name__== "__main__":
    app.run(debug=True, port=8000)