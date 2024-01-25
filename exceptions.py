import logging

class BaseException(Exception):
	@staticmethod
	def log_exception(message):
		logging.debug(message)

class OAuthTokenException(BaseException):
	def log_exception(message):
		super(BaseException, self).log_exception(message)


class UnauthorizedClientException(OAuthTokenException):
	message = "please encure client id has access"

	def __init(self):
		super(OAuthTokenException, self).log_exception(self.message)

class InvalidSecretException(OAuthTokenException):
	message = "secret is invalid"

	def __init__(self):
		super(OAuthTokenException, self).log_exception(self.message)


class InvalidTenantException(OAuthTokenException):

	message = "Tenant id is invalid"

	def __init__(self):
		super(OAuthTokenException, self).log_exception(self.message)

