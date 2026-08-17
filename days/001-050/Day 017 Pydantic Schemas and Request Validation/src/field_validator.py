from pydantic import (
    BaseModel,
    Field,
    field_validator
)


class SensorData(BaseModel):

    temperature: float = Field(
        gt=-273.15
    )

    signals: list[float] = Field(
        min_items=3
    )

    @field_validator("signals")

    @classmethod

    def validate_signals(

        cls,

        value

    ):

        if any(v < 0 for v in value):

            raise ValueError(
                "Negative signal detected"
            )

        return value