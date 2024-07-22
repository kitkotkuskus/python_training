from python_training.model.group import Group


def test_upd_group(app):
        if app.group.count() == 0:
                app.group.create(Group(name="test1"))
        old_groups = app.group.get_group_list()
        app.group.update(Group(name="one", header="two", footer="three"))
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)