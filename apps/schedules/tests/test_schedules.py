import pytest
from datetime import datetime
from django.core.exceptions import ValidationError
from apps.schedules.models.schedule import Schedule
from apps.environments.models.environment import Environment
from apps.users.models.user import CustomUser
from apps.programs.models.program import Program

pytestmark = pytest.mark.django_db


def create_base_data():
    environment = Environment.objects.create(name="Aula 101")
    teacher = CustomUser.objects.create_user(username="docente1", password="test1234", role="TEACHER")
    program = Program.objects.create(name="Programación Backend")
    return environment, teacher, program


def test_schedule_creation_success():
    environment, teacher, program = create_base_data()

    schedule = Schedule.objects.create(
        day="LUNES",
        start_time=datetime(2025, 1, 1, 8, 0).time(),
        end_time=datetime(2025, 1, 1, 10, 0).time(),
        environment=environment,
        teacher=teacher,
        program=program,
        description="Clase de Django"
    )

    assert schedule.pk is not None
    assert schedule.day == "LUNES"
    assert schedule.environment == environment


def test_schedule_ordering():
    environment, teacher, program = create_base_data()

    s1 = Schedule.objects.create(
        day="LUNES",
        start_time=datetime(2025, 1, 1, 9, 0).time(),
        end_time=datetime(2025, 1, 1, 10, 0).time(),
        environment=environment,
        teacher=teacher,
        program=program,
        description="Clase B"
    )
    s2 = Schedule.objects.create(
        day="LUNES",
        start_time=datetime(2025, 1, 1, 8, 0).time(),
        end_time=datetime(2025, 1, 1, 9, 0).time(),
        environment=environment,
        teacher=teacher,
        program=program,
        description="Clase A"
    )

    schedules = list(Schedule.objects.all())
    assert schedules[0] == s2
    assert schedules[1] == s1


def test_invalid_schedule_same_time_and_environment():
    environment, teacher, program = create_base_data()

    Schedule.objects.create(
        day="MARTES",
        start_time=datetime(2025, 1, 1, 9, 0).time(),
        end_time=datetime(2025, 1, 1, 10, 0).time(),
        environment=environment,
        teacher=teacher,
        program=program,
        description="Clase A"
    )

    with pytest.raises(ValidationError):
        duplicate = Schedule(
            day="MARTES",
            start_time=datetime(2025, 1, 1, 9, 0).time(),
            end_time=datetime(2025, 1, 1, 10, 0).time(),
            environment=environment,
            teacher=teacher,
            program=program,
            description="Clase duplicada"
        )
        duplicate.full_clean()
