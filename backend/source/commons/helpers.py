def update_create_instance(instance, args, exception=["id"]):
    if instance:
        [
            setattr(instance, key, value) for key, value in args.items() if key not in exception
        ]

    # Cheat for create_update user
    # 78 is default length of password hash
    if hasattr(instance, 'password') and len(instance.password) < 78:
        instance.set_password(instance.password)

    instance.save()

    return instance
