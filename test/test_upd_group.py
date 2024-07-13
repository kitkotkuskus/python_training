from python_training.model.group import Group


def test_upd_group(app):
        app.session.login(username="admin", password="secret")
        app.group.update(Group(name="one", header="two", footer="three"))
        app.session.logout()