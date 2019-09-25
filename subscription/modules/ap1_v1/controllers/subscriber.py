from flask import Blueprint, request

from subscription.core.models import db, Subscription
from subscription.core.utils import (
    make_created_response,
    make_deleted_response,
    make_failure_response,
    make_success_response)

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1.0')


@api_v1.route('/subscriptions', methods=['POST'])
def add_subscriber():
    email_address = request.args.get('email_address')

    if email_address is None:
        return make_failure_response(400, 'Bad Request')

    subscription = Subscription.query.filter(Subscription.email ==
                                             email_address).first()

    if subscription is not None:
        return make_failure_response(409, 'Subscriber already exists')

    subscription = Subscription(email=email_address)
    db.session.add(subscription)
    db.session.commit()

    return make_created_response('Subscriber added successfully')


@api_v1.route('/subscriptions', methods=['GET'])
def get_subscribers():
    query = Subscription.query

    pagination = query.paginate()
    response_data = [subscriber.as_json() for subscriber in pagination.items]

    return make_success_response(response_data, meta=pagination.meta)


@api_v1.route('/subscriptions', methods=['DELETE'])
def delete_subscriber():
    email_address = request.args.get('email_address')

    if email_address is None:
        return make_failure_response(400, 'Bad Request')

    try:
        Subscription.query.filter(Subscription.email == email_address).one()
    except NameError:
        return make_failure_response(403, 'Subscriber not found')

    Subscription.query.filter(Subscription.email == email_address).delete()
    db.session.commit()

    return make_deleted_response()
