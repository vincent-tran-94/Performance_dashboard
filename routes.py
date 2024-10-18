from flask import render_template, request, redirect, session, url_for
from app import app
from models import InfosPerformance, SpeedLength
from visualisation import *

@app.route('/')
def dashboard():
    infos_performance = InfosPerformance.query.all()
    speed_length = SpeedLength.query.all()

    selected_participants = session.get('selected_participants', [])
    if selected_participants:
        infos_performance = [p for p in infos_performance if p.Participant in selected_participants]
        speed_length = [s for s in speed_length if s.Participant in selected_participants]

    participants = sorted([p.Participant for p in infos_performance])

    performance_line_chart_html = create_performance_chart(infos_performance)
    radar_chart_html = create_radar_chart(infos_performance, participants)
    speed_line_chart_html = create_speed_chart(speed_length)
    cadence_length_scatter_html, best_speed_info = create_scatter_plot(infos_performance, speed_length)

    return render_template(
        'dashboard.html', 
        participants=participants,
        performance_line_chart_html=performance_line_chart_html,
        radar_chart_html=radar_chart_html,
        cadence_length_scatter_html=cadence_length_scatter_html,
        speed_line_chart_html=speed_line_chart_html,
        selected_participants=selected_participants,
        **best_speed_info 
    )


# Route pour ajouter des participants à la session
@app.route('/add_participants', methods=['POST'])
def add_participants():
    # Récupérer la liste actuelle des participants sélectionnés
    selected_participants = session.get('selected_participants', [])
    # Ajouter les nouveaux participants à la liste existante
    new_participants = request.form.getlist('participants')
    selected_participants.extend(new_participants)  # Ajouter les nouveaux participants
    selected_participants = list(set(selected_participants))  # Éliminer les doublons
    session['selected_participants'] = selected_participants  # Mettre à jour la session
    return redirect(url_for('dashboard'))


# Route pour retirer tous les participants
@app.route('/remove_participants')
def remove_participants():
    session.pop('selected_participants', None)  # Retirer les participants de la session
    return redirect(url_for('dashboard'))