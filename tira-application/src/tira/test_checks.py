from django.test import TestCase
from unittest import mock
from django.core.exceptions import PermissionDenied
from .checks import actions_check_permissions

@actions_check_permissions({'admin'})
def method_that_requires_admin_access(request):
    return True

@actions_check_permissions({'admin'})
def method_that_requires_admin_access_with_vmid(request, vm_id):
    return True

@actions_check_permissions({'any'})
def method_allowed_by_any(request):
    return True

@actions_check_permissions({'participant'})
def method_allowed_by_participant(request):
    return True

@actions_check_permissions({'participant'})
def method_allowed_by_participant_with_vm_id(request, vm_id):
    return True

def mocked_request(headers):
    ret = mock.MagicMock()
    ret.headers = headers

    return ret


class PermissionsCheckTest(TestCase):
    def setUp(self):
        pass

    def test_admin_method_can_not_be_called_by_non_admin(self):
        with self.assertRaises(PermissionDenied):
            method_that_requires_admin_access(mocked_request({'X-Disraptor-Groups': 'a,b,c'}))

    def test_admin_method_with_vm_id_can_not_be_called_by_non_admin(self):
        with self.assertRaises(PermissionDenied):
            method_that_requires_admin_access_with_vmid(mocked_request({'X-Disraptor-Groups': 'a,b,c'}), 'some-vm-id')

    def test_admin_method_can_be_called_by_admin_01(self):
        self.assertTrue(method_that_requires_admin_access(mocked_request({'X-Disraptor-Groups': 'a,admins,c'})))

    def test_admin_method_with_vm_id_can_be_called_by_admin_01(self):
        self.assertTrue(method_that_requires_admin_access_with_vmid(mocked_request({'X-Disraptor-Groups': 'a,b,admins'}), 'some-vm-id'))

    def test_admin_method_can_be_called_by_admin_02(self):
        self.assertTrue(method_that_requires_admin_access(mocked_request({'X-Disraptor-Groups': 'tira_reviewer,a,c,c'})))

    def test_admin_method_with_vm_id_can_be_called_by_admin_02(self):
        self.assertTrue(method_that_requires_admin_access_with_vmid(mocked_request({'X-Disraptor-Groups': 'tira_reviewer'}), 'some-vm-id'))

    def test_method_allowed_for_anyone_can_be_called_by_anyone(self):
       self.assertTrue(method_allowed_by_any(mocked_request({'X-Disraptor-Groups': 'a,b,c'})))

    def test_participant_method_can_not_be_called_by_non_participant(self):
        with self.assertRaises(PermissionDenied):
            method_allowed_by_participant(mocked_request({'X-Disraptor-Groups': 'a,b,c'}))

    def test_participant_method_with_vm_id_can_not_be_called_by_non_participant(self):
        with self.assertRaises(PermissionDenied):
            method_allowed_by_participant_with_vm_id(mocked_request({'X-Disraptor-Groups': 'a,b,c'}), 'dummy-vm-id')

    def test_participant_method_with_vm_id_can_be_called_by_participant(self):
       self.assertTrue(method_allowed_by_participant_with_vm_id(mocked_request({'X-Disraptor-Groups': 'a,tira_vm_dummy-vm-id,c'}), vm_id='dummy-vm-id'))

