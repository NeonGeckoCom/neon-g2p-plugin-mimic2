#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'neon-g2p-mimic2-plugin=neon_g2p_mimic2_plugin:Mimic2PhonemesPlugin'
CONFIG_ENTRY_POINT = 'neon-g2p-mimic2-plugin.config=neon_g2p_mimic2_plugin:Mimic2G2PConfig'

setup(
    name='neon-g2p-mimic2-plugin',
    version='0.0.1',
    description='A utterance2phoneme plugin ovos/neon/mycroft',
    url='https://github.com/NeonGeckoCom/g2p-mimic2-plugin',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='bsd3',
    packages=['neon_g2p_mimic2_plugin'],
    zip_safe=True,
    keywords='mycroft plugin utterance phoneme',
    entry_points={'ovos.plugin.g2p': PLUGIN_ENTRY_POINT,
                  'ovos.plugin.g2p.config': CONFIG_ENTRY_POINT}
)
