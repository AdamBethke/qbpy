"""API Wrapper Specific Exceptions"""
import warnings


class RequestException(Exception):
    """Raise an error returned by the HTTPS request"""


class QuickBaseException(Exception):
    """Raise an error returned by the QuickBase API"""


class NotImplementedWarning(Warning):
    """Raise a warning to signal that an option is not implemented"""

