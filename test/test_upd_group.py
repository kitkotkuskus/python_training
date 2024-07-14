from python_training.model.group import Group


def test_upd_group(app):
        app.group.update(Group(name="one", header="two", footer="three"))