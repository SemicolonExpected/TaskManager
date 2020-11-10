'''
DO NOT DELETE THIS I AM WORKING ON IT
THIS IS A PLACE HOLDER AS I LOOK UP HOW TO DO THE THING
SERIOUSLY DO NOT DELETE THIS
'''

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from task_manager import db, ma


class Assignment(db.Model):
    __tablename__ = 'Assignment'
    id = Column(Integer, primary_key=True)
    time_added = Column(DateTime, nullable=False)
    task_id = db.Column(Integer, ForeignKey('task.id'))
    user_id = db.Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return '<Assignment {} {}>'.format(self.task_id, self.user_id)


class AssignmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Assignment
        include_fk = True
