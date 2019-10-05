from flask import Flask, render_template, request

import config
from extensions import db
from models import Account

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def accounts():
    page = request.args.get('page', 1, type=int)
    result = Account.query
    pagination = result.order_by(Account.id.desc()).paginate(page, per_page=20, error_out=False)
    context = {'pagination': pagination, 'accounts': pagination.items}
    return render_template('accounts.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
