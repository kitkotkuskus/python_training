from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test2"))
    old_groups = db.get_group_list()
    random_groups = random.choice(old_groups)
    group = Group(name="New group")
    group.id =  random_groups.id
    app.group.modify_group_by_id(random_groups.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    index = old_groups.index(random_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test3"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

