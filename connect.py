assest_schema = {
        'csvs': {'type': 'array', 'minlength': 1, 'required': True},
        'endpoints': {'type': 'array', 'minlength': 1, 'required': True},
        'configuration': {'type': 'string', 'required': True}
}

assistant_schema = {
        'assistant_id': {'type': 'string', 'minlength': 1, 'required': True},
        'tenant_id': {'type': 'string', 'minlength': 1, 'required': True},
        'allowed_channels': {'type': 'array', 'required': True},
        'category': {'type': 'string','required': True},
        'gpt_assistant_id': {'type': 'string', 'minlength': 1, 'required': True},
        'assistant_name': {'type': 'string', 'minlength': 1, 'required': True},
        'assistant_description': {'type': 'string', 'minlength': 1, 'required': True},
        'assistant_image': {'type': 'binData','required': True},
        'assistant_goal': {'type': 'string', 'required': True},
        'assistant_nature': {'type': 'string','required': True},
        'business_name': {'type': 'string', 'required': True},
        'business_description': {'type': 'string','required': True},
        'timestamp': {'type': 'timestamp', 'required': True}
}

channel_schema = {
        'channel_id': {'type': 'string', 'minlength': 1, 'required': True},
        'tenant_id': {'type': 'string', 'minlength': 1, 'required': True},
        'assistant_id': {'type': 'string', 'minlength': 1, 'required': True},
        'cache': {'type': 'object','required': True},
        'channel_uuid': {'type': 'binary', 'minlength': 1, 'required': True},
        'channel_token': {'type': 'string', 'minlength': 1, 'required': True},
        'channel_type': {'type': 'array', 'minlength': 1, 'required': True},
        'timestamp': {'type': 'timestamp', 'required': True}
}

session_schema = {
        '_id': {'type': 'string', 'minlength': 1, 'required': True},
        'assistant_id': {'type': 'string', 'minlength': 1, 'required': True},
        'channel': {'type': 'string', 'minlength': 1, 'required': True},
        'timestamp': {'type': 'timestamp', 'required': True},
        'cache': {'type': 'object', 'required': True},
        'value': {'type': 'int', 'required': True}
}


tenant_schema = {
        'tenant_id': {'type': 'string', 'minlength': 1, 'required': True},
        'tenant_name': {'type': 'string', 'minlength': 1, 'required': True},
        'tenant_email': {'type': 'string', 'minlength':1, 'required': True},
        'password_hash': {'type': 'string', 'minlength':1, 'required': True},
        'tenant_image': {'type': 'binData', 'minlength':1, 'required': True},
        'timestamp': {'type':'timestamp', 'required': True},
}


thread_schema = {
        'assistant_id': {'type': 'string', 'minlength': 1, 'required': True},
        'thread_id': {'type': 'string', 'minlength': 1, 'required': True},
        'timestamp': {'type': 'timestamp', 'required': True},
        'messages': {'type': 'array', 'required': True},
        'channel' : {'type': 'string', 'minlength': 1, 'required': True},
        'contact': {'type': 'string', 'required': True}
}

user_schema = {
        'user_id': {'type': 'string', 'minlength': 1, 'required': True},
        'user_email': {'type': 'string', 'minlength': 1, 'required': True},
        'user_name': {'type': 'string', 'minlength' : 1 ,'required': True},
        'password_hash': {'type': 'string', 'minlength':1, 'required': True},
        'user_image': {'type': 'binData', 'minlength':1, 'required': True},
        'timestamp': {'type':'timestamp', 'required': True}
}