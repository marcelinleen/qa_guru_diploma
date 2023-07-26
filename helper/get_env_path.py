import os.path


def get_personal_env_path():
    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    if os.path.exists(os.path.join(main_path, '.env.personal_data.private')):
        return os.path.join(main_path, '.env.personal_data.private')
    else:
        return os.path.join(main_path, '.env.personal_data.example')


def get_test_data_path():
    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(main_path, '.env.test_data')


test_data_path = get_test_data_path()

