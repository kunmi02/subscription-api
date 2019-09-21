mport uuid
from datetime import datetime
from decimal import localcontext as decimal_context, Decimal


def noner():
    return None


def seconds_to_hours_and_mins_and_secs(total_seconds):
    minutes, secs = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return hours, minutes, secs


def get_start_of_day(date_):
    return datetime.combine(date_, datetime.min.time())


def get_end_of_day(date_):
    return datetime.combine(date_, datetime.max.time())


def generate_unique_reference():
    return uuid.uuid4().hex


def kobo_to_naira(kobo_amt):
    """Convert an amount in kobo to it's naira value

    :param kobo_amt: kobo value of amount to be converted
        as an integer type
    :return: converted amount as a `decimal.Decimal` type
    """
    try:
        with decimal_context() as ctx:
            ctx.prec = 3  # Force Decimal values to 2 decimal places
            return Decimal('%.2f' % (int(kobo_amt) / 100.0))
    except Exception:
        raise ValueError('Kobo-to-naira conversion error: {}'
                         ''.format(repr(kobo_amt)))


def seconds_since_some_epoch(epoch_date):
    return abs((datetime.now() - epoch_date).total_seconds())


def getattr_nested(root_object, attr_chain, default_value=None):
    attr_chain = attr_chain.split('.')
    return reduce(lambda object_, attr: getattr(object_, attr, None),
                  attr_chain, root_object) or default_value


# def remove_empty_str(dict_):
#     for key, value in dict_.iteritems():
#         if (value is not None and isinstance(value, basestring) and
#                 not value.strip()):
#             dict_.pop(key)
#
#     return dict_


def normalise_str_values(dict_, remove_empty=False):
    new_dict = {}

    for key, value in dict_.iteritems():

        if not isinstance(value, basestring):

            new_dict[key] = value
            continue

        value = value.strip()
        if remove_empty and not value:
            continue

        new_dict[key] = value

    return new_dict
