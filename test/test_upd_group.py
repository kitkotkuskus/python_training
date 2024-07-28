from python_training.model.group import Group


def test_upd_group(app):
        if app.group.count() == 0:
                app.group.create(Group(name="test1"))
        old_groups = app.group.get_group_list()
        group = Group(name="one", header="two", footer="three")
        group.id = old_groups[0].id
        app.group.update(group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[0] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)