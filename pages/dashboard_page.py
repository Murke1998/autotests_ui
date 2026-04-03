import pytest
from playwright.sync_api import sync_playwright, Page, expect

class DashboardPage:
    def __init__(self, page:Page):
        self.page = page
        self.dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")

    def visible_dashboard_title_text(self):
        expect(self.dashboard_title).is_visible()


