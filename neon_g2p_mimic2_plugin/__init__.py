import requests
from ovos_plugin_manager.templates.g2p import Grapheme2PhonemePlugin, OutOfVocabulary
from ovos_utils.lang.visimes import VISIMES


class Mimic2PhonemesPlugin(Grapheme2PhonemePlugin):

    def __init__(self, config=None):
        super().__init__(config)
        self.url = self.config.get("url", "https://mimic-api.mycroft.ai/synthesize")

    def get_mimic2_phonemes(self, sentence):
        params = {"text": sentence, "visimes": True}
        results = requests.get(self.url, params=params).json()
        phonemes = results['visimes']  # dont blame me for their api
        return [(p[0], float(p[1])) for p in phonemes]

    def get_arpa(self, word, lang, ignore_oov=False):
        if lang.lower().startswith("en"):
            return [p[0] for p in self.get_mimic2_phonemes(word)]
        if ignore_oov:
            return None
        raise OutOfVocabulary

    def utterance2visemes(self, utterance, lang="en", default_dur=0.4):
        phonemes = self.get_mimic2_phonemes(utterance)
        return [(VISIMES.get(pho[0].lower(), '4'), float(pho[1]))
                for pho in phonemes]

    @property
    def available_languages(self):
        """Return languages supported by this G2P implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        return {"en"}


# sample valid configurations per language
# "display_name" and "offline" provide metadata for UI
# "priority" is used to calculate position in selection dropdown
#       0 - top, 100-bottom
# all keys represent an example valid config for the plugin
Mimic2G2PConfig = {
    "en-us": [
        {"lang": "en-us",
         "display_name": "Mimic2 G2P",
         "priority": 70,
         "native_alphabet": "ARPA",
         "durations": True,
         "offline": False}
    ]
}
