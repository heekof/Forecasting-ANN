# (C) Copyright 2014-2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import sys

from oslo_serialization import jsonutils

verbose = 0

log = logging.getLogger(__name__)


class BaseException(Exception):

    """An error occurred."""

    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message or self.__class__.__doc__


class CommandError(BaseException):

    """Invalid usage of CLI."""


class InvalidEndpoint(BaseException):

    """The provided endpoint is invalid."""


class CommunicationError(BaseException):

    """Unable to communicate with server."""


class RequestTimeoutError(BaseException):

    """Timeout making a POST, GET, PATCH, DELETE, or PUT request to the server."""


class KeystoneException(Exception):

    """Base exception for all Keystone-derived exceptions."""
    # This is initialized with the exception raised by the Keystone client so
    # deriving this class from Exception instead of BaseException allows that to
    # be handled without any additional code
    pass


class HTTPException(BaseException):

    """Base exception for all HTTP-derived exceptions."""
    code = 'N/A'

    def __init__(self, message=None):
        super(HTTPException, self).__init__(message)
        try:
            log.error("exception: {}".format(message))
            self.error = jsonutils.loads(message)
        except Exception:
            self.error = {'error':
                          {'message': self.message or self.__class__.__doc__}}

    def __str__(self):

        if 'description' in self.error:
            # Python API:
            # Expected message format:
            # {
            #    "title": "Foo",
            #    "description": "Bar"
            # }
            message = self.error['description']
        else:
            # Java API:
            # Expected message format:
            # {
            #    "conflict":{"code":409,
            #                "message":"Bar",
            #                "details":"",
            #                "internal_code":"Baz"}
            # }
            for key in self.error:
                message = self.error[key].get('message', 'Internal Error')

        if verbose:
            traceback = self.error['error'].get('traceback', '')
            return '%s\n%s' % (message, traceback)
        else:
            return '%s' % message


class HTTPMultipleChoices(HTTPException):
    code = 300

    def __str__(self):
        self.details = ("Requested version of Monasca API is not"
                        "available.")
        return "%s (HTTP %s) %s" % (self.__class__.__name__, self.code,
                                    self.details)


class BadRequest(HTTPException):
    code = 400


class HTTPBadRequest(BadRequest):
    pass


class Unauthorized(HTTPException):
    code = 401


class HTTPUnauthorized(Unauthorized):
    pass


class Forbidden(HTTPException):

    """DEPRECATED."""
    code = 403


class HTTPForbidden(Forbidden):
    pass


class NotFound(HTTPException):

    """DEPRECATED."""
    code = 404


class HTTPNotFound(NotFound):
    pass


class HTTPMethodNotAllowed(HTTPException):
    code = 405


class Conflict(HTTPException):

    """DEPRECATED."""
    code = 409


class HTTPConflict(Conflict):
    pass


class OverLimit(HTTPException):

    """DEPRECATED."""
    code = 413


class HTTPOverLimit(OverLimit):
    pass


class HTTPUnsupported(HTTPException):
    code = 415


class HTTPUnProcessable(HTTPException):
    code = 422


class HTTPInternalServerError(HTTPException):
    code = 500


class HTTPNotImplemented(HTTPException):
    code = 501


class HTTPBadGateway(HTTPException):
    code = 502


class ServiceUnavailable(HTTPException):

    """DEPRECATED."""
    code = 503


class HTTPServiceUnavailable(ServiceUnavailable):
    pass


# NOTE(bcwaldon): Build a mapping of HTTP codes to corresponding exception
# classes
_code_map = {}
for obj_name in dir(sys.modules[__name__]):
    if obj_name.startswith('HTTP'):
        obj = getattr(sys.modules[__name__], obj_name)
        _code_map[obj.code] = obj


def from_response(response):
    """Return an instance of an HTTPException based on requests response."""
    cls = _code_map.get(response.status_code, HTTPException)
    return cls(response.content)


class NoTokenLookupException(Exception):

    """DEPRECATED."""
    pass


class EndpointNotFound(Exception):

    """DEPRECATED."""
    pass
