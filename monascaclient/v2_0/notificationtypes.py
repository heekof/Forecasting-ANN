# (C) Copyright 2016 Hewlett Packard Enterprise Development LP
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

from monascaclient.common import monasca_manager
from monascaclient.openstack.common.apiclient import base
from monascaclient.openstack.common.py3kcompat import urlutils


class NotificationTypes(base.Resource):

    def __repr__(self):
        return "<NotificationTypes %s>" % self._info


class NotificationTypesManager(monasca_manager.MonascaManager):
    resource_class = NotificationTypes
    base_url = '/notification-methods/types'

    def list(self, **kwargs):
        """Get a list of notifications."""
        newheaders = self.get_headers()
        url_str = self.base_url
        if kwargs:
            url_str = url_str + '?%s' % urlutils.urlencode(kwargs, True)

        resp, body = self.client.json_request('GET', url_str,
                                              headers=newheaders)
        return body['elements'] if type(body) is dict else body
