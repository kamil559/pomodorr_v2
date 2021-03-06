import uuid

import pytest
from pomodoros_infrastructure.queries.pomodoros import SQLGetRecentPomodoros
from pony.orm import db_session


@pytest.mark.usefixtures("setup_teardown_tables")
class TestGetRecentPomodorosQuery:
    @db_session
    def test_query_returns_pomodoro_from_today(self, orm_task, orm_pomodoro_for_today, orm_pomodoro_for_yesterday):
        query_object = SQLGetRecentPomodoros()
        result = query_object.query(orm_task.id)

        assert len(result) == 1
        assert orm_pomodoro_for_yesterday.id != result[0].id
        assert orm_pomodoro_for_today.id == result[0].id

    @db_session
    def test_query_returns_task_related_pomodoros_only(
        self,
        orm_task,
        orm_pomodoro_for_today,
        orm_random_pomodoro_for_today,
        orm_pomodoro_for_yesterday,
        orm_random_pomodoro_for_yesterday,
    ):
        query_object = SQLGetRecentPomodoros()
        result = query_object.query(orm_task.id)

        assert len(result) == 1
        assert orm_pomodoro_for_yesterday.id != result[0].id
        assert orm_random_pomodoro_for_yesterday.id != result[0].id
        assert orm_random_pomodoro_for_today.id != result[0].id
        assert orm_pomodoro_for_today.id == result[0].id

    @db_session
    def test_query_returns_empty_collection_if_task_has_no_recent_pomodoros(self, orm_task):
        query_object = SQLGetRecentPomodoros()
        result = query_object.query(orm_task.id)

        assert result == []

    @db_session
    def test_query_returns_empty_collection_if_non_existing_task_id_was_passed(self):
        query_object = SQLGetRecentPomodoros()
        random_uuid = uuid.uuid4()
        result = query_object.query(random_uuid)

        assert result == []
