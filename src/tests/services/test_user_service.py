import pytest
from unittest.mock import patch, MagicMock
from src.services import user_service
from src.models.user_interface import UserCreate

@pytest.fixture
def user_data():
    return UserCreate(
        email="test@pod.com",
        password="pod2025",
        name="Test"
    )

@patch("src.services.user_service.user_repo")
def test_register_user_success(mock_user_repo, user_data):
    mock_user_repo.create_user_auth.return_value = "mocked_uid"

    uid = user_service.register_user(user_data)

    assert uid == "mocked_uid"
    mock_user_repo.create_user_auth.assert_called_once_with(user_data.email, user_data.password)
    mock_user_repo.save_user_data.assert_called_once_with("mocked_uid", {
        "email": user_data.email,
        "name": user_data.name
    })

@patch("src.services.user_service.user_repo")
def test_register_user_failure(mock_user_repo, user_data):
    mock_user_repo.create_user_auth.side_effect = Exception("Auth failed")

    with pytest.raises(RuntimeError, match="Failed to register user"):
        user_service.register_user(user_data)

@patch("src.services.user_service.firebase_sign_in")
def test_login_user_service_success(mock_sign_in):
    mock_sign_in.return_value = {"token": "abc123"}

    result = user_service.login_user_service("test@pod.com", "pod2025")
    assert result == {"token": "abc123"}
    mock_sign_in.assert_called_once_with("test@pod.com", "pod2025")

@patch("src.services.user_service.firebase_sign_in")
def test_login_user_service_failure(mock_sign_in):
    mock_sign_in.side_effect = Exception("Failed to login")

    with pytest.raises(RuntimeError, match="Failed to login"):
        user_service.login_user_service("test@pod.com", "pod2025")