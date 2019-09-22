from flask import Blueprint
from flask import request

from subscription.core.models import Subscriber
from subscription.core.utils import make_success_response, make_created_response, make_failure_response
from subscription.core.models import db

subscriber = Blueprint('subscriber', __name__, url_prefix='/subscription')


@subscriber.route('/subscribers', methods=['POST'])
def add_email():
    email_address = request.args.get('email_address')

    if email_address is not None:
        query = Subscriber.query.filter(Subscriber.email_address ==
                                        email_address).first()

        if query is not None:
            return make_failure_response('409', 'email already exist')

        subscriber_mail = Subscriber(email_address)
        db.session.add(subscriber_mail)
        db.session.commit()

        return make_created_response('Subscriber added successfully')

    return make_failure_response('409', 'Error in adding subscriber')


@subscriber.route('/subscribers', methods=['GET'])
def get_subscribers():
    query = Subscriber.query
    pagination = query.paginate()
    response_data = [mail.as_json() for mail in pagination.items]
    return make_success_response(response_data)


@subscriber.route('/subscribers', methods=['DELETE'])
def delete_subscriber():
    email_address = request.args.get('email_address')
    if email_address is not None:
        Subscriber.query.filter(Subscriber.email_address == email_address).delete()
        db.session.commit()
        return make_success_response('email address deleted')
