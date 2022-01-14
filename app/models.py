from mongoengine import *


class DateValue(EmbeddedDocument):
    date = DateTimeField()
    value = FloatField()


class Data(EmbeddedDocument):
    x_data_type = StringField(max_length=200)
    y_data_type = StringField(max_length=200)

    x = ListField(EmbeddedDocumentField(DateValue))
    y = ListField(EmbeddedDocumentField(DateValue))


class User(Document):
    user_id = IntField()
    data = EmbeddedDocumentField(Data)


class Correlation(EmbeddedDocument):
    value = FloatField()
    p_value = FloatField()


class CorrelationResults(Document):
    id = StringField(primary_key=True, max_length=200)
    user_id = IntField()
    x_data_type = StringField(max_length=200)
    y_data_type = StringField(max_length=200)
    correlation = EmbeddedDocumentField(Correlation)
