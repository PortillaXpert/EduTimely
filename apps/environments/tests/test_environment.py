import pytest
from django.urls import reverse
from django.contrib.auth.models import User, Group
from apps.environments.models.environment import Environment


@pytest.fixture
def coordinator_user(db):
    user = User.objects.create_user(username='coordinator', password='pass')
    group = Group.objects.get_or_create(name='COORDINATOR')[0]
    user.groups.add(group)
    return user


@pytest.mark.django_db
def test_environment_list_view(client, coordinator_user):
    client.force_login(coordinator_user)
    response = client.get(reverse('environments:list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_environment_create_view(client, coordinator_user):
    client.force_login(coordinator_user)
    response = client.post(reverse('environments:create'), {'name': 'Lab A', 'capacity': 30})
    assert response.status_code == 302
    assert Environment.objects.filter(name='Lab A').exists()


@pytest.mark.django_db
def test_environment_update_view(client, coordinator_user):
    environment = Environment.objects.create(name='Old Lab', capacity=20)
    client.force_login(coordinator_user)
    response = client.post(reverse('environments:update', args=[environment.id]), {'name': 'New Lab', 'capacity': 25})
    assert response.status_code == 302
    environment.refresh_from_db()
    assert environment.name == 'New Lab'
    assert environment.capacity == 25


@pytest.mark.django_db
def test_environment_delete_view(client, coordinator_user):
    environment = Environment.objects.create(name='To Delete', capacity=10)
    client.force_login(coordinator_user)
    response = client.post(reverse('environments:delete', args=[environment.id]))
    assert response.status_code == 302
    assert not Environment.objects.filter(id=environment.id).exists()
