from flask import Blueprint
from flask import request

from subscription.core.models import Subscription
from subscription.core.utils import make_success_response, make_created_response, make_failure_response
from subscription.core.models import db

api_v1 = Blueprint('api_v1', __name__,
                       url_prefix='/api/v1.0')


@api_v1.route('/subscriptions', methods=['POST'])
def add_subscriber():
    email_address = request.args.get('email_address')

    if email_address is not None and not email_address.isspace():
        query = Subscription.query.filter(Subscription.email_address ==
                                        email_address).first()

        if query is not None:
            return make_failure_response(409, 'email already exist')

        subscriber_mail = Subscription(email_address=email_address)
        db.session.add(subscriber_mail)
        db.session.commit()

        return make_created_response('Subscriber added successfully')

    return make_failure_response(409, 'Error in adding subscriber')


@api_v1.route('/subscriptions', methods=['GET'])
def get_subscribers():

    query = Subscription.query

    pagination = query.paginate()
    response_data = [mail.as_json() for mail in pagination.items]

    return make_success_response(response_data)


@api_v1.route('/subscriptions', methods=['DELETE'])
def delete_subscriber():
    email_address = request.args.get('email_address')

    if email_address is not None:
        Subscription.query.filter(Subscription.email_address ==
                              email_address).delete()
        db.session.commit()

        return make_success_response('Subscriber deleted')

    return make_failure_response(409, 'Error')
