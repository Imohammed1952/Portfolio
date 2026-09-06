from pydantic import BaseModel, ConfigDict


class ReceiptItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    description: str
    quantity: int | None = None
    total_cents: int | None = None


class Receipt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    merchant: str | None = None
    transaction_date: str | None = None
    subtotal_cents: int | None = None
    tax_cents: int | None = None
    total_cents: int | None = None
    currency: str | None = None
    payment_method: str | None = None
    payment_last_four: str | None = None
    items: list[ReceiptItem] = []
