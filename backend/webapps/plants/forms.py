# > webapps > plants > forms.py
from typing import List
from typing import Optional

from fastapi import Request


class PlantCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.english_name: Optional[str] = None
        self.family_name: Optional[str] = None
        self.wikipedia_url: Optional[str] = None
        self.location: Optional[str] = None
        self.description: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.english_name = form.get("english_name")
        self.family_name = form.get("family_name")
        self.wikipedia_url = form.get("wikipedia_url")
        self.location = form.get("location")
        self.description = form.get("description")

    def is_valid(self):
        if not self.english_name or not len(self.english_name) >= 4:
            self.errors.append("A valid English Name is required")
        if not self.wikipedia_url or not (self.wikipedia_url.__contains__("http")):
            self.errors.append("Valid Url is required e.g. https://example.com")
        if not self.family_name or not len(self.family_name) >= 1:
            self.errors.append("A valid Family Name is required")
        if not self.description or not len(self.description) >= 20:
            self.errors.append("Description too short")
        if not self.errors:
            return True
        return False
