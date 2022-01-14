import pandas as pd

from .models import *
from scipy.stats import pearsonr


def get_users(query_params):
    return User.objects.filter(**query_params.dict())


def get_user_by_id(user_id):
    return User.objects.get(user_id=user_id)


def get_correlation(query_params):
    return CorrelationResults.objects.filter(**query_params.dict())


def calculate(user_data):
    """
    Save user data and count correlation
    :param user_data:
    :return:
    """
    user = User(**user_data)
    calculate_correlation(user_data)
    return user.save()


def calculate_correlation(user):
    """
    Calculate pearson correlation and save to database
    :param user:
    """
    x_raw, y_raw = [user.get('data', {}).get(field, {}) for field in ['x', 'y']]
    if len(x_raw) < 2 or len(y_raw) < 2:
        return 0

    x_df, y_df = create_df(x_raw, 'date'), create_df(y_raw, 'date')
    df = x_df.join(y_df, lsuffix='_x', rsuffix='_y')
    df = df.dropna()

    corr_value, p_value = pearsonr(df['value_x'], df['value_y'])
    save_corr_res(user, corr_value, p_value)


def create_df(raw_data, index=None):
    """
    Create dataframe from dictionary
    :param raw_data: dictionary with data
    :param index: index column
    :return: dataframe
    """
    df = pd.DataFrame(raw_data)
    if index is None:
        return df

    return df.set_index(index)


def save_corr_res(user, corr_value: float, p_value: float):
    """
    Create CorrelationResults object and save to database
    :param user:
    :param corr_value: correlation value
    :param p_value: correlation p-value
    """
    data = user.get('data', {})
    user_id = user.get('user_id', None)
    x_type = data.get('x_data_type', None)
    y_type = data.get('y_data_type', None)
    corr_res = {
        'id': str(user_id) + '_' + x_type + '_' + y_type,
        'user_id': user_id,
        'x_data_type': x_type,
        'y_data_type': y_type,
        'correlation': {
            'value': corr_value,
            'p_value': p_value
        }
    }
    CorrelationResults(**corr_res).save()
