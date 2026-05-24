

from unittest.mock import Mock


def send_welcome(email_sender, user):
	"""Sends a welcome email using the provided sender object.

	The sender must implement a `send(address)` method.
	"""
	email_sender.send(user.email)


class FakeSender:
	"""A tiny fake used in tests to capture sent addresses."""

	def __init__(self):
		self.sent = []

	def send(self, to):
		self.sent.append(to)


def demo_with_mock():
	mock_sender = Mock()
	user = type("U", (), {"email": "a@example.com"})()
	send_welcome(mock_sender, user)
	# Assert interaction (example):
	mock_sender.send.assert_called_once_with("a@example.com")
	print("Mock demo: send called once with a@example.com")


def demo_with_fake():
	fake = FakeSender()
	user = type("U", (), {"email": "b@example.com"})()
	send_welcome(fake, user)
	assert fake.sent == ["b@example.com"]
	print("Fake demo: captured sent addresses:", fake.sent)


if __name__ == "__main__":
	demo_with_mock()
	demo_with_fake()
