from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
from backend.db import get_db_connection

router = APIRouter()

class InvoiceItem(BaseModel):
    description: str
    quantity: int
    unit_price: float

class InvoiceData(BaseModel):
    invoice_number: str
    invoice_date: str
    customer_name: str
    tax_registration: str
    customer_address: str
    document_type: str
    items: List[InvoiceItem]
    tax_rate: Optional[float] = 0.0

@router.post("/invoices")
async def save_invoice(invoice: InvoiceData):
    conn = get_db_connection()
    cursor = conn.cursor()
    items_json = json.dumps([item.dict() for item in invoice.items])
    cursor.execute(
        "INSERT INTO invoices (invoice_number, invoice_date, customer_name, tax_registration, customer_address, document_type, items, tax_rate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (invoice.invoice_number, invoice.invoice_date, invoice.customer_name, invoice.tax_registration, invoice.customer_address, invoice.document_type, items_json, invoice.tax_rate)
    )
    conn.commit()
    conn.close()
    return {"message": f"Invoice {invoice.invoice_number} saved"}

@router.get("/invoices")
async def list_invoices():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM invoices")
    rows = cursor.fetchall()
    conn.close()
    invoices = []
    for row in rows:
        invoices.append({
            "invoice_number": row["invoice_number"],
            "invoice_date": row["invoice_date"],
            "customer_name": row["customer_name"],
            "tax_registration": row["tax_registration"],
            "customer_address": row["customer_address"],
            "document_type": row["document_type"],
            "items": json.loads(row["items"]),
            "tax_rate": row["tax_rate"],
            "status": row["status"],
        })
    return invoices
