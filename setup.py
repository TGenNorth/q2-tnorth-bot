# ----------------------------------------------------------------------------
# Copyright (c) 2024, Greg Caporaso.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

description = ("A template QIIME 2 plugin.")

setup(
    name="q2-tnorth-bot",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="Greg Caporaso",
    author_email="gcaporaso@tgen.org",
    description=description,
    url="https://github.com/TGenNorth",
    entry_points={
        "qiime2.plugins": [
            "q2_tnorth_bot="
            "q2_tnorth_bot"
            ".plugin_setup:plugin"]
    },
    package_data={
        "q2_tnorth_bot": ["citations.bib"],
        "q2_tnorth_bot.tests": ["data/*"],
    },
    zip_safe=False,
    scripts=['scripts/auto-qc']
)
