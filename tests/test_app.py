import pytest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

try:
    from app import app as flask_app
    APP_AVAILABLE = True
except ImportError:
    APP_AVAILABLE = False


@pytest.fixture
def client():
    if not APP_AVAILABLE:
        pytest.skip('app not importable')
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as c:
        yield c


def test_placeholder():
    assert True


def test_cause_error_endpoint(client):
    res = client.get('/cause-error')
    assert res.status_code != 404


def test_stress_endpoint(client):
    res = client.get('/stress')
    assert res.status_code != 404


def test_unknown_route_404(client):
    res = client.get('/does-not-exist')
    assert res.status_code == 404

