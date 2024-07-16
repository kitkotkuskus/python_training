from python_training.model.group import Group


def test_upd_group(app):
        if app.group.count() == 0:
                app.group.create(Group(name="test1"))
        app.group.update(Group(name="one", header="two", footer="three"))