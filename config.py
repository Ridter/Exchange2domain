#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class global_var:
    success = False
    fail = False
def set_suc(status):
    global_var.success = status
def get_suc():
    return global_var.success

def set_fail(status):
    global_var.fail = status
def get_fail():
    return global_var.fail
