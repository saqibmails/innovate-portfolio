from flask import Flask, render_template, url_for, redirect

app= Flask(__name__)

#############################################################

@app.route("/")
def home():
    return render_template("index.html")

    @app.errohandler(404)
    def page_not_found (e):
        return render_template("404.html"),
        404
    @app.errorhandler(500)
    def internal_server_erros(e):
        return render_template("500.html"),
        500
#############################################################




#############################################################
if __name__== "__main__":
    app.run(debug=True, port=8000)