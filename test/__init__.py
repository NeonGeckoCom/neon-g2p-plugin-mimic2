from neon_g2p_mimic2_plugin import Mimic2PhonemesPlugin



print(Mimic2PhonemesPlugin().utterance2arpa("hello world", "en"))
print(Mimic2PhonemesPlugin().utterance2visemes("hello world"))
a = Mimic2PhonemesPlugin().get_ipa("hello", "en")
print(a)