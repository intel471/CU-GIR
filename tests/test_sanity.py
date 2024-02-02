import json
import os

import pytest
from stix2 import parse


HERE = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(HERE, "..", "STIX", "Current", "intel471_cu-gir.json")) as fh:
    girs = json.load(fh)


@pytest.mark.parametrize("gir", girs)
def test_sanity(gir):
    parse(gir, allow_custom=True)


