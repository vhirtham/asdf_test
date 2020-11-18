"""Test methods to use different quality standards"""


import asdf

import custom_module.quality_standard_extension as qse
import custom_module.quality_types as qt





tree = {
    "obj": qt.QualityClass({"a":"string","c": 1}),
}

ext = qse.QualityStandardExtensionRetag(standard="default")
# ext = qse.QualityStandardExtensionSameTag(standard="same_tag_b")

af = asdf.AsdfFile(
    tree,
    extensions=ext
)

af.write_to("quality.yml")