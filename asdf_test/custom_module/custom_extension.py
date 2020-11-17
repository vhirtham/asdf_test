"""A custom extension."""

import os

import asdf
from asdf import util

from .custom_types import CustomClassTypeASDF


class CustomExtensions(asdf.extension.AsdfExtension):
    """A custom class."""

    @classmethod
    def __subclasshook__(cls, C):
        print("CustomExtension --- __subclasshook__")
        super(cls, cls).__subclasshook__(C)

    @property
    def types(self):
        """Returns a list of asdf intermediate types."""
        print("CustomExtension --- Return types")
        return [CustomClassTypeASDF]

    @property
    def tag_mapping(self):
        print("CustomExtension --- Return tag mapping")
        return [
            (
                "tag:CustomOrganization:CustomStandard",
                "http://CustomOrganization/schemas/CustomStandard{tag_suffix}",
            )
        ]

    @property
    def url_mapping(self):
        print("CustomExtension --- Return url mapping")
        return [
            (
                "http://CustomOrganization/schemas/CustomStandard/",
                util.filepath_to_url(os.path.dirname(__file__))
                + "/schemas/{url_suffix}.yaml",
            )
        ]
