#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class global_var:
    success = False
def set_suc(status):
    global_var.success = status
def get_suc():
    return global_var.success
