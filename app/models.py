from mongoengine import *


class DateValue(Document):
    date = DateTimeField()
    value = FloatField()


class Data(Document):
    x_data_type = StringField(max_length=200)
    y_data_type = StringField(max_length=200)

    x = ListField(ReferenceField('DateValue', reverse_delete_rule=CASCADE))
    y = ListField(ReferenceField('DateValue', reverse_delete_rule=CASCADE))


class User(Document):
    user_id = IntField()
    data = ReferenceField('Data', reverse_delete_rule=CASCADE)


class Correlation(Document):
    value = FloatField()
    p_value = FloatField()


class CorrelationResults(Document):
    user_id = IntField()
    x_data_type = StringField(max_length=200)
    y_data_type = StringField(max_length=200)
    correlation = ReferenceField('Correlation', reverse_delete_rule=CASCADE)
