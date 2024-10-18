import plotly.express as px

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

def create_radar_chart(infos_performance, participants):
    radar_chart = px.line_polar(
        r=[p.TotalStrokes2000m for p in infos_performance],
        theta=participants,
        title='Comparaison des Total des Coups de Rame (2000m)',
        line_close=True
    )
    style_chart(radar_chart, polar=True)
    return radar_chart.to_html(full_html=False)

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

def create_scatter_plot(infos_performance, speed_length):
    all_vitesses = []
    cadence_dict = {p.Participant: p for p in infos_performance}

    cadence_values, length_values = [], []
    for s in speed_length:
        if s.Participant in cadence_dict:
            participant_cadences = cadence_dict[s.Participant]

            for i in range(1, 5):
                speed = getattr(s, f'AvgSpeedKmh500mP{i}')
                cadence = getattr(participant_cadences, f'AvgCadenceMin500mP{i}')
                length = getattr(s, f'StrokeLengh500mP{i}')

                all_vitesses.append({'Participant': s.Participant, 'Speed': speed, 'Cadence': cadence, 'Length': length})
                cadence_values.append(cadence)
                length_values.append(length)

    max_speed_entry = max(all_vitesses, key=lambda x: x['Speed'])
    best_speed_info = {
        'participant_max_speed': max_speed_entry['Participant'],
        'max_speed': max_speed_entry['Speed'],
        'max_cadence': max_speed_entry['Cadence'],
        'max_length': max_speed_entry['Length']
    }

    scatter_plot = px.scatter(
        x=cadence_values,
        y=length_values,
        title='Relation entre Cadence et Longueur de Coup de Rame pour tout les participants',
        labels={'x': 'Cadence moyenne (rame/min)', 'y': 'Longueur moyenne par coup de rame (m)'}
    )

    scatter_plot.add_scatter(
        x=[best_speed_info['max_cadence']],
        y=[best_speed_info['max_length']],
        mode='markers',
        marker=dict(color='red', size=10),
        name='Vitesse Max'
    )

    return scatter_plot.to_html(full_html=False), best_speed_info

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
