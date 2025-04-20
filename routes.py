from app import app


# Home page
@app.route('/')
def index():
    from datetime import datetime
    return render_template('index.html', now=datetime.now())