from app import db
from typing import Optional
import sqlalchemy as sqla # TODO CheckConstraint
import sqlalchemy.orm as sqlo

from datetime import datetime, timezone

PROGRESS_OPTIONS = [
    'Not started',
    'In progress',
    'Almost done',
    'Done',
    'Waiting on others'
]

PRIORITIES = [
    'Default',
    'Not posted'
]