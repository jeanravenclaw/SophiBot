import inspect

l = inspect.cleandoc
# this helps with long strings
""" 
import inspect

query = inspect.cleandoc(f'''
    SELECT action.descr as "action",
    role.id as role_id,
    role.descr as role
    FROM
    public.role_action_def,
    public.role,
    public.record_def,
    public.action
    WHERE role.id = role_action_def.role_id AND
    record_def.id = role_action_def.def_id AND
    action.id = role_action_def.action_id AND
    role_action_def.account_id = {account_id} AND
    record_def.account_id={account_id} AND
    def_id={def_id}'''
)
"""
# above code will remove any local tabs
