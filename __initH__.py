from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #define URL
def homepage():	# function to be executed when accessing the URL
				# returns templates or html templates or jinga templates
	return render_template("HomeH.html") # looks inside the templates folder, i.e. home.html


@app.route('/video/')
def video_page():
	return render_template("VideoH.html")

if __name__ == "__main__":
    app.run()
