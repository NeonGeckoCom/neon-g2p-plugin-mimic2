from ovos_plugin_manager.g2p import Grapheme2PhonemePlugin
from ovos_utils.lang.visimes import VISIMES
import requests


class Mimic2PhonemesPlugin(Grapheme2PhonemePlugin):

    def __init__(self, config=None):
        super().__init__(config)
        self.url = self.config.get("url", "https://mimic-api.mycroft.ai/synthesize")

    def get_mimic2_phonemes(self, sentence):
        params = {"text": sentence, "visimes": True}
        results = requests.get(self.url, params=params).json()
        phonemes = results['visimes']  # dont blame me for their api
        return [(p[0], float(p[1])) for p in phonemes]

    def get_arpa(self, word, lang):
        if lang.lower().startswith("en"):
            return [p[0] for p in self.get_mimic2_phonemes(word)]
        return None

    def utterance2visemes(self, utterance, lang="en", default_dur=0.4):
        phonemes = self.get_mimic2_phonemes(utterance)
        return [(VISIMES.get(pho[0].lower(), '4'), float(pho[1]))
                for pho in phonemes]
