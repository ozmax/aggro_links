import ast

from django.utils.encoding import force_text
from rest_framework.metadata import SimpleMetadata
from rest_framework.compat import OrderedDict


class LinkMetaData(SimpleMetadata):

    def get_field_info(self, field):
        field_info = super(LinkMetaData, self).get_field_info(field)
        field_info = OrderedDict()
        field_info['type'] = self.label_lookup[field]
        field_info['required'] = getattr(field, 'required', False)

        attrs = [
            'read_only', 'label', 'help_text',
            'min_length', 'max_length',
            'min_value', 'max_value'
        ]

        for attr in attrs:
            value = getattr(field, attr, None)
            if value is not None and value != '':
                field_info[attr] = force_text(value, strings_only=True)

        if getattr(field, 'child', None):
            field_info['child'] = self.get_field_info(field.child)
        elif getattr(field, 'fields', None):
            field_info['children'] = self.get_serializer_info(field)
        if not field_info.get('read_only') and hasattr(field, 'choices'):
            field_info['choices'] = []
            for data, junk in field.choices.items():
                if data and (data != 'None'):
                    data = ast.literal_eval(data)
                    field_info['choices'].append(
                        {
                            'value': data['id'],
                            'display_name': force_text(
                                data['name'],
                                strings_only=True)
                        }
                    )
        return field_info
