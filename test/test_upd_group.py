from python_training.model.group import Group
from random import randrange


def test_upd_group(app):
        if app.group.count() == 0:
                app.group.create(Group(name="test1"))
        old_groups = app.group.get_group_list()
        index = randrange(len(old_groups))
        group = Group(name="one", header="two", footer="three")
        group.id = old_groups[index].id
        app.group.update_by_index(index, group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)