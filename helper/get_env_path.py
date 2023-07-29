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


def get_app_path(file: str):

    if file.startswith('./'):
        file = file[2:]

    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path_to_file = os.path.join(main_path, f'files/{file}')
    return path_to_file


def get_mobile_env_path(env):

    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path_to_mobile_env = os.path.join(main_path, 'tests', 'mobile', f'.env.mobile.{env}')
    return path_to_mobile_env
