"""Config flow for the Rubber Duck AI integration."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN


class RubberDuckConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Rubber Duck AI."""

    async def async_step_user(
        self, _: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""

        return self.async_create_entry(title="Rubber Duck AI", data={})
