import json
import os
from typing import Any, Dict
from pyutils.logger.logger import Logger


class I18nUtil:
    def __init__(self, locale: str):
        self.locale = locale
        self.translations = {}
        self.load_translations()

    def load_translations(self):
        translations_file = f"translations_{self.locale}.json"
        if os.path.exists(translations_file):
            with open(translations_file, 'r', encoding='utf-8') as file:
                self.translations = json.load(file)
            Logger.info(f"Loaded translations for locale: {self.locale}")
        else:
            Logger.error(f"Translations file not found: {translations_file}")

    def translate(self, key: str) -> str:
        return self.translations.get(key, key)

    def add_translation(self, key: str, value: str) -> None:
        self.translations[key] = value
        Logger.info(f"Added translation: '{key}' -> '{value}'")
        with open(f"translations_{self.locale}.json", 'w', encoding='utf-8') as file:
            json.dump(self.translations, file, ensure_ascii=False, indent=4)
