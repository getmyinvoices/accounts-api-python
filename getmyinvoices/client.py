import json

import urllib3
from urllib3 import Timeout

class GMI:
    __HOST = "https://api.getmyinvoices.com/accounts/v2"

    def __init__(self, api_key, timeout=120000):
        self.api_key = api_key
        self.timeout = timeout

    def _post(self, payload, path):
        payload["api_key"] = self.api_key
        return _http.request("POST",
                             self.__HOST + path,
                             body=json.dumps(payload).encode("utf-8"),
                             timeout=self.timeout)

    @staticmethod
    def _optional(payload, key, value):
        if value is not None:
            payload[key] = value

    def api_status(self):
        response = self._post({}, "/apiStatus")
        return json.loads(response.data)

    def list_companies(self, status_filter=None, company_type_filter=None):
        payload = {}
        self._optional(payload, "status_filter", status_filter)
        self._optional(payload, "company_type_filter", company_type_filter)

        response = self._post(payload, "/listCompanies")
        return json.loads(response.data)

    def get_company(self, company_id):
        payload = {
            "company_id": company_id,
        }

        response = self._post(payload, "/getCompany")
        return json.loads(response.data)

    def list_documents(self,
                       company_filter=None,
                       archived_filter=None,
                       document_type_filter=None,
                       document_number_filter=None,
                       note_filter=None,
                       start_date_filter=None,
                       end_date_filter=None,
                       prim_uid_exclusion_filter=None,
                       prim_uid_start_filter=None,
                       updated_or_new_since_filter=None):
        payload = {}
        self._optional(payload, "company_filter", company_filter)
        self._optional(payload, "archived_filter", archived_filter)
        self._optional(payload, "document_type_filter", document_type_filter)
        self._optional(payload, "document_number_filter", document_number_filter)
        self._optional(payload, "note_filter", note_filter)
        self._optional(payload, "start_date_filter", start_date_filter)
        self._optional(payload, "end_date_filter", end_date_filter)
        self._optional(payload, "prim_uid_exclusion_filter", prim_uid_exclusion_filter)
        self._optional(payload, "prim_uid_start_filter", prim_uid_start_filter)
        self._optional(payload, "updated_or_new_since_filter", updated_or_new_since_filter)

        response = self._post(payload, "/listDocuments")
        return json.loads(response.data)

    def get_document(self, document_prim_uid, load_line_items=None, readable_text=None):
        payload = {"document_prim_uid": document_prim_uid}
        self._optional(payload, "load_line_items", load_line_items)
        self._optional(payload, "readable_text", readable_text)

        response = self._post(payload, "/getDocument")
        return json.loads(response.data)

    def upload_new_document(self,
                            file_name,
                            document_type,
                            file_content=None,
                            company_id=None,
                            document_number=None,
                            document_date=None,
                            document_due_date=None,
                            payment_method=None,
                            payment_status=None,
                            net_amount=None,
                            gross_amount=None,
                            currency=None,
                            vat=None,
                            cash_discount_date=None,
                            cash_discount_value=None,
                            tags=None,
                            note=None,
                            line_items=None,
                            run_ocr=None):
        payload = {
            "file_name": file_name,
            "document_type": document_type,
        }
        self._optional(payload, "file_content", file_content)
        self._optional(payload, "company_id", company_id)
        self._optional(payload, "document_type", document_type)
        self._optional(payload, "document_number", document_number)
        self._optional(payload, "document_date", document_date)
        self._optional(payload, "payment_method", payment_method)
        self._optional(payload, "payment_status", payment_status)
        self._optional(payload, "gross_amount", gross_amount)
        self._optional(payload, "net_amount", net_amount)
        self._optional(payload, "currency", currency)
        self._optional(payload, "vat", vat)
        self._optional(payload, "cash_discount_date", cash_discount_date)
        self._optional(payload, "document_due_date", document_due_date)
        self._optional(payload, "cash_discount_value", cash_discount_value)
        self._optional(payload, "tags", tags)
        self._optional(payload, "note", note)
        self._optional(payload, "line_items", line_items)
        self._optional(payload, "runOCR", run_ocr)

        response = self._post(payload, "/uploadNewDocument")
        return json.loads(response.data)

    def update_document(self,
                        document_prim_uid,
                        company_id=None,
                        document_type=None,
                        document_number=None,
                        document_date=None,
                        document_due_date=None,
                        payment_method=None,
                        payment_status=None,
                        net_amount=None,
                        gross_amount=None,
                        currency=None,
                        vat=None,
                        cash_discount_date=None,
                        cash_discount_value=None,
                        is_archived=None,
                        tags=None,
                        note=None,
                        line_items=None,
                        ):
        payload = {"document_prim_uid": document_prim_uid}
        self._optional(payload, "company_id", company_id)
        self._optional(payload, "document_type", document_type)
        self._optional(payload, "document_number", document_number)
        self._optional(payload, "document_date", document_date)
        self._optional(payload, "document_due_date", document_due_date)
        self._optional(payload, "payment_method", payment_method)
        self._optional(payload, "payment_status", payment_status)
        self._optional(payload, "net_amount", net_amount)
        self._optional(payload, "gross_amount", gross_amount)
        self._optional(payload, "vat", vat)
        self._optional(payload, "cash_discount_date", cash_discount_date)
        self._optional(payload, "cash_discount_value", cash_discount_value)
        self._optional(payload, "currency", currency)
        self._optional(payload, "is_archived", is_archived)
        self._optional(payload, "tags", tags)
        self._optional(payload, "note", note)
        self._optional(payload, "line_items", line_items)

        response = self._post(payload, "/updateDocument")
        return json.loads(response.data)

    def get_countries(self):
        response = self._post({}, "/getCountries")
        return json.loads(response.data)

    def get_currencies(self):
        response = self._post({}, "/getCurrencies")
        return json.loads(response.data)

    def add_custom_company(self,
                           company_name,
                           company_country,
                           company_tags=None,
                           company_street=None,
                           company_zip=None,
                           company_city=None,
                           company_email=None,
                           company_phone=None,
                           company_fax=None,
                           company_tax_number=None,
                           company_vat_id=None,
                           company_commercial_register=None,
                           company_iban=None,
                           company_bic=None,
                           company_url=None):
        payload = {
            "company_name": company_name,
            "company_country": company_country
        }
        self._optional(payload, "company_tags", company_tags)
        self._optional(payload, "company_street", company_street)
        self._optional(payload, "company_zip", company_zip)
        self._optional(payload, "company_city", company_city)
        self._optional(payload, "company_email", company_email)
        self._optional(payload, "company_phone", company_phone)
        self._optional(payload, "company_fax", company_fax)
        self._optional(payload, "company_tax_number", company_tax_number)
        self._optional(payload, "company_vat_id", company_vat_id)
        self._optional(payload, "company_commercial_register", company_commercial_register)
        self._optional(payload, "company_iban", company_iban)
        self._optional(payload, "company_bic", company_bic)
        self._optional(payload, "company_url", company_url)

        response = self._post(payload, "/addCustomCompany")
        return json.loads(response.data)

    def update_custom_company(self,
                              company_id,
                              company_name,
                              company_country,
                              company_tags=None,
                              company_street=None,
                              company_zip=None,
                              company_city=None,
                              company_email=None,
                              company_phone=None,
                              company_fax=None,
                              company_tax_number=None,
                              company_vat_id=None,
                              company_commercial_register=None,
                              company_iban=None,
                              company_bic=None,
                              company_url=None):
        payload = {
            "company_id": company_id,
            "company_name": company_name,
            "company_country": company_country
        }
        self._optional(payload, "company_tags", company_tags)
        self._optional(payload, "company_street", company_street)
        self._optional(payload, "company_zip", company_zip)
        self._optional(payload, "company_city", company_city)
        self._optional(payload, "company_email", company_email)
        self._optional(payload, "company_phone", company_phone)
        self._optional(payload, "company_fax", company_fax)
        self._optional(payload, "company_tax_number", company_tax_number)
        self._optional(payload, "company_vat_id", company_vat_id)
        self._optional(payload, "company_commercial_register", company_commercial_register)
        self._optional(payload, "company_iban", company_iban)
        self._optional(payload, "company_bic", company_bic)
        self._optional(payload, "company_url", company_url)

        response = self._post(payload, "/updateCustomCompany")
        return json.loads(response.data)

    def delete_custom_company(self, company_id):
        payload = {"company_id": company_id}

        response = self._post(payload, "/deleteCustomCompany")
        return json.loads(response.data)

    def list_attachments(self, invoice_id):
        payload = {"invoice_id": invoice_id}

        response = self._post(payload, "/listAttachments")
        return json.loads(response.data)

    def upload_attachment(self, file_name, file_content, invoice_id):
        payload = {
            "file_name": file_name,
            "file_content": file_content,
            "invoice_id": invoice_id
        }

        response = self._post(payload, "/uploadAttachment")
        return json.loads(response.data)

    def delete_attachment(self, attachment_uid):
        payload = {"attachment_uid": attachment_uid}

        response = self._post(payload, "/deleteAttachment")
        return json.loads(response.data)


_http = urllib3.PoolManager(headers={"Content-Type": "application/json"},
                            timeout=Timeout(connect=None, read=None))
