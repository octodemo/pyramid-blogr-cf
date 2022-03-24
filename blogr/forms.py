from wtforms import (
    Form,
    BooleanField,
    HiddenField,
    TextField,
    TextAreaField,
    validators,
    )

strip_filter = lambda x: x.strip() if x else None


class BlogCreateForm(Form):
    #title = TextField('Entry title', [validators.Length(min=1, max=9999999999)],
                      #filters=[strip_filter])
    title = TextField('Entry title', [validators.Length(min=1, max=9999999999)])
    #body = TextAreaField('Entry body', [validators.Length(min=1)],
                         #filters=[strip_filter])
    body = TextAreaField('Entry body', [validators.Length(min=1)])


class BlogUpdateForm(BlogCreateForm):
    id = HiddenField()


class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=1, max=999999999)])
    password = TextField('Password', [validators.Length(min=1, max=999999999)])
