__author__ = 'purg'

import mock
import nose.tools as ntools
import numpy
import unittest

from smqtk.data_rep import DescriptorElementFactory


class TestDescriptorElemFactory (unittest.TestCase):

    def test_no_params(self):
        test_params = {}

        d_type = mock.Mock()
        factory = DescriptorElementFactory(d_type, test_params)

        expected_type = 'type'
        expected_uuid = 'uuid'
        r = factory.new_descriptor(expected_type, expected_uuid)

        ntools.assert_true(d_type.called)
        d_type.assert_called_once_with(expected_type, expected_uuid)
        ntools.assert_equal(r, d_type())

    def test_with_params(self):
        v = numpy.random.randint(0, 10, 10)
        test_params = {
            'p1': 'some dir',
            'vec': v
        }

        d_type = mock.Mock()
        factory = DescriptorElementFactory(d_type, test_params)

        ex_type = 'type'
        ex_uuid = 'uuid'
        r = factory.new_descriptor(ex_type, ex_uuid)

        ntools.assert_true(d_type.called)
        d_type.assert_called_once_with(ex_type, ex_uuid, p1='some dir', vec=v)
        ntools.assert_equal(r, d_type())

    def test_call(self):
        # Same as `test_with_params` but using __call__ entry point
        v = numpy.random.randint(0, 10, 10)
        test_params = {
            'p1': 'some dir',
            'vec': v
        }

        d_type = mock.Mock()
        factory = DescriptorElementFactory(d_type, test_params)

        ex_type = 'type'
        ex_uuid = 'uuid'
        r = factory(ex_type, ex_uuid)

        ntools.assert_true(d_type.called)
        d_type.assert_called_once_with(ex_type, ex_uuid, p1='some dir', vec=v)
        ntools.assert_equal(r, d_type())
