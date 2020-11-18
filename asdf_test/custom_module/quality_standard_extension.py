import asdf
from asdf import util, generic_io
import os
import custom_module.quality_types as qt


class QualityStandardExtensionRetag():

    def __init__(self, standard = None):
        if standard is None:
            standard ="a"
        self._standard = standard
        for cls in self.types:
            cls.standard = self._standard
            cls.yaml_tag = cls.make_yaml_tag(cls.name, True)

    @property
    def types(self):
        """Returns a list of asdf intermediate types."""
        return [qt.QualityClassTypeASDF]

    @property
    def tag_mapping(self):
        return [
            (
                "tag:QualityOrganization:"+self._standard,
                "http://QualityOrganization/schemas/"+self._standard+"/{tag_suffix}",
            )
        ]

    @property
    def url_mapping(self):
        return [
            (
                "http://QualityOrganization/schemas/"+self._standard+"/",
                util.filepath_to_url(os.path.dirname(__file__))
                + "/schemas/standards/"+self._standard+"/{url_suffix}.yaml",
            )
        ]

class QualityStandardExtensionSameTag():

    def __init__(self, standard=None):
        if standard is None:
            standard = "a"
        self._standard = standard

        mappings = {}

        for cls in self.types:
            key = "http://QualityOrganization/schemas/default/"+cls.name+"-1.0.0.yaml"
            schema_path = "custom_module/schemas/standards/"+self._standard+"/"+cls.name+"-1.0.0.yaml"
            schema = generic_io.get_file(schema_path).read().decode('utf-8')
            mappings[key]=schema
        asdf.get_config().add_resource_mapping(mappings)

    @property
    def types(self):
        """Returns a list of asdf intermediate types."""
        return [qt.QualityClassTypeASDF]

    @property
    def tag_mapping(self):
        return [
            (
                "tag:QualityOrganization:default",
                "http://QualityOrganization/schemas/default/{tag_suffix}",
            )
        ]

    @property
    def url_mapping(self):
        return [
            (
                "http://QualityOrganization/schemas/default/",
                util.filepath_to_url(os.path.dirname(__file__))
                + "/schemas/standards/"+self._standard+"/{url_suffix}.yaml",
            )
        ]