"""Text-to-Speech support for the Rubber Duck integration."""

from pathlib import Path
from typing import Any

from homeassistant.components.tts import (
    ATTR_VOICE,
    TextToSpeechEntity,
    TtsAudioType,
    Voice,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Rubber Duck speech platform via config entry."""

    async_add_entities([RubberDuckTTSEntity(config_entry)])


class RubberDuckTTSEntity(TextToSpeechEntity):
    """The Rubber Duck TTS entity."""

    _attr_translation_key = "rubber_duck"
    _attr_default_language = "en"
    _attr_supported_languages = [_attr_default_language]
    _attr_supported_options = [ATTR_VOICE]
    _attr_has_entity_name = True

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the entity."""
        self.entry = entry

        self._attr_unique_id = entry.entry_id
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="Rubber Duck AI",
            manufacturer="Avian Intelligence Inc.",
            model="Rubber Duck",
            entry_type=DeviceEntryType.SERVICE,
        )

    @callback
    def async_get_supported_voices(self, language: str) -> list[Voice]:
        """Return a list of supported voices for a language."""
        return [
            Voice(voice_id="quack", name="Quack"),
            # Voice(voice_id="meow", name="Meow"),
            # Voice(voice_id="woof", name="Woof"),
        ]

    def get_tts_audio(
        self, message: str, language: str, options: dict[str, Any] | None = None
    ) -> TtsAudioType:
        """Load TTS from Rubber Duck."""

        quack = Path(__file__).parent / ("quack.mp3")

        return "mp3", quack.read_bytes()
