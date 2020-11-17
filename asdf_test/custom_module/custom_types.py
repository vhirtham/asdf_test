"""Defines some custom types that should be serialized using asdf."""

from typing import List

import asdf


class CustomClass:
    """A custom class"""

    def __init__(self, a: float = 42.0, b: List[int] = None):
        """Initialize the custom class.

        Parameters
        ----------
        a : float
            Some floating point number.
        b : List[int]
            A list of integers
        """
        self.a = a
        self.b = b


class CustomClassTypeASDF(asdf.CustomType):
    """ASDF serialization class for `CustomClass`."""

    name = "CustomClass"
    organization = "CustomOrganization"
    version = (1, 0, 0)
    standard = "CustomStandard"
    types = [CustomClass]
    validators = {}

    @classmethod
    def names(cls):
        print("CustomClassTypeASDF --- names")
        return super(cls, cls).names()

    @classmethod
    def make_yaml_tag(cls, name, versioned=True):
        print("CustomClassTypeASDF --- make_yaml_tag")
        return super(cls, cls).make_yaml_tag(name, versioned)

    @classmethod
    def tag_base(cls):
        print("CustomClassTypeASDF --- tag_base")
        return super(cls, cls).tag_base()

    @classmethod
    def to_tree(cls, node: CustomClass, ctx: asdf.AsdfFile):
        print("CustomClassTypeASDF --- to_tree")
        return {"a": node.a, "b": node.b}

    @classmethod
    def to_tree_tagged(cls, node, ctx):
        print("CustomClassTypeASDF --- to_tree_tagged")
        return super(cls, cls).to_tree_tagged(node, ctx)

    @classmethod
    def from_tree(cls, tree, ctx: asdf.AsdfFile):
        print("CustomClassTypeASDF --- from_tree")
        return CustomClass(tree["a"], tree["b"])

    @classmethod
    def from_tree_tagged(cls, tree, ctx):
        print("CustomClassTypeASDF --- from_tree_tagged")
        return super(cls, cls).from_tree_tagged(tree, ctx)

    @classmethod
    def incompatible_version(cls, version):
        print("CustomClassTypeASDF --- incompatible_version")
        return super(cls, cls).incompatible_version(version)

    @classmethod
    def subclass(cls, *args, attribute="subclass"):
        print("CustomClassTypeASDF --- subclass")
        return super(cls, cls).subclass(*args, attribute="subclass")

    @classmethod
    def subclass_property(cls, attribute):
        print("CustomClassTypeASDF --- subclass_property")
        return super(cls, cls).subclass(attribute)

    # Hooks ----------------------------------------------------------------------------

    def pre_write(self, ctx: asdf.AsdfFile):
        print("CustomClassTypeASDF --- pre_write")

    def post_write(self, ctx: asdf.AsdfFile):
        print("CustomClassTypeASDF --- post_write")
