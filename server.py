from re import template
from flask import Flask, request, render_template

app = Flask('app') # changed from invite_app; apparently this makes cloud appd deployment so much easier?

@app.route("/")	# Use this root page to make a form that'll then generate our invite template
def form():
	return render_template("farm.html")

@app.route("/view")
def view_invite():
	# to = "Sarah"
	# event="Artemis' birthday party"
	# date="February 10th"
	# time="6PM"
	# sender="Zeus"
	to = request.args.get("to")
	event = request.args.get("event")
	date = request.args.get("date")
	time = request.args.get("time")
	sender = request.args.get("sender")
	style = request.args.get('style')
# query from URL to inform filename to retrieve.
	template = "invite-"+style+".html"
	return render_template(template,to=to,event_name=event,date=date,time=time,sender=sender)

if __name__=='__main__':
	app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8080)