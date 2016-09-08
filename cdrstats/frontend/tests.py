#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2015 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

# from django.test import TestCase
from django_lets_go.utils import BaseAuthenticatedClient
from frontend.views import login_view, logout_view, diagnostic


class FrontendView(BaseAuthenticatedClient):

    """Test cases for Cdr-stats Admin Interface."""

    def test_admin(self):
        """Test Function to check Admin index page"""
        response = self.client.get('/admin/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/base_site.html')
        response = self.client.login(username=self.user.username,
                                     password='admin')
        self.assertEqual(response, True)


class FrontendCustomerView(BaseAuthenticatedClient):

    """Test cases for Cdr-stats Customer Interface."""

    fixtures = ['auth_user.json']

    def test_login_view(self):
        """Test Function to check login view"""
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/login/',
                                    {'user': 'admin',
                                     'password': 'admin'}, follow=True)
        self.assertEqual(response.status_code, 200)

        request = self.factory.post('/login/',
                                    {'user': 'admin',
                                     'password': 'admin'}, follow=True)
        request.user = self.user
        request.session = self.client.session
        response = login_view(request)
        self.assertEqual(response.status_code, 302)

        request = self.factory.post('/login/',
                                    {'user': 'admin1',
                                     'password': 'admin1'}, follow=True)

        self.user.is_active = False
        self.user.save()
        request.user = self.user
        request.session = self.client.session
        response = login_view(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.post('/login/',
                                    {'user': '', 'password': ''}, follow=True)
        request.user = self.user
        request.session = self.client.session
        response = login_view(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.post('/login/',
                                    {'user': 'admin', 'password': 'admin123'}, follow=True)
        request.user = self.user
        request.session = self.client.session
        response = login_view(request)
        self.assertEqual(response.status_code, 200)

    def test_pleaselog(self):
        """Test Function to check pleaselog view"""
        response = self.client.get('/pleaselog/')
        self.assertTemplateUsed(response, 'frontend/index.html')
        self.assertEqual(response.status_code, 200)

    def test_diagnostic(self):
        """Test Function to check diagnostic view"""
        response = self.client.get('/diagnostic/')
        self.assertTemplateUsed(response, 'frontend/diagnostic.html')
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/diagnostic/')
        request.user = self.user
        request.session = {}
        response = diagnostic(request)
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        """Test Function to check customer index page"""
        request = self.factory.get('/login/')
        request.user = self.user
        request.session = {}
        response = login_view(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.post('/login/',
                                    {'username': 'admin',
                                     'password': 'admin'})
        request.user = self.user
        request.session = {}
        response = login_view(request)
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        """Test Function to check logout view"""
        response = self.client.post('/logout/', follow=True)
        self.assertEqual(response.status_code, 200)

        request = self.factory.post('/logout/', follow=True)
        request.user = self.user
        request.session = self.client.session
        request.LANGUAGE_CODE = 'en'
        response = logout_view(request)
        self.assertEqual(response.status_code, 302)
