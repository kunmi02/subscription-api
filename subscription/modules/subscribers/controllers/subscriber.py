from flask import Blueprint
from flask import request

from subscription.core.models import Subscriber
from subscription.core.utils import make_success_response, make_created_response
from subscription.core.models import db

subscriber = Blueprint('subscriber', __name__, url_prefix='/subscription')


@subscriber.route('/subscribers', methods=['POST'])
def add_email():
    email_address = request.args.get('email_address')

    if email_address is not None:
        subscriber_mail = Subscriber(email_address)
        db.session.add(subscriber_mail)
        db.session.commit()

        return make_created_response('Subscriber added successfully')

    return 'subscribed not added succesfully'


@subscriber.route('/subscribers', methods=['GET'])
def get_subscribers():
    query = Subscriber.query
    pagination = query.paginate()
    response_data = [mail.as_json() for mail in pagination.items]
    return make_success_response(response_data)
