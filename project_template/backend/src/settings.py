# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tmpl_middleware
from tekton.gae.middleware import router_middleware, parameter, webapp2_dependencies, email_errors, json_middleware

SENDER_EMAIL = 'renzon@gmail.com'
WEB_BASE_PACKAGE = "web"
MIDDLEWARES = [tmpl_middleware.execute,
               json_middleware.execute,
               email_errors.execute,
               webapp2_dependencies.execute,
               parameter.execute,
               router_middleware.execute]

