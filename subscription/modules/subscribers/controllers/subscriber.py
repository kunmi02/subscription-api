from flask import Blueprint
from flask import request

from subscription.core.models import Subscription
from subscription.core.utils import (make_success_response,
                                     make_created_response,
                                     make_failure_response)
from subscription.core.models import db

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1.0')


@api_v1.route('/subscriptions', methods=['POST'])
def add_subscriber():
    email_address = request.args.get('email_address')

    if email_address is not None:
        email = Subscription.query.filter(Subscription.email ==
                                          email_address).first()

        if email is not None:
            return make_failure_response(409, 'email already exists')

        subscriber = Subscription(email=email_address)
        db.session.add(subscriber)
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

    if email_address is not None:
        Subscription.query.filter(Subscription.email == email_address).delete()
        db.session.commit()

        return make_success_response('Subscriber deleted')

    return make_failure_response(409, 'Error')
