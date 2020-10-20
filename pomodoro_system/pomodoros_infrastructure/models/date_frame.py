import uuid
from datetime import datetime

from pony.orm import PrimaryKey, Required, Optional, Set

from foundation.models import db


class DateFrameModel(db.Entity):
    _table_ = 'date_frames'

    id = PrimaryKey(uuid.UUID, auto=False)
    frame_type = Required(int)
    start_date = Required(datetime)
    end_date = Optional(datetime)


class PomodoroModel(DateFrameModel):
    task_id = Required(uuid.UUID)
    contained_pauses = Set(lambda: PauseModel)


class PauseModel(DateFrameModel):
    pomodoro = Required(PomodoroModel)
