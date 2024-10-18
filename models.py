from app import db

class InfosPerformance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Participant = db.Column(db.String, nullable=False)
    TotalTime2000m = db.Column(db.String, nullable=False)
    AvgCadenceMin2000m = db.Column(db.Float, nullable=False)
    TotalStrokes2000m = db.Column(db.Integer, nullable=False)
    Time500mP1 = db.Column(db.String)
    AvgCadenceMin500mP1 = db.Column(db.Float)
    Strokes500mP1 = db.Column(db.Integer)
    Time500mP2 = db.Column(db.String)
    AvgCadenceMin500mP2 = db.Column(db.Float)
    Strokes500mP2 = db.Column(db.Integer)
    Time500mP3 = db.Column(db.String)
    AvgCadenceMin500mP3 = db.Column(db.Float)
    Strokes500mP3 = db.Column(db.Integer)
    Time500mP4 = db.Column(db.String)
    AvgCadenceMin500mP4 = db.Column(db.Float)
    Strokes500mP4 = db.Column(db.Integer)

    def __repr__(self):
        return f'<InfosPerformance {self.Participant}>'

class SpeedLength(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Participant = db.Column(db.String, nullable=False)
    AvgSpeedKmh2000m = db.Column(db.Float, nullable=False)
    StrokeLength2000m = db.Column(db.Float, nullable=False)
    AvgSpeedKmh500mP1 = db.Column(db.Float)
    StrokeLengh500mP1 = db.Column(db.Float)
    AvgSpeedKmh500mP2 = db.Column(db.Float)
    StrokeLengh500mP2 = db.Column(db.Float)
    AvgSpeedKmh500mP3 = db.Column(db.Float)
    StrokeLengh500mP3 = db.Column(db.Float)
    AvgSpeedKmh500mP4 = db.Column(db.Float)
    StrokeLengh500mP4 = db.Column(db.Float)

    def __repr__(self):
        return f'<SpeedLength {self.Participant}>'