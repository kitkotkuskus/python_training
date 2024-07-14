# -*- coding: utf-8 -*-
from python_training.model.group import Group


def test_add_group(app):
        app.group.create(Group(name="hfo", header="fghd", footer="sdfdg"))


def test_add_empty_group(app):
        app.group.create(Group(name="", header="", footer=""))

