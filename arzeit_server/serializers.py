from rest_framework.serializers import HyperlinkedModelSerializer


class HyperlinkedModelSerializerWithPKs(HyperlinkedModelSerializer):
    """
    Subclassing HyperlinkedModelSerializer to force inclusion of pk fields in
    serialized data, rather than providing just the URL (which is also handy).
    """
    def get_pk_field(self, model_field):
        return self.get_field(model_field)
