# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class BindingTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .bindings(sid="BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://notify.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Bindings/BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address": "a7c658f4111ec4ff5a1a647f9d0edd819025b9f20522d2fae897049f32873e73",
                "binding_type": "apn",
                "credential_sid": null,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "endpoint": "26607274",
                "identity": "24987039",
                "notification_protocol_version": "3",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "tags": [
                    "26607274"
                ],
                "links": {
                    "user": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/24987039"
                },
                "url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings/BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .bindings(sid="BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .bindings(sid="BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://notify.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Bindings/BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .bindings(sid="BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .bindings.create(identity="identity", binding_type="apn", address="address")

        values = {'Identity': "identity", 'BindingType': "apn", 'Address': "address", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://notify.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Bindings',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address": "a7c658f4111ec4ff5a1a647f9d0edd819025b9f20522d2fae897049f32873e73",
                "binding_type": "apn",
                "credential_sid": null,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "endpoint": "26607274",
                "identity": "24987039",
                "notification_protocol_version": "3",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "tags": [
                    "26607274"
                ],
                "links": {
                    "user": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/24987039"
                },
                "url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings/BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .bindings.create(identity="identity", binding_type="apn", address="address")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .bindings.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://notify.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Bindings',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "bindings": [],
                "meta": {
                    "first_page_url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?Tag=tag&Identity=identity&PageSize=50&Page=0",
                    "key": "bindings",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?Tag=tag&Identity=identity&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .bindings.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "bindings": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "address": "a7c658f4111ec4ff5a1a647f9d0edd819025b9f20522d2fae897049f32873e73",
                        "binding_type": "apn",
                        "credential_sid": null,
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "endpoint": "26607274",
                        "identity": "24987039",
                        "notification_protocol_version": "3",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "tags": [
                            "26607274"
                        ],
                        "links": {
                            "user": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/24987039"
                        },
                        "url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings/BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?Tag=tag&Identity=identity&PageSize=50&Page=0",
                    "key": "bindings",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?Tag=tag&Identity=identity&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .bindings.list()

        self.assertIsNotNone(actual)
