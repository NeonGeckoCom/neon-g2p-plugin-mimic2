from neon_g2p_mimic2_plugin import Mimic2PhonemesPlugin



print(Mimic2PhonemesPlugin().utterance2ipa("hello world", "en"))
a = Mimic2PhonemesPlugin().get_arpa("hello", "en")
print(a)