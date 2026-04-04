"""Conversation support for the Google Generative AI Conversation integration."""

from __future__ import annotations

import asyncio
from random import randint
from typing import Literal

from homeassistant.components.conversation import (
    ChatLog,
    ConversationEntity,
    ConversationInput,
    ConversationResult,
)
from homeassistant.const import MATCH_ALL
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.intent import IntentResponse

from . import RubberDuckConfigEntry
from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: RubberDuckConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up conversation entities."""
    async_add_entities([RubberDuckConversationEntity(config_entry)])


class RubberDuckConversationEntity(ConversationEntity):
    """Represent a conversation entity."""

    _attr_translation_key = "rubber_duck"
    _attr_has_entity_name = True

    def __init__(self, entry: RubberDuckConfigEntry) -> None:
        """Initialize the agent."""
        self.entry = entry

        self._attr_unique_id = entry.entry_id
        self._attr_device_info = dr.DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="Rubber Duck AI",
            manufacturer="Avian Intelligence Inc.",
            model="Rubber Duck",
            entry_type=dr.DeviceEntryType.SERVICE,
        )

    @property
    def supported_languages(self) -> list[str] | Literal["*"]:
        """Return a list of supported languages."""
        return MATCH_ALL

    async def _async_handle_message(
        self,
        user_input: ConversationInput,
        chat_log: ChatLog,
    ) -> ConversationResult:
        """Call the API."""
        await asyncio.sleep(
            randint(1, 5)
        )  # Simulate a delay for processing the message
        response = IntentResponse(language=user_input.language)
        response.async_set_speech("🦆")
        return ConversationResult(
            conversation_id=None,
            response=response,
            continue_conversation=False,
        )
