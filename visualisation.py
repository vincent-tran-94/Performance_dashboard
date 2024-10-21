import plotly.express as px

#Visualisation pour la performance du temps pour chaque tranche de 500m des participants
def create_performance_chart(infos_performance):
    times_500m = []
    intervals = ['500m', '1000m', '1500m', '2000m']

    for p in infos_performance:
        for i, interval in enumerate(intervals):
            times_500m.append({'Participant': p.Participant, 'Interval': interval, 'Time': getattr(p, f'Time500mP{i+1}')})

    performance_line_chart = px.line(
        times_500m,
        x='Interval',
        y='Time',
        color='Participant',
        title="Temps aux Intervalles de 500m par Participant",
        labels={'Interval': 'Intervalle (m)', 'Time': 'Temps (s)'}
    )
    style_chart(performance_line_chart)
    return performance_line_chart.to_html(full_html=False)

#Visualisation pour le total des coups de Rame sur 2000m des participants
def create_radar_chart(infos_performance, participants):
    radar_chart = px.line_polar(
        r=[p.TotalStrokes2000m for p in infos_performance],
        theta=participants,
        title='Comparaison des Total des Coups de Rame (2000m)',
        line_close=True
    )
    style_chart(radar_chart, polar=True)
    return radar_chart.to_html(full_html=False)

#Visualisation pour la performance de vitesse moyenne pour chaque tranche de 500m des participants
def create_speed_chart(speed_length):
    speeds_500m = []
    intervals = ['500m', '1000m', '1500m', '2000m']

    for s in speed_length:
        for i, interval in enumerate(intervals):
            speeds_500m.append({'Participant': s.Participant, 'Interval': interval, 'Speed': getattr(s, f'AvgSpeedKmh500mP{i+1}')})

    speed_line_chart = px.line(
        speeds_500m,
        x='Interval',
        y='Speed',
        color='Participant',
        title="Vitesse Moyenne aux Intervalles de 500m par Participant",
        labels={'Interval': 'Intervalle (m)', 'Speed': 'Vitesse (km/h)'}
    )
    style_chart(speed_line_chart)
    return speed_line_chart.to_html(full_html=False)


#Fonction pour déterminer quel sont les meilleurs critères de performance (vitesse, cadence et coup de rame / min) en focntion du choix des participants 
def get_best_speed_info(infos_performance, speed_length):
    all_vitesses = []
    cadence_dict = {p.Participant: p for p in infos_performance}  #Récupération les données des cadences sur les infos de performance qui se trouve sur une autre table  

    for s in speed_length:
        if s.Participant in cadence_dict:
            participant_cadences = cadence_dict[s.Participant] 

            # Création de listes d'attributs correspond à chaque participant pour déterminer quel participant possèdera les vitesses 
            speeds = [s.AvgSpeedKmh500mP1, s.AvgSpeedKmh500mP2, s.AvgSpeedKmh500mP3, s.AvgSpeedKmh500mP4]
            cadences = [participant_cadences.AvgCadenceMin500mP1, participant_cadences.AvgCadenceMin500mP2, participant_cadences.AvgCadenceMin500mP3, participant_cadences.AvgCadenceMin500mP4]
            lengths = [s.StrokeLengh500mP1, s.StrokeLengh500mP2, s.StrokeLengh500mP3, s.StrokeLengh500mP4]

            # Parcourir les listes pour créer all_vitesses
            for speed, cadence, length in zip(speeds, cadences, lengths):
                all_vitesses.append({'Participant': s.Participant, 'Speed': speed, 'Cadence': cadence, 'Length': length})

    # Trouver l'entrée avec la vitesse maximale
    max_speed_entry = max(all_vitesses, key=lambda x: x['Speed'])

    best_speed_info = {
        'participant_max_speed': max_speed_entry['Participant'],
        'max_speed': max_speed_entry['Speed'],
        'max_cadence': max_speed_entry['Cadence'],
        'max_length': max_speed_entry['Length']
    }

    return best_speed_info

#Visualisation des nuage de points pour mettre la relation cadence et longueur en fonction des participants 
def create_scatter_plot(infos_performance, speed_length):
    # Appel à la fonction get_best_speed_info pour obtenir les infos de la meilleure vitesse
    best_speed_info = get_best_speed_info(infos_performance, speed_length)

    # Création des valeurs de cadence et longueur des participants
    cadence_values, length_values = [], []
    cadence_dict = {p.Participant: p for p in infos_performance}

    for s in speed_length:
        if s.Participant in cadence_dict:
            participant_cadences = cadence_dict[s.Participant]

            # Création des listes des valeurs des 4 intervalles (500mP1 à 500mP4)
            cadences = [
                participant_cadences.AvgCadenceMin500mP1,
                participant_cadences.AvgCadenceMin500mP2,
                participant_cadences.AvgCadenceMin500mP3,
                participant_cadences.AvgCadenceMin500mP4
            ]

            lengths = [
                s.StrokeLengh500mP1,
                s.StrokeLengh500mP2,
                s.StrokeLengh500mP3,
                s.StrokeLengh500mP4
            ]

            # Ajout des valeurs à la liste
            cadence_values.extend(cadences)
            length_values.extend(lengths)

    # Création du scatter plot
    scatter_plot = px.scatter(
        x=cadence_values,
        y=length_values,
        title='Relation entre Cadence et Longueur de Coup de Rame pour tous les participants',
        labels={'x': 'Cadence moyenne (rame/min)', 'y': 'Longueur moyenne par coup de rame (m)'}
    )

    # Ajout du marqueur de la meilleure vitesse
    scatter_plot.add_scatter(
        x=[best_speed_info['max_cadence']],
        y=[best_speed_info['max_length']],
        mode='markers',
        marker=dict(color='red', size=10),
        name='Vitesse Max'
    )

    return scatter_plot.to_html(full_html=False)

#Fonction pour changer le style des couleurs pour les grilles à un graphique polaire ou un graphique classique
def style_chart(chart, polar=False):
    if polar:
        chart.update_layout(
            polar=dict(
                radialaxis=dict(showgrid=True, gridcolor='black'),
                angularaxis=dict(showgrid=True, gridcolor='black')
            ),
        )
    else:
        chart.update_layout(
            xaxis=dict(showgrid=True, gridcolor='black'),
            yaxis=dict(showgrid=True, gridcolor='black')
        )
