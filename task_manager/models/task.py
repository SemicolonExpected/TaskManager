from task_manager import db


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    priority = db.Column(db.Integer, default=1, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    time_estimate = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return '<Task {} {}>'.format(self.title, self.priority)
