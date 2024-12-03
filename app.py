from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/preventive')
def preventive():
    return render_template('preventive.html')

@app.route('/ai-troubleshooter')
def ai_troubleshooter():
    return render_template('ai-troubleshooter.html')

@app.route('/alert-alarm')
def alert_alarm():
    return render_template('alert-alarm.html')

@app.route('/fault-report')
def fault_report():
    return render_template('fault-report.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)
