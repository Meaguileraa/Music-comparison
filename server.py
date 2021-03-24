
"""Flask server for Spotify Music Comparison web application."""

from flask import Flask, render_template, jsonify, request, redirect


"""Server for music app."""
app = Flask(__name__)
app.secret_key = "music"

@app.route("/", methods=["GET"])
def homepage():

    return_render("index.html")

    
    #api call 
    # ability to compare when button is clicked 
    #after clicking compare then make the api call 
    #return render a html template 

#post route as well 
#and push data to html page 

#get artists 
#make a method that says given two artists get the info I want 
#call api in helper function 

#request a key from spotify 

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host="0.0.0.0")
    #change to app.run() when complete 

    #get retreiving data post sending data 