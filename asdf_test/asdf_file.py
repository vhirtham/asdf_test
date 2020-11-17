"""Test functions of the asdf_file class"""

import os

import asdf
import numpy as np
from asdf.schema import load_schema
from asdf import generic_io
from custom_module.custom_extension import CustomExtensions
from custom_module.custom_types import CustomClass

my_float = 12.45
my_list = [3, 4, 6]
my_dict = {"a": 1, "b": 42}

cc = CustomClass(2.45, [2, 8, 64])

tree = {
    "cc": cc,
}

s = load_schema("custom_module/schemas/CustomClass-alternative.yaml")
s_string = generic_io.get_file("custom_module/schemas/CustomClass-alternative.yaml").read().decode('utf-8')
asdf.get_config().add_resource_mapping({"http://CustomOrganization/schemas/CustomStandard/CustomClass-1.0.0": s_string})

print("Script --- Create AsdfFile instance")
af = asdf.AsdfFile(
    tree,
    extensions=CustomExtensions(),
    custom_schema=f"custom_module\\schemas\\CustomSchema.yaml",
)

print("\nScript --- Call write_to of AsdfFile instance")
af.write_to("test.yml")
