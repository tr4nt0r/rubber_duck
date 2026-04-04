"""The Rubber Duck AI integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

_PLATFORMS: list[Platform] = [Platform.CONVERSATION, Platform.TTS]

type RubberDuckConfigEntry = ConfigEntry[None]


async def async_setup_entry(hass: HomeAssistant, entry: RubberDuckConfigEntry) -> bool:
    """Set up Rubber Duck AI from a config entry."""

    await hass.config_entries.async_forward_entry_setups(entry, _PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: RubberDuckConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, _PLATFORMS)
