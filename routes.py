from flask import Blueprint, request, render_template, redirect, url_for, session
from hospital.models import Patient
from flask import current_app as app
import requests

hospital_bp = Blueprint('hospital', __name__)

@hospital_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(app.config['OAUTH2_AUTHORIZE_URL'])
    return render_template('login.html')

@hospital_bp.route('/callback')
def callback():
    code = request.args.get('code')
    token_data = requests.post(app.config['OAUTH2_TOKEN_URL'], data={
        'client_id': app.config['OAUTH2_CLIENT_ID'],
        'client_secret': app.config['OAUTH2_CLIENT_SECRET'],
        'code': code,
    }).json()

    session['access_token'] = token_data['access_token']
    return redirect(url_for('hospital.dashboard'))

@hospital_bp.route('/dashboard')
def dashboard():
    if 'access_token' not in session:
        return redirect(url_for('hospital.login'))

    patients = Patient.query.all()
    return render_template('dashboard.html', patients=patients)

@hospital_bp.route('/patient/<int:id>')
def patient_record(id):
    if 'access_token' not in session:
        return redirect(url_for('hospital.login'))

    patient = Patient.query.get_or_404(id)
    medical_history = patient.get_medical_history()
    return f"Patient NIN: {patient.nin}, Medical History: {medical_history}"
